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
     
    # unity settings on start page 
    def on_tool_launcher_clicked(self,nb_unitysettings):
        builder.get_object('tool_unitysettings').set_active(True)
        nb_unitysettings.set_current_page(0)
    def on_tool_dash_clicked(self,nb_unitysettings):
        builder.get_object('tool_unitysettings').set_active(True)
        nb_unitysettings.set_current_page(1)
    def on_tool_panel_clicked(self,nb_unitysettings):
        builder.get_object('tool_unitysettings').set_active(True)
        nb_unitysettings.set_current_page(2)
    def on_tool_unity_switcher_clicked(self,nb_unitysettings):
        builder.get_object('tool_unitysettings').set_active(True)
        nb_unitysettings.set_current_page(3)    
    def on_tool_additional_clicked(self,nb_unitysettings):
        builder.get_object('tool_unitysettings').set_active(True)
        nb_unitysettings.set_current_page(4)    
    def on_tool_launcher_clicked(self,nb_unitysettings):
        builder.get_object('tool_unitysettings').set_active(True)
        nb_unitysettings.set_current_page(0)
        
    # Compiz settings buttons on start page        
    def on_tool_general_clicked(self,nb_compizsettings):
        builder.get_object('tool_compizsettings').set_active(True)
        nb_compizsettings.set_current_page(0)                        
    def on_tool_compiz_switcher_clicked(self,nb_compizsettings):
        builder.get_object('tool_compizsettings').set_active(True)
        nb_compizsettings.set_current_page(1)
    def on_tool_windows_spread_clicked(self,nb_compizsettings):
        builder.get_object('tool_compizsettings').set_active(True)
        nb_compizsettings.set_current_page(2)
    def on_tool_windows_snapping_clicked(self,nb_compizsettings):
        builder.get_object('tool_compizsettings').set_active(True)
        nb_compizsettings.set_current_page(3)
    def on_tool_hotcorners_clicked(self,nb_compizsettings):
        builder.get_object('tool_compizsettings').set_active(True)
        nb_compizsettings.set_current_page(4)
        
    # Theme settings on Start page    
    def on_tool_system_clicked(self,nb_themesettings):
        builder.get_object('tool_themesettings').set_active(True)
        nb_themesettings.set_current_page(0)  
    def on_tool_icons_clicked(self,nb_themesettings):
        builder.get_object('tool_themesettings').set_active(True)
        nb_themesettings.set_current_page(1) 
    def on_tool_cursors_clicked(self,nb_themesettings):
        builder.get_object('tool_themesettings').set_active(True)
        nb_themesettings.set_current_page(2)     
    def on_tool_fonts_clicked(self,nb_themesettings):
        builder.get_object('tool_themesettings').set_active(True)
        nb_themesettings.set_current_page(3)     
        
    # desktop settings on start page    
        
    def on_tool_desktop_clicked(self,box_settings):
        builder.get_object('tool_desktopsettings').set_active(True)
        
    # compiz hotcorner linked button
    
    def on_lb_configure_hot_corner_activate_link(self,nb_compizsettings):
        nb_compizsettings.set_current_page(4)
    
    def on_lb_configure_hot_corner_windows_spread_activate_link(self,nb_compizsettings):
        nb_compizsettings.set_current_page(4)    
        
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
