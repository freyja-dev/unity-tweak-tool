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

from gi.repository import Gtk, Gio

from UnityTweakTool.config.ui import ui
from . import unitytweakconfig

class Startpage ():
    def __init__(self, container, notebook):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.container = container
        self.notebook = notebook
        self.glade = (os.path.join(unitytweakconfig.get_data_path(),
                                   'startpage.ui'))
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['box_startpage']
        self.page.unparent()
        self.builder.connect_signals(self)

        # Symbolic icons
        self.icons = Gtk.IconTheme.get_default()
        self.style_context = self.ui['startpage_window'].get_style_context()
        self.style_context.connect('changed', self.on_style_context_change)

    # Unity settings buttons on start page
    def on_tool_launcher_clicked(self, udata):
        self.notebook.set_current_page(1)
        self.notebook.get_nth_page(1).set_current_page(0)
    def on_tool_dash_clicked(self, udata):
        self.notebook.set_current_page(1)
        self.notebook.get_nth_page(1).set_current_page(1)
    def on_tool_panel_clicked(self, udata):
        self.notebook.set_current_page(1)
        self.notebook.get_nth_page(1).set_current_page(2)
    def on_tool_unity_switcher_clicked(self, udata):
        self.notebook.set_current_page(1)
        self.notebook.get_nth_page(1).set_current_page(3)
    def on_tool_unity_webapps_clicked(self, udata):
        self.notebook.set_current_page(1)
        self.notebook.get_nth_page(1).set_current_page(4)
    def on_tool_additional_clicked(self, udata):
        self.notebook.set_current_page(1)
        self.notebook.get_nth_page(1).set_current_page(5)

    # Compiz settings buttons on start page
    def on_tool_general_clicked(self, udata):
        self.notebook.set_current_page(2)
        self.notebook.get_nth_page(2).set_current_page(0)
    def on_tool_compiz_switcher_clicked(self, udata):
        self.notebook.set_current_page(2)
        self.notebook.get_nth_page(2).set_current_page(1)
    def on_tool_windows_spread_clicked(self, udata):
        self.notebook.set_current_page(2)
        self.notebook.get_nth_page(2).set_current_page(2)
    def on_tool_windows_snapping_clicked(self, udata):
        self.notebook.set_current_page(2)
        self.notebook.get_nth_page(2).set_current_page(3)
    def on_tool_hotcorners_clicked(self, udata):
        self.notebook.set_current_page(2)
        self.notebook.get_nth_page(2).set_current_page(4)
    def on_tool_wm_additional_clicked(self, udata):
        self.notebook.set_current_page(2)
        self.notebook.get_nth_page(2).set_current_page(5)

    # Theme settings on Start page
    def on_tool_system_clicked(self, udata):
        self.notebook.set_current_page(3)
        self.notebook.get_nth_page(3).set_current_page(0)
    def on_tool_icons_clicked(self, udata):
        self.notebook.set_current_page(3)
        self.notebook.get_nth_page(3).set_current_page(1)
    def on_tool_cursors_clicked(self, udata):
        self.notebook.set_current_page(3)
        self.notebook.get_nth_page(3).set_current_page(2)
    def on_tool_fonts_clicked(self, udata):
        self.notebook.set_current_page(3)
        self.notebook.get_nth_page(3).set_current_page(3)
    def on_tool_window_controls_clicked(self, udata):
        self.notebook.set_current_page(3)
        self.notebook.get_nth_page(3).set_current_page(4)

    # Desktop settings on start page
    def on_tool_desktop_icons_clicked(self, udata):
        self.notebook.set_current_page(4)
        self.notebook.get_nth_page(4).set_current_page(0)
    def on_tool_desktop_security_clicked(self, udata):
        self.notebook.set_current_page(4)
        self.notebook.get_nth_page(4).set_current_page(1)
    def on_tool_desktop_scrolling_clicked(self, udata):
        self.notebook.set_current_page(4)
        self.notebook.get_nth_page(4).set_current_page(2)

    # Symbolic icons
    def on_style_context_change(self, widget):
        self.symbolic_color = self.style_context.get_color(Gtk.StateFlags.ACTIVE)

        appearance_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-appearance-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if appearance_symbolic_icon:
            appearance_symbolic_icon_pixbuf, was_sym = appearance_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.ui['image_start_theme'].set_from_pixbuf(appearance_symbolic_icon_pixbuf)

        unity_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-unity-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if unity_symbolic_icon:
            unity_symbolic_icon_pixbuf, was_sym = unity_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.ui['image_box_start_unity'].set_from_pixbuf(unity_symbolic_icon_pixbuf)

        system_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-system-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if system_symbolic_icon:
            system_symbolic_icon_pixbuf, was_sym = system_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.ui['image_start_desktop'].set_from_pixbuf(system_symbolic_icon_pixbuf)

        wm_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-wm-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if wm_symbolic_icon:
            wm_symbolic_icon_pixbuf, was_sym = wm_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.ui['image_box_start_compiz'].set_from_pixbuf(wm_symbolic_icon_pixbuf)


if __name__ == '__main__':
# Fire up the Engines
    Startpage()
# FIXME : This should fail. 2 missing arguments.
