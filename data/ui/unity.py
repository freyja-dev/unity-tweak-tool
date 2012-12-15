#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio
from ui import ui

class Unitysettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = 'unity.ui'
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['nb_unitysettings']
        self.page.unparent()
        self.builder.connect_signals(self)


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

      # selective selection in unity-dash - part 2

    def on_radio_dash_color_cus_active_notify(self,widget,udata=None):
        dependants=['color_dash_color_cus']

        if self.ui['radio_dash_color_cus'].get_active():
            self.ui.sensitize(dependants)
        else:
            self.ui.unsensitize(dependants)


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
            self.unityshell.set_boolean('',)


    def on_check_indicator_batterytime_toggled(self,widget,udata=None):

        if widget.get_active():
            self.power.set_boolean('show-time',True)
        else:
            self.power.set_boolean('show-time',False)


#-----BEGIN: Switcher-----

    def on_check_switchwindows_all_workspaces_toggled(self,widget,udata=None):

        if widget.get_active():
            self.unityshell.set_boolean()

        else:
            self.unityshell.set_boolean()


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
            self.unityshell.set_boolean()

        else:
            self.unityshell.set_boolean()

    # keyboard widgets in unity-windows-switcher

    def on_craccel_unity_switcher_windows_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_unity_switcher_windows_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_windows_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_switcher_windows_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")

    # keyboard widgets in unity-launcher-switcher

    def on_craccel_unity_switcher_launcher_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_unity_switcher_launcher_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_switcher_launcher_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")


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

    def on_craccel_unity_additional_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_additional_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")


if __name__=='__main__':
# Fire up the Engines
    Unitysettings()
