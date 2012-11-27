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
    
    # keyboard widgets in unity-additional
    
    def on_craccel_unity_additional_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_additional_accel_cleared(self, craccel, path, model=None):
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

    # keyboard widgets in unity-panel-windows-switcher
     
    def on_craccel_unity_switcher_windows_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_windows_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)
 
    # keyboard widgets in unity-panel-launcher-switcher
     
    def on_craccel_unity_switcher_launcher_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None) 
 
    # keyboard widgets in unity-panel-launcher-switcher
     
    def on_craccel_unity_switcher_launcher_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)  


    # keyboard widgets in compiz-general-zoom
     
    def on_craccel_compiz_general_zoom_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_general_zoom_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None) 
        
    # keyboard widgets in compiz-general-keys
     
    def on_craccel_compiz_general_keys_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_general_keys_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None) 
        
        
    # keyboard widgets in compiz-workspace
     #FIXME: Doesn't work in compiz-workspace.
     
    def on_craccel_compiz_workspace_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None) 

    # keyboard widgets in compiz-windows-spread
     
    #FIXME: Doesn't work in compiz-windows-spread 
     
    def on_craccel_compiz_windows_spread_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model=None):
    
        #FIXME: TypeError: Argument 3 does not allow None as a value
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)
        
    
    # selective selection in unity-launcher - part 1
                
    def on_sw_launcher_hidemode_active_notify(self,widget,udata=None):
        radio_reveal_left = builder.get_object('radio_reveal_left')   
        radio_reveal_topleft = builder.get_object('radio_reveal_topleft')
        sc_reveal_sensitivity = builder.get_object('sc_reveal_sensitivity')
        l_launcher_reveal = builder.get_object('l_launcher_reveal')
        l_launcher_reveal_sensitivity = builder.get_object('l_launcher_reveal_sensitivity')
        
        if sw_launcher_hidemode.get_active() == True:
            radio_reveal_left.set_sensitive(True)
            radio_reveal_topleft.set_sensitive(True)
            sc_reveal_sensitivity.set_sensitive(True)
            l_launcher_reveal.set_sensitive(True)
            l_launcher_reveal_sensitivity.set_sensitive(True)
        else:
            radio_reveal_left.set_sensitive(False)
            radio_reveal_topleft.set_sensitive(False)
            sc_reveal_sensitivity.set_sensitive(False)
            l_launcher_reveal.set_sensitive(False)
            l_launcher_reveal_sensitivity.set_sensitive(False)
# Basic builder setting up
        
builder = Gtk.Builder()
builder.add_from_file("mechanig.glade")
builder.connect_signals(Handler())


# setting up switches that sensitivize things

sw_launcher_hidemode = builder.get_object('sw_launcher_hidemode')





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
