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


from UnityTweakTool.section.skeletonpage import Section, Tab
from UnityTweakTool.elements.cbox import ComboBox
from UnityTweakTool.elements.checkbox import CheckBox
from UnityTweakTool.elements.spin import SpinButton
from UnityTweakTool.elements.switch import Switch

from UnityTweakTool.section.spaghetti.compiz import Compizsettings as SpaghettiCompizSettings
from UnityTweakTool.elements.option import Option,HandlerObject

from collections import defaultdict


WindowManager=Section(ui='windowmanager.ui',id='nb_compizsettings')

#=============== GENERAL ==========================

#sw_compiz_zoom= Switch({
#    'id'        : 'sw_compiz_zoom',
#    'builder'   : WindowManager.builder,
#    'schema'    : 'org.compiz.ezoom',
#    'path'      : '/org/compiz/profiles/unity/plugins/ezoom/',
#    'key'       : 'integration-allowed',
#    'type'      : 'boolean',
#    'map'       : {True:True,False:False},
#    'dependants': []
#})

cbox_opengl=ComboBox({
    'id'        : 'cbox_opengl',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.compiz.opengl',
    'path'      : '/org/compiz/profiles/unity/plugins/opengl/',
    'key'       : 'texture-filter',
    'type'      : 'int',
    'map'       : {0:0,1:1,2:2}
})


# TODO:
# TypeError: unhashable type: 'list'

# cbox_minimize_animation=ComboBox({
#     'id'        : 'cbox_minimize_animation',
#     'builder'   : WindowManager.builder,
#     'schema'    : 'org.compiz.animation',
#     'path'      : '/org/compiz/profiles/unity/plugins/animation/',
#     'key'       : 'minimize-effects',
#     'type'      : 'strv',
#     'map'       : {'animation:None':0,
#     				 'animation:Random':1,
#     				 'animation:Curved Fold':2,
#     				 'animation:Fade':3,
#     				 'animation:Glide 1':4,
#     				 'animation:Glide 2':5,
#     				 'animation:Horizontal Folds':6,
#     				 'animation:Magic Lamp':7,
#     				 'animation:Magic Lamp Wavy':8,
#     				 'animation:Sidekick':9,
#     				 'animation:Zoom':10}
# })

# TODO:
# TypeError: unhashable type: 'list'

# cbox_unminimize_animation=ComboBox({
#     'id'        : 'cbox_unminimize_animation',
#     'builder'   : WindowManager.builder,
#     'schema'    : 'org.compiz.animation',
#     'path'      : '/org/compiz/profiles/unity/plugins/animation/',
#     'key'       : 'unminimize-effects',
#     'type'      : 'strv',
#     'map'       : {'animation:None':0,
#     				 'animation:Random':1,
#     				 'animation:Curved Fold':2,
#     				 'animation:Fade':3,
#     				 'animation:Glide 1':4,
#     				 'animation:Glide 2':5,
#     				 'animation:Horizontal Folds':6,
#     				 'animation:Magic Lamp':7,
#     				 'animation:Magic Lamp Wavy':8,
#     				 'animation:Sidekick':9,
#     				 'animation:Zoom':10}
# })


# TODO
# sw_compiz_zoom
# list_compiz_general_zoom_accelerators
# cbox_minimize_animation
# cbox_unminimize_animation
# list_compiz_general_keys_accelerators

GeneralIcons=Tab([cbox_opengl]) #,
				  # cbox_minimize_animation,
				  # cbox_unminimize_animation])


#=============== WORKSPACE SETTINGS ==========================

spin_horizontal_desktop=SpinButton({
    'id'     : 'spin_horizontal_desktop',
    'builder': WindowManager.builder,
    'schema' : 'org.compiz.core',
    'path'   : '/org/compiz/profiles/unity/plugins/core/',
    'key'    : 'hsize',
    'type'   : 'int',
    'min'    : 1,
    'max'    : 25
})

spin_vertical_desktop=SpinButton({
    'id'     : 'spin_vertical_desktop',
    'builder': WindowManager.builder,
    'schema' : 'org.compiz.core',
    'path'   : '/org/compiz/profiles/unity/plugins/core/',
    'key'    : 'vsize',
    'type'   : 'int',
    'min'    : 1,
    'max'    : 25
})

# TODO:

# sw_workspace_switcher
# color_desk_outline
# list_compiz_workspace_accelerators


WorkspaceSettingsIcons=Tab([spin_horizontal_desktop,
							spin_vertical_desktop])

#=============== WINDOW SPREAD ==========================

spin_compiz_spacing=SpinButton({
    'id'     : 'spin_compiz_spacing',
    'builder': WindowManager.builder,
    'schema' : 'org.compiz.scale',
    'path'   : '/org/compiz/profiles/unity/plugins/scale/',
    'key'    : 'spacing',
    'type'   : 'int',
    'min'    : 0,
    'max'    : 250
})

check_overlay_emblem= CheckBox({
    'id'        : 'check_overlay_emblem',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.compiz.scale',
    'path'      : '/org/compiz/profiles/unity/plugins/scale/',
    'key'       : 'overlay-icon',
    'type'      : 'int',
    'map'       : defaultdict(lambda:True,{1:True,0:False}),
    'dependants': []
})

check_click_desktop= CheckBox({
    'id'        : 'check_click_desktop',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.compiz.scale',
    'path'      : '/org/compiz/profiles/unity/plugins/scale/',
    'key'       : 'show-desktop',
    'type'      : 'boolean',
    'map'       : {True:True,False:False},
    'dependants': []
})


# TODO:

# sw_windows_spread
# list_compiz_windows_spread_accelerators

WindowSpreadIcons=Tab([spin_compiz_spacing,
					   check_overlay_emblem,
					   check_click_desktop])

#=============== WINDOW SNAPPING ==========================

# TODO:

# sw_window_snapping
# color_fill_color
# color_outline_color
# window snapping -- comboboxes


#WindowSnappingIcons=Tab([])

#=============== HOTCORNERS ==========================

# TODO:

# switch_hotcorners
# hotcorner comboboxes


#=============== ADDITIONAL ==========================


switch_auto_raise= Switch({
   'id'        : 'switch_auto_raise',
   'builder'   : WindowManager.builder,
   'schema'    : 'org.gnome.desktop.wm.preferences',
   'path'      : None,
   'key'       : 'auto-raise',
   'type'      : 'boolean',
   'map'       : {True:True,False:False},
   'dependants': []
})

switch_raise_on_click= Switch({
   'id'        : 'switch_raise_on_click',
   'builder'   : WindowManager.builder,
   'schema'    : 'org.gnome.desktop.wm.preferences',
   'path'      : None,
   'key'       : 'raise-on-click',
   'type'      : 'boolean',
   'map'       : {True:True,False:False},
   'dependants': []
})


cbox_focus_mode=ComboBox({
    'id'        : 'cbox_focus_mode',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'focus-mode',
    'type'      : 'enum',
    'map'       : {0:0,1:1,2:2}
})

cbox_double_click=ComboBox({
    'id'        : 'cbox_double_click',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'focus-mode',
    'type'      : 'enum',
    'map'       : {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7}
})

cbox_middle_click=ComboBox({
    'id'        : 'cbox_middle_click',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'focus-mode',
    'type'      : 'enum',
    'map'       : {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7}
})

cbox_right_click=ComboBox({
    'id'        : 'cbox_right_click',
    'builder'   : WindowManager.builder,
    'schema'    : 'org.gnome.desktop.wm.preferences',
    'path'      : None,
    'key'       : 'focus-mode',
    'type'      : 'enum',
    'map'       : {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7}
})

# TODO:

# scale_auto_raise_delay
# colorbutton_resize_outline
# colorbutton_resize_fill


AdditionalIcons=Tab([switch_auto_raise,
                     switch_raise_on_click,
					 cbox_focus_mode,
					 cbox_double_click,
					 cbox_middle_click,
					 cbox_right_click])


# Pass in the id of restore defaults button to enable it.
GeneralIcons.enable_restore('b_compiz_general_reset')
WorkspaceSettingsIcons.enable_restore('b_compiz_workspace_reset')
WindowSpreadIcons.enable_restore('b_compiz_windows_spread_reset')
#WindowSnappingIcons.enable_restore('')
AdditionalIcons.enable_restore('b_wm_additional_reset')

## Each page must be added using add_page
WindowManager.add_page(GeneralIcons)
WindowManager.add_page(WorkspaceSettingsIcons)
WindowManager.add_page(WindowSpreadIcons)
#WindowManager.add_page(WindowSnappingIcons)
WindowManager.add_page(AdditionalIcons)

# XXX : Spaghetti bridge
wmsettings=HandlerObject(SpaghettiCompizSettings(WindowManager.builder))
WindowManager.add_page(wmsettings)

# After all pages are added, the section needs to be registered to start listening for events
WindowManager.register()
