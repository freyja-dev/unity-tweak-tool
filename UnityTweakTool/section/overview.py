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

from UnityTweakTool.section.skeletonpage import Section,Tab,Gtk
from UnityTweakTool.elements.toolbutton import OverviewToolButton

class Overview(Tab,Section):
    def __init__(self,notebook):
        Section.__init__(self,ui='startpage.ui',id='box_startpage')
        self.sections={
            1:{ 0:'tool_launcher',
                1:'tool_dash',
                2:'tool_panel',
                3:'tool_unity_switcher',
                4:'tool_unity_webapps',
                5:'tool_additional'},
            2:{ 0:'tool_general',
                1:'tool_compiz_switcher',
                2:'tool_windows_spread',
                3:'tool_windows_snapping',
                4:'tool_hotcorners',
                5:'tool_wm_additional'},
            3:{ 0:'tool_system',
                1:'tool_icons',
                2:'tool_cursors',
                3:'tool_fonts',
                4:'tool_window_controls'},
            4:{ 0:'tool_desktop_icons',
                1:'tool_desktop_security',
                2:'tool_desktop_scrolling'}
        }

        Tab.__init__(self,[OverviewToolButton(
                            section=section,page=page,id=id,notebook=notebook)
                    for section,set in self.sections.items()
                        for page,id in set.items()
            ]
        )

        self.register_tab(self.handler)
        self.register()
 
        # Symbolic icons
        self.icons = Gtk.IconTheme.get_default()
        self.style_context = self.builder.get_object('startpage_window').get_style_context()
        self.style_context.connect('changed', self.on_style_context_change)
# XXX : Delete the next line and UTT crashes with attribute error. absolutely no idea why.
        self.on_style_context_change()

    def on_style_context_change(self, *args):
        self.symbolic_color = self.style_context.get_color(Gtk.StateFlags.ACTIVE)

        appearance_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-appearance-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if appearance_symbolic_icon:
            appearance_symbolic_icon_pixbuf, was_sym = appearance_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('image_start_theme').set_from_pixbuf(appearance_symbolic_icon_pixbuf)

        unity_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-unity-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if unity_symbolic_icon:
            unity_symbolic_icon_pixbuf, was_sym = unity_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('image_box_start_unity').set_from_pixbuf(unity_symbolic_icon_pixbuf)

        system_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-system-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if system_symbolic_icon:
            system_symbolic_icon_pixbuf, was_sym = system_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('image_start_desktop').set_from_pixbuf(system_symbolic_icon_pixbuf)

        wm_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-wm-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if wm_symbolic_icon:
            wm_symbolic_icon_pixbuf, was_sym = wm_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('image_box_start_compiz').set_from_pixbuf(wm_symbolic_icon_pixbuf)

