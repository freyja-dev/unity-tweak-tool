#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio
from ui import ui

class Desktopsettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = 'desktop.ui'
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['box_desktop_settings']
        self.page.unparent()

#========= Begin Desktop Settings
    def on_sw_desktop_icon_active_notify(self,widget,udata=None):
        dependants=['l_desktop_icons_display','check_desktop_home','check_desktop_networkserver','check_desktop_trash','check_desktop_devices']

        if widget.get_active():
            self.background.set_boolean("show-desktop-icons",True)
            self.ui.sensitize(dependants)

        else:
            self.ui.unsensitize(dependants)
            self.background.set_boolean("show-desktop-icons",False)

    def on_check_desktop_home_toggled(self,widget,udata=None):
        self.desktop.set_boolean('home-icon-visible',
                                 self.ui['check_desktop_home'].get_active())

    def on_check_desktop_networkserver_toggled(self,widget,udata=None):
        self.desktop.set_boolean('network-icon-visible',
                            self.ui['check_desktop_networkserver'].get_active())

    def on_check_desktop_trash_toggled(self,widget,udata=None):
        self.desktop.set_boolean('trash-icon-visible',
                            self.ui['check_desktop_trash'].get_active())

    def on_check_desktop_devices_toggled(self,widget,udata=None):
        self.desktop.set_boolean('volumes-visible',
                            self.ui['check_desktop_devices'].get_active())

    def on_spin_iconsize_value_changed(self,udata=None):
        size=self.ui['spin_iconsize'].get_value()
# TODO : Find where this setting is.

    def on_check_alignment_toggled(self,widget,udata=None):
        pass
# TODO : Find where this setting is.

if __name__=='__main__':
# Fire up the Engines
    Desktopsettings()
