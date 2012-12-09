#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Team:
#   J Phani Mahesh <phanimahesh@gmail.com> 
#   Barneedhar (jokerdino) <barneedhar@ubuntu.com> 
#   Amith KK <amithkumaran@gmail.com>
#   Georgi Karavasilev <motorslav@gmail.com>
#   Sam Tran <samvtran@gmail.com>
#
# Description:
#   A One-stop configuration tool for Unity.
#
# Legal Stuff:
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

from gi.repository import Gtk,Gio
import os
from ui import ui

class Mechanig ():
    def __init__(self):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade="mechanig.glade"
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui=ui(self.builder)

# GSettings objects go here
        self.unityshell=self.plugin('unityshell')

# Fire the engines
        self.builder.connect_signals(self)
        self.ui['mechanig_main'].set_resizable(False)
        self.ui['nb_mechanig'].set_show_tabs(False)
        self.refresh()
        self.ui['mechanig_main'].connect("delete-event", Gtk.main_quit)
        self.ui['mechanig_main'].show_all()
        Gtk.main()

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
    def compiz(child):
        schema='org.compiz.'+child
        return Gio.Settings(schema)

    def refresh(self):
        '''Reads the current config and refreshes the displayed values'''
        pass
# TODO : Find a clever way or set each one manually.

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, mechanig can resist glade stupidity.            |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/

# ===== Top Navigation bar =====
    def on_tool_startpage_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(0)
    def on_tool_unitysettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(1)
    def on_tool_compizsettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(2)
    def on_tool_themesettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(3)
    def on_tool_desktopsettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(4)
        
# ===== Start page =====
    # unity settings on start page 
    def on_tool_launcher_clicked(self,udata):
        self.ui['tool_unitysettings'].set_active(True)
        self.ui['nb_unitysettings'].set_current_page(0)
    def on_tool_dash_clicked(self,udata):
        self.ui['tool_unitysettings'].set_active(True)
        self.ui['nb_unitysettings'].set_current_page(1)
    def on_tool_panel_clicked(self,udata):
        self.ui['tool_unitysettings'].set_active(True)
        self.ui['nb_unitysettings'].set_current_page(2)
    def on_tool_unity_switcher_clicked(self,udata):
        self.ui['tool_unitysettings'].set_active(True)
        self.ui['nb_unitysettings'].set_current_page(3)    
    def on_tool_additional_clicked(self,udata):
        self.ui['tool_unitysettings'].set_active(True)
        self.ui['nb_unitysettings'].set_current_page(4)    
    def on_tool_launcher_clicked(self,udata):
        self.ui['tool_unitysettings'].set_active(True)
        self.ui['nb_unitysettings'].set_current_page(0)
        
    # Compiz settings buttons on start page        
    def on_tool_general_clicked(self,udata):
        self.ui['tool_compizsettings'].set_active(True)
        self.ui['nb_compizsettings'].set_current_page(0)                        
    def on_tool_compiz_switcher_clicked(self,udata):
        self.ui['tool_compizsettings'].set_active(True)
        self.ui['nb_compizsettings'].set_current_page(1)
    def on_tool_windows_spread_clicked(self,udata):
        self.ui['tool_compizsettings'].set_active(True)
        self.ui['nb_compizsettings'].set_current_page(2)
    def on_tool_windows_snapping_clicked(self,udata):
        self.ui['tool_compizsettings'].set_active(True)
        self.ui['nb_compizsettings'].set_current_page(3)
    def on_tool_hotcorners_clicked(self,udata):
        self.ui['tool_compizsettings'].set_active(True)
        self.ui['nb_compizsettings'].set_current_page(4)
        
    # Theme settings on Start page    
    def on_tool_system_clicked(self,udata):
        self.ui['tool_themesettings'].set_active(True)
        self.ui['nb_themesettings'].set_current_page(0)  
    def on_tool_icons_clicked(self,udata):
        self.ui['tool_themesettings'].set_active(True)
        self.ui['nb_themesettings'].set_current_page(1) 
    def on_tool_cursors_clicked(self,udata):
        self.ui['tool_themesettings'].set_active(True)
        self.ui['nb_themesettings'].set_current_page(2)     
    def on_tool_fonts_clicked(self,udata):
        self.ui['tool_themesettings'].set_active(True)
        self.ui['nb_themesettings'].set_current_page(3)     
        
    # desktop settings on start page    
    def on_tool_desktop_clicked(self,udata): 
        self.ui['tool_desktopsettings'].set_active(True)

#===================END OF START PAGE===================#

    # compiz hotcorner linked button
    def on_lb_configure_hot_corner_activate_link(self,udata):
        self.ui['nb_compizsettings'].set_current_page(4)
    
    def on_lb_configure_hot_corner_windows_spread_activate_link(self,udata):
        self.ui['nb_compizsettings'].set_current_page(4)

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
        model.set_value(iter, 1, None)

    # keyboard widgets in unity-panel-windows-switcher

    def on_craccel_unity_switcher_windows_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_unity_switcher_windows_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_windows_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_switcher_windows_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)
 
    # keyboard widgets in unity-panel-launcher-switcher

    def on_craccel_unity_switcher_launcher_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_unity_switcher_launcher_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_unity_switcher_launcher_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)
    # keyboard widgets in compiz-general-zoom

    def on_craccel_compiz_general_zoom_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_general_zoom_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)
    def on_craccel_compiz_general_zoom_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_general_zoom_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

    # keyboard widgets in compiz-general-keys

    def on_craccel_compiz_general_keys_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_general_keys_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_general_keys_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_general_keys_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

    # keyboard widgets in compiz-workspace

    def on_craccel_compiz_workspace_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_workspace_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_workspace_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

    # keyboard widgets in compiz-windows-spread

    def on_craccel_compiz_windows_spread_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_windows_spread_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_windows_spread_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

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

    def on_radio_reveal_topleft_toggled(self,button,udata=None):
        radio=self.ui['radio_reveal_topleft']
        mode=0 if not radio.get_active() else 1
        self.unityshell.set_int('reveal-trigger',mode)

    def on_sc_reveal_sensitivity_value_changed(self,widget,udata=None):
        slider=self.ui['sc_reveal_sensitivity']
        val=slider.get_value()
# TODO : Set the sensitivity
# Two settings possible: reveal-pressure and edge-responsiveness
# Discuss and decide which to use.

    def on_sw_launcher_transparent_active_notify(self,widget,udata=None):
        dependants=['l_launcher_transparency_scale',
                    'sc_launcher_transparency']
        if self.ui['sw_launcher_transparent'].get_active():
            self.ui.sensitize(dependants)
            self.unityshell.set_double('launcher-opacity',1)
        else:
            self.ui.unsensitize(dependants)
            opacity=self.ui['sc_launcher_transparency'].get_value()
            self.unityshell.set_double('launcher-opacity',opacity)
# Check adj_launcher_transparency if this misbehaves

    def on_sc_launcher_transparency_value_changed(self,widget,udata=None):
        opacity=self.ui['sc_launcher_transparency'].get_value()
        self.unityshell.set_double('launcher-opacity',opacity)
# Check adj_launcher_transparency if this misbehaves
        
    def on_radio_launcher_color_cus_active_notify(self,widget,udata=None):
        dependants=['color_launcher_color_cus']
        if self.ui['radio_launcher_color_cus'].get_active():
            self.ui.sensitize(dependants)
        else:
            self.ui.unsensitize(dependants)
   # TODO : Get the color and set it.

    def on_spin_launcher_icon_size_value_changed(self,udata=None):
        size=self.ui['spin_launcher_icon_size'].get_value()
        self.unityshell.set_int('icon-size',size)

# TODO : Icon colouring handler
    
    def on_sw_launcher_show_desktop_active_notify(self,widget,udata=None):
        launcher=Gio.Settings("com.canonical.Unity.Launcher")
        fav=launcher.get_strv('favorites')
        desktop="unity://desktop-icon"
        if self.ui['sw_launcher_show_desktop'].get_active():
            if desktop not in fav:
                fav.append(desktop)
                launcher.set_strv('favorites',fav)
        else:
            if desktop in fav:
                fav.remove(desktop)
                launcher.set_strv('favorites',fav)

# TODO : RESET handler
# ---------- END Launcher -------

# ---------- BEGIN DASH

    def on_sw_dash_blur_active_notify(self,widget,udata=None):
        dependants=['radio_dash_blur_smart',
                    'radio_dash_blur_static',
                    'l_dash_blur']
        
        if self.ui['sw_dash_blur'].get_active():
            self.ui.sensitize(dependants)
        else:
            self.ui.unsensitize(dependants)
      # selective selection in unity-dash - part 2
      
    def on_radio_dash_color_cus_active_notify(self,widget,udata=None):
        dependants=['color_dash_color_cus']
        
        if self.ui['radio_dash_color_cus'].get_active():
            self.ui.sensitize(dependants)
        else:
            self.ui.unsensitize(dependants)
            
            
             
#========= Begin Desktop Settings
    def on_sw_desktop_icon_active_notify(self,widget,udata=None):
        if self.ui['sw_desktop_icon'].get_active():
            pass
# TODO : Find where this setting is.

    def on_spin_iconsize_value_changed(self,udata=None):
        size=self.ui['spin_iconsize'].get_value()
# TODO : Find where this setting is.


if __name__=='__main__':
# Fire up the Engines
    Mechanig()
else:
    print("WARNING: This module is not tailored to be imported. Proceed at your own risk.")
