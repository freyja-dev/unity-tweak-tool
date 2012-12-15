#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio
from ui import ui



class Startpage ():
    def __init__(self):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade="startpage.ui"
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui=ui(self.builder)
        
        
        self.builder.connect_signals(self)
        self.ui['startpage_window'].set_resizable(False)
        #self.ui['nb_mechanig'].set_show_tabs(False)
        self.ui['startpage_window'].connect("delete-event", Gtk.main_quit)
        #self.ui['startpage_window'].show_all()
        #Gtk.main()




if __name__=='__main__':
# Fire up the Engines
    Startpage()
