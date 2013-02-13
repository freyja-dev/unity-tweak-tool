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
from UnityTweakTool.elements.cbox import ComboBox

from UnityTweakTool.section.sphagetti.unity import Unitysettings as SphagettiUnitySettings
from UnityTweakTool.elements.option import Option,HandlerObject

from collections import defaultdict

Unity=Section(ui='unity.ui',id='nb_unitysettings')

sw_launcher_hidemode= Switch({
    'id'        : 'sw_launcher_hidemode',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'launcher-hide-mode',
    'type'      : 'int',
    'map'       : {1:True,0:False},
    'dependants': ['radio_reveal_left',
                   'radio_reveal_topleft',
                   'sc_reveal_sensitivity',
                   'l_launcher_reveal',
                   'l_launcher_reveal_sensitivity',
                   'l_autohide_animation',
                   'cbox_autohide_animation']
})

cbox_autohide_animation=ComboBox({
    'id'        : 'cbox_autohide_animation',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'autohide-animation',
    'type'      : 'int',
    'map'       : {0:0,1:1,2:2,3:3}
})

LauncherIcons=Tab([sw_launcher_hidemode,
                    cbox_autohide_animation])


sw_dash_blur= Switch({
    'id'        : 'sw_dash_blur',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'dash-blur-experimental',
    'type'      : 'int',
    'map'       : {2:True,0:False},
    'dependants': ['radio_dash_blur_smart',
                   'radio_dash_blur_static',
                   'l_dash_blur_type']
})
DashIcons=Tab([sw_dash_blur])

sw_transparent_panel= Switch({
    'id'        : 'sw_transparent_panel',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'panel-opacity',
    'type'      : 'double',
    'map'       : defaultdict(lambda:True,{0.33:True,1:False}),
    'dependants': ['sc_panel_transparency',
                   'l_transparent_panel',
                   'check_panel_opaque']
})
PanelIcons=Tab([sw_transparent_panel])

switch_unity_webapps= Switch({
    'id'        : 'switch_unity_webapps',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.unity.webapps',
    'path'      : None,
    'key'       : 'integration-allowed',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})
WebappsIcons=Tab([switch_unity_webapps])


# Each page must be added using add_page
Unity.add_page(LauncherIcons)
Unity.add_page(DashIcons)
#Unity.add_page(PanelIcons)
Unity.add_page(WebappsIcons)

# XXX : Sphagetti bridge
unitysettings=HandlerObject(SphagettiUnitySettings(Unity.builder))
Unity.add_page(unitysettings)
# After all pages are added, the section needs to be registered to start listening for events
Unity.register()
