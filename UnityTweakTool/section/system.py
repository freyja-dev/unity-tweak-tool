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
from UnityTweakTool.elements.switch import Switch
from UnityTweakTool.elements.checkbox import CheckBox
from UnityTweakTool.elements.cbox import ComboBox
from UnityTweakTool.elements.radio import Radio
from UnityTweakTool.elements.togglebutton import ToggleButton
import UnityTweakTool.section.dynamic as dynamic


System=Section(ui='system.ui',id='nb_desktop_settings')

tb_home_folder= ToggleButton({
    'id'        : 'tb_home_folder',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.nautilus.desktop',
    'path'      : None,
    'key'       : 'home-icon-visible',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

tb_network= ToggleButton({
    'id'        : 'tb_network',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.nautilus.desktop',
    'path'      : None,
    'key'       : 'network-icon-visible',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

tb_trash= ToggleButton({
    'id'        : 'tb_trash',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.nautilus.desktop',
    'path'      : None,
    'key'       : 'trash-icon-visible',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

tb_devices= ToggleButton({
    'id'        : 'tb_devices',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.nautilus.desktop',
    'path'      : None,
    'key'       : 'volumes-visible',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

DesktopIcons=Tab([  tb_home_folder,
                    tb_network,
                    tb_trash,
                    tb_devices])

check_security_lock_screen= CheckBox({
    'id'        : 'check_security_lock_screen',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.desktop.lockdown',
    'path'      : None,
    'key'       : 'disable-lock-screen',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_security_logout= CheckBox({
    'id'        : 'check_security_logout',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.desktop.lockdown',
    'path'      : None,
    'key'       : 'disable-log-out',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_security_user_switching= CheckBox({
    'id'        : 'check_security_user_switching',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.desktop.lockdown',
    'path'      : None,
    'key'       : 'disable-user-switching',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

# TODO: This check should tweak 'disable-print-setup' key too.

check_security_printing= CheckBox({
    'id'        : 'check_security_printing',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.desktop.lockdown',
    'path'      : None,
    'key'       : 'disable-printing',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

SecurityIcons=Tab([check_security_lock_screen,
                   check_security_logout,
                   check_security_user_switching,
                   check_security_printing])

radio_overlay_scrollbars=Radio({
    'id'        : 'radio_overlay_scrollbars',
    'builder'   : System.builder,
    'schema'    : 'com.canonical.desktop.interface',
    'path'      : None,
    'key'       : 'scrollbar-mode',
    'type'      : 'string',
    'group'     : 'radio_legacy_scrollbars',
    'value'     : 'overlay-auto',
    'dependants': ['l_overlay_scrollbar_mode',
                   'cbox_overlay_scrollbar_mode']
})

# TODO: Look at overlay-auto

cbox_overlay_scrollbar_mode=ComboBox({
    'id'      : 'cbox_overlay_scrollbar_mode',
    'builder' : System.builder,
    'schema'  : 'com.canonical.desktop.interface',
    'path'    : None,
    'key'     : 'scrollbar-mode',
    'type'    : 'string',
    'map'     : {'overlay-auto':0,'overlay-pointer':1,'overlay-touch':2,'normal':0}
})

radio_legacy_scrollbars=Radio({
    'id'        : 'radio_legacy_scrollbars',
    'builder'   : System.builder,
    'schema'    : 'com.canonical.desktop.interface',
    'path'      : None,
    'key'       : 'scrollbar-mode',
    'type'      : 'string',
    'group'     : 'radio_legacy_scrollbars',
    'value'     : 'normal',
    'dependants': []
})

check_horizontal_scrolling= CheckBox({
    'id'        : 'check_horizontal_scrolling',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.' + dynamic.touchpad_schema + '.peripherals.touchpad',
    'path'      : None,
    'key'       : 'horiz-scroll-enabled',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

radio_edge=Radio({
    'id'        : 'radio_edge',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.' + dynamic.touchpad_schema + '.peripherals.touchpad',
    'path'      : None,
    'key'       : 'scroll-method',
    'type'      : 'string',
    'group'     : 'radio_two_finger',
    'value'     : 'edge-scrolling',
    'dependants': []
})

radio_two_finger=Radio({
    'id'        : 'radio_two_finger',
    'builder'   : System.builder,
    'schema'    : 'org.gnome.' + dynamic.touchpad_schema + '.peripherals.touchpad',
    'path'      : None,
    'key'       : 'scroll-method',
    'type'      : 'string',
    'group'     : 'radio_two_finger',
    'value'     : 'two-finger-scrolling',
    'dependants': []
})

ScrollingIcons=Tab([radio_overlay_scrollbars,
                    cbox_overlay_scrollbar_mode,
                    radio_legacy_scrollbars,
                    radio_edge,
                    radio_two_finger,
                    check_horizontal_scrolling])

# Pass in the id of restore defaults button to enable it.
DesktopIcons.enable_restore('b_desktop_settings_icons_reset')
SecurityIcons.enable_restore('b_desktop_settings_security_reset')
ScrollingIcons.enable_restore('b_settings_scrolling_reset')

# Each page must be added using add_page
System.add_page(DesktopIcons)
System.add_page(SecurityIcons)
System.add_page(ScrollingIcons)

# After all pages are added, the section needs to be registered to start listening for events
System.register()
