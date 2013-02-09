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

def connectpages(notebook):
    from UnityTweakTool.section.overview import Overview
    from UnityTweakTool.section.unity import Unity
    from UnityTweakTool.section.windowmanager import WindowManager
    from UnityTweakTool.section.system import System
    from UnityTweakTool.section.appearance import Appearance
    sections=[Overview(notebook),Unity,WindowManager,Appearance,System]
    for section in sections:
        id=notebook.append_page(section.page,None)
        assert id is not -1
    notebook.set_current_page(0)

def init(page='overview'):
    print('Initialising...')
    from UnityTweakTool.config.data import get_data_path
    builder=Gtk.Builder()
    ui=os.path.join(get_data_path(),'unitytweak.ui')
    builder.add_from_file(ui)
    notebook=builder.get_object('nb_unitytweak')
    connectpages(notebook)
    def show_overview(*args,**kwargs):
        notebook.set_current_page(0)
    handler={'on_b_overview_clicked':show_overview}
    builder.connect_signals(handler)
    builder.get_object('unitytweak_main').show_all()
    builder.get_object('unitytweak_main').connect('delete-event',Gtk.main_quit)
    Gtk.main()

