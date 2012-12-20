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

class Startpage ():
    def __init__(self, container, notebook):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.container = container
        self.notebook = notebook
        #self.page = 'box_startpage'
# TODO : Use os module to resolve to the full path.
        #self.builder.add_objects_from_file('startpage.ui', [self.page])
        self.builder.add_from_file('startpage.ui')
        self.ui = ui(self.builder)
        self.page = self.ui['box_startpage']
        self.page.unparent()
        self.builder.connect_signals(self)

    # Word wrapping in labels in Start page buttons
        label_tool_windows_spread = Gtk.Label("Windows spread")
        label_tool_windows_spread.set_line_wrap(True)
        self.ui['tool_windows_spread'].set_label_widget(label_tool_windows_spread)

        label_tool_windows_snapping = Gtk.Label("Windows snapping")
        label_tool_windows_snapping.set_line_wrap(True)
        self.ui['tool_windows_snapping'].set_label_widget(label_tool_windows_snapping)

    # Unity settings buttons on start page
    def on_tool_launcher_clicked(self,udata):
        self.container['tool_unitysettings'].set_active(True)
        self.notebook.get_nth_page(1).set_current_page(0)
    def on_tool_dash_clicked(self,udata):
        self.container['tool_unitysettings'].set_active(True)
        self.notebook.get_nth_page(1).set_current_page(1)
    def on_tool_panel_clicked(self,udata):
        self.container['tool_unitysettings'].set_active(True)
        self.notebook.get_nth_page(1).set_current_page(2)
    def on_tool_unity_switcher_clicked(self,udata):
        self.container['tool_unitysettings'].set_active(True)
        self.notebook.get_nth_page(1).set_current_page(3)
    def on_tool_additional_clicked(self,udata):
        self.container['tool_unitysettings'].set_active(True)
        self.notebook.get_nth_page(1).set_current_page(4)

    # Compiz settings buttons on start page
    def on_tool_general_clicked(self,udata):
        self.container['tool_compizsettings'].set_active(True)
        self.notebook.get_nth_page(2).set_current_page(0)
    def on_tool_compiz_switcher_clicked(self,udata):
        self.container['tool_compizsettings'].set_active(True)
        self.notebook.get_nth_page(2).set_current_page(1)
    def on_tool_windows_spread_clicked(self,udata):
        self.container['tool_compizsettings'].set_active(True)
        self.notebook.get_nth_page(2).set_current_page(2)
    def on_tool_windows_snapping_clicked(self,udata):
        self.container['tool_compizsettings'].set_active(True)
        self.notebook.get_nth_page(2).set_current_page(3)
    def on_tool_hotcorners_clicked(self,udata):
        self.container['tool_compizsettings'].set_active(True)
        self.notebook.get_nth_page(2).set_current_page(4)

    # Theme settings on Start page
    def on_tool_system_clicked(self,udata):
        self.container['tool_themesettings'].set_active(True)
        self.notebook.get_nth_page(3).set_current_page(0)
    def on_tool_icons_clicked(self,udata):
        self.container['tool_themesettings'].set_active(True)
        self.notebook.get_nth_page(3).set_current_page(1)
    def on_tool_cursors_clicked(self,udata):
        self.container['tool_themesettings'].set_active(True)
        self.notebook.get_nth_page(3).set_current_page(2)
    def on_tool_fonts_clicked(self,udata):
        self.container['tool_themesettings'].set_active(True)
        self.notebook.get_nth_page(3).set_current_page(3)

    # desktop settings on start page
    def on_tool_desktop_clicked(self,udata):
        self.container['tool_desktopsettings'].set_active(True)

if __name__=='__main__':
# Fire up the Engines
    Startpage()
