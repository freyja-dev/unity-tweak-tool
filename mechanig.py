#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Team:
#   J Phani Mahesh <phanimahesh@gmail.com> 
#   Barneedhar (jokerdino) <barneedhar@ubuntu.com> 
#   Amith KK <amithkumaran@gmail.com>
#   Georgi
#   Sam
#
#  TODO : ask George and Sam their preferred display names and mail ids
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
# TODO : Change all references below to use the above  ones

#=====================================================================#
#                                Helpers                              #
#=====================================================================#
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
# will push once complete.

##########################################################
# TODO : Dont trust glade to pass the objects properly.
# Always add required references to init and use them.
# That way, mechanig can resist glade stupidity

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
        dependants=['radio_reveal_left','radio_reveal_topleft','sc_reveal_sensitivity','l_launcher_reveal','l_launcher_reveal_sensitivity']
        if self.ui['sw_launcher_hidemode'].get_active():
            self.unityshell.set_int("launcher-hide-mode",1)
            self.ui.sensitize(dependants)
        else:
            self.unityshell.set_int("launcher-hide-mode",0)
            self.ui.unsensitize(dependants)

    def on_radio_reveal_left_toggled(self,button,udata=None):
        mode=0 if button.get_active() else 1
        self.unityshell.set_int('reveal-trigger',mode)
#--- SNIP: buggy code not committed ---





# selective selection in unity-launcher - part 2
    
    def on_sw_launcher_transparent_active_notify(self,widget,udata=None):
        l_launcher_transparency_scale = builder.get_object('l_launcher_transparency_scale')
        sc_launcher_transparency = builder.get_object('sc_launcher_transparency')
        if sw_launcher_transparent.get_active() == True:
            l_launcher_transparency_scale.set_sensitive(True)
            sc_launcher_transparency.set_sensitive(True)
            
        else:
            l_launcher_transparency_scale.set_sensitive(False)
            sc_launcher_transparency.set_sensitive(False)
            
    # selective selection in unity-launcher - part 3
    
    def on_radio_launcher_color_cus_active_notify(self,widget,udata=None):
        color_launcher_color_cus  = builder.get_object('color_launcher_color_cus')
        if radio_launcher_color_cus.get_active() == True:
            color_launcher_color_cus.set_sensitive(True)
            
        else:
            color_launcher_color_cus.set_sensitive(False)   
   
    # selective selection in unity-dash - part 1
   
    def on_sw_dash_blur_active_notify(self,widget,udata=None):
        radio_dash_blur_smart = builder.get_object('radio_dash_blur_smart')
        radio_dash_blur_static = builder.get_object('radio_dash_blur_static')
        l_dash_blur = builder.get_object('l_dash_blur')
        
        if sw_dash_blur.get_active() == True:
            radio_dash_blur_smart.set_sensitive(True)
            radio_dash_blur_static.set_sensitive(True)
            l_dash_blur.set_sensitive(True)
        
        else:
            radio_dash_blur_smart.set_sensitive(False)
            radio_dash_blur_static.set_sensitive(False) 
            l_dash_blur.set_sensitive(False)
      
      # selective selection in unity-dash - part 2
      
    def on_radio_dash_color_cus_active_notify(self,widget,udata=None):
        color_dash_color_cus = builder.get_object('color_dash_color_cus')
        
        if radio_dash_color_cus.get_active() == True:
            color_dash_color_cus.set_sensitive(True)
            
        else:
            color_dash_color_cus.set_sensitive(False)   # selective selection in unity-launcher - part 2
    
    def on_sw_launcher_transparent_active_notify(self,widget,udata=None):
        l_launcher_transparency_scale = builder.get_object('l_launcher_transparency_scale')
        sc_launcher_transparency = builder.get_object('sc_launcher_transparency')
        if sw_launcher_transparent.get_active() == True:
            l_launcher_transparency_scale.set_sensitive(True)
            sc_launcher_transparency.set_sensitive(True)
            
        else:
            l_launcher_transparency_scale.set_sensitive(False)
            sc_launcher_transparency.set_sensitive(False)
            
    # selective selection in unity-launcher - part 3
    
    def on_radio_launcher_color_cus_active_notify(self,widget,udata=None):
        color_launcher_color_cus  = builder.get_object('color_launcher_color_cus')
        if radio_launcher_color_cus.get_active() == True:
            color_launcher_color_cus.set_sensitive(True)
            
        else:
            color_launcher_color_cus.set_sensitive(False)   
   
    # selective selection in unity-dash - part 1
   
    def on_sw_dash_blur_active_notify(self,widget,udata=None):
        radio_dash_blur_smart = builder.get_object('radio_dash_blur_smart')
        radio_dash_blur_static = builder.get_object('radio_dash_blur_static')
        l_dash_blur = builder.get_object('l_dash_blur')
        
        if sw_dash_blur.get_active() == True:
            radio_dash_blur_smart.set_sensitive(True)
            radio_dash_blur_static.set_sensitive(True)
            l_dash_blur.set_sensitive(True)
        
        else:
            radio_dash_blur_smart.set_sensitive(False)
            radio_dash_blur_static.set_sensitive(False) 
            l_dash_blur.set_sensitive(False)
      
      # selective selection in unity-dash - part 2
      
    def on_radio_dash_color_cus_active_notify(self,widget,udata=None):
        color_dash_color_cus = builder.get_object('color_dash_color_cus')
        
        if radio_dash_color_cus.get_active() == True:
            color_dash_color_cus.set_sensitive(True)
            
        else:
            color_dash_color_cus.set_sensitive(False)





if __name__=='__main__':
# Fire up the Engines
    Mechanig()

