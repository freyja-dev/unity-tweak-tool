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
#   Angel Araya <al.arayaq@gmail.com>
#
# Description:
#   A One-stop configuration tool for Unity.
#
# Legal Stuff:
#
# This file is a part of Unity Tweak Tool
#
# Unity Tweak Tool is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# Unity Tweak Tool is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>

import os, os.path
import cairo

from gi.repository import Gtk, Gdk
from math import pi, sqrt

from UnityTweakTool.config.ui import ui
from . import unitytweakconfig
from . import gsettings

class Compizsettings ():
    def __init__(self, builder):
        self.ui = ui(builder)
        self.page = self.ui['nb_compizsettings']

        self.ui['scale_auto_raise_delay'].add_mark(500, Gtk.PositionType.BOTTOM, None)


        # Initialise Cairo bits
        self.window_snapping_drawable = self.ui['draw_window_snapping']
        self._base_window_snapping_surface = cairo.ImageSurface.create_from_png(os.path.join(unitytweakconfig.get_data_path(), 'monitor-window-snapping.png'))

        self.hotcorners_drawable = self.ui['draw_hotcorners']
        self._base_hotcorners_surface = cairo.ImageSurface.create_from_png(os.path.join(unitytweakconfig.get_data_path(), 'monitor-hotcorners.png'))

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

        self.hotcorners_cboxes = {
            'cbox_hotcorners_top': [0, 'Top'],
            'cbox_hotcorners_topleft': [0, 'TopLeft'],
            'cbox_hotcorners_left': [0, 'Left'],
            'cbox_hotcorners_bottomleft': [0, 'BottomLeft'],
            'cbox_hotcorners_bottom': [0, 'Bottom'],
            'cbox_hotcorners_topright': [0, 'TopRight'],
            'cbox_hotcorners_right': [0, 'Right'],
            'cbox_hotcorners_bottomright': [0, 'BottomRight']
        }

    def on_draw_hotcorners_draw (self, window, cr):
        self.draw_monitor(window, cr, self._base_hotcorners_surface, self.hotcorners_cboxes, 'hotcorners')

    def on_draw_window_snapping_draw (self, window, cr):
        self.draw_monitor(window, cr, self._base_window_snapping_surface, self.window_snapping_cboxes, 'window_snapping')

    def draw_monitor (self, window, cr, base_surface, corner_store, cbox_title):
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

        cr.set_source_surface(base_surface)
        cr.paint()
        cr.set_source_rgba(221/255, 72/255, 20/255)

        if corner_store['cbox_' + cbox_title + '_top'][0] != 0:
            cr.new_path()
            cr.move_to(x3, y1)
            cr.line_to (x3 + top_bottom_width, y1)
            values = self.arc_values(top_bottom_width, side_height)
            cr.arc(x3 + (top_bottom_width / 2), y1 - values['offset'], values['radius'], pi/4 , (3 * pi)/4)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_topleft'][0] != 0:
            cr.new_path()
            cr.move_to(x1, y1)
            cr.line_to(x1 + corner_width, y1)
            cr.arc(x1, y1, corner_width, 0, pi/2)
            cr.line_to(x1, y1)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_left'][0] != 0:
            cr.new_path()
            cr.move_to(x1, y3 + left_right_width)
            cr.line_to(x1, y3)
            values = self.arc_values(left_right_width, side_height)
            cr.arc(x1 - values['offset'], y3 + (left_right_width / 2), values['radius'], -pi/4, pi/4)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_bottomleft'][0] != 0:
            cr.new_path()
            cr.move_to(x1, y2 - corner_width)
            cr.line_to(x1, y2)
            cr.line_to(x1 + corner_width, y2)
            cr.arc(x1, y2, corner_width, - pi / 2, 0)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_bottom'][0] != 0:
            cr.new_path()
            cr.move_to(x3 + top_bottom_width, y2)
            cr.line_to(x3, y2)
            values = self.arc_values(top_bottom_width, side_height)
            cr.arc(x3 + (top_bottom_width / 2), y2 + values['offset'], values['radius'], (5 * pi) / 4, (7 * pi) / 4)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_topright'][0] != 0:
            cr.new_path()
            cr.move_to(x2, y1)
            cr.line_to(x2, y1 + corner_width)
            cr.arc(x2, y1, corner_width, pi / 2, pi)
            cr.line_to(x2, y1)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_right'][0] != 0:
            # TODO : DRAW
            cr.new_path()
            cr.move_to(x2, y3)
            cr.line_to(x2, y3 + left_right_width)
            values = self.arc_values(left_right_width, side_height)
            cr.arc(x2 + values['offset'], y3 + (left_right_width / 2), values['radius'], (3 * pi) / 4, (5 * pi) / 4)
            cr.fill_preserve()

        if corner_store['cbox_' + cbox_title + '_bottomright'][0] != 0:
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

    def on_cbox_hotcorners_changed (self, combobox, cbox_id):
        self.hotcorners_cboxes[cbox_id][0] = combobox.get_active()
        clear_corners = []
        if combobox.get_active() == 0:
            clear_corners = ['show_desktop', 'expo', 'window_spread']

        if combobox.get_active() == 1:
            if self.hotcorners_cboxes[cbox_id][1] not in self.hotcorner_values['show_desktop']:
                self.hotcorner_values['show_desktop'].append(self.hotcorners_cboxes[cbox_id][1])
                gsettings.core.set_string('show-desktop-edge', '|'.join(self.hotcorner_values['show_desktop']))
        else:
            clear_corners.append('show_desktop')

        if combobox.get_active() == 2:
            if self.hotcorners_cboxes[cbox_id][1] not in self.hotcorner_values['expo']:
                self.hotcorner_values['expo'].append(self.hotcorners_cboxes[cbox_id][1])
                gsettings.expo.set_string('expo-edge', '|'.join(self.hotcorner_values['expo']))
        else:
            clear_corners.append('expo')

        if combobox.get_active() == 3:
            if self.hotcorners_cboxes[cbox_id][1] not in self.hotcorner_values['window_spread']:
                self.hotcorner_values['window_spread'].append(self.hotcorners_cboxes[cbox_id][1])
                gsettings.scale.set_string('initiate-edge', '|'.join(self.hotcorner_values['window_spread']))
        else:
            clear_corners.append('window_spread')

        if combobox.get_active() == 4:
            if self.hotcorners_cboxes[cbox_id][1] not in self.hotcorner_values['all_window_spread']:
                self.hotcorner_values['all_window_spread'].append(self.hotcorners_cboxes[cbox_id][1])
                gsettings.scale.set_string('initiate-all-edge', '|'.join(self.hotcorner_values['all_window_spread']))
        else:
            clear_corners.append('all_window_spread')

        # Removing potentially conflicting bindings
        if 'show_desktop' in clear_corners and self.hotcorners_cboxes[cbox_id][1] in self.hotcorner_values['show_desktop']:
            self.hotcorner_values['show_desktop'].remove(self.hotcorners_cboxes[cbox_id][1])
            gsettings.core.set_string('show-desktop-edge', '|'.join(self.hotcorner_values['show_desktop']))
        if 'expo' in clear_corners and self.hotcorners_cboxes[cbox_id][1] in self.hotcorner_values['expo']:
            self.hotcorner_values['expo'].remove(self.hotcorners_cboxes[cbox_id][1])
            gsettings.expo.set_string('expo-edge', '|'.join(self.hotcorner_values['expo']))
        if 'window_spread' in clear_corners and self.hotcorners_cboxes[cbox_id][1] in self.hotcorner_values['window_spread']:
            self.hotcorner_values['window_spread'].remove(self.hotcorners_cboxes[cbox_id][1])
            gsettings.scale.set_string('initiate-edge', '|'.join(self.hotcorner_values['window_spread']))
        if 'all_window_spread' in clear_corners and self.hotcorners_cboxes[cbox_id][1] in self.hotcorner_values['all_window_spread']:
            self.hotcorner_values['all_window_spread'].remove(self.hotcorners_cboxes[cbox_id][1])
            gsettings.scale.set_string('initiate-all-edge', '|'.join(self.hotcorner_values['all_window_spread']))

        self.hotcorners_drawable.queue_draw()


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


        # Animations
        unminimize_value = gsettings.animation.get_strv('unminimize-effects')
        dependants = ['cbox_minimize_animation',
                    'l_minimize_animation',
                    'cbox_unminimize_animation',
                    'l_unminimize_animation']

        if unminimize_value == ['animation:None']:
            self.ui['cbox_unminimize_animation'].set_active(0)
            self.ui['switch_window_animations'].set_active(False)
            self.ui.unsensitize(dependants)
        elif unminimize_value == ['animation:Random']:
            self.ui['cbox_unminimize_animation'].set_active(1)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Curved Fold']:
            self.ui['cbox_unminimize_animation'].set_active(2)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Fade']:
            self.ui['cbox_unminimize_animation'].set_active(3)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Glide 1']:
            self.ui['cbox_unminimize_animation'].set_active(4)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Glide 2']:
            self.ui['cbox_unminimize_animation'].set_active(5)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Horizontal Folds']:
            self.ui['cbox_unminimize_animation'].set_active(6)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Magic Lamp']:
            self.ui['cbox_unminimize_animation'].set_active(7)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Magic Lamp Wavy']:
            self.ui['cbox_unminimize_animation'].set_active(8)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Sidekick']:
            self.ui['cbox_unminimize_animation'].set_active(9)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif unminimize_value == ['animation:Zoom']:
            self.ui['cbox_unminimize_animation'].set_active(10)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        else:
            self.ui['cbox_unminimize_animation'].set_active(0)
            self.ui['switch_window_animations'].set_active(False)
            self.ui.unsensitize(dependants)
        del unminimize_value

        minimize_value = gsettings.animation.get_strv('minimize-effects')

        if minimize_value == ['animation:None']:
            self.ui['cbox_minimize_animation'].set_active(0)
            self.ui['switch_window_animations'].set_active(False)
            self.ui.unsensitize(dependants)
        elif minimize_value == ['animation:Random']:
            self.ui['cbox_minimize_animation'].set_active(1)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Curved Fold']:
            self.ui['cbox_minimize_animation'].set_active(2)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Fade']:
            self.ui['cbox_minimize_animation'].set_active(3)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Glide 1']:
            self.ui['cbox_minimize_animation'].set_active(4)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Glide 2']:
            self.ui['cbox_minimize_animation'].set_active(5)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Horizontal Folds']:
            self.ui['cbox_minimize_animation'].set_active(6)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Magic Lamp']:
            self.ui['cbox_minimize_animation'].set_active(7)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Magic Lamp Wavy']:
            self.ui['cbox_minimize_animation'].set_active(8)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        elif minimize_value == ['animation:Sidekick']:
            self.ui['cbox_minimize_animation'].set_active(9)
            self.ui['switch_window_animations'].set_active(True)
        elif minimize_value == ['animation:Zoom']:
            self.ui['cbox_minimize_animation'].set_active(10)
            self.ui['switch_window_animations'].set_active(True)
            self.ui.sensitize(dependants)
        else:
            self.ui['cbox_minimize_animation'].set_active(0)
            self.ui['switch_window_animations'].set_active(False)
            self.ui.unsensitize(dependants)
        del minimize_value

        # ===== Workspace settings ===== #

        hsize = gsettings.core.get_int('hsize')
        vsize = gsettings.core.get_int('vsize')
        dependants = ['spin_horizontal_desktop',
                    'spin_vertical_desktop']

        if hsize > 1 or vsize > 1:
            self.ui['sw_workspace_switcher'].set_active(True)
            self.ui.sensitize(dependants)
        else:
            self.ui['sw_workspace_switcher'].set_active(False)
            self.ui.unsensitize(dependants)

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

        # ===== Windows Spread settings ===== #

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

        model = self.ui['list_compiz_windows_spread_accelerators']

        initiate_key = gsettings.scale.get_string('initiate-key')
        iter_initiate_key = model.get_iter_first()
        model.set_value(iter_initiate_key, 1, initiate_key)

        initiate_all_key = gsettings.scale.get_string('initiate-all-key')
        iter_initiate_all_key = model.iter_next(iter_initiate_key)
        model.set_value(iter_initiate_all_key, 1, initiate_all_key)

        del model, initiate_key, iter_initiate_key, initiate_all_key, iter_initiate_all_key

        # ===== Window Snapping settings ===== #

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

        for box in self.window_snapping_cboxes:
            self.window_snapping_cboxes[box][0] = gsettings.grid.get_int(self.window_snapping_cboxes[box][1])
            self.ui[box].set_active(self.window_snapping_cboxes[box][0])
            self.ui[box].connect("changed", self.on_cbox_window_snapping_changed, box)

        # ===== Hotcorners settings ===== #
        self.hotcorner_values = {
            'show_desktop': gsettings.core.get_string('show-desktop-edge').split('|'),
            'expo': gsettings.expo.get_string('expo-edge').split('|'),
            'window_spread': gsettings.scale.get_string('initiate-edge').split('|'),
            'all_window_spread': gsettings.scale.get_string('initiate-all-edge').split('|')
        }
        for box in self.hotcorners_cboxes:
            if self.hotcorners_cboxes[box][1] in self.hotcorner_values['show_desktop']:
                self.hotcorners_cboxes[box][0] = 1
            elif self.hotcorners_cboxes[box][1] in self.hotcorner_values['expo']:
                self.hotcorners_cboxes[box][0] = 2
            elif self.hotcorners_cboxes[box][1] in self.hotcorner_values['window_spread']:
                self.hotcorners_cboxes[box][0] = 3
            elif self.hotcorners_cboxes[box][1] in self.hotcorner_values['all_window_spread']:
                self.hotcorners_cboxes[box][0] = 4
            else:
                self.hotcorners_cboxes[box][0] = 0
            self.ui[box].set_active(self.hotcorners_cboxes[box][0])
            self.ui[box].connect("changed", self.on_cbox_hotcorners_changed, box)

        # ===== Additional settings ===== #

        # Auto raise
        self.ui['switch_auto_raise'].set_active(gsettings.wm.get_boolean('auto-raise'))
        self.ui['scale_auto_raise_delay'].set_value(gsettings.wm.get_int('auto-raise-delay'))

        # Titlebar actions
        self.ui['cbox_double_click'].set_active(gsettings.wm.get_enum('action-double-click-titlebar'))
        self.ui['cbox_middle_click'].set_active(gsettings.wm.get_enum('action-middle-click-titlebar'))
        self.ui['cbox_right_click'].set_active(gsettings.wm.get_enum('action-right-click-titlebar'))

        # Focus mode
        if gsettings.wm.get_enum('focus-mode') == 0:
            self.ui['cbox_focus_mode'].set_active(0)
        elif gsettings.wm.get_enum('focus-mode') == 1:
            self.ui['cbox_focus_mode'].set_active(1)
        elif gsettings.wm.get_enum('focus-mode') == 2:
            self.ui['cbox_focus_mode'].set_active(2)
        else:
            pass

        # Resize colours
        color = gsettings.resize.get_string('border-color')
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['colorbutton_resize_outline'].set_color(gdkcolor)
        del color, valid, gdkcolor

        color = gsettings.resize.get_string('fill-color')
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['colorbutton_resize_fill'].set_color(gdkcolor)
        del color, valid, gdkcolor


# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, unity-tweak-tool can resist glade stupidity.    |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/

# ===== BEGIN: Compiz settings =====

#-----BEGIN: General -----

    def on_sw_compiz_zoom_active_notify(self, widget, udata = None):
        dependants = ['scrolledwindow_compiz_general_zoom']
        plugins = gsettings.core.get_strv('active-plugins')
        if self.ui['sw_compiz_zoom'].get_active() == True:
            self.ui.sensitize(dependants)
            if 'ezoom' not in plugins:
                plugins.append('ezoom')
                gsettings.core.set_strv('active-plugins', plugins)
        else:
            self.ui.unsensitize(dependants)
            if 'ezoom' in plugins:
                plugins.remove('ezoom')
                gsettings.core.set_strv('active-plugins', plugins)

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

    def on_cbox_opengl_changed(self, widget, udata = None):
        gsettings.opengl.set_int('texture-filter', self.ui['cbox_opengl'].get_active())

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
        titer = model.get_iter(path)
        self.ui['list_compiz_general_keys_accelerators'].set_value(titer, 1, "Disabled")
        if path  ==  '0':
            gsettings.core.set_string('close-window-key', "Disabled")
        elif path  ==  '1':
            gsettings.move.set_string('initiate-key', "Disabled")
        else:
            gsettings.core.set_string('show-desktop-key', "Disabled")

    #-----General: Animations

    def on_switch_window_animations_active_notify(self, widget, udata = None):
        dependants = ['cbox_minimize_animation',
                    'l_minimize_animation',
                    'cbox_unminimize_animation',
                    'l_unminimize_animation']

        if self.ui['switch_window_animations'].get_active() == True:
            self.ui.sensitize(dependants)
            maximize_combobox_text = self.ui['cbox_minimize_animation'].get_active_text()
            gsettings.animation.set_strv('minimize-effects', ['animation:'+maximize_combobox_text])
            minimize_combobox_text = self.ui['cbox_unminimize_animation'].get_active_text()
            gsettings.animation.set_strv('unminimize-effects', ['animation:'+minimize_combobox_text])
        else:
            self.ui.unsensitize(dependants)
            gsettings.animation.set_strv('minimize-effects', ['animation:None'])
            gsettings.animation.set_strv('unminimize-effects', ['animation:None'])

    def on_cbox_unminimize_animation_changed(self, widget, udata = None):
        combobox_text = self.ui['cbox_unminimize_animation'].get_active_text()
        gsettings.animation.set_strv('unminimize-effects', ['animation:'+combobox_text])

    def on_cbox_minimize_animation_changed(self, widget, udata = None):
        combobox_text = self.ui['cbox_minimize_animation'].get_active_text()
        gsettings.animation.set_strv('minimize-effects', ['animation:'+combobox_text])

    def on_b_compiz_general_reset_clicked(self, widget):
        gsettings.core.reset('active-plugins')
        gsettings.animation.reset('unminimize-effects')
        gsettings.animation.reset('minimize-effects')
        gsettings.zoom.reset('zoom-in-key')
        gsettings.zoom.reset('zoom-out-key')
        gsettings.opengl.reset('texture-filter')
        gsettings.opengl.reset('sync-to-vblank')
        gsettings.core.reset('close-window-key')
        gsettings.move.reset('initiate-key')
        gsettings.core.reset('show-desktop-key')
        self.refresh()

#-----BEGIN: Workspaces -----

    def on_sw_workspace_switcher_active_notify(self, widget, udata = None):
        dependants = ['l_horizontal_desktop',
                    'l_vertical_desktop',
                    'spin_horizontal_desktop',
                    'spin_vertical_desktop']

        if self.ui['sw_workspace_switcher'].get_active() == True:
            self.ui.sensitize(dependants)
            gsettings.core.set_int('hsize', 2)
            gsettings.core.set_int('hsize', 2)
            self.ui['spin_horizontal_desktop'].set_value(2)
            self.ui['spin_vertical_desktop'].set_value(2)

        else:
            self.ui.unsensitize(dependants)
            gsettings.core.set_int('hsize', 1)
            gsettings.core.set_int('vsize', 1)
            self.ui['spin_horizontal_desktop'].set_value(1)
            self.ui['spin_vertical_desktop'].set_value(1)

    def on_spin_horizontal_desktop_value_changed(self, widget, udata = None):
        gsettings.core.set_int('hsize', self.ui['spin_horizontal_desktop'].get_value())

    def on_spin_vertical_desktop_value_changed(self, widget, udata = None):
        gsettings.core.set_int('vsize', self.ui['spin_vertical_desktop'].get_value())

    def on_color_desk_outline_color_set(self, widget, udata = None):
        colorhash = gsettings.color_to_hash(self.ui['color_desk_outline'].get_color(),alpha=1)
        gsettings.expo.set_string('selected-color', colorhash)

    def on_craccel_compiz_workspace_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        accel = Gtk.accelerator_name(key, mods)
        titer = self.ui['list_compiz_workspace_accelerators'].get_iter(path)
        self.ui['list_compiz_workspace_accelerators'].set_value(titer, 1, accel)
        gsettings.expo.set_string('expo-key', accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model = None):
        titer = self.ui['list_compiz_workspace_accelerators'].get_iter(path)
        self.ui['list_compiz_workspace_accelerators'].set_value(titer, 1, "Disabled")
        gsettings.expo.set_string('expo-key', "Disabled")

    def on_b_compiz_workspace_reset_clicked(self, widget):
        gsettings.core.reset('hsize')
        gsettings.core.reset('vsize')
        gsettings.expo.reset('selected-color')
        gsettings.expo.reset('expo-key')
        self.refresh()

#-----BEGIN: Windows Spread -----

    def on_sw_windows_spread_active_notify(self, widget, udata = None):
        dependants = ['l_compiz_spacing',
                    'spin_compiz_spacing',
                    'check_overlay_emblem',
                    'check_click_desktop',
                    'scrolledwindow_compiz_window_spread']

        plugins = gsettings.core.get_strv('active-plugins')

        if self.ui['sw_windows_spread'].get_active() == True:
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
        if self.ui['check_overlay_emblem'].get_active() == True:
            gsettings.scale.set_int('overlay-icon', 1)
        else:
            gsettings.scale.set_int('overlay-icon', 0)

    def on_craccel_compiz_windows_spread_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        accel = Gtk.accelerator_name(key, mods)
        titer = self.ui['list_compiz_windows_spread_accelerators'].get_iter(path)
        self.ui['list_compiz_windows_spread_accelerators'].set_value(titer, 1, accel)
        if path  ==  '0':
            gsettings.scale.set_string("initiate-key", accel)
        else:
            gsettings.scale.set_string("initiate-all-key", accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model = None):
        titer = model.get_iter(path)
        self.ui['list_compiz_windows_spread_accelerators'].set_value(titer, 1, "Disabled")
        if path  ==  '0':
            gsettings.scale.set_string("initiate-key", "Disabled")
        else:
            gsettings.scale.set_string("initiate-all-key", "Disabled")

    def on_b_compiz_windows_spread_reset_clicked(self, widget):
        gsettings.core.reset('active-plugins')
        gsettings.scale.reset('spacing')
        gsettings.scale.reset('overlay-icon')
        gsettings.scale.reset('show-desktop')
        gsettings.scale.reset('initiate-key')
        gsettings.scale.reset('initiate-all-key')
        self.refresh()

#-----BEGIN: Window Snapping -----

    def on_sw_window_snapping_active_notify(self, widget, udata=None):

        plugins = gsettings.core.get_strv('active-plugins')
        if self.ui['sw_window_snapping'].get_active() == True:
            if 'grid' not in plugins:
                plugins.append('grid')
                gsettings.core.set_strv('active-plugins', plugins)
        else:
            if 'grid' in plugins:
                plugins.remove('grid')
                gsettings.core.set_strv('active-plugins', plugins)

    def on_color_outline_color_color_set(self, widget, udata=None):
        colorhash = gsettings.color_to_hash(self.ui['color_outline_color'].get_color(),alpha=1)
        gsettings.grid.set_string('outline-color', colorhash)

    def on_color_fill_color_color_set(self, widget, udata=None):
        colorhash = gsettings.color_to_hash(self.ui['color_fill_color'].get_color(),alpha=0.31)
        gsettings.grid.set_string('fill-color', colorhash)

    def on_b_compiz_windowsnapping_reset_clicked(self, widget):
        gsettings.core.reset('active-plugins')
        gsettings.grid.reset('fill-color')
        gsettings.grid.reset('outline-color')
        gsettings.grid.reset('top-left-corner-action')
        gsettings.grid.reset('top-edge-action')
        gsettings.grid.reset('top-right-corner-action')
        gsettings.grid.reset('left-edge-action')
        gsettings.grid.reset('right-edge-action')
        gsettings.grid.reset('bottom-left-corner-action')
        gsettings.grid.reset('bottom-edge-action')
        gsettings.grid.reset('bottom-right-corner-action')
        self.refresh()


# ----- BEGIN: Hot Corners -----

    def on_switch_hotcorners_active_notify(self, widget, udata = None):
        dependants = ['cbox_hotcorners_topleft',
                    'cbox_hotcorners_left',
                    'cbox_hotcorners_bottomleft',
                    'cbox_hotcorners_topright',
                    'cbox_hotcorners_right',
                    'cbox_hotcorners_bottomright',
                    'cbox_hotcorners_top',
                    'cbox_hotcorners_bottom']

        if not hasattr(self, 'hotcorners_previous'):
            self.hotcorners_previous = {}

        if self.ui['switch_hotcorners'].get_active() == True:
            self.ui.sensitize(dependants)
            for box in self.hotcorners_cboxes:
                self.ui[box].set_active(self.hotcorners_previous[box])

        else:
            self.ui.unsensitize(dependants)
            for box in self.hotcorners_cboxes:
                self.hotcorners_previous[box] = self.hotcorners_cboxes[box][0]
                self.ui[box].set_active(0)

    def on_b_compiz_hotcorners_reset_clicked(self, widget):
        gsettings.core.reset('show-desktop-edge')
        gsettings.expo.reset('expo-edge')
        gsettings.scale.reset('initiate-edge')
        gsettings.scale.reset('initiate-all-edge')
        self.refresh()

# ----- BEGIN: Additional -----

    def on_switch_auto_raise_active_notify(self, widget, udata = None):
        if self.ui['switch_auto_raise'].get_active() == True:
            gsettings.wm.set_boolean('auto-raise', True)
        else:
            gsettings.wm.set_boolean('auto-raise', False)

    def on_cbox_focus_mode_changed(self, widget, udata = None):
        gsettings.wm.set_enum('focus-mode', self.ui['cbox_focus_mode'].get_active())

    def on_cbox_double_click_changed(self, widget, udata = None):
        gsettings.wm.set_enum('action-double-click-titlebar', self.ui['cbox_double_click'].get_active())

    def on_cbox_middle_click_changed(self, widget, udata = None):
        gsettings.wm.set_enum('action-middle-click-titlebar', self.ui['cbox_middle_click'].get_active())

    def on_cbox_right_click_changed(self, widget, udata = None):
        gsettings.wm.set_enum('action-right-click-titlebar', self.ui['cbox_right_click'].get_active())

    def on_scale_auto_raise_delay_value_changed(self, widget, udata = None):
        value = self.ui['scale_auto_raise_delay'].get_value()
        gsettings.wm.set_int('auto-raise-delay', value)
        del value

    def on_colorbutton_resize_outline_color_set(self, widget, udata=None):
        colorhash = gsettings.color_to_hash(self.ui['colorbutton_resize_outline'].get_color(),alpha=1)
        gsettings.resize.set_string('border-color', colorhash)

    def on_colorbutton_resize_fill_color_set(self, widget, udata=None):
        colorhash = gsettings.color_to_hash(self.ui['colorbutton_resize_fill'].get_color(),alpha=0.31)
        gsettings.resize.set_string('fill-color', colorhash)

    def on_b_wm_additional_reset_clicked(self, widget):
        gsettings.wm.reset('auto-raise-delay')
        gsettings.wm.reset('auto-raise')
        gsettings.wm.reset('focus-mode')
        gsettings.wm.reset('action-double-click-titlebar')
        gsettings.wm.reset('action-middle-click-titlebar')
        gsettings.wm.reset('action-right-click-titlebar')
        gsettings.resize.reset('border-color')
        gsettings.resize.reset('fill-color')
        self.refresh()

if __name__ == '__main__':
# Fire up the Engines
    Compizsettings()
# FIXME : This is guaranteed to fail.
