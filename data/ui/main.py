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
        self.glade="mechanig.ui"
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui=ui(self.builder)
        
        self.builder.connect_signals(self)
        #self.ui['mechanig_main'].set_resizable(False)
        #self.ui['nb_mechanig'].set_show_tabs(False)
        
        print("poke")
        
        self.start = Startpage()
        #self.add(self.start)
        
        self.box = self.builder.get_object("box_toolbar")
        
        self.box.pack_end(self.start, True, True, 0)
        print("poketest")
        
        self.ui['mechanig_main'].show_all()
        self.ui['mechanig_main'].connect("delete-event", Gtk.main_quit)
        
        Gtk.main()  

if __name__=='__main__':
# Fire up the Engines
    Mechanig()
