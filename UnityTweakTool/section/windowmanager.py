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


from UnityTweakTool.section.skeletonpage import Section, Tab
from UnityTweakTool.elements.switch import Switch

WindowManager=Section(ui='compiz.ui',id='nb_compizsettings')

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
#GeneralIcons=Tab([sw_compiz_zoom])

## Each page must be added using add_page
#WindowManager.add_page(GeneralIcons)

# After all pages are added, the section needs to be registered to start listening for events
WindowManager.register()
