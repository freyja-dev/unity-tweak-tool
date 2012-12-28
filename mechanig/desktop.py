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
# This file is a part of Mechanig
#
# Mechanig is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# Mechanig is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>

import os, os.path

from gi.repository import Gtk, Gio

from .ui import ui
from . import settings
from . import gsettings

class Desktopsettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = (os.path.join(settings.UI_DIR, 
                                    'desktop.ui'))
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['box_desktop_settings']
        self.page.unparent()

        self.builder.connect_signals(self)
        self.refresh()

#=====================================================================#
#                                Helpers                              #
#=====================================================================#
    def refresh(self):
        return True

# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, mechanig can resist glade stupidity.            |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/

#======== Begin Desktop Settings
    def on_sw_desktop_icon_active_notify(self, widget, udata = None):
        dependants = ['l_desktop_icons_display', 
                    'check_desktop_home', 
                    'check_desktop_networkserver', 
                    'check_desktop_trash', 
                    'check_desktop_devices']

        if widget.get_active():
            gsettings.background.set_boolean("show-desktop-icons", True)
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)
            gsettings.background.set_boolean("show-desktop-icons", False)

    def on_check_desktop_home_toggled(self, widget, udata = None):
        gsettings.desktop.set_boolean('home-icon-visible', 
                                 self.ui['check_desktop_home'].get_active())

    def on_check_desktop_networkserver_toggled(self, widget, udata = None):
        gsettings.desktop.set_boolean('network-icon-visible', 
                            self.ui['check_desktop_networkserver'].get_active())

    def on_check_desktop_trash_toggled(self, widget, udata = None):
        gsettings.desktop.set_boolean('trash-icon-visible', 
                            self.ui['check_desktop_trash'].get_active())

    def on_check_desktop_devices_toggled(self, widget, udata = None):
        gsettings.desktop.set_boolean('volumes-visible', 
                            self.ui['check_desktop_devices'].get_active())

    def on_spin_iconsize_value_changed(self, udata = None):
        size = self.ui['spin_iconsize'].get_value()
# TODO : Find where this setting is.

    def on_check_alignment_toggled(self, widget, udata = None):
        pass
# TODO : Find where this setting is.

if __name__ == '__main__':
# Fire up the Engines
    Desktopsettings()
