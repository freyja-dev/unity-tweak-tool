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


from UnityTweakTool.section.skeletonpage import Section,Tab
from UnityTweakTool.elements.fontbutton import FontButton
from UnityTweakTool.elements.cbox import ComboBox
from UnityTweakTool.elements.spin import SpinButton
from UnityTweakTool.elements.radio import Radio
from UnityTweakTool.elements.checkbox import CheckBox
from UnityTweakTool.section.spaghetti.theme import Themesettings as SpaghettiThemeSettings
from UnityTweakTool.elements.option import Option,HandlerObject

from collections import defaultdict

Appearance =Section(ui='appearance.ui',id='nb_themesettings')

#=============== THEME ==========================

#=============== ICONS ==========================

#=============== CURSOR =========================

#=============== FONTS ==========================

font_default= FontButton({
    'id'        : 'font_default',
    'builder'   : Appearance.builder,
    'schema'    : 'org.gnome.desktop.interface',
    'path'      : None,
    'key'       : 'font-name',
    'type'      : 'string'
})

font_document= FontButton({
    'id'        : 'font_document',
    'builder'   : Appearance.builder,
    'schema'    : 'org.gnome.desktop.interface',
    'path'      : None,
    'key'       : 'document-font-name',
    'type'      : 'string'
})

font_monospace= FontButton({
    'id'        : 'font_monospace',
    'builder'   : Appearance.builder,
    'schema'    : 'org.gnome.desktop.interface',
    'path'      : None,
    'key'       : 'monospace-font-name',
    'type'      : 'string'
})

font_window_title= FontButton({
    'id'        : 'font_window_title',
    'builder'   : Appearance.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'titlebar-font',
    'type'      : 'string'
})

cbox_antialiasing=ComboBox({
    'id'      : 'cbox_antialiasing',
    'builder' : Appearance.builder,
    'schema'  : 'org.gnome.settings-daemon.plugins.xsettings',
    'path'    : None,
    'key'     : 'antialiasing',
    'type'    : 'string',
    'map'     : {'none':0,'grayscale':1,'rgba':2}
})

cbox_hinting=ComboBox({
    'id'      : 'cbox_hinting',
    'builder' : Appearance.builder,
    'schema'  : 'org.gnome.settings-daemon.plugins.xsettings',
    'path'    : None,
    'key'     : 'hinting',
    'type'    : 'string',
    'map'     : {'none':0,'slight':1,'medium':2,'full':3}
})

spin_textscaling=SpinButton({
    'id'     : 'spin_textscaling',
    'builder': Appearance.builder,
    'schema' : 'org.gnome.desktop.interface',
    'path'   : None,
    'key'    : 'text-scaling-factor',
    'type'   : 'double',
    'min'    : 0.50,
    'max'    : 3.00
})

Fonts=Tab([font_default,
                font_document,
                font_monospace,
                font_window_title,
                cbox_antialiasing,
                cbox_hinting,
                spin_textscaling])

#========== WINDOW CONTROLS =====================

radio_left=Radio({
    'id'        : 'radio_left',
    'builder'   : Appearance.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'button-layout',
    'type'      : 'string',
    'group'     : 'radio_left',
    'value'     : 'close,minimize,maximize:',
    'dependants': []
})

radio_right=Radio({
    'id'        : 'radio_right',
    'builder'   : Appearance.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'button-layout',
    'type'      : 'string',
    'group'     : 'radio_right',
    'value'     : ':minimize,maximize,close',
    'dependants': []
})


WindowControls=Tab([radio_left,
                    radio_right])

# Pass in the id of restore defaults button to enable it.
Fonts.enable_restore('b_theme_font_reset')
WindowControls.enable_restore('b_window_control_reset')

# Each page must be added using add_page
Appearance.add_page(Fonts)
# XXX : Disabled since the implementation is inadequate
# Appearance.add_page(WindowControls)

themesettings=HandlerObject(SpaghettiThemeSettings(Appearance.builder))
Appearance.add_page(themesettings)

# After all pages are added, the section needs to be registered to start listening for events
Appearance.register()
