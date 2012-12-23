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

from gi.repository import Gtk,Gio,Gdk
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
        self.expo=self.plugin('expo')
        self.move=self.plugin('move')
        self.zoom=self.plugin('ezoom')

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

        plugins = self.core.get_strv('active-plugins')
        if 'ezoom' in plugins:
            self.ui['sw_compiz_zoom'].set_active(True)
        else:
            self.ui['sw_compiz_zoom'].set_active(False)
        del plugins

        model = self.ui['list_compiz_general_zoom_accelerators']

        zoom_in_key = self.zoom.get_string('zoom-in-key')
        iter_zoom_in_key = model.get_iter_first()
        model.set_value(iter_zoom_in_key, 1, zoom_in_key)

        zoom_out_key = self.zoom.get_string('zoom-out-key')
        iter_zoom_out_key = model.iter_next(iter_zoom_in_key)
        model.set_value(iter_zoom_out_key, 1, zoom_out_key)

        del model, zoom_in_key, iter_zoom_in_key, zoom_out_key, iter_zoom_out_key

        self.ui['cbox_opengl'].set_active(self.opengl.get_int('texture-filter'))
        self.ui['check_synctovblank'].set_active(self.opengl.get_boolean('sync-to-vblank'))

        model = self.ui['list_compiz_general_keys_accelerators']

        close_window_key = self.core.get_string('close-window-key')
        iter_close_window_key = model.get_iter_first()
        model.set_value(iter_close_window_key, 1, close_window_key)

        initiate_key = self.move.get_string('initiate-key')
        iter_initiate_key = model.iter_next(iter_close_window_key)
        model.set_value(iter_initiate_key, 1, initiate_key)

        show_desktop_key = self.core.get_string('show-desktop-key')
        iter_show_desktop_key = model.iter_next(iter_initiate_key)
        model.set_value(iter_show_desktop_key, 1, show_desktop_key)

        del model, close_window_key, iter_close_window_key, initiate_key, iter_initiate_key, show_desktop_key, iter_show_desktop_key

        hsize=self.core.get_int('hsize')
        vsize=self.core.get_int('vsize')

        if hsize > 1 or vsize > 1:
            self.ui['sw_workspace_switcher'].set_active(True)
        else:
            self.ui['sw_workspace_switcher'].set_active(False)

        self.ui['spin_horizontal_desktop'].set_value(hsize)
        self.ui['spin_vertical_desktop'].set_value(vsize)
        del hsize, vsize

        color = self.expo.get_string('selected-color')
        valid,gdkcolor=Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_desk_outline'].set_color(gdkcolor)
        del color,valid,gdkcolor

        model = self.ui['list_compiz_workspace_accelerators']

        expo_key = self.expo.get_string('expo-key')
        iter_expo_key = model.get_iter_first()
        model.set_value(iter_expo_key, 1, expo_key)

        del model, expo_key, iter_expo_key

        plugins = self.core.get_strv('active-plugins')
        if 'scale' in plugins:
            self.ui['sw_windows_spread'].set_active(True)
        else:
            self.ui['sw_windows_spread'].set_active(False)
        del plugins

        self.ui['spin_compiz_spacing'].set_value(self.scale.get_int('spacing'))

        if self.scale.get_int('overlay-icon') >= 1:
            self.ui['check_overlay_emblem'].set_active(True)
        else:
            self.ui['check_overlay_emblem'].set_active(False)

        self.ui['check_click_desktop'].set_active(self.scale.get_boolean('show-desktop'))

        model = self.ui['list_compiz_windows_spread_accelerators']

        initiate_key = self.scale.get_string('initiate-key')
        iter_initiate_key = model.get_iter_first()
        model.set_value(iter_initiate_key, 1, initiate_key)

        initiate_all_key = self.scale.get_string('initiate-all-key')
        iter_initiate_all_key = model.iter_next(iter_initiate_key)
        model.set_value(iter_initiate_all_key, 1, initiate_all_key)

        del model, initiate_key, iter_initiate_key, initiate_all_key, iter_initiate_all_key

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
        dependants=['l_default_zoom_level',
                    'sc_zoom_level',
                    'scrolledwindow_compiz_general_zoom']

        plugins = self.core.get_strv('active-plugins')

        if widget.get_active():
            self.ui.sensitize(dependants)
            if 'ezoom' not in plugins:
                plugins.append('ezoom')
                self.core.set_strv('active-plugins', plugins)

        else:
            self.ui.unsensitize(dependants)
            if 'ezoom' in plugins:
                plugins.remove('ezoom')
                self.core.set_strv('active-plugins', plugins)

    def on_sc_zoom_level_value_changed(self, widget, udata=None):
        return True

    # keyboard widgets in compiz-general-zoom

    def on_craccel_compiz_general_zoom_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_general_zoom_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)
        if path == '0':
            self.zoom.set_string('zoom-in-key',accel)
        elif path == '1':
            self.zoom.set_string('zoom-out-key',accel)

    def on_craccel_compiz_general_zoom_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_general_zoom_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        if path == '0':
            self.zoom.set_string('zoom-in-key',"Disabled")
        elif path == '1':
            self.zoom.set_string('zoom-out-key',"Disabled")

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
        if path == '0':
            self.core.set_string('close-window-key',accel)
        elif path == '1':
            self.move.set_string('initiate-key',accel)
        else:
            self.core.set_string('show-desktop-key',accel)

    def on_craccel_compiz_general_keys_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_general_keys_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        if path == '0':
            self.core.set_string('close-window-key',"Disabled")
        elif path == '1':
            self.move.set_string('initiate-key',"Disabled")
        else:
            self.core.set_string('show-desktop-key',"Disabled")

    def on_b_compiz_general_reset_clicked(self, widget):
        self.core.reset('active-plugins')
        self.zoom.reset('zoom-in-key')
        self.zoom.reset('zoom-out-key')
        self.opengl.reset('texture-filter')
        self.opengl.reset('sync-to-vblank')
        self.core.reset('close-window-key')
        self.move.reset('initiate-key')
        self.core.reset('show-desktop-key')
        self.refresh()

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

    def on_spin_horizontal_desktop_value_changed(self,widget,udata=None):
        hsize=self.ui['spin_horizontal_desktop'].get_value()
        self.core.set_int('hsize',hsize)

    def on_spin_vertical_desktop_value_changed(self,widget,udata=None):
        vsize=self.ui['spin_vertical_desktop'].get_value()
        self.core.set_int('vsize',vsize)

    def on_color_desk_outline_color_set(self,widget,udata=None):
        color=self.ui['color_desk_outline'].get_color()
        colorhash=self.color_to_hash(color)
        self.expo.set_string('selected-color',colorhash)

    # keyboard widgets in compiz-workspace

    def on_craccel_compiz_workspace_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        model=self.ui['list_compiz_workspace_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)
        self.expo.set_string('expo-key',accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_workspace_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        self.expo.set_string('expo-key',"Disabled")


    # compiz hotcorner linked button
    def on_lb_configure_hot_corner_activate_link(self,udata):
        self.ui['nb_compizsettings'].set_current_page(4)

    def on_b_compiz_workspace_reset_clicked(self, widget):
        self.core.reset('hsize')
        self.core.reset('vsize')
        self.expo.reset('selected-color')
        self.expo.reset('expo-key')
        self.refresh()



#-----BEGIN: Windows Spread -----

    # selective sensitivity in compiz - windows spread

    def on_sw_windows_spread_active_notify(self,widget,udata=None):
        dependants=['l_compiz_spacing',
                    'spin_compiz_spacing',
                    'check_overlay_emblem',
                    'check_click_desktop',
                    'scrolledwindow_compiz_window_spread']

        plugins = self.core.get_strv('active-plugins')

        # XXX: Playing with this switch can crash Unity and/or Compiz
        if widget.get_active():
            self.ui.sensitize(dependants)
            if 'scale' not in plugins:
                plugins.append('scale')
                self.core.set_strv('active-plugins', plugins)

        else:
            self.ui.unsensitize(dependants)
            if 'scale' in plugins:
                plugins.remove('scale')
                self.core.set_strv('active-plugins', plugins)

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
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        if path == '0':
            self.scale.set_string("initiate-key",accel)
        else:
            self.scale.set_string("initiate-all-key", accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model=None):
        model=self.ui['list_compiz_windows_spread_accelerators']
        iter = model.get_iter(path)
        model.set_value(iter, 1, "Disabled")
        if path == '0':
            self.scale.set_string("initiate-key","Disabled")
        else:
            self.scale.set_string("initiate-all-key", "Disabled")

    # compiz hotcorner linked button

    def on_lb_configure_hot_corner_windows_spread_activate_link(self,udata):
        self.ui['nb_compizsettings'].set_current_page(4)

    def on_b_compiz_windows_spread_reset_clicked(self,widget):
        self.core.reset('active-plugins')
        self.scale.reset('spacing')
        self.scale.reset('overlay-icon')
        self.scale.reset('show-desktop')
        self.scale.reset('initiate-key')
        self.scale.reset('initiate-all-key')
        self.refresh()

if __name__=='__main__':
# Fire up the Engines
    Compizsettings()
