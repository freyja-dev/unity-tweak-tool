#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Team:
#   J Phani Mahesh <phanimahesh@gmail.com>
#   Barneedhar (jokerdino) <barneedhar@ubuntu.com>
#   Amith KK <amithkumaran@gmail.com>
#   Georgi Karavasilev <motorslav@gmail.com>
#   Sam Tran <samvtran@gmail.com>
#   Sam Hewitt <hewittsamuel@gmail.com>
#
# Description:
#   A One-stop configuration tool for Unity.
#
# Legal Stuff:
#
# This file is a part of Mechanig
#
# Mechanig is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# Mechanig is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>

import os, os.path

from gi.repository import Gtk,Gio,Gdk

from .ui import ui
from . import settings

class Unitysettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = (os.path.join(settings.UI_DIR,
                                    'unity.ui'))
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['nb_unitysettings']
        self.page.unparent()
        self.builder.connect_signals(self)

# TODO : Set these marks to the proper "sticky" location
        revealScale = self.ui['sc_reveal_sensitivity']
        revealScale.add_mark(5.333, Gtk.PositionType.BOTTOM, None)

        transparencyScale = self.ui['sc_launcher_transparency']
        transparencyScale.add_mark(.666, Gtk.PositionType.BOTTOM, None)


# GSettings objects go here
        self.unityshell=self.plugin('unityshell')
        self.desktop=self.gnome('nautilus.desktop')
        self.background=self.gnome('desktop.background')
        self.launcher=self.unity('Launcher')
        self.power=self.canonical('indicator.power')
        self.session=self.canonical('indicator.session')
        self.datetime=self.canonical('indicator.datetime')

        self.refresh()

#=====================================================================#
#                                Helpers                              #
#=====================================================================#
# TODO : Find better names.
    @staticmethod
    def resetAllKeys(schema,path=None):
        """Reset all keys in given Schema."""
        gsettings=Gio.Settings(schema=schema,path=path)
        for key in gsettings.list_keys():
            gsettings.reset(key)


    @staticmethod
    def color_to_hash(c):
        """Convert a Gdk.Color or Gdk.RGBA object to hex representation"""
        if isinstance(c,Gdk.Color):
            return "#{:02x}{:02x}{:02x}ff".format(*map(lambda x: round(x*255),[c.red_float,c.green_float,c.blue_float]))
        if isinstance(x,Gdk.RGBA):
            return "#{:02x}{:02x}{:02x}{:02x}".format(*map(lambda x: round(x*255),[c.red,c.green,c.blue,c.alpha]))
        # If it is neither a Gdk.Color object nor a Gdk.RGBA objcect,
        raise NotImplementedError

    def refresh(self):
        '''Reads the current config and refreshes the displayed values'''
    # Launcher
        dependants=['radio_reveal_left',
                    'radio_reveal_topleft',
                    'sc_reveal_sensitivity',
                    'l_launcher_reveal',
                    'l_launcher_reveal_sensitivity']
        if self.unityshell.get_int('launcher-hide-mode'):
            self.ui['sw_launcher_hidemode'].set_active(True)
            self.ui.sensitize(dependants)
        else:
            self.ui['sw_launcher_hidemode'].set_active(False)
            self.ui.unsensitize(dependants)
        del dependants
# Preferring readability over optimisations.
# I am aware of the redundancy and the better "[not] bool(value)"
        self.ui['radio_reveal_left'].set_active(True if self.unityshell.get_int('reveal-trigger') is 0 else False)
        self.ui['radio_reveal_topleft'].set_active(True if self.unityshell.get_int('reveal-trigger') is 1 else False)
        self.ui['sc_reveal_sensitivity'].set_value(self.unityshell.get_double('edge-responsiveness'))

        dependants=['l_launcher_transparency_scale',
                    'sc_launcher_transparency']
        opacity=self.unityshell.get_double('launcher-opacity')
        if opacity==1:
            self.ui['sw_launcher_transparent'].set_active(False)
            self.ui.unsensitize(dependants)
        else:
            self.ui['sw_launcher_transparent'].set_active(True)
            self.ui.sensitize(dependants)
        self.ui['sc_launcher_transparency'].set_value(opacity)
        del dependants
        del opacity

        mode = self.unityshell.get_int('num-launchers')
        self.ui['radio_launcher_visibility_all'].set_active(True if mode is 0 else False)
        self.ui['radio_launcher_visibility_primary'].set_active(True if mode is 1 else False)
        del mode

        color = self.unityshell.get_string('background-color')
        if color.endswith('00'):
            self.ui['radio_launcher_color_cham'].set_active(True)
            self.ui.unsensitize(['color_launcher_color_cus'])
        else:
            self.ui['radio_launcher_color_cus'].set_active(True)
            self.ui.sensitize(['color_launcher_color_cus'])
        valid,gdkcolor=Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_launcher_color_cus'].set_color(gdkcolor)
        del color,valid,gdkcolor

        self.ui['spin_launcher_icon_size'].set_value(self.unityshell.get_int('icon-size'))

        self.ui['cbox_launcher_icon_colouring'].set_active(self.unityshell.get_int('backlight-mode'))

        self.ui['sw_launcher_show_desktop'].set_active(True if 'unity://desktop-icon' in self.launcher.get_strv('favorites') else False)

        # Refreshing Unity panel settings

        dependants=['l_transparent_panel',
                    'sc_panel_transparency',
                    'check_panel_opaque']
        opacity=self.unityshell.get_double('panel-opacity')
        if opacity==1:
            self.ui['sw_transparent_panel'].set_active(False)
            self.ui.unsensitize(dependants)
        else:
            self.ui['sw_transparent_panel'].set_active(True)
            self.ui.sensitize(dependants)
        self.ui['sc_panel_transparency'].set_value(opacity)
        del dependants
        del opacity

        time_format = self.datetime.get_string('time-format')

        if time_format == '12-hour':
            self.ui['cbox_formattime'].set_active(0)
        elif time_format == '24-hour':
            self.ui['cbox_formattime'].set_active(1)
        else:
            self.ui['cbox_formattime'].set_active(2)
        del time_format

        if self.datetime.get_boolean('show-seconds') is True:
            self.ui['cbox_time_seconds'].set_active(0)
        else:
            self.ui['cbox_time_seconds'].set_active(1)

        # Refreshing Unity switcher settings

        self.ui['check_switchwindows_all_workspaces'].set_active(self.unityshell.get_boolean('alt-tab-bias-viewport'))
        self.ui['check_switcher_showdesktop'].set_active(True if self.unityshell.get_boolean('disable-show-desktop')is False else False)
        self.ui['check_minimizedwindows_switch'].set_active(self.unityshell.get_boolean('show-minimized-windows'))
        self.ui['check_autoexposewindows'].set_active(self.unityshell.get_boolean('alt-tab-timeout'))


        model = self.ui['list_unity_switcher_windows_accelerators']

        alt_tab_forward = self.unityshell.get_string('alt-tab-forward')
        iter_alt_tab_forward = model.get_iter_first()
        model.set_value(iter_alt_tab_forward, 1, alt_tab_forward)

        alt_tab_prev = self.unityshell.get_string('alt-tab-prev')
        iter_alt_tab_prev = model.iter_next(iter_alt_tab_forward)
        model.set_value(iter_alt_tab_prev, 1, alt_tab_prev)

        alt_tab_forward_all = self.unityshell.get_string('alt-tab-forward-all')
        iter_alt_tab_forward_all = model.iter_next(iter_alt_tab_prev)
        model.set_value(iter_alt_tab_forward_all, 1, alt_tab_forward_all)

        alt_tab_prev_all = self.unityshell.get_string('alt-tab-prev-all')
        iter_alt_tab_prev_all = model.iter_next(iter_alt_tab_forward_all)
        model.set_value(iter_alt_tab_prev_all, 1, alt_tab_prev_all)

        alt_tab_right = self.unityshell.get_string('alt-tab-right')
        iter_alt_tab_right = model.iter_next(iter_alt_tab_prev_all)
        model.set_value(iter_alt_tab_right, 1, alt_tab_right)

        alt_tab_left = self.unityshell.get_string('alt-tab-left')
        iter_alt_tab_left = model.iter_next(iter_alt_tab_right)
        model.set_value(iter_alt_tab_left, 1, alt_tab_left)

        alt_tab_detail_start = self.unityshell.get_string('alt-tab-detail-start')
        iter_alt_tab_detail_start = model.iter_next(iter_alt_tab_left)
        model.set_value(iter_alt_tab_detail_start, 1, alt_tab_detail_start)

        alt_tab_detail_stop = self.unityshell.get_string('alt-tab-detail-stop')
        iter_alt_tab_detail_stop = model.iter_next(iter_alt_tab_detail_start)
        model.set_value(iter_alt_tab_detail_stop, 1, alt_tab_detail_stop)

        alt_tab_next_window = self.unityshell.get_string('alt-tab-next-window')
        iter_alt_tab_next_window = model.iter_next(iter_alt_tab_detail_stop)
        model.set_value(iter_alt_tab_next_window, 1, alt_tab_next_window)

        alt_tab_prev_window = self.unityshell.get_string('alt-tab-prev-window')
        iter_alt_tab_prev_window = model.iter_next(iter_alt_tab_next_window)
        model.set_value(iter_alt_tab_prev_window, 1, alt_tab_next_window)

        del model

        model = self.ui['list_unity_switcher_launcher_accelerators']

        launcher_switcher_forward = self.unityshell.get_string('launcher-switcher-forward')
        iter_launcher_switcher_forward = model.get_iter_first()
        model.set_value(iter_launcher_switcher_forward, 1, launcher_switcher_forward)

        launcher_switcher_prev = self.unityshell.get_string('launcher-switcher-prev')
        iter_launcher_switcher_prev = model.iter_next(iter_launcher_switcher_forward)
        model.set_value(iter_launcher_switcher_prev, 1, launcher_switcher_prev)

        del model, launcher_switcher_forward, iter_launcher_switcher_forward, launcher_switcher_prev, iter_launcher_switcher_prev


        # Refreshing Unity additional settings

        self.ui['check_shortcuts_hints_overlay'].set_active(self.unityshell.get_boolean('shortcut-overlay'))

        model = self.ui['list_unity_additional_accelerators']

        show_hud = self.unityshell.get_string('show-hud')
        iter_show_hud = model.get_iter_first()
        model.set_value(iter_show_hud, 1, show_hud)

        show_launcher = self.unityshell.get_string('show-launcher')
        iter_show_launcher = model.iter_next(iter_show_hud)
        model.set_value(iter_show_launcher, 1, show_launcher)

        execute_command = self.unityshell.get_string('execute-command')
        iter_execute_command = model.iter_next(iter_show_launcher)
        model.set_value(iter_execute_command, 1, execute_command)

        keyboard_focus = self.unityshell.get_string('keyboard-focus')
        iter_keyboard_focus = model.iter_next(iter_execute_command)
        model.set_value(iter_keyboard_focus, 1, keyboard_focus)

        panel_first_menu = self.unityshell.get_string('panel-first-menu')
        iter_panel_first_menu = model.iter_next(iter_keyboard_focus)
        model.set_value(iter_panel_first_menu, 1, panel_first_menu)

        del model, show_hud, iter_show_hud, show_launcher, iter_show_launcher, execute_command, iter_execute_command, keyboard_focus, iter_keyboard_focus, panel_first_menu, iter_panel_first_menu


# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.


    @staticmethod
    def plugin(plugin):
        schema='org.compiz.'+plugin
        path='/org/compiz/profiles/unity/plugins/'+plugin+'/'
        return Gio.Settings(schema=schema,path=path)

    @staticmethod
    def unity(child=None):
        schema='com.canonical.Unity'
        schema=schema+'.'+child if child else schema
        return Gio.Settings(schema)

    @staticmethod
    def canonical(child):
        schema='com.canonical.'+child
        return Gio.Settings(schema)

    @staticmethod
    def compiz(child):
        schema='org.compiz.'+child
        return Gio.Settings(schema)

    @staticmethod
    def gnome(child):
        schema='org.gnome.'+child
        return Gio.Settings(schema)


#=====BEGIN: Unity settings=====
#-----BEGIN: Launcher ----------
    def on_sw_launcher_hidemode_active_notify(self,widget,udata=None):
        dependants=['radio_reveal_left',
                    'radio_reveal_topleft',
                    'sc_reveal_sensitivity',
                    'l_launcher_reveal',
                    'l_launcher_reveal_sensitivity']
        if self.ui['sw_launcher_hidemode'].get_active():
            self.unityshell.set_int("launcher-hide-mode",1)
            self.ui.sensitize(dependants)
        else:
            self.unityshell.set_int("launcher-hide-mode",0)
            self.ui.unsensitize(dependants)

    def on_radio_reveal_left_toggled(self,button,udata=None):
        radio=self.ui['radio_reveal_left']
        mode=0 if radio.get_active() else 1
        self.unityshell.set_int('reveal-trigger',mode)

# XXX :Strictly speaking, only one of these two will suffice.
    def on_radio_reveal_topleft_toggled(self,button,udata=None):
        radio=self.ui['radio_reveal_topleft']
        mode=0 if not radio.get_active() else 1
        self.unityshell.set_int('reveal-trigger',mode)

    def on_sc_reveal_sensitivity_value_changed(self,widget,udata=None):
        slider=self.ui['sc_reveal_sensitivity']
        val=slider.get_value()
        self.unityshell.set_double('edge-responsiveness',val)
# Two settings possible:
#        reveal-pressure (int,(1,1000))
#        edge-responsiveness (double,(0.2,8.0))
# XXX : To be discussed and changed if necessary.

    def on_sw_launcher_transparent_active_notify(self,widget,udata=None):
        dependants=['l_launcher_transparency_scale',
                    'sc_launcher_transparency']
        if self.ui['sw_launcher_transparent'].get_active():
            self.ui.sensitize(dependants)
            opacity=self.ui['sc_launcher_transparency'].get_value()
            self.unityshell.set_double('launcher-opacity',opacity)
        else:
            self.ui.unsensitize(dependants)
            self.unityshell.set_double('launcher-opacity',1)
            self.ui['sc_launcher_transparency'].set_value(1)
# Check adj_launcher_transparency if this misbehaves

    def on_sc_launcher_transparency_value_changed(self,widget,udata=None):
        opacity=self.ui['sc_launcher_transparency'].get_value()
        self.unityshell.set_double('launcher-opacity',opacity)
# Check adj_launcher_transparency if this misbehaves

    def on_radio_launcher_visibility_all_toggled(self,widget,udata=None):
        if self.ui['radio_launcher_visibility_all'].get_active():
            self.unityshell.set_int('num-launchers',0)
        else:
            self.unityshell.set_int('num-launchers',1)

    def on_radio_launcher_color_cus_toggled(self,widget,udata=None):
        dependants=['color_launcher_color_cus']
        color=self.ui['color_launcher_color_cus'].get_color()
        colorhash=self.color_to_hash(color)
        if self.ui['radio_launcher_color_cus'].get_active():
            self.ui.sensitize(dependants)
            self.unityshell.set_string('background-color',colorhash)
        else:
            self.ui.unsensitize(dependants)
            self.unityshell.set_string('background-color',colorhash[:-2]+'00')

    def on_color_launcher_color_cus_color_set(self,widget,udata=None):
        color=self.ui['color_launcher_color_cus'].get_color()
        colorhash=self.color_to_hash(color)
        self.unityshell.set_string('background-color',colorhash)

    def on_spin_launcher_icon_size_value_changed(self,widget,udata=None):
        size=self.ui['spin_launcher_icon_size'].get_value()
        self.unityshell.set_int('icon-size',size)

    def on_cbox_launcher_icon_colouring_changed(self,widget,udata=None):
        mode=self.ui['cbox_launcher_icon_colouring'].get_active()
        self.unityshell.set_int('backlight-mode',mode)

    def on_sw_launcher_show_desktop_active_notify(self,widget,udata=None):
        fav=self.launcher.get_strv('favorites')
        desktop="unity://desktop-icon"
        if self.ui['sw_launcher_show_desktop'].get_active():
            if desktop not in fav:
                fav.append(desktop)
                self.launcher.set_strv('favorites',fav)
        else:
            if desktop in fav:
                fav.remove(desktop)
                self.launcher.set_strv('favorites',fav)

# TODO : RESET handler
# ---------- END Launcher -------

# ---------- BEGIN DASH

    def on_sw_dash_blur_active_notify(self,widget,udata=None):
        dependants=['radio_dash_blur_smart',
                    'radio_dash_blur_static',
                    'l_dash_blur']

        if self.ui['sw_dash_blur'].get_active():
            self.ui.sensitize(dependants)
            self.unityshell.set_int('dash-blur-experimental',1)

        else:
            self.ui.unsensitize(dependants)
            self.unityshell.set_int('dash-blur-experimental',0)

    def on_radio_dash_blur_smart_toggled(self,button,udata=None):
        mode=1 if button.get_active() else 2
        self.unityshell.set_int('dash-blur-experimental',mode)


#-----BEGIN: Panel -----

    def on_sw_appmenu_autohide_active_notify(self,widget,udata=None):
        dependants=['spin_menu_visible','l_menu_visible']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)

    # selective selection in unity-panel  part 2

    def on_sw_transparent_panel_active_notify(self,widget,udata=None):
        dependants=['sc_panel_transparency','l_transparent_panel','check_panel_opaque']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)
            self.unityshell.set_double('panel-opacity',1.00)
            self.ui['sc_panel_transparency'].set_value(1.00)

    def on_sc_panel_transparency_value_changed(self,widget,udata=None):
        panel_transparency=widget.get_value()
        self.unityshell.set_double('panel-opacity',panel_transparency)

    def on_check_panel_opaque_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean('panel-opacity-maximized-toggle',True)
        else:
            self.unityshell.set_boolean('panel-opacity-maximized-toggle',False)


    def on_check_indicator_username_toggled(self,widget,udata=None):

        if widget.get_active():
            self.session.set_boolean('show-real-name-on-panel',True)
        else:
            self.session.set_boolean('show-real-name-on-panel',False)


    def on_check_indicator_batterytime_toggled(self,widget,udata=None):

        if widget.get_active():
            self.power.set_boolean('show-time',True)
        else:
            self.power.set_boolean('show-time',False)

    def on_cbox_formattime_changed(self, widget, udata=None):

        mode = self.ui['cbox_formattime'].get_active()

        if mode == 0:
            self.datetime.set_string('time-format', '12-hour')
        elif mode == 1:
            self.datetime.set_string('time-format', '24-hour')

    def on_cbox_time_seconds_changed(self, widget, udata=None):

        mode = self.ui['cbox_time_seconds'].get_active()

        if mode == 0:
            self.datetime.set_boolean('show-seconds', True)
        else:
            self.datetime.set_boolean('show-seconds', False)


#-----BEGIN: Switcher-----

    def on_check_switchwindows_all_workspaces_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean('alt-tab-bias-viewport',True)

        else:
            self.unityshell.set_boolean('alt-tab-bias-viewport',False)


    def on_check_switcher_showdesktop_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean("disable-show-desktop",False)

        else:
            self.unityshell.set_boolean("disable-show-desktop",True)

    def on_check_minimizedwindows_switch_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean("show-minimized-windows",True)

        else:
            self.unityshell.set_boolean("show-minimized-windows",False)

    def on_check_autoexposewindows_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean('alt-tab-timeout',True)

        else:
            self.unityshell.set_boolean('alt-tab-timeout',False)

    # keyboard widgets in unity-windows-switcher

    def on_craccel_unity_switcher_windows_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_unity_switcher_windows_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)
        # Python has no switch statement, right?

        if path == '0':
            self.unityshell.set_string('alt-tab-forward', accel)
        elif path == '1':
            self.unityshell.set_string('alt-tab-prev', accel)
        elif path == '2':
            self.unityshell.set_string('alt-tab-forward-all', accel)
        elif path == '3':
            self.unityshell.set_string('alt-tab-prev-all', accel)
        elif path == '4':
            self.unityshell.set_string('alt-tab-right', accel)
        elif path == '5':
            self.unityshell.set_string('alt-tab-left', accel)
        elif path == '6':
            self.unityshell.set_string('alt-tab-detail-start', accel)
        elif path == '7':
            self.unityshell.set_string('alt-tab-detail-stop', accel)
        elif path == '8':
            self.unityshell.set_string('alt-tab-next-window', accel)
        elif path == '9':
            self.unityshell.set_string('alt-tab-prev-window', accel)

    def on_craccel_unity_switcher_windows_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_switcher_windows_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        if path == '0':
            self.unityshell.set_string('alt-tab-forward', "Disabled")
        elif path == '1':
            self.unityshell.set_string('alt-tab-prev', "Disabled")
        elif path == '2':
            self.unityshell.set_string('alt-tab-forward-all', "Disabled")
        elif path == '3':
            self.unityshell.set_string('alt-tab-prev-all', "Disabled")
        elif path == '4':
            self.unityshell.set_string('alt-tab-right', "Disabled")
        elif path == '5':
            self.unityshell.set_string('alt-tab-left', "Disabled")
        elif path == '6':
            self.unityshell.set_string('alt-tab-detail-start', "Disabled")
        elif path == '7':
            self.unityshell.set_string('alt-tab-detail-stop', "Disabled")
        elif path == '8':
            self.unityshell.set_string('alt-tab-next-window', "Disabled")
        elif path == '9':
            self.unityshell.set_string('alt-tab-prev-window', "Disabled")

    # keyboard widgets in unity-launcher-switcher

    def on_craccel_unity_switcher_launcher_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_unity_switcher_launcher_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)
        # Python has no switch statement, right?

        if path == '0':
            self.unityshell.set_string('launcher-switcher-forward', accel)
        else:
            self.unityshell.set_string('launcher-switcher-prev', accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_switcher_launcher_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        if path == '0':
            self.unityshell.set_string('launcher-switcher-forward', "Disabled")
        else:
            self.unityshell.set_string('launcher-switcher-prev', "Disabled")

    def on_b_unity_switcher_reset_clicked(self, widget):
        self.unityshell.reset('alt-tab-bias-viewport')
        self.unityshell.reset('disable-show-desktop')
        self.unityshell.reset('show-minimized-windows')
        self.unityshell.reset('alt-tab-timeout')
        self.unityshell.reset('alt-tab-forward')
        self.unityshell.reset('alt-tab-prev')
        self.unityshell.reset('alt-tab-forward-all')
        self.unityshell.reset('alt-tab-prev-all')
        self.unityshell.reset('alt-tab-right')
        self.unityshell.reset('alt-tab-left')
        self.unityshell.reset('alt-tab-detail-start')
        self.unityshell.reset('alt-tab-detail-stop')
        self.unityshell.reset('alt-tab-next-window')
        self.unityshell.reset('alt-tab-prev-window')
        self.unityshell.reset('launcher-switcher-forward')
        self.unityshell.reset('launcher-switcher-prev')
        self.refresh()



#-----BEGIN: Additional -----

    def on_check_shortcuts_hints_overlay_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean('shortcut-overlay',True)

        else:
            self.unityshell.set_boolean('shortcut-overlay',False)


    # keyboard widgets in unity-additional

    def on_craccel_unity_additional_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        # Glade has a habit of swapping arguments. beware.
        model=self.ui['list_unity_additional_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

        # Python has no switch statement, right?

        if path == '0':
            self.unityshell.set_string('show-hud', accel)
        elif path == '1':
            self.unityshell.set_string('show-launcher', accel)
        elif path == '2':
            self.unityshell.set_string('execute-command', accel)
        elif path == '3':
            self.unityshell.set_string('keyboard-focus', accel)
        else:
            self.unityshell.set_string('panel-first-menu', accel)

    def on_craccel_unity_additional_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_additional_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        if path == '0':
            self.unityshell.set_string('show-hud', "Disabled")
        elif path == '1':
            self.unityshell.set_string('show-launcher', "Disabled")
        elif path == '2':
            self.unityshell.set_string('execute-command', "Disabled")
        elif path == '3':
            self.unityshell.set_string('keyboard-focus', "Disabled")
        else:
            self.unityshell.set_string('panel-first-menu', "Disabled")

    def on_b_unity_additional_reset_clicked(self, widget):
        self.unityshell.reset('shortcut-overlay')
        self.unityshell.reset('show-hud')
        self.unityshell.reset('show-launcher')
        self.unityshell.reset('execute-command')
        self.unityshell.reset('keyboard-focus')
        self.unityshell.reset('panel-first-menu')
        self.refresh()

if __name__=='__main__':
# Fire up the Engines
    Unitysettings()
