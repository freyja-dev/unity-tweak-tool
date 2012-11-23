#!/usr/bin/env python3
from gi.repository import Gtk

class Handler ():
    '''Clicking the toolbars'''
    def on_tool_startpage_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(0)
    def on_tool_unitysettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(1)
    def on_tool_compizsettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(2)
    def on_tool_themesettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(3)
    def on_tool_desktopsettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(4)
        
    '''Clicking on the icons in the start page'''
     
    def on_tool_launcher_clicked(self,nb_unitysettings):
        #destroy()
        nb_unitysettings.set_current_page(0)
                        
        
# Basic builder setting up
        
builder = Gtk.Builder()
builder.add_from_file("mechanig.glade")
builder.connect_signals(Handler())


# The main Mechanig window that needs to be shown
mechanig_main = builder.get_object('mechanig_main')

# This signal is emitted when you close the window,
# which triggers Gtk.main_quit, which tells the main Gtk loop to quit
mechanig_main.connect("delete-event", Gtk.main_quit)

# This is required, otherwise Gtk leaves the window hidden.
# Useful, like with our dummy "windows" that get reparented
mechanig_main.show_all()

# Runs the main loop
Gtk.main()
