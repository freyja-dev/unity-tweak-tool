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

from gi.repository import Gtk,Gio
from ui import ui

class Compizsettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = 'compiz.ui'
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['nb_compizsettings']
        self.page.unparent()


# GSettings objects go here
        self.unityshell=self.plugin('unityshell')
        self.desktop=self.gnome('nautilus.desktop')
        self.background=self.gnome('desktop.background')
        self.launcher=self.unity('Launcher')
        self.opengl=self.plugin('opengl')
        self.core=self.plugin('core')
        self.scale=self.plugin('scale')
        
        self.builder.connect_signals(self)
        
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
        self.ui['cbox_opengl'].set_active(self.opengl.get_int('texture-filter'))
        self.ui['check_synctovblank'].set_active(self.opengl.get_boolean('sync-to-vblank'))    


        hsize=self.core.get_int('hsize')
        vsize=self.core.get_int('vsize')
        
        if hsize >= 1 or vsize >= 1:
            self.ui['sw_workspace_switcher'].set_active(True)
        else:
            self.ui['sw_workspace_switcher'].set_active(False)

        self.ui['spin_horizontal_desktop'].set_value(hsize)
        self.ui['spin_vertical_desktop'].set_value(vsize)
        
        
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

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, mechanig can resist glade stupidity.            |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/

#=====BEGIN: Compiz settings=====
#-----BEGIN: General -----

     # selective sensitivity in compiz - general

    def on_sw_compiz_zoom_active_notify(self,widget,udata=None):
        dependants=['radio_zoom_type_standard','radio_zoom_type_lg','l_compiz_zoom_type']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)



    # keyboard widgets in compiz-general-zoom

    def on_craccel_compiz_general_zoom_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_general_zoom_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)
    def on_craccel_compiz_general_zoom_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_general_zoom_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")


    #-----General: OpenGL

    def on_cbox_opengl_changed(self,widget,udata=None):
        mode=self.ui['cbox_opengl'].get_active()
        self.opengl.set_int('texture-filter',mode)    

    def on_check_synctovblank_toggled(self,widget,udata=None):
        self.opengl.set_boolean('sync-to-vblank',self.ui['check_synctovblank'].get_active())

    # keyboard widgets in compiz-general-keys

    def on_craccel_compiz_general_keys_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_general_keys_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_general_keys_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_general_keys_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")

#-----BEGIN: Workspaces -----

    # selective sensitivity in compiz - workspaces

    def on_sw_workspace_switcher_active_notify(self,widget,udata=None):
        dependants=['l_horizontal_desktop',
                    'l_vertical_desktop',
                    'spin_horizontal_desktop',
                    'spin_vertical_desktop']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)
            self.core.set_int('hsize',1)
            self.core.set_int('vsize',1)
            self.ui['spin_horizontal_desktop'].set_value(1)
            self.ui['spin_vertical_desktop'].set_value(1)
            #self.refresh()
            
            
    def on_spin_horizontal_desktop_value_changed(self,widget,udata=None):
        hsize=self.ui['spin_horizontal_desktop'].get_value()
        self.core.set_int('hsize',hsize)
    
    def on_spin_vertical_desktop_value_changed(self,widget,udata=None):
        vsize=self.ui['spin_vertical_desktop'].get_value()
        self.core.set_int('vsize',vsize)
        
    # keyboard widgets in compiz-workspace

    def on_craccel_compiz_workspace_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_workspace_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_workspace_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")


    # compiz hotcorner linked button
    def on_lb_configure_hot_corner_activate_link(self,udata):
        self.ui['nb_compizsettings'].set_current_page(4)





#-----BEGIN: Windows Spread -----

    # selective sensitivity in compiz - windows spread

    def on_sw_windows_spread_active_notify(self,widget,udata=None):
        dependants=['l_compiz_spacing',
                    'spin_compiz_spacing',
                    'check_overlay_emblem',
                    'check_click_desktop',
                    'scrolledwindow_compiz_window_spread']

        if widget.get_active():
            self.ui.sensitize(dependants)
            self.scale.set_string('initiate-key','<Super>W')

        else:
            self.ui.unsensitize(dependants)
            self.scale.set_string('initiate-key','Disabled')

    def on_spin_compiz_spacing_value_changed(self,widget):
        self.scale.set_int('spacing',self.ui['spin_compiz_spacing'].get_value())

    def on_check_overlay_emblem_toggled(self,widget):
        if self.ui['check_overlay_emblem'].get_active():
            self.scale.set_int('overlay-icon',1)
        else:
            self.scale.set_int('overlay-icon',0)
    def on_check_click_desktop_toggled(self,widget):
    
        if self.ui['check_click_desktop'].get_active():
            self.scale.set_boolean('show-desktop',True)
        else:
            self.scale.set_boolean('show-desktop',False)

    # keyboard widgets in compiz-windows-spread

    def on_craccel_compiz_windows_spread_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_windows_spread_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_windows_spread_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")


    # compiz hotcorner linked button

    def on_lb_configure_hot_corner_windows_spread_activate_link(self,udata):
        self.ui['nb_compizsettings'].set_current_page(4)


if __name__=='__main__':
# Fire up the Engines
    Compizsettings()
