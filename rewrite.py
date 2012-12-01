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
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUTa
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

from gi.repository import Gtk,Gio
import os

class Mechanig ():
    def __init__(self):
        '''Handler Initialisations.
        Obtain all references here.'''
# Builder goes here
        self.builder = Gtk.Builder()
# TODO : Use os module to resolve to the full path.
        self.ui="mechanig.glade"
        self.builder.add_from_file(self.ui)

# GSettings objects go here
        self.unityshell=self.plugin('unityshell')

# Glade objects go here
        self.mechanig_main=self.obj('mechanig_main')
        self.nb_mechanig=self.obj('nb_mechanig')
        self.tool_unitysettings=self.obj('tool_unitysettings')
        self.tool_compizsettings=self.obj('tool_compizsettings')
        self.tool_themesettings=self.obj('tool_themesettings')
        self.tool_desktopsettings=self.obj('tool_desktopsettings')
        self.nb_unitysettings=self.obj('nb_unitysettings')
        self.nb_compizsettings=self.obj('nb_compizsettings')
        self.nb_themesettings=self.obj('nb_themesettings')
# Fire the engines
        self.builder.connect_signals(self)
        self.refresh()
        self.mechanig_main.connect("delete-event", Gtk.main_quit)
        self.mechanig_main.show_all()
        Gtk.main()
# TODO : Change all references below to use the above  ones

#==== Helpers =====
    def resetAllKeys(self,schema,path=None,check=False):
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

    def obj(self,obj):
        return self.builder.get_object(obj)

    def refresh(self):
        '''Reads the current config and refreshes the displayed values'''
# will push once complete.

# TODO : Dont trust glade to pass the objects properly.
# Always add required references to init and use them.
# That way, mechanig can resist glade stupidity
    '''Clicking the toolbars'''
    def on_tool_startpage_toggled(self,nb_mechanig):
        self.nb_mechanig.set_current_page(0)
    def on_tool_unitysettings_toggled(self,nb_mechanig):
        self.nb_mechanig.set_current_page(1)
    def on_tool_compizsettings_toggled(self,nb_mechanig):
        self.nb_mechanig.set_current_page(2)
    def on_tool_themesettings_toggled(self,nb_mechanig):
        self.nb_mechanig.set_current_page(3)
    def on_tool_desktopsettings_toggled(self,nb_mechanig):
        self.nb_mechanig.set_current_page(4)
        
    '''Clicking on the icons in the start page'''
     
    # unity settings on start page 
    def on_tool_launcher_clicked(self,nb_unitysettings):
        self.tool_unitysettings.set_active(True)
        self.nb_unitysettings.set_current_page(0)
    def on_tool_dash_clicked(self,nb_unitysettings):
        self.tool_unitysettings.set_active(True)
        self.nb_unitysettings.set_current_page(1)
    def on_tool_panel_clicked(self,nb_unitysettings):
        self.tool_unitysettings.set_active(True)
        self.nb_unitysettings.set_current_page(2)
    def on_tool_unity_switcher_clicked(self,nb_unitysettings):
        self.tool_unitysettings.set_active(True)
        self.nb_unitysettings.set_current_page(3)    
    def on_tool_additional_clicked(self,nb_unitysettings):
        self.tool_unitysettings.set_active(True)
        self.nb_unitysettings.set_current_page(4)    
    def on_tool_launcher_clicked(self,nb_unitysettings):
        self.tool_unitysettings.set_active(True)
        self.nb_unitysettings.set_current_page(0)
        
    # Compiz settings buttons on start page        
    def on_tool_general_clicked(self,nb_compizsettings):
        self.tool_compizsettings.set_active(True)
        self.nb_compizsettings.set_current_page(0)                        
    def on_tool_compiz_switcher_clicked(self,nb_compizsettings):
        self.tool_compizsettings.set_active(True)
        self.nb_compizsettings.set_current_page(1)
    def on_tool_windows_spread_clicked(self,nb_compizsettings):
        self.tool_compizsettings.set_active(True)
        self.nb_compizsettings.set_current_page(2)
    def on_tool_windows_snapping_clicked(self,nb_compizsettings):
        self.tool_compizsettings.set_active(True)
        self.nb_compizsettings.set_current_page(3)
    def on_tool_hotcorners_clicked(self,nb_compizsettings):
        self.tool_compizsettings.set_active(True)
        self.nb_compizsettings.set_current_page(4)
        
    # Theme settings on Start page    
    def on_tool_system_clicked(self,nb_themesettings):
        self.tool_themesettings.set_active(True)
        self.nb_themesettings.set_current_page(0)  
    def on_tool_icons_clicked(self,nb_themesettings):
        self.tool_themesettings.set_active(True)
        self.nb_themesettings.set_current_page(1) 
    def on_tool_cursors_clicked(self,nb_themesettings):
        self.tool_themesettings.set_active(True)
        self.nb_themesettings.set_current_page(2)     
    def on_tool_fonts_clicked(self,nb_themesettings):
        self.tool_themesettings.set_active(True)
        self.nb_themesettings.set_current_page(3)     
        
    # desktop settings on start page    
        
    def on_tool_desktop_clicked(self,box_settings): 
        self.tool_desktopsettings.set_active(True)
    # compiz hotcorner linked button
    
    def on_lb_configure_hot_corner_activate_link(self,nb_compizsettings):
        nb_compizsettings.set_current_page(4)
    
    def on_lb_configure_hot_corner_windows_spread_activate_link(self,nb_compizsettings):
        nb_compizsettings.set_current_page(4)    
 
    def on_craccel_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_accel_cleared(self, craccel, path, model=None):
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

#=====BEGIN: Unity settings=====
#-----BEGIN: Launcher ----------
    def on_sw_launcher_hidemode_active_notify(self,widget,udata=None):
        mode=1 if widget.get_active() else 0
        self.unityshell.set_int("launcher-hide-mode",mode)

    def on_radio_reveal_left_toggled(self,button,udata=None):
        mode=0 if button.get_active() else 1
        self.unityshell.set_int('reveal-trigger',mode)
#--- SNIP: buggy code not committed ---
# Fire up the Engines
Mechanig()
