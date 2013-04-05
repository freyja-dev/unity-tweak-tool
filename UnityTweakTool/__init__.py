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

# List of all subpackages that can be imported using
# from UnityTweakTool import *
__all__=['backends','config','elements']

import os
import logging
from gi.repository import Gtk
from UnityTweakTool.config.logging import LOGFILE,LOGFMT,LOGLVL

logger=logging.getLogger('UnityTweakTool')
logger.setLevel(LOGLVL)

_fh=logging.FileHandler(LOGFILE)
_fh.setLevel(LOGLVL)

_formatter=logging.Formatter(LOGFMT)

_fh.setFormatter(_formatter)
logger.addHandler(_fh)

del _fh, _formatter

def pid_lock_exists():
    return False
# TODO : implement this.

def connectpages():
    from UnityTweakTool.section.overview import Overview
    from UnityTweakTool.section.unity import Unity
    from UnityTweakTool.section.windowmanager import WindowManager
    from UnityTweakTool.section.system import System
    from UnityTweakTool.section.appearance import Appearance
    sections=[Overview(notebook),Unity,WindowManager,Appearance,System]
    for section in sections:
        id=notebook.append_page(section.page,None)
        assert id is not -1

def connecthandlers(builder):
    handler={}
    def show_overview(*args,**kwargs):
        notebook.set_current_page(0)
    handler['on_b_overview_clicked']=show_overview

    appmenu={
        'unity_launcher'    :(1,0),
        'unity_dash'        :(1,1),
        'unity_panel'       :(1,2),
        'unity_switcher'    :(1,3),
        'unity_webapps'     :(1,4),
        'unity_additional'  :(1,5),

        'compiz_general'    :(2,0),
        'compiz_workspace'  :(2,1),
        'compiz_windows_spread' :(2,2),
        'compiz_windows_snapping':(2,3),
        'compiz_hotcorners'         :(2,4),
        'compiz_additional'         :(2,5),

        'theme_system'      :(3,0),
        'theme_icon'        :(3,1),
        'theme_cursor'      :(3,2),
        'theme_fonts'       :(3,3),
        'window_controls'   :(3,4),

        'desktop_icons'     :(4,0),
        'system_security'   :(4,1),
        'scrolling'         :(4,2)
    }

    def gen_appmenu_handler(loc):
        def appmenu_handler(*args):
            notebook.set_current_page(loc[0])
            notebook.get_nth_page(loc[0]).set_current_page(loc[1])
        return appmenu_handler

    for item,location in appmenu.items():
        handler['on_menuitem_%s_activate'%item]=gen_appmenu_handler(location)

    handler['on_menuimage_quit_activate']=lambda *args:Gtk.main_quit()
    from UnityTweakTool.about import About
    handler['on_menuimage_about_activate']=lambda *args: About()
    builder.connect_signals(handler)
##########################################################################
def init(page=0):
    if pid_lock_exists():
        return
    from UnityTweakTool.config.data import get_data_path
    global notebook
    builder=Gtk.Builder()
    builder.set_translation_domain('unity-tweak-tool')
    ui=os.path.join(get_data_path(),'unitytweak.ui')
    builder.add_from_file(ui)
    notebook=builder.get_object('nb_unitytweak')
    connectpages()
    notebook.set_current_page(page)
    connecthandlers(builder)
    builder.get_object('unitytweak_main').show_all()
    builder.get_object('unitytweak_main').connect('delete-event',Gtk.main_quit)
    Gtk.main()

