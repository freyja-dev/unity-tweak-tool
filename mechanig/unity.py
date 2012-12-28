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

from gi.repository import Gtk, Gio, Gdk

from .ui import ui
from . import settings
from . import gsettings

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

        self.refresh()

#=====================================================================#
#                                Helpers                              #
#=====================================================================#
    def refresh(self):
        '''Reads the current config and refreshes the displayed values'''
    # Launcher
        dependants = ['radio_reveal_left', 
                    'radio_reveal_topleft', 
                    'sc_reveal_sensitivity', 
                    'l_launcher_reveal', 
                    'l_launcher_reveal_sensitivity']
        if gsettings.unityshell.get_int('launcher-hide-mode'):
            self.ui['sw_launcher_hidemode'].set_active(True)
            self.ui.sensitize(dependants)
        else:
            self.ui['sw_launcher_hidemode'].set_active(False)
            self.ui.unsensitize(dependants)
        del dependants
# Preferring readability over optimisations.
# I am aware of the redundancy and the better "[not] bool(value)"
        self.ui['radio_reveal_left'].set_active(True if gsettings.unityshell.get_int('reveal-trigger') is 0 else False)
        self.ui['radio_reveal_topleft'].set_active(True if gsettings.unityshell.get_int('reveal-trigger') is 1 else False)
        self.ui['sc_reveal_sensitivity'].set_value(gsettings.unityshell.get_double('edge-responsiveness'))

        dependants = ['l_launcher_transparency_scale', 
                    'sc_launcher_transparency']
        opacity = gsettings.unityshell.get_double('launcher-opacity')
        if opacity == 1:
            self.ui['sw_launcher_transparent'].set_active(False)
            self.ui.unsensitize(dependants)
        else:
            self.ui['sw_launcher_transparent'].set_active(True)
            self.ui.sensitize(dependants)
        self.ui['sc_launcher_transparency'].set_value(opacity)
        del dependants
        del opacity

        mode = gsettings.unityshell.get_int('num-launchers')
        self.ui['radio_launcher_visibility_all'].set_active(True if mode is 0 else False)
        self.ui['radio_launcher_visibility_primary'].set_active(True if mode is 1 else False)
        del mode

        color = gsettings.unityshell.get_string('background-color')
        if color.endswith('00'):
            self.ui['radio_launcher_color_cham'].set_active(True)
            self.ui.unsensitize(['color_launcher_color_cus'])
        else:
            self.ui['radio_launcher_color_cus'].set_active(True)
            self.ui.sensitize(['color_launcher_color_cus'])
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_launcher_color_cus'].set_color(gdkcolor)
        del color, valid, gdkcolor

        self.ui['spin_launcher_icon_size'].set_value(gsettings.unityshell.get_int('icon-size'))

        self.ui['cbox_launcher_icon_colouring'].set_active(gsettings.unityshell.get_int('backlight-mode'))

        self.ui['sw_launcher_show_desktop'].set_active(True if 'unity://desktop-icon' in gsettings.launcher.get_strv('favorites') else False)


        # Unity dash settings

        dash_blur = gsettings.unityshell.get_int('dash-blur-experimental')

        dependants = ['radio_dash_blur_smart', 
                    'radio_dash_blur_static', 
                    'l_dash_blur_type']

        if dash_blur == 0:
            self.ui['sw_dash_blur'].set_active(False)
            self.ui.unsensitize(dependants)

        elif dash_blur == 1:
            self.ui['sw_dash_blur'].set_active(True)
            self.ui.sensitize(dependants)
            self.ui['radio_dash_blur_static'].set_active(True)

        else:
            self.ui['sw_dash_blur'].set_active(True)
            self.ui.sensitize(dependants)
            self.ui['radio_dash_blur_smart'].set_active(True)

        del dependants

        # Refreshing Unity panel settings

        self.ui['spin_menu_visible'].set_value(gsettings.unityshell.get_int('menus-discovery-duration'))

        dependants = ['l_transparent_panel', 
                    'sc_panel_transparency', 
                    'check_panel_opaque']
        opacity = gsettings.unityshell.get_double('panel-opacity')
        if opacity == 1:
            self.ui['sw_transparent_panel'].set_active(False)
            self.ui.unsensitize(dependants)
        else:
            self.ui['sw_transparent_panel'].set_active(True)
            self.ui.sensitize(dependants)
        self.ui['sc_panel_transparency'].set_value(opacity)
        del dependants
        del opacity

        self.ui['check_indicator_username'].set_active(gsettings.session.get_boolean('show-real-name-on-panel'))
        self.ui['check_indicator_batterytime'].set_active(gsettings.power.get_boolean('show-time'))

        self.ui['check_panel_opaque'].set_active(gsettings.unityshell.get_boolean('panel-opacity-maximized-toggle'))

        time_format = gsettings.datetime.get_string('time-format')

        if time_format == '12-hour':
            self.ui['cbox_formattime'].set_active(0)
        elif time_format == '24-hour':
            self.ui['cbox_formattime'].set_active(1)
        else:
            self.ui['cbox_formattime'].set_active(2)
        del time_format

        if gsettings.datetime.get_boolean('show-seconds') is True:
            self.ui['cbox_time_seconds'].set_active(0)
        else:
            self.ui['cbox_time_seconds'].set_active(1)

        # Refreshing Unity switcher settings

        self.ui['check_switchwindows_all_workspaces'].set_active(gsettings.unityshell.get_boolean('alt-tab-bias-viewport'))
        self.ui['check_switcher_showdesktop'].set_active(True if gsettings.unityshell.get_boolean('disable-show-desktop')is False else False)
        self.ui['check_minimizedwindows_switch'].set_active(gsettings.unityshell.get_boolean('show-minimized-windows'))
        self.ui['check_autoexposewindows'].set_active(gsettings.unityshell.get_boolean('alt-tab-timeout'))


        model = self.ui['list_unity_switcher_windows_accelerators']

        alt_tab_forward = gsettings.unityshell.get_string('alt-tab-forward')
        iter_alt_tab_forward = model.get_iter_first()
        model.set_value(iter_alt_tab_forward, 1, alt_tab_forward)

        alt_tab_prev = gsettings.unityshell.get_string('alt-tab-prev')
        iter_alt_tab_prev = model.iter_next(iter_alt_tab_forward)
        model.set_value(iter_alt_tab_prev, 1, alt_tab_prev)

        alt_tab_forward_all = gsettings.unityshell.get_string('alt-tab-forward-all')
        iter_alt_tab_forward_all = model.iter_next(iter_alt_tab_prev)
        model.set_value(iter_alt_tab_forward_all, 1, alt_tab_forward_all)

        alt_tab_prev_all = gsettings.unityshell.get_string('alt-tab-prev-all')
        iter_alt_tab_prev_all = model.iter_next(iter_alt_tab_forward_all)
        model.set_value(iter_alt_tab_prev_all, 1, alt_tab_prev_all)

        alt_tab_right = gsettings.unityshell.get_string('alt-tab-right')
        iter_alt_tab_right = model.iter_next(iter_alt_tab_prev_all)
        model.set_value(iter_alt_tab_right, 1, alt_tab_right)

        alt_tab_left = gsettings.unityshell.get_string('alt-tab-left')
        iter_alt_tab_left = model.iter_next(iter_alt_tab_right)
        model.set_value(iter_alt_tab_left, 1, alt_tab_left)

        alt_tab_detail_start = gsettings.unityshell.get_string('alt-tab-detail-start')
        iter_alt_tab_detail_start = model.iter_next(iter_alt_tab_left)
        model.set_value(iter_alt_tab_detail_start, 1, alt_tab_detail_start)

        alt_tab_detail_stop = gsettings.unityshell.get_string('alt-tab-detail-stop')
        iter_alt_tab_detail_stop = model.iter_next(iter_alt_tab_detail_start)
        model.set_value(iter_alt_tab_detail_stop, 1, alt_tab_detail_stop)

        alt_tab_next_window = gsettings.unityshell.get_string('alt-tab-next-window')
        iter_alt_tab_next_window = model.iter_next(iter_alt_tab_detail_stop)
        model.set_value(iter_alt_tab_next_window, 1, alt_tab_next_window)

        alt_tab_prev_window = gsettings.unityshell.get_string('alt-tab-prev-window')
       
        iter_alt_tab_prev_window = model.iter_next(iter_alt_tab_next_window)
        model.set_value(iter_alt_tab_prev_window, 1, alt_tab_prev_window)

        del model

        model = self.ui['list_unity_switcher_launcher_accelerators']

        launcher_switcher_forward = gsettings.unityshell.get_string('launcher-switcher-forward')
        iter_launcher_switcher_forward = model.get_iter_first()
        model.set_value(iter_launcher_switcher_forward, 1, launcher_switcher_forward)

        launcher_switcher_prev = gsettings.unityshell.get_string('launcher-switcher-prev')
        iter_launcher_switcher_prev = model.iter_next(iter_launcher_switcher_forward)
        model.set_value(iter_launcher_switcher_prev, 1, launcher_switcher_prev)

        del model, launcher_switcher_forward, iter_launcher_switcher_forward, launcher_switcher_prev, iter_launcher_switcher_prev


        # Refreshing Unity additional settings

        self.ui['check_shortcuts_hints_overlay'].set_active(gsettings.unityshell.get_boolean('shortcut-overlay'))

        model = self.ui['list_unity_additional_accelerators']

        show_hud = gsettings.unityshell.get_string('show-hud')
        iter_show_hud = model.get_iter_first()
        model.set_value(iter_show_hud, 1, show_hud)

        show_launcher = gsettings.unityshell.get_string('show-launcher')
        iter_show_launcher = model.iter_next(iter_show_hud)
        model.set_value(iter_show_launcher, 1, show_launcher)

        execute_command = gsettings.unityshell.get_string('execute-command')
        iter_execute_command = model.iter_next(iter_show_launcher)
        model.set_value(iter_execute_command, 1, execute_command)

        keyboard_focus = gsettings.unityshell.get_string('keyboard-focus')
        iter_keyboard_focus = model.iter_next(iter_execute_command)
        model.set_value(iter_keyboard_focus, 1, keyboard_focus)

        panel_first_menu = gsettings.unityshell.get_string('panel-first-menu')
        iter_panel_first_menu = model.iter_next(iter_keyboard_focus)
        model.set_value(iter_panel_first_menu, 1, panel_first_menu)

        del model, show_hud, iter_show_hud, show_launcher, iter_show_launcher, execute_command, iter_execute_command, keyboard_focus, iter_keyboard_focus, panel_first_menu, iter_panel_first_menu


# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.



#===== BEGIN: Unity settings ===== 
#-----BEGIN: Launcher ----------
    def on_sw_launcher_hidemode_active_notify(self, widget, udata = None):
        dependants = ['radio_reveal_left', 
                    'radio_reveal_topleft', 
                    'sc_reveal_sensitivity', 
                    'l_launcher_reveal', 
                    'l_launcher_reveal_sensitivity']
        if self.ui['sw_launcher_hidemode'].get_active():
            gsettings.unityshell.set_int("launcher-hide-mode", 1)
            self.ui.sensitize(dependants)
        else:
            gsettings.unityshell.set_int("launcher-hide-mode", 0)
            self.ui.unsensitize(dependants)

    def on_radio_reveal_left_toggled(self, button, udata = None):
        radio = self.ui['radio_reveal_left']
        mode = 0 if radio.get_active() else 1
        gsettings.unityshell.set_int('reveal-trigger', mode)

# XXX :Strictly speaking, only one of these two will suffice.
    def on_radio_reveal_topleft_toggled(self, button, udata = None):
        radio = self.ui['radio_reveal_topleft']
        mode = 0 if not radio.get_active() else 1
        gsettings.unityshell.set_int('reveal-trigger', mode)

    def on_sc_reveal_sensitivity_value_changed(self, widget, udata = None):
        slider = self.ui['sc_reveal_sensitivity']
        val = slider.get_value()
        gsettings.unityshell.set_double('edge-responsiveness', val)
# Two settings possible:
#        reveal-pressure (int, (1, 1000))
#        edge-responsiveness (double, (0.2, 8.0))
# XXX : To be discussed and changed if necessary.

    def on_sw_launcher_transparent_active_notify(self, widget, udata = None):
        dependants = ['l_launcher_transparency_scale', 
                    'sc_launcher_transparency']
        if self.ui['sw_launcher_transparent'].get_active():
            self.ui.sensitize(dependants)
            opacity = self.ui['sc_launcher_transparency'].get_value()
            gsettings.unityshell.set_double('launcher-opacity', opacity)
        else:
            self.ui.unsensitize(dependants)
            gsettings.unityshell.set_double('launcher-opacity', 1)
            self.ui['sc_launcher_transparency'].set_value(1)
# Check adj_launcher_transparency if this misbehaves

    def on_sc_launcher_transparency_value_changed(self, widget, udata = None):
        opacity = self.ui['sc_launcher_transparency'].get_value()
        gsettings.unityshell.set_double('launcher-opacity', opacity)
# Check adj_launcher_transparency if this misbehaves

    def on_radio_launcher_visibility_all_toggled(self, widget, udata = None):
        if self.ui['radio_launcher_visibility_all'].get_active():
            gsettings.unityshell.set_int('num-launchers', 0)
        else:
            gsettings.unityshell.set_int('num-launchers', 1)

    def on_radio_launcher_color_cus_toggled(self, widget, udata = None):
        dependants = ['color_launcher_color_cus']
        color = self.ui['color_launcher_color_cus'].get_color()
        colorhash = gsettings.color_to_hash(color)
        if self.ui['radio_launcher_color_cus'].get_active():
            self.ui.sensitize(dependants)
            gsettings.unityshell.set_string('background-color', colorhash)
        else:
            self.ui.unsensitize(dependants)
            gsettings.unityshell.set_string('background-color', colorhash[:-2]+'00')

    def on_color_launcher_color_cus_color_set(self, widget, udata = None):
        color = self.ui['color_launcher_color_cus'].get_color()
        colorhash = gsettings.color_to_hash(color)
        gsettings.unityshell.set_string('background-color', colorhash)

    def on_spin_launcher_icon_size_value_changed(self, widget, udata = None):
        size = self.ui['spin_launcher_icon_size'].get_value()
        gsettings.unityshell.set_int('icon-size', size)

    def on_cbox_launcher_icon_colouring_changed(self, widget, udata = None):
        mode = self.ui['cbox_launcher_icon_colouring'].get_active()
        gsettings.unityshell.set_int('backlight-mode', mode)

    def on_sw_launcher_show_desktop_active_notify(self, widget, udata = None):
        fav = gsettings.launcher.get_strv('favorites')
        desktop = "unity://desktop-icon"
        if self.ui['sw_launcher_show_desktop'].get_active():
            if desktop not in fav:
                fav.append(desktop)
                gsettings.launcher.set_strv('favorites', fav)
        else:
            if desktop in fav:
                fav.remove(desktop)
                gsettings.launcher.set_strv('favorites', fav)

# TODO : RESET handler
# ---------- END Launcher -------

# ---------- BEGIN DASH

    def on_sw_dash_blur_active_notify(self, widget, udata = None):
        dependants = ['radio_dash_blur_smart', 
                    'radio_dash_blur_static', 
                    'l_dash_blur_type']

        if self.ui['sw_dash_blur'].get_active():
            self.ui.sensitize(dependants)
            gsettings.unityshell.set_int('dash-blur-experimental', 2)
            self.ui['radio_dash_blur_smart'].set_active(True)

        else:
            self.ui.unsensitize(dependants)
            gsettings.unityshell.set_int('dash-blur-experimental', 0)

    def on_radio_dash_blur_smart_toggled(self, button, udata = None):

        mode = 2 if button.get_active() else 1
        gsettings.unityshell.set_int('dash-blur-experimental', mode)


#-----BEGIN: Panel -----

    def on_spin_menu_visible_value_changed(self, widget, udata = None):

        seconds = self.ui['spin_menu_visible'].get_value()
        gsettings.unityshell.set_int('menus-discovery-duration', seconds)


    # selective selection in unity-panel  part 1

    def on_sw_transparent_panel_active_notify(self, widget, udata = None):
        dependants = ['sc_panel_transparency', 
                    'l_transparent_panel', 
                    'check_panel_opaque']

        if widget.get_active():
            self.ui.sensitize(dependants)
            self.ui['check_panel_opaque'].set_active(True)

            # Design call from me4oslav to do the following if the switch is turned on

            if self.ui['sc_panel_transparency'].get_value() == 1.0:
                self.ui['sc_panel_transparency'].set_value(0.67)
                gsettings.unityshell.set_double('panel-opacity', 0.33)

            else:
                panel_transparency = self.ui['sc_panel_transparency'].get_value()
                gsettings.unityshell.set_double('panel-opacity', panel_transparency)

        else:
            self.ui.unsensitize(dependants)
            gsettings.unityshell.set_double('panel-opacity', 1.00)

    def on_sc_panel_transparency_value_changed(self, widget, udata = None):
        panel_transparency = widget.get_value()
        gsettings.unityshell.set_double('panel-opacity', panel_transparency)

    def on_check_panel_opaque_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.unityshell.set_boolean('panel-opacity-maximized-toggle', True)
        else:
            gsettings.unityshell.set_boolean('panel-opacity-maximized-toggle', False)


    def on_check_indicator_username_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.session.set_boolean('show-real-name-on-panel', True)
        else:
            gsettings.session.set_boolean('show-real-name-on-panel', False)


    def on_check_indicator_batterytime_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.power.set_boolean('show-time', True)
        else:
            gsettings.power.set_boolean('show-time', False)

    def on_cbox_formattime_changed(self, widget, udata = None):

        mode = self.ui['cbox_formattime'].get_active()

        if mode == 0:
            gsettings.datetime.set_string('time-format', '12-hour')
        elif mode == 1:
            gsettings.datetime.set_string('time-format', '24-hour')

    def on_cbox_time_seconds_changed(self, widget, udata = None):

        mode = self.ui['cbox_time_seconds'].get_active()

        if mode == 0:
            gsettings.datetime.set_boolean('show-seconds', True)
        else:
            gsettings.datetime.set_boolean('show-seconds', False)


#-----BEGIN: Switcher-----

    def on_check_switchwindows_all_workspaces_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.unityshell.set_boolean('alt-tab-bias-viewport', True)

        else:
            gsettings.unityshell.set_boolean('alt-tab-bias-viewport', False)


    def on_check_switcher_showdesktop_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.unityshell.set_boolean("disable-show-desktop", False)

        else:
            gsettings.unityshell.set_boolean("disable-show-desktop", True)

    def on_check_minimizedwindows_switch_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.unityshell.set_boolean("show-minimized-windows", True)

        else:
            gsettings.unityshell.set_boolean("show-minimized-windows", False)

    def on_check_autoexposewindows_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.unityshell.set_boolean('alt-tab-timeout', True)

        else:
            gsettings.unityshell.set_boolean('alt-tab-timeout', False)

    # keyboard widgets in unity-windows-switcher

    def on_craccel_unity_switcher_windows_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_unity_switcher_windows_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        # Python has no switch statement, right?

        if path == '0':
            gsettings.unityshell.set_string('alt-tab-forward', accel)
        elif path == '1':
            gsettings.unityshell.set_string('alt-tab-prev', accel)
        elif path == '2':
            gsettings.unityshell.set_string('alt-tab-forward-all', accel)
        elif path == '3':
            gsettings.unityshell.set_string('alt-tab-prev-all', accel)
        elif path == '4':
            gsettings.unityshell.set_string('alt-tab-right', accel)
        elif path == '5':
            gsettings.unityshell.set_string('alt-tab-left', accel)
        elif path == '6':
            gsettings.unityshell.set_string('alt-tab-detail-start', accel)
        elif path == '7':
            gsettings.unityshell.set_string('alt-tab-detail-stop', accel)
        elif path == '8':
            gsettings.unityshell.set_string('alt-tab-next-window', accel)
        elif path == '9':
            gsettings.unityshell.set_string('alt-tab-prev-window', accel)

    def on_craccel_unity_switcher_windows_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_unity_switcher_windows_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        if path == '0':
            gsettings.unityshell.set_string('alt-tab-forward', "Disabled")
        elif path == '1':
            gsettings.unityshell.set_string('alt-tab-prev', "Disabled")
        elif path == '2':
            gsettings.unityshell.set_string('alt-tab-forward-all', "Disabled")
        elif path == '3':
            gsettings.unityshell.set_string('alt-tab-prev-all', "Disabled")
        elif path == '4':
            gsettings.unityshell.set_string('alt-tab-right', "Disabled")
        elif path == '5':
            gsettings.unityshell.set_string('alt-tab-left', "Disabled")
        elif path == '6':
            gsettings.unityshell.set_string('alt-tab-detail-start', "Disabled")
        elif path == '7':
            gsettings.unityshell.set_string('alt-tab-detail-stop', "Disabled")
        elif path == '8':
            gsettings.unityshell.set_string('alt-tab-next-window', "Disabled")
        elif path == '9':
            gsettings.unityshell.set_string('alt-tab-prev-window', "Disabled")

    # keyboard widgets in unity-launcher-switcher

    def on_craccel_unity_switcher_launcher_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_unity_switcher_launcher_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        # Python has no switch statement, right?

        if path == '0':
            gsettings.unityshell.set_string('launcher-switcher-forward', accel)
        else:
            gsettings.unityshell.set_string('launcher-switcher-prev', accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_unity_switcher_launcher_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        if path == '0':
            gsettings.unityshell.set_string('launcher-switcher-forward', "Disabled")
        else:
            gsettings.unityshell.set_string('launcher-switcher-prev', "Disabled")

    def on_b_unity_switcher_reset_clicked(self, widget):
        gsettings.unityshell.reset('alt-tab-bias-viewport')
        gsettings.unityshell.reset('disable-show-desktop')
        gsettings.unityshell.reset('show-minimized-windows')
        gsettings.unityshell.reset('alt-tab-timeout')
        gsettings.unityshell.reset('alt-tab-forward')
        gsettings.unityshell.reset('alt-tab-prev')
        gsettings.unityshell.reset('alt-tab-forward-all')
        gsettings.unityshell.reset('alt-tab-prev-all')
        gsettings.unityshell.reset('alt-tab-right')
        gsettings.unityshell.reset('alt-tab-left')
        gsettings.unityshell.reset('alt-tab-detail-start')
        gsettings.unityshell.reset('alt-tab-detail-stop')
        gsettings.unityshell.reset('alt-tab-next-window')
        gsettings.unityshell.reset('alt-tab-prev-window')
        gsettings.unityshell.reset('launcher-switcher-forward')
        gsettings.unityshell.reset('launcher-switcher-prev')
        self.refresh()



#-----BEGIN: Additional -----

    def on_check_shortcuts_hints_overlay_toggled(self, widget, udata = None):

        if widget.get_active():
            gsettings.unityshell.set_boolean('shortcut-overlay', True)

        else:
            gsettings.unityshell.set_boolean('shortcut-overlay', False)


    # keyboard widgets in unity-additional

    def on_craccel_unity_additional_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        # Glade has a habit of swapping arguments. beware.
        model = self.ui['list_unity_additional_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)

        # Python has no switch statement, right?

        if path == '0':
            gsettings.unityshell.set_string('show-hud', accel)
        elif path == '1':
            gsettings.unityshell.set_string('show-launcher', accel)
        elif path == '2':
            gsettings.unityshell.set_string('execute-command', accel)
        elif path == '3':
            gsettings.unityshell.set_string('keyboard-focus', accel)
        else:
            gsettings.unityshell.set_string('panel-first-menu', accel)

    def on_craccel_unity_additional_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_unity_additional_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        if path == '0':
            gsettings.unityshell.set_string('show-hud', "Disabled")
        elif path == '1':
            gsettings.unityshell.set_string('show-launcher', "Disabled")
        elif path == '2':
            gsettings.unityshell.set_string('execute-command', "Disabled")
        elif path == '3':
            gsettings.unityshell.set_string('keyboard-focus', "Disabled")
        else:
            gsettings.unityshell.set_string('panel-first-menu', "Disabled")

    def on_b_unity_additional_reset_clicked(self, widget):
        gsettings.unityshell.reset('shortcut-overlay')
        gsettings.unityshell.reset('show-hud')
        gsettings.unityshell.reset('show-launcher')
        gsettings.unityshell.reset('execute-command')
        gsettings.unityshell.reset('keyboard-focus')
        gsettings.unityshell.reset('panel-first-menu')
        self.refresh()

if __name__ == '__main__':
# Fire up the Engines
    Unitysettings()
