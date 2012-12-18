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
import cairo
from math import pi, sqrt

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

# Initialise Cairo bits
        self.window_snapping_drawable = self.ui['draw_window_snapping']
        self._base_window_snapping_surface = cairo.ImageSurface.create_from_png('monitor-window-snapping.png')

        self.window_snapping_cboxes = {
            'cbox_window_snapping_top': 0,
            'cbox_window_snapping_topleft': 0,
            'cbox_window_snapping_left': 0,
            'cbox_window_snapping_bottomleft': 0,
            'cbox_window_snapping_bottom': 0,
            'cbox_window_snapping_topright': 0,
            'cbox_window_snapping_right': 0,
            'cbox_window_snapping_bottomright': 0
        }

# TODO grab active corners from the backend and set the values in
# self.window_snapping_cboxes appropriately
        for box in self.window_snapping_cboxes:
            self.ui[box].set_active(self.window_snapping_cboxes[box])
            self.ui[box].connect("changed", self.on_cbox_window_snapping_changed, box)


# GSettings objects go here
        self.unityshell=self.plugin('unityshell')
        self.desktop=self.gnome('nautilus.desktop')
        self.background=self.gnome('desktop.background')
        self.launcher=self.unity('Launcher')
        self.power=self.canonical('indicator.power')

        self.builder.connect_signals(self)

        self.refresh()

    def on_draw_window_snapping_draw (self, window, cr):
# TODO : Since this gets retrigged completely on queue_draw,
# need to have it query for active hot corners

        x1 = 16
        y1 = 16
        x2 = 284
        y2 = 200
        x3 = 116 # Top/bottom side left-corner
        y3 = 73  # Left/right side top-corner

        corner_width = 36
        side_height = 16
        left_right_width = 70
        top_bottom_width = 68

        cr.set_source_surface(self._base_window_snapping_surface)
        cr.paint()
        cr.set_source_rgba(221/255, 72/255, 20/255);

        if self.window_snapping_cboxes['cbox_window_snapping_top'] != 0:
            cr.new_path()
            cr.move_to(x3, y1)
            cr.line_to (x3 + top_bottom_width, y1)
            values = self.arc_values(top_bottom_width, side_height)
            cr.arc(x3 + (top_bottom_width / 2), y1 - values['offset'], values['radius'], pi/4 , (3 * pi)/4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_topleft'] != 0:
            cr.new_path()
            cr.move_to(x1, y1)
            cr.line_to(x1 + corner_width, y1)
            cr.arc(x1, y1, corner_width, 0, pi/2)
            cr.line_to(x1, y1)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_left'] != 0:
            cr.new_path()
            cr.move_to(x1, y3 + left_right_width)
            cr.line_to(x1, y3)
            values = self.arc_values(left_right_width, side_height)
            cr.arc(x1 - values['offset'], y3 + (left_right_width / 2), values['radius'], -pi/4, pi/4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_bottomleft'] != 0:
            cr.new_path()
            cr.move_to(x1, y2 - corner_width)
            cr.line_to(x1, y2)
            cr.line_to(x1 + corner_width, y2)
            cr.arc(x1, y2, corner_width, - pi / 2, 0)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_bottom'] != 0:
            cr.new_path()
            cr.move_to(x3 + top_bottom_width, y2)
            cr.line_to(x3, y2)
            values = self.arc_values(top_bottom_width, side_height)
            cr.arc(x3 + (top_bottom_width / 2), y2 + values['offset'], values['radius'], (5 * pi) / 4, (7 * pi) / 4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_topright'] != 0:
            cr.new_path()
            cr.move_to(x2, y1)
            cr.line_to(x2, y1 + corner_width)
            cr.arc(x2, y1, corner_width, pi / 2, pi)
            cr.line_to(x2, y1)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_right'] != 0:
            # TODO : DRAW
            cr.new_path()
            cr.move_to(x2, y3)
            cr.line_to(x2, y3 + left_right_width)
            values = self.arc_values(left_right_width, side_height)
            cr.arc(x2 + values['offset'], y3 + (left_right_width / 2), values['radius'], (3 * pi) / 4, (5 * pi) / 4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_bottomright'] != 0:
            cr.new_path()
            cr.move_to(x2, y2)
            cr.line_to(x2 - corner_width, y2)
            cr.arc(x2, y2, corner_width, pi, (3 * pi ) / 2)
            cr.line_to(x2, y2)
            cr.fill_preserve()

    def arc_values (self, length, height):
        # radius = (h^2 + 1/4 length^2)/2h
        radius = ((height**2) + (.25 * (length**2))) / (2 * height)
        return {
            'radius': radius,
            'offset': sqrt((radius**2) - ((length / 2)**2))
        }

    def on_cbox_window_snapping_changed (self, combobox, cbox_id):
        self.window_snapping_cboxes[cbox_id] = combobox.get_active()
        self.window_snapping_drawable.queue_draw()

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
        return True

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
        dependants=['l_horizontal_desktop','l_vertical_desktop','spin_horizontal_desktop','spin_vertical_desktop']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)


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
        dependants=['l_compiz_spacing','spin_compiz_spacing','check_overlay_emblem','check_click_desktop']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)


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
