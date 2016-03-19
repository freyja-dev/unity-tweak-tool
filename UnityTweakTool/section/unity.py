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
from UnityTweakTool.elements.cbox import ComboBox
from UnityTweakTool.elements.checkbox import CheckBox
from UnityTweakTool.elements.colorchooser import ColorChooser
from UnityTweakTool.elements.radio import Radio
from UnityTweakTool.elements.scale import Scale
from UnityTweakTool.elements.spin import SpinButton
from UnityTweakTool.elements.switch import Switch

from UnityTweakTool.section.spaghetti.unity import Unitysettings as SpaghettiUnitySettings
from UnityTweakTool.elements.option import Option,HandlerObject

from UnityTweakTool.backends import gsettings

from collections import defaultdict
from gi.repository import Gtk

Unity=Section(ui='unity.ui',id='nb_unitysettings')


#=============== LAUNCHER ==========================

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

radio_reveal_left=Radio({
    'id'        : 'radio_reveal_left',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'reveal-trigger',
    'type'      : 'int',
    'group'     : 'radio_reveal_topleft',
    'value'     : 0,
    'dependants': []
})

radio_reveal_topleft=Radio({
    'id'        : 'radio_reveal_topleft',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'reveal-trigger',
    'type'      : 'int',
    'group'     : 'radio_reveal_topleft',
    'value'     : 1,
    'dependants': []
})

radio_launcher_visibility_all=Radio({
    'id'        : 'radio_launcher_visibility_all',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'num-launchers',
    'type'      : 'int',
    'group'     : 'radio_launcher_visibility_primary',
    'value'     : 0,
    'dependants': []
})

radio_launcher_visibility_primary=Radio({
    'id'        : 'radio_launcher_visibility_primary',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'num-launchers',
    'type'      : 'int',
    'group'     : 'radio_launcher_visibility_primary',
    'value'     : 1,
    'dependants': []
})

cbox_urgent_animation=ComboBox({
    'id'        : 'cbox_urgent_animation',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'urgent-animation',
    'type'      : 'int',
    'map'       : {0:0,1:1,2:2}
})

cbox_launch_animation=ComboBox({
    'id'        : 'cbox_launch_animation',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'launch-animation',
    'type'      : 'int',
    'map'       : {0:0,1:1,2:2}
})

cbox_launcher_icon_colouring=ComboBox({
    'id'        : 'cbox_launcher_icon_colouring',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'backlight-mode',
    'type'      : 'int',
    'map'       : {0:0,1:1,2:2,3:3,4:4}
})

spin_launcher_icon_size=SpinButton({
    'id'     : 'spin_launcher_icon_size',
    'builder': Unity.builder,
    'schema' : 'org.compiz.unityshell',
    'path'   : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'    : 'icon-size',
    'type'   : 'int',
    'min'    : 8,
    'max'    : 64
})

# TODO:

# sc_launcher_transparency
# radio_launcher_color_cham
# radio_launcher_color_cus
# sw_show_desktop

color_launcher_color_cus=ColorChooser({
     'id'      : 'color_launcher_color_cus',
     'builder' : Unity.builder,
     'schema'  : 'org.compiz.unityshell',
     'path'    : '/org/compiz/profiles/unity/plugins/unityshell/',
     'key'     : 'background-color',
     'type'    : 'string',
})


sc_reveal_sensitivity=Scale({
     'id'     : 'sc_reveal_sensitivity',
     'builder': Unity.builder,
     'schema' : 'org.compiz.unityshell',
     'path'   : '/org/compiz/profiles/unity/plugins/unityshell/',
     'key'    : 'edge-responsiveness',
     'type'   : 'double',
     'min'    : 0.2,
     'max'    : 8.0,
     'ticks'  : [(2.0,Gtk.PositionType.BOTTOM,None)] # XXX : Correct this or get rid of ticks altogether
 })


sc_launcher_transparency=Scale({
     'id'     : 'sc_launcher_transparency',
     'builder': Unity.builder,
     'schema' : 'org.compiz.unityshell',
     'path'   : '/org/compiz/profiles/unity/plugins/unityshell/',
     'key'    : 'launcher-opacity',
     'type'   : 'double',
     'min'    : 0.2, # TODO : Check these min max. Most prolly wrong.
     'max'    : 8.0, # But fine since they are ignored anyway.
     'ticks'  : [(0.666, Gtk.PositionType.BOTTOM, None)]

 })

check_minimize_window= CheckBox({
    'id'        : 'check_minimize_window',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'launcher-minimize-window',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

radio_launcher_position_left=Radio({
    'id'        : 'radio_launcher_position_left',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.Unity.Launcher',
    'path'      : '/com/canonical/unity/launcher/',
    'key'       : 'launcher-position',
    'type'      : 'string',
    'group'     : 'radio_launcher_position_left',
    'value'     : 'Left',
    'dependants': []
})

radio_launcher_position_bottom=Radio({
    'id'        : 'radio_launcher_position_bottom',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.Unity.Launcher',
    'path'      : '/com/canonical/unity/launcher/',
    'key'       : 'launcher-position',
    'type'      : 'string',
    'group'     : 'radio_launcher_position_left',
    'value'     : 'Bottom',
    'dependants': []
})

LauncherIcons=Tab([sw_launcher_hidemode,
                   cbox_autohide_animation,
                   radio_reveal_left,
                   radio_reveal_topleft,
                   radio_launcher_visibility_primary,
                   radio_launcher_visibility_all,
                   radio_launcher_position_left,
                   radio_launcher_position_bottom,
                   cbox_urgent_animation,
                   cbox_launch_animation,
                   cbox_launcher_icon_colouring,
                   spin_launcher_icon_size,
                   sc_reveal_sensitivity,
                   sc_launcher_transparency,
                   color_launcher_color_cus,
                   check_minimize_window])



#=============== DASH ==========================


sw_dash_blur= Switch({
    'id'        : 'sw_dash_blur',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'dash-blur-experimental',
    'type'      : 'int',
    'map'       : defaultdict(lambda:True,{2:True,0:False}),
    'dependants': ['radio_dash_blur_smart',
                   'radio_dash_blur_static',
                   'l_dash_blur_type']
})

radio_dash_blur_smart=Radio({
    'id'        : 'radio_dash_blur_smart',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'dash-blur-experimental',
    'type'      : 'int',
    'group'     : 'radio_dash_blur_static',
    'value'     : 2,
    'dependants': []
})

radio_dash_blur_static=Radio({
    'id'        : 'radio_dash_blur_static',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'dash-blur-experimental',
    'type'      : 'int',
    'group'     : 'radio_dash_blur_static',
    'value'     : 1,
    'dependants': []
})

check_suggestions= CheckBox({
    'id'        : 'check_suggestions',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.Unity.Lenses',
    'path'      : None,
    'key'       : 'remote-content-search',
    'type'      : 'string',
    'map'       : {'all':True,'none':False},
    'dependants': []
})



check_show_available_apps= CheckBox({
    'id'        : 'check_show_available_apps',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.Unity.ApplicationsLens',
    'path'      : None,
    'key'       : 'display-available-apps',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_show_recent_apps= CheckBox({
    'id'        : 'check_show_recent_apps',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.Unity.ApplicationsLens',
    'path'      : None,
    'key'       : 'display-recent-apps',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_use_locate= CheckBox({
    'id'        : 'check_use_locate',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.Unity.FilesLens',
    'path'      : None,
    'key'       : 'use-locate',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

# TODO:
# b_clear_run_history


DashIcons=Tab([sw_dash_blur,
               radio_dash_blur_smart,
               radio_dash_blur_static,
               check_suggestions,
               check_show_recent_apps,
               check_show_available_apps,
               check_use_locate])


#=============== PANEL ==========================

spin_menu_visible=SpinButton({
    'id'     : 'spin_menu_visible',
    'builder': Unity.builder,
    'schema' : 'org.compiz.unityshell',
    'path'   : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'    : 'menus-discovery-duration',
    'type'   : 'int',
    'min'    : 0,
    'max'    : 10
})

sc_panel_transparency=Scale({
     'id'     : 'sc_panel_transparency',
     'builder': Unity.builder,
     'schema' : 'org.compiz.unityshell',
     'path'   : '/org/compiz/profiles/unity/plugins/unityshell/',
     'key'    : 'panel-opacity',
     'type'   : 'double',
     'min'    : 0.2, # TODO : Check these min max. Most prolly wrong.
     'max'    : 8.0, # But fine since they are ignored anyway.
     'ticks'  : [(0.666, Gtk.PositionType.BOTTOM, None)]
 })


check_panel_opaque= CheckBox({
    'id'        : 'check_panel_opaque',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'panel-opacity-maximized-toggle',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_indicator_datetime= CheckBox({
    'id'        : 'check_indicator_datetime',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'show-clock',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': ['radio_12hour',
                    'radio_24hour',
                    'check_date',
                    'check_weekday',
                    'check_calendar',
                    'l_clock',
                    'check_time_seconds']
})

radio_12hour=Radio({
    'id'        : 'radio_12hour',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'time-format',
    'type'      : 'string',
    'group'     : 'radio_24hour',
    'value'     : '12-hour',
    'dependants': []
})

radio_24hour=Radio({
    'id'        : 'radio_24hour',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'time-format',
    'type'      : 'string',
    'group'     : 'radio_24hour',
    'value'     : '24-hour',
    'dependants': []
})

check_time_seconds= CheckBox({
    'id'        : 'check_time_seconds',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'show-seconds',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_date= CheckBox({
    'id'        : 'check_date',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'show-date',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_weekday= CheckBox({
    'id'        : 'check_weekday',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'show-day',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_calendar= CheckBox({
    'id'        : 'check_calendar',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.datetime',
    'path'      : None,
    'key'       : 'show-calendar',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_indicator_bluetooth= CheckBox({
    'id'        : 'check_indicator_bluetooth',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.bluetooth',
    'path'      : None,
    'key'       : 'visible',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_indicator_battery= CheckBox({
    'id'        : 'check_indicator_battery',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.power',
    'path'      : None,
    'key'       : 'icon-policy',
    'type'      : 'string',
    'map'       : defaultdict(lambda:True,{'present':True,'never':False}),
    'dependants': ['check_indicator_battery_life',
                    'radio_power_charging',
                    'radio_power_always']
})


radio_power_always=Radio({
    'id'        : 'radio_power_always',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.power',
    'path'      : None,
    'key'       : 'icon-policy',
    'type'      : 'string',
    'group'     : 'radio_power_charging',
    'value'     : 'present',
    'dependants': []
})

radio_power_charging=Radio({
    'id'        : 'radio_power_charging',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.power',
    'path'      : None,
    'key'       : 'icon-policy',
    'type'      : 'string',
    'group'     : 'radio_power_charging',
    'value'     : 'charge',
    'dependants': []
})


check_indicator_battery_life= CheckBox({
    'id'        : 'check_indicator_battery_life',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.power',
    'path'      : None,
    'key'       : 'show-time',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_indicator_sound= CheckBox({
    'id'        : 'check_indicator_sound',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.sound',
    'path'      : None,
    'key'       : 'visible',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_scroll_notifyosd= CheckBox({
    'id'        : 'check_scroll_notifyosd',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.sound',
    'path'      : None,
    'key'       : 'show-notify-osd-on-scroll',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_indicator_username= CheckBox({
    'id'        : 'check_indicator_username',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.session',
    'path'      : None,
    'key'       : 'show-real-name-on-panel',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})



# TODO:

# cbox_default_player

PanelIcons=Tab([spin_menu_visible,
                 sc_panel_transparency,
                 check_panel_opaque,
                 check_indicator_datetime,
                 radio_12hour,
                 radio_24hour,
                 check_time_seconds,
                 check_date,
                 check_weekday,
                 check_calendar,
                 check_indicator_battery,
                 radio_power_charging,
                 radio_power_always,
                 check_indicator_battery_life,
                 check_indicator_bluetooth,
                 check_indicator_sound,
                 check_scroll_notifyosd,
                 check_indicator_username])

#=============== SWITCHER ==========================


check_switchwindows_all_workspaces= CheckBox({
    'id'        : 'check_switchwindows_all_workspaces',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'alt-tab-bias-viewport',
    'type'      : 'boolean',
    'map'       : {False:True,True:False},
    'dependants': []
})

check_switcher_showdesktop= CheckBox({
    'id'        : 'check_switcher_showdesktop',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'disable-show-desktop',
    'type'      : 'boolean',
    'map'       : {False:True,True:False},
    'dependants': []
})

check_minimizedwindows_switch= CheckBox({
    'id'        : 'check_minimizedwindows_switch',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'show-minimized-windows',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

check_autoexposewindows= CheckBox({
    'id'        : 'check_autoexposewindows',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'alt-tab-timeout',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

# TODO:
# list_unity_switcher_windows_accelerators
# list_unity_switcher_launcher_accelerators

SwitcherIcons=Tab([check_switchwindows_all_workspaces,
                    check_switcher_showdesktop,
                    check_minimizedwindows_switch,
                    check_autoexposewindows])

#=============== WEB APPS ==========================


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

# XXX : functors
# check_preauthorized_amazon= CheckBox({
#     'id'        : 'check_preauthorized_amazon',
#     'builder'   : Unity.builder,
#     'schema'    : 'com.canonical.unity.webapps',
#     'path'      : None,
#     'key'       : 'preauthorized-domains',
#     'type'      : 'strv',
#     'map'       : {True:True,False:False},
#     'dependants': []
# })

# check_preauthorized_ubuntuone= CheckBox({
#     'id'        : 'check_preauthorized_ubuntuone',
#     'builder'   : Unity.builder,
#     'schema'    : 'com.canonical.unity.webapps',
#     'path'      : None,
#     'key'       : 'preauthorized-domains',
#     'type'      : 'strv',
#     'map'       : {True:True,False:False},
#     'dependants': []
# })

# TODO:
# check_preauthorized_amazon
# check_preauthorized_ubuntuone

WebappsIcons=Tab([switch_unity_webapps])

#=============== ADDITIONAL ==========================

check_hud_store_data= CheckBox({
    'id'        : 'check_hud_store_data',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.indicator.appmenu.hud',
    'path'      : None,
    'key'       : 'store-usage-data',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})



check_shortcuts_hints_overlay= CheckBox({
    'id'        : 'check_shortcuts_hints_overlay',
    'builder'   : Unity.builder,
    'schema'    : 'org.compiz.unityshell',
    'path'      : '/org/compiz/profiles/unity/plugins/unityshell/',
    'key'       : 'shortcut-overlay',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})

radio_all_monitors=Radio({
    'id'        : 'radio_all_monitors',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.notify-osd',
    'path'      : None,
    'key'       : 'multihead-mode',
    'type'      : 'string',
    'group'     : 'radio_active_monitor',
    'value'     : 'dont-follow-focus',
    'dependants': []
})

radio_active_monitor=Radio({
    'id'        : 'radio_active_monitor',
    'builder'   : Unity.builder,
    'schema'    : 'com.canonical.notify-osd',
    'path'      : None,
    'key'       : 'multihead-mode',
    'type'      : 'string',
    'group'     : 'radio_active_monitor',
    'value'     : 'follow-focus',
    'dependants': []
})

# TODO
# list_unity_additional_accelerators


AdditionalIcons=Tab([check_hud_store_data,
                     check_shortcuts_hints_overlay,
                     radio_all_monitors,
                     radio_active_monitor])

# Pass in the id of restore defaults button to enable it.
LauncherIcons.enable_restore('b_unity_launcher_reset')
DashIcons.enable_restore('b_unity_dash_reset')
PanelIcons.enable_restore('b_unity_panel_reset')
SwitcherIcons.enable_restore('b_unity_switcher_reset')
WebappsIcons.enable_restore('b_unity_webapps_reset')
AdditionalIcons.enable_restore('b_unity_additional_reset')

# Each page must be added using add_page
Unity.add_page(LauncherIcons)
Unity.add_page(DashIcons)
Unity.add_page(PanelIcons)
Unity.add_page(SwitcherIcons)
Unity.add_page(WebappsIcons)
Unity.add_page(AdditionalIcons)

# XXX : Spaghetti bridge
unitysettings=HandlerObject(SpaghettiUnitySettings(Unity.builder))
Unity.add_page(unitysettings)
# After all pages are added, the section needs to be registered to start listening for events
Unity.register()
