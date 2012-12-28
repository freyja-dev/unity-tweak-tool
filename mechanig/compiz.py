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
import cairo

from gi.repository import Gtk, Gio, Gdk
from math import pi, sqrt

from .ui import ui
from . import settings
from . import gsettings

class Compizsettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = (os.path.join(settings.UI_DIR,
                                    'compiz.ui'))
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['nb_compizsettings']
        self.page.unparent()


# Initialise Cairo bits
        self.window_snapping_drawable = self.ui['draw_window_snapping']
        self._base_window_snapping_surface = cairo.ImageSurface.create_from_png(os.path.join(settings.UI_DIR, 'monitor-window-snapping.png'))

        self.window_snapping_cboxes = {
            'cbox_window_snapping_top': [0, 'top-edge-action'],
            'cbox_window_snapping_topleft': [0, 'top-left-corner-action'],
            'cbox_window_snapping_left': [0, 'left-edge-action'],
            'cbox_window_snapping_bottomleft': [0, 'bottom-left-corner-action'],
            'cbox_window_snapping_bottom': [0, 'bottom-edge-action'],
            'cbox_window_snapping_topright': [0, 'top-right-corner-action'],
            'cbox_window_snapping_right': [0, 'right-edge-action'],
            'cbox_window_snapping_bottomright': [0, 'bottom-right-corner-action']
        }

# TODO grab active corners from the backend and set the values in
# self.window_snapping_cboxes appropriately
        for box in self.window_snapping_cboxes:
            self.window_snapping_cboxes[box][0] = gsettings.grid.get_int(self.window_snapping_cboxes[box][1])
            self.ui[box].set_active(self.window_snapping_cboxes[box][0])
            self.ui[box].connect("changed", self.on_cbox_window_snapping_changed, box)

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

        if self.window_snapping_cboxes['cbox_window_snapping_top'][0] != 0:
            cr.new_path()
            cr.move_to(x3, y1)
            cr.line_to (x3 + top_bottom_width, y1)
            values = self.arc_values(top_bottom_width, side_height)
            cr.arc(x3 + (top_bottom_width / 2), y1 - values['offset'], values['radius'], pi/4 , (3 * pi)/4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_topleft'][0] != 0:
            cr.new_path()
            cr.move_to(x1, y1)
            cr.line_to(x1 + corner_width, y1)
            cr.arc(x1, y1, corner_width, 0, pi/2)
            cr.line_to(x1, y1)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_left'][0] != 0:
            cr.new_path()
            cr.move_to(x1, y3 + left_right_width)
            cr.line_to(x1, y3)
            values = self.arc_values(left_right_width, side_height)
            cr.arc(x1 - values['offset'], y3 + (left_right_width / 2), values['radius'], -pi/4, pi/4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_bottomleft'][0] != 0:
            cr.new_path()
            cr.move_to(x1, y2 - corner_width)
            cr.line_to(x1, y2)
            cr.line_to(x1 + corner_width, y2)
            cr.arc(x1, y2, corner_width, - pi / 2, 0)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_bottom'][0] != 0:
            cr.new_path()
            cr.move_to(x3 + top_bottom_width, y2)
            cr.line_to(x3, y2)
            values = self.arc_values(top_bottom_width, side_height)
            cr.arc(x3 + (top_bottom_width / 2), y2 + values['offset'], values['radius'], (5 * pi) / 4, (7 * pi) / 4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_topright'][0] != 0:
            cr.new_path()
            cr.move_to(x2, y1)
            cr.line_to(x2, y1 + corner_width)
            cr.arc(x2, y1, corner_width, pi / 2, pi)
            cr.line_to(x2, y1)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_right'][0] != 0:
            # TODO : DRAW
            cr.new_path()
            cr.move_to(x2, y3)
            cr.line_to(x2, y3 + left_right_width)
            values = self.arc_values(left_right_width, side_height)
            cr.arc(x2 + values['offset'], y3 + (left_right_width / 2), values['radius'], (3 * pi) / 4, (5 * pi) / 4)
            cr.fill_preserve()

        if self.window_snapping_cboxes['cbox_window_snapping_bottomright'][0] != 0:
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
        self.window_snapping_cboxes[cbox_id][0] = combobox.get_active()
        gsettings.grid.set_int(self.window_snapping_cboxes[cbox_id][1], combobox.get_active())
        self.window_snapping_drawable.queue_draw()



#=====================================================================#
#                                Helpers                              #
#=====================================================================#

    def refresh(self):

        plugins = gsettings.core.get_strv('active-plugins')
        if 'ezoom' in plugins:
            self.ui['sw_compiz_zoom'].set_active(True)
        else:
            self.ui['sw_compiz_zoom'].set_active(False)
        del plugins

        model = self.ui['list_compiz_general_zoom_accelerators']

        zoom_in_key = gsettings.zoom.get_string('zoom-in-key')
        iter_zoom_in_key = model.get_iter_first()
        model.set_value(iter_zoom_in_key, 1, zoom_in_key)

        zoom_out_key = gsettings.zoom.get_string('zoom-out-key')
        iter_zoom_out_key = model.iter_next(iter_zoom_in_key)
        model.set_value(iter_zoom_out_key, 1, zoom_out_key)

        del model, zoom_in_key, iter_zoom_in_key, zoom_out_key, iter_zoom_out_key

        self.ui['cbox_opengl'].set_active(gsettings.opengl.get_int('texture-filter'))
        self.ui['check_synctovblank'].set_active(gsettings.opengl.get_boolean('sync-to-vblank'))

        model = self.ui['list_compiz_general_keys_accelerators']

        close_window_key = gsettings.core.get_string('close-window-key')
        iter_close_window_key = model.get_iter_first()
        model.set_value(iter_close_window_key, 1, close_window_key)

        initiate_key = gsettings.move.get_string('initiate-key')
        iter_initiate_key = model.iter_next(iter_close_window_key)
        model.set_value(iter_initiate_key, 1, initiate_key)

        show_desktop_key = gsettings.core.get_string('show-desktop-key')
        iter_show_desktop_key = model.iter_next(iter_initiate_key)
        model.set_value(iter_show_desktop_key, 1, show_desktop_key)

        del model, close_window_key, iter_close_window_key, initiate_key, iter_initiate_key, show_desktop_key, iter_show_desktop_key

        # refreshing workspace settings

        hsize = gsettings.core.get_int('hsize')
        vsize = gsettings.core.get_int('vsize')

        if hsize > 1 or vsize > 1:
            self.ui['sw_workspace_switcher'].set_active(True)
        else:
            self.ui['sw_workspace_switcher'].set_active(False)

        self.ui['spin_horizontal_desktop'].set_value(hsize)
        self.ui['spin_vertical_desktop'].set_value(vsize)
        del hsize, vsize

        color = gsettings.expo.get_string('selected-color')
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_desk_outline'].set_color(gdkcolor)
        del color, valid, gdkcolor

        model = self.ui['list_compiz_workspace_accelerators']

        expo_key = gsettings.expo.get_string('expo-key')
        iter_expo_key = model.get_iter_first()
        model.set_value(iter_expo_key, 1, expo_key)

        del model, expo_key, iter_expo_key

        # refreshing windows spread settings

        plugins = gsettings.core.get_strv('active-plugins')
        if 'scale' in plugins:
            self.ui['sw_windows_spread'].set_active(True)
        else:
            self.ui['sw_windows_spread'].set_active(False)
        del plugins

        self.ui['spin_compiz_spacing'].set_value(gsettings.scale.get_int('spacing'))

        if gsettings.scale.get_int('overlay-icon') >=  1:
            self.ui['check_overlay_emblem'].set_active(True)
        else:
            self.ui['check_overlay_emblem'].set_active(False)

        self.ui['check_click_desktop'].set_active(gsettings.scale.get_boolean('show-desktop'))

        model = self.ui['list_compiz_windows_spread_accelerators']

        initiate_key = gsettings.scale.get_string('initiate-key')
        iter_initiate_key = model.get_iter_first()
        model.set_value(iter_initiate_key, 1, initiate_key)

        initiate_all_key = gsettings.scale.get_string('initiate-all-key')
        iter_initiate_all_key = model.iter_next(iter_initiate_key)
        model.set_value(iter_initiate_all_key, 1, initiate_all_key)

        del model, initiate_key, iter_initiate_key, initiate_all_key, iter_initiate_all_key

        # refreshing window snapping settings

        plugins = gsettings.core.get_strv('active-plugins')
        if 'grid' in plugins:
            self.ui['sw_window_snapping'].set_active(True)
        else:
            self.ui['sw_window_snapping'].set_active(False)
        del plugins

        color = gsettings.grid.get_string('fill-color')
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_fill_color'].set_color(gdkcolor)
        del color, valid, gdkcolor

        color = gsettings.grid.get_string('outline-color')
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_outline_color'].set_color(gdkcolor)
        del color, valid, gdkcolor


# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, mechanig can resist glade stupidity.            |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/

# ===== BEGIN: Compiz settings =====
#-----BEGIN: General -----

     # selective sensitivity in compiz - general

    def on_sw_compiz_zoom_active_notify(self, widget, udata = None):
        dependants = ['scrolledwindow_compiz_general_zoom']

        plugins = gsettings.core.get_strv('active-plugins')

        if widget.get_active():
            self.ui.sensitize(dependants)
            if 'ezoom' not in plugins:
                plugins.append('ezoom')
                gsettings.core.set_strv('active-plugins', plugins)

        else:
            self.ui.unsensitize(dependants)
            if 'ezoom' in plugins:
                plugins.remove('ezoom')
                gsettings.core.set_strv('active-plugins', plugins)

    # keyboard widgets in compiz-general-zoom

    def on_craccel_compiz_general_zoom_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_compiz_general_zoom_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        if path  ==  '0':
            gsettings.zoom.set_string('zoom-in-key', accel)
        elif path  ==  '1':
            gsettings.zoom.set_string('zoom-out-key', accel)

    def on_craccel_compiz_general_zoom_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_compiz_general_zoom_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        if path  ==  '0':
            gsettings.zoom.set_string('zoom-in-key', "Disabled")
        elif path  ==  '1':
            gsettings.zoom.set_string('zoom-out-key', "Disabled")

    #-----General: OpenGL

    def on_cbox_opengl_changed(self, widget, udata = None):
        mode = self.ui['cbox_opengl'].get_active()
        gsettings.opengl.set_int('texture-filter', mode)

    def on_check_synctovblank_toggled(self, widget, udata = None):
        gsettings.opengl.set_boolean('sync-to-vblank', self.ui['check_synctovblank'].get_active())

    # keyboard widgets in compiz-general-keys

    def on_craccel_compiz_general_keys_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_compiz_general_keys_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        if path  ==  '0':
            gsettings.core.set_string('close-window-key', accel)
        elif path  ==  '1':
            gsettings.move.set_string('initiate-key', accel)
        else:
            gsettings.core.set_string('show-desktop-key', accel)

    def on_craccel_compiz_general_keys_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_compiz_general_keys_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        if path  ==  '0':
            gsettings.core.set_string('close-window-key', "Disabled")
        elif path  ==  '1':
            gsettings.move.set_string('initiate-key', "Disabled")
        else:
            gsettings.core.set_string('show-desktop-key', "Disabled")

    def on_b_compiz_general_reset_clicked(self, widget):
        gsettings.core.reset('active-plugins')
        gsettings.zoom.reset('zoom-in-key')
        gsettings.zoom.reset('zoom-out-key')
        gsettings.opengl.reset('texture-filter')
        gsettings.opengl.reset('sync-to-vblank')
        gsettings.core.reset('close-window-key')
        gsettings.move.reset('initiate-key')
        gsettings.core.reset('show-desktop-key')
        self.refresh()

#-----BEGIN: Workspaces -----

    # selective sensitivity in compiz - workspaces

    def on_sw_workspace_switcher_active_notify(self, widget, udata = None):
        dependants = ['l_horizontal_desktop',
                    'l_vertical_desktop',
                    'spin_horizontal_desktop',
                    'spin_vertical_desktop']

        if widget.get_active():
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)
            gsettings.core.set_int('hsize', 1)
            gsettings.core.set_int('vsize', 1)
            self.ui['spin_horizontal_desktop'].set_value(1)
            self.ui['spin_vertical_desktop'].set_value(1)

    def on_spin_horizontal_desktop_value_changed(self, widget, udata = None):
        hsize = self.ui['spin_horizontal_desktop'].get_value()
        gsettings.core.set_int('hsize', hsize)

    def on_spin_vertical_desktop_value_changed(self, widget, udata = None):
        vsize = self.ui['spin_vertical_desktop'].get_value()
        gsettings.core.set_int('vsize', vsize)

    def on_color_desk_outline_color_set(self, widget, udata = None):
        color = self.ui['color_desk_outline'].get_color()
        colorhash = self.color_to_hash(color)
        gsettings.expo.set_string('selected-color', colorhash)

    # keyboard widgets in compiz-workspace

    def on_craccel_compiz_workspace_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_compiz_workspace_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        gsettings.expo.set_string('expo-key', accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_compiz_workspace_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        gsettings.expo.set_string('expo-key', "Disabled")


    # compiz hotcorner linked button
    def on_lb_configure_hot_corner_activate_link(self, udata):
        self.ui['nb_compizsettings'].set_current_page(4)

    def on_b_compiz_workspace_reset_clicked(self, widget):
        gsettings.core.reset('hsize')
        gsettings.core.reset('vsize')
        gsettings.expo.reset('selected-color')
        gsettings.expo.reset('expo-key')
        self.refresh()



#-----BEGIN: Windows Spread -----

    # selective sensitivity in compiz - windows spread

    def on_sw_windows_spread_active_notify(self, widget, udata = None):
        dependants = ['l_compiz_spacing',
                    'spin_compiz_spacing',
                    'check_overlay_emblem',
                    'check_click_desktop',
                    'scrolledwindow_compiz_window_spread']

        plugins = gsettings.core.get_strv('active-plugins')

        # XXX: Playing with this switch can crash Unity and/or Compiz
        if widget.get_active():
            self.ui.sensitize(dependants)
            if 'scale' not in plugins:
                plugins.append('scale')
                gsettings.core.set_strv('active-plugins', plugins)

        else:
            self.ui.unsensitize(dependants)
            if 'scale' in plugins:
                plugins.remove('scale')
                gsettings.core.set_strv('active-plugins', plugins)

    def on_spin_compiz_spacing_value_changed(self, widget):
        gsettings.scale.set_int('spacing', self.ui['spin_compiz_spacing'].get_value())

    def on_check_overlay_emblem_toggled(self, widget):
        if self.ui['check_overlay_emblem'].get_active():
            gsettings.scale.set_int('overlay-icon', 1)
        else:
            gsettings.scale.set_int('overlay-icon', 0)

    def on_check_click_desktop_toggled(self, widget):

        if self.ui['check_click_desktop'].get_active():
            gsettings.scale.set_boolean('show-desktop', True)
        else:
            gsettings.scale.set_boolean('show-desktop', False)

    # keyboard widgets in compiz-windows-spread
    def on_craccel_compiz_windows_spread_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_compiz_windows_spread_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        if path  ==  '0':
            gsettings.scale.set_string("initiate-key", accel)
        else:
            gsettings.scale.set_string("initiate-all-key", accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_compiz_windows_spread_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, "Disabled")
        if path  ==  '0':
            gsettings.scale.set_string("initiate-key", "Disabled")
        else:
            gsettings.scale.set_string("initiate-all-key", "Disabled")

    # compiz hotcorner linked button

    def on_lb_configure_hot_corner_windows_spread_activate_link(self, udata):
        self.ui['nb_compizsettings'].set_current_page(4)

    def on_b_compiz_windows_spread_reset_clicked(self, widget):
        gsettings.core.reset('active-plugins')
        gsettings.scale.reset('spacing')
        gsettings.scale.reset('overlay-icon')
        gsettings.scale.reset('show-desktop')
        gsettings.scale.reset('initiate-key')
        gsettings.scale.reset('initiate-all-key')
        self.refresh()

    # Compiz - Window snapping
    def on_sw_window_snapping_active_notify(self, widget, udata=None):

        plugins = gsettings.core.get_strv('active-plugins')

        if widget.get_active():
            if 'grid' not in plugins:
                plugins.append('grid')
                gsettings.core.set_strv('active-plugins', plugins)

        else:
            if 'grid' in plugins:
                plugins.remove('grid')
                gsettings.core.set_strv('active-plugins', plugins)

    def on_color_outline_color_color_set(self, widget, udata=None):
        color = self.ui['color_outline_color'].get_color()
        colorhash = self.color_to_hash(color)
        gsettings.grid.set_string('outline-color', colorhash)

    def on_color_fill_color_color_set(self, widget, udata=None):
        color = self.ui['color_fill_color'].get_color()
        colorhash = self.color_to_hash(color)
        gsettings.grid.set_string('fill-color', colorhash)

    def on_b_compiz_windowsnapping_reset_clicked(self, widget):
        gsettings.core.reset('active-plugins')
        gsettings.core.reset('show-desktop-edge')
        gsettings.expo.reset('expo-edge')
        gsettings.grid.reset('fill-color')
        gsettings.grid.reset('outline-color')
        gsettings.grid.reset('top-edge-action')

if __name__ == '__main__':
# Fire up the Engines
    Compizsettings()
