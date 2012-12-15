#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio
from ui import ui
from start import Startpage
from unity import Unitysettings
from compiz import Compizsettings
from theme import Themesettings
from desktop import Desktopsettings


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

        self.notebook = self.ui['nb_mechanig']

        self.startpage = Startpage(self.ui, self.notebook)
        self.unitysettings = Unitysettings(self.ui)
        self.compizsettings = Compizsettings(self.ui)
        self.themesettings = Themesettings(self.ui)
        self.desktopsettings = Desktopsettings(self.ui)

        #self.box.pack_end(self.start, True, True, 0)

        self.notebook.append_page(self.startpage.page, None)
        self.notebook.append_page(self.unitysettings.page, None)
        self.notebook.append_page(self.compizsettings.page, None)
        self.notebook.append_page(self.themesettings.page, None)
        self.notebook.append_page(self.desktopsettings.page, None)

        self.ui['mechanig_main'].show_all()
        self.ui['mechanig_main'].connect("delete-event", Gtk.main_quit)

        Gtk.main()

    # ===== Top Navigation bar =====
    def on_tool_startpage_toggled(self,udata):
        self.notebook.set_current_page(0)
    def on_tool_unitysettings_toggled(self,udata):
        self.notebook.set_current_page(1)
        self.unitysettings.page.set_current_page(0)
    def on_tool_compizsettings_toggled(self,udata):
        self.notebook.set_current_page(2)
        self.compizsettings.page.set_current_page(0)
    def on_tool_themesettings_toggled(self,udata):
        self.notebook.set_current_page(3)
        self.themesettings.page.set_current_page(0)
    def on_tool_desktopsettings_toggled(self,udata):
        self.notebook.set_current_page(4)



    # gtk search box

    # inserting text shows the secondary icon (stock-clear)

    def on_tool_entry_search_insert_text(self,text,length,position,udata):

        # getting the text length to workaround some Gtk bug
        if self.ui['tool_entry_search'].get_text_length()+1:
            self.ui['tool_entry_search'].set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY,
                Gtk.STOCK_CLEAR)

        else:
            self.ui['tool_entry_search'].set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY, None)

    def on_tool_entry_search_delete_text(self,start_pos,end_pos,udata):

        # getting the text length to workaround some Gtk bug

        if (self.ui['tool_entry_search'].get_text_length()-1) == 0:
            self.ui['tool_entry_search'].set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY, None)

    # clicking on secondary icon clearing text

    def on_tool_entry_search_icon_press(self, widget, icon, mouse_button):

        if icon == Gtk.EntryIconPosition.SECONDARY:
            widget.set_text("")
            widget.set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY, None)

        if icon == Gtk.EntryIconPosition.PRIMARY:
            print("Searching")

if __name__=='__main__':
# Fire up the Engines
    Mechanig()
else:
    print("WARNING: This module is not tailored to be imported. Proceed at your own risk.")
