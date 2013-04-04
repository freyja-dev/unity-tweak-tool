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
import sys
import logging
import dbus, dbus.service
from gi.repository import Gtk
from dbus.mainloop.glib import DBusGMainLoop
from UnityTweakTool.config.logging import LOGFILE,LOGFMT,LOGLVL

DBusGMainLoop(set_as_default=True)

logger=logging.getLogger('UnityTweakTool')
logger.setLevel(LOGLVL)

_fh=logging.FileHandler(LOGFILE)
_fh.setLevel(LOGLVL)

_formatter=logging.Formatter(LOGFMT)

_fh.setFormatter(_formatter)
logger.addHandler(_fh)

del _fh, _formatter


##########################################################################

class Application(dbus.service.Object):
    def __init__(self,pageid=-1):
        DIR=os.path.expanduser('~/.config/unity-tweak-tool/')
        LOCKFILE=os.path.join(DIR,"pid.lockfile")
        if not os.path.exists(DIR):
            os.makedirs(DIR)
        if os.access(LOCKFILE, os.F_OK):
            pidfile = open(LOCKFILE, "r")
            pidfile.seek(0)
            old_pd = pidfile.readline()
            pidfile.close()
            if os.path.exists("/proc/%s" % old_pd):
                print("""
        Another instance of Unity Tweak Tool seems to be running with
        process id %s. Switching to the already existing window.
                    """ % old_pd)
                self.call_running_instance(pageid)
                sys.exit(1)
            else:
                os.remove(LOCKFILE)

        pidfile = open(LOCKFILE, "w")
        pidfile.write("%s" % os.getpid())
        pidfile.close()

        self.register_dbus_session()
        self.run(pageid)

    def run(self,pageid):
        from UnityTweakTool.config.data import get_data_path
        self.builder=Gtk.Builder()
        self.ui=os.path.join(get_data_path(),'unitytweak.ui')
        self.builder.add_from_file(self.ui)
        self.notebook=self.builder.get_object('nb_unitytweak')
        self.connectpages()
        self.connecthandlers()
# from gi.repository import Unity
#        self.launcher = Unity.LauncherEntry.get_for_desktop_id("unity-tweak-tool.desktop")        
        self.window=self.builder.get_object('unitytweak_main')
        self.window.show_all()
        self.window.connect('delete-event',Gtk.main_quit)
        if pageid is not None:
            self.switch_to_page(pageid)
        Gtk.main()

    def connectpages(self):
        from UnityTweakTool.section.overview import Overview
        from UnityTweakTool.section.unity import Unity
        from UnityTweakTool.section.windowmanager import WindowManager
        from UnityTweakTool.section.system import System
        from UnityTweakTool.section.appearance import Appearance
        sections=[Overview(self.notebook),Unity,WindowManager,Appearance,System]
        for section in sections:
            id=self.notebook.append_page(section.page,None)
            assert id is not -1

    def connecthandlers(self):
        handler={}
        def show_overview(*args,**kwargs):
            self.notebook.set_current_page(0)
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
        self.builder.connect_signals(handler)
    


    def register_dbus_session(self):
        bus_name = dbus.service.BusName('org.freyja.utt', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/freyja/utt')

    def call_running_instance(self, pageid):
        bus = dbus.SessionBus()
        service = bus.get_object('org.freyja.utt', '/org/freyja/utt')
        service.get_dbus_method('switch_to_page', 'org.freyja.utt')(pageid)

    @dbus.service.method('org.freyja.utt', in_signature='i')
    def switch_to_page(self, pageid):
        if pageid is not -1:
            self.notebook.set_current_page(pageid)
        self.window.present()

