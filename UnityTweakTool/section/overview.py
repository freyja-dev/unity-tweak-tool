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
from UnityTweakTool.elements.button import OverviewButton

class Overview(Tab,Section):
    def __init__(self,notebook):
        Section.__init__(self,ui='overview.ui',id='box_overview')
        self.sections={
            1:{ 0:'b_unity-launcher',
                1:'b_unity-search',
                2:'b_unity-panel',
                3:'b_unity-switcher',
                4:'b_unity-webapps',
                5:'b_unity-additional'},
            2:{ 0:'b_wm-general',
                1:'b_wm-workspaces',
                2:'b_wm-window-spread',
                3:'b_wm-window-snapping',
                4:'b_wm-hotcorners',
                5:'b_wm-additional'},
            3:{ 0:'b_appearance-theme',
                1:'b_appearance-icons',
                2:'b_appearance-cursors',
                3:'b_appearance-fonts'},
            4:{ 0:'b_system-desktop-icons',
                1:'b_system-security',
                2:'b_system-scrolling'}
        }

        Tab.__init__(self,[OverviewButton(
                            section=section,page=page,id=id,notebook=notebook)
                    for section,set in self.sections.items()
                        for page,id in set.items()
            ]
        )

        self.register_tab(self.handler)
        self.register()
 
        # Symbolic icons
        self.icons = Gtk.IconTheme.get_default()
        self.style_context = self.builder.get_object('overview_window').get_style_context()
        self.style_context.connect('changed', self.on_style_context_change)

    def on_style_context_change(self, *args):
     try:
        self.symbolic_color = self.style_context.get_color(Gtk.StateFlags.ACTIVE)

        appearance_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-appearance-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if appearance_symbolic_icon:
            appearance_symbolic_icon_pixbuf, was_sym = appearance_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('i_appearance-title').set_from_pixbuf(appearance_symbolic_icon_pixbuf)

        unity_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-unity-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if unity_symbolic_icon:
            unity_symbolic_icon_pixbuf, was_sym = unity_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('i_unity-title').set_from_pixbuf(unity_symbolic_icon_pixbuf)

        system_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-system-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if system_symbolic_icon:
            system_symbolic_icon_pixbuf, was_sym = system_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('i_system-title').set_from_pixbuf(system_symbolic_icon_pixbuf)

        wm_symbolic_icon = self.icons.lookup_icon('unity-tweak-tool-wm-symbolic', 24, Gtk.IconLookupFlags.FORCE_SIZE)
        if wm_symbolic_icon:
            wm_symbolic_icon_pixbuf, was_sym = wm_symbolic_icon.load_symbolic(self.symbolic_color, None, None, None)
            self.builder.get_object('i_wm-title').set_from_pixbuf(wm_symbolic_icon_pixbuf)
     except Exception:
        pass
# XXX : Temporary fix to prevent random attributeerrors.

