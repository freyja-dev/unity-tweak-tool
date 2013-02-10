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

import os, os.path

from gi.repository import Gtk, Gio, Gdk

from .ui import ui
from . import unitytweakconfig
from . import gsettings

class Desktopsettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = (os.path.join(unitytweakconfig.get_data_path(),
                                    'desktop.ui'))
        self.container = container
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['nb_desktop_settings']
        self.page.unparent()

        self.refresh()
        self.builder.connect_signals(self)

#=====================================================================#
#                                Helpers                              #
#=====================================================================#
    def refresh(self):
        '''Reads the current config and refreshes the displayed values'''

        # ===== Icons ===== #
    
        # Show desktop icons
        dependants = ['l_desktop_icons_display',
                    'check_desktop_home',
                    'check_desktop_networkserver',
                    'check_desktop_trash',
                    'check_desktop_devices']
        if gsettings.background.get_boolean('show-desktop-icons') == True:
            self.ui['switch_desktop_icons'].set_active(True)
            self.ui.sensitize(dependants)
        else:
            self.ui['switch_desktop_icons'].set_active(False)
            self.ui.unsensitize(dependants)
        del dependants

        # Visible icons
        self.ui['check_desktop_home'].set_active(gsettings.desktop.get_boolean('home-icon-visible'))
        self.ui['check_desktop_networkserver'].set_active(gsettings.desktop.get_boolean('network-icon-visible'))
        self.ui['check_desktop_trash'].set_active(gsettings.desktop.get_boolean('trash-icon-visible'))
        self.ui['check_desktop_devices'].set_active(gsettings.desktop.get_boolean('volumes-visible'))


        # ===== Security ===== #

        self.ui['check_security_lock_screen'].set_active(True if gsettings.lockdown.get_boolean('disable-lock-screen') is False else False)
        self.ui['check_security_logout'].set_active(True if gsettings.lockdown.get_boolean('disable-log-out') is False else False)
        self.ui['check_security_printing'].set_active(True if gsettings.lockdown.get_boolean('disable-printing') is False else False)
        self.ui['check_security_user_switching'].set_active(True if gsettings.lockdown.get_boolean('disable-user-switching') is False else False)

        # ===== Scrolling ===== #

        # Scrollbars
        overlay_scrollbars = gsettings.scrollbars.get_string('scrollbar-mode')
        dependants = ['l_overlay_scrollbar_mode',
                    'cbox_overlay_scrollbar_mode']

        if overlay_scrollbars == 'normal':
            self.ui['radio_overlay_scrollbars'].set_active(False)
            self.ui['radio_legacy_scrollbars'].set_active(True)
            self.ui.unsensitize(dependants)
        else:
            self.ui['radio_overlay_scrollbars'].set_active(True)
            self.ui['radio_legacy_scrollbars'].set_active(False)
            self.ui.sensitize(dependants)
        del overlay_scrollbars, dependants

        # Scrollbar mode
        scrollbar_mode = gsettings.scrollbars.get_string('scrollbar-mode')
        if scrollbar_mode == 'overlay-auto':
            self.ui['cbox_overlay_scrollbar_mode'].set_active(0)
        elif scrollbar_mode == 'overlay-pointer':
            self.ui['cbox_overlay_scrollbar_mode'].set_active(1)
        elif scrollbar_mode == 'overlay-touch':
            self.ui['cbox_overlay_scrollbar_mode'].set_active(2)
        else:
            self.ui['cbox_overlay_scrollbar_mode'].set_active(0)

        # Touchpad scroll mode
        scroll_mode = gsettings.touch.get_string('scroll-method')
        if scroll_mode == 'edge-scrolling':
            self.ui['radio_edge'].set_active(True)
        else:
            self.ui['radio_two_finger'].set_active(True)
        del scroll_mode

        # Horizontal Scrolling
        self.ui['check_horizontal_scrolling'].set_active(True if gsettings.touch.get_boolean('horiz-scroll-enabled') is True else False)

# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, unity-tweak-tool can resist glade stupidity.    |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/


#======== Begin Desktop Icons Settings

    def on_switch_desktop_icons_active_notify(self, widget, udata = None):
        dependants = ['l_desktop_icons_display',
                    'check_desktop_home',
                    'check_desktop_networkserver',
                    'check_desktop_trash',
                    'check_desktop_devices']

        if self.ui['switch_desktop_icons'].get_active():
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

    def on_b_desktop_settings_icons_reset_clicked(self, widget):
        gsettings.desktop.reset('show-desktop-icons')
        gsettings.desktop.reset('home-icon-visible')
        gsettings.desktop.reset('network-icon-visible')
        gsettings.desktop.reset('trash-icon-visible')
        gsettings.desktop.reset('volumes-visible')
        self.refresh()

#======== Begin Desktop Security Settings

    def on_check_security_lock_screen_toggled(self, widget, udata = None):
        if self.ui['check_security_lock_screen'].get_active() == True :
            gsettings.lockdown.set_boolean('disable-lock-screen', False)
        else:
            gsettings.lockdown.set_boolean('disable-lock-screen', True)

    def on_check_security_logout_toggled(self, widget, udata = None):
        if self.ui['check_security_logout'].get_active() == True :
            gsettings.lockdown.set_boolean('disable-log-out', False)
        else:
            gsettings.lockdown.set_boolean('disable-log-out', True)

    def on_check_security_printing_toggled(self, widget, udata = None):
        if self.ui['check_security_printing'].get_active() == True :
            gsettings.lockdown.set_boolean('disable-printing', False)
            gsettings.lockdown.set_boolean('disable-print-setup', False)
        else:
            gsettings.lockdown.set_boolean('disable-printing', True)
            gsettings.lockdown.set_boolean('disable-print-setup', True)

    def on_check_security_user_switching_toggled(self, widget, udata = None):
        if self.ui['check_security_user_switching'].get_active() == True :
            gsettings.lockdown.set_boolean('disable-user-switching', False)
        else:
            gsettings.lockdown.set_boolean('disable-user-switching', True)

    def on_b_desktop_settings_security_reset_clicked(self, widget):
        gsettings.lockdown.reset('disable-lock-screen')
        gsettings.lockdown.reset('disable-log-out')
        gsettings.lockdown.reset('disable-printing')
        gsettings.lockdown.reset('disable-print-setup')
        gsettings.lockdown.reset('disable-user-switching')
        self.refresh()

#======== Begin Desktop Scrolling Settings

    def on_radio_legacy_scrollbars_toggled(self, button, udata = None):
        dependants = ['l_overlay_scrollbar_mode',
                    'cbox_overlay_scrollbar_mode']
        if self.ui['radio_legacy_scrollbars'].get_active() == True:
            gsettings.scrollbars.set_string('scrollbar-mode', 'normal')
            self.ui.unsensitize(dependants)
        else:
            gsettings.scrollbars.set_string('scrollbar-mode', 'overlay-auto')
            self.ui.sensitize(dependants)

    def on_radio_overlay_scrollbars_toggled(self, button, udata = None):
        dependants = ['l_overlay_scrollbar_mode',
                    'cbox_overlay_scrollbar_mode']
        if self.ui['radio_overlay_scrollbars'].get_active() == True:
            gsettings.scrollbars.set_string('scrollbar-mode', 'overlay-auto')
            self.ui.sensitize(dependants)
        else:
            gsettings.scrollbars.set_string('scrollbar-mode', 'normal')
            self.ui.unsensitize(dependants)

    def on_cbox_overlay_scrollbar_mode_changed(self, widget, udata = None):
        if self.ui['cbox_overlay_scrollbar_mode'].get_active() == 0:
            gsettings.scrollbars.set_string('scrollbar-mode', 'overlay-auto')
        elif self.ui['cbox_overlay_scrollbar_mode'].get_active() == 1:
            gsettings.scrollbars.set_string('scrollbar-mode', 'overlay-pointer')
        elif self.ui['cbox_overlay_scrollbar_mode'].get_active() == 2:
            gsettings.scrollbars.set_string('scrollbar-mode', 'overlay-touch')
        else:
            gsettings.scrollbars.set_string('scrollbar-mode', 'overlay-auto')

    def on_radio_edge_toggled(self, button, udata = None):
        if self.ui['radio_edge'].get_active() == True:
            gsettings.touch.set_string('scroll-method', 'edge-scrolling')
        else:
            gsettings.touch.set_string('scroll-method', 'two-finger-scrolling')

    def on_radio_two_finger_toggled(self, button, udata = None):
        if self.ui['radio_two_finger'].get_active() == True:
            gsettings.touch.set_string('scroll-method', 'two-finger-scrolling')
        else:
            gsettings.touch.set_string('scroll-method', 'edge-scrolling')

    def on_check_horizontal_scrolling_toggled(self, widget, udata = None):
        if self.ui['check_horizontal_scrolling'].get_active() == True :
            gsettings.touch.set_boolean('horiz-scroll-enabled', True)
        else:
            gsettings.touch.set_boolean('horiz-scroll-enabled', False)

    def on_b_settings_scrolling_reset_clicked(self, widget):
        gsettings.touch.reset('scroll-method')
        gsettings.scrollbars.reset('scrollbar-mode')
        self.refresh()


if __name__ == '__main__':
# Fire up the Engines
    Desktopsettings()
# FIXME : Guaranteed to fail
