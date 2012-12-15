#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio
from ui import ui
from start import Startpage


class Mechanig ():
    def __init__(self):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = "mechanig.ui"
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)

        self.builder.connect_signals(self)
        #self.ui['mechanig_main'].set_resizable(False)
        #self.ui['nb_mechanig'].set_show_tabs(False)

        self.start = Startpage().ui['box_startpage']
        #self.add(self.start)

        self.box = self.builder.get_object("box_toolbar")

        self.box.pack_end(self.start, True, True, 0)

        self.ui['mechanig_main'].show_all()
        self.ui['mechanig_main'].connect("delete-event", Gtk.main_quit)

        Gtk.main()

    # ===== Top Navigation bar =====
    def on_tool_startpage_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(0)
    def on_tool_unitysettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(1)
        self.ui['nb_unitysettings'].set_current_page(0)
    def on_tool_compizsettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(2)
        self.ui['nb_compizsettings'].set_current_page(0)
    def on_tool_themesettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(3)
        self.ui['nb_themesettings'].set_current_page(0)
    def on_tool_desktopsettings_toggled(self,udata):
        self.ui['nb_mechanig'].set_current_page(4)

if __name__=='__main__':
# Fire up the Engines
    Mechanig()
else:
    print("WARNING: This module is not tailored to be imported. Proceed at your own risk.")
