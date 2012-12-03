#!/usr/bin/env python3
from gi.repository import Gtk

class Handler ():
    '''Clicking the toolbars'''
    def on_tool_startpage_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(0)
    def on_tool_unitysettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(1)
        builder.get_object('nb_unitysettings').set_current_page(0)
    def on_tool_compizsettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(2)
        builder.get_object('nb_compizsettings').set_current_page(0)
    def on_tool_themesettings_toggled(self,nb_mechanig):
        nb_mechanig.set_current_page(3)
        builder.get_object('nb_themesettings').set_current_page(0)
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
    
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None) 
        
    # keyboard widgets in compiz-workspace
     
    def on_craccel_compiz_workspace_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_workspace_accel_cleared(self, craccel, path, model=None):
    
        craccel,model=model,craccel
        iter = model.get_iter(path)
        model.set_value(iter, 1, None) 

    # keyboard widgets in compiz-windows-spread
     
    def on_craccel_compiz_windows_spread_accel_edited(self,craccel, path, key, mods, hwcode,model=None):
        craccel,model=model,craccel
# This sorcery is required to compensate for glade's stupidity of passing the arguments always swapped. and thats not a bug, its a feature.
        accel = Gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def on_craccel_compiz_windows_spread_accel_cleared(self, craccel, path, model=None):
    
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


    # selective selection in unity-launcher - part 2
    
    def on_sw_launcher_transparent_active_notify(self,widget,udata=None):
        l_launcher_transparency_scale = builder.get_object('l_launcher_transparency_scale')
        sc_launcher_transparency = builder.get_object('sc_launcher_transparency')
        if sw_launcher_transparent.get_active() == True:
            l_launcher_transparency_scale.set_sensitive(True)
            sc_launcher_transparency.set_sensitive(True)
            
        else:
            l_launcher_transparency_scale.set_sensitive(False)
            sc_launcher_transparency.set_sensitive(False)
            
    # selective selection in unity-launcher - part 3
    
    def on_radio_launcher_color_cus_active_notify(self,widget,udata=None):
        color_launcher_color_cus  = builder.get_object('color_launcher_color_cus')
        if radio_launcher_color_cus.get_active() == True:
            color_launcher_color_cus.set_sensitive(True)
            
        else:
            color_launcher_color_cus.set_sensitive(False)   
   
    # selective selection in unity-dash - part 1
   
    def on_sw_dash_blur_active_notify(self,widget,udata=None):
        radio_dash_blur_smart = builder.get_object('radio_dash_blur_smart')
        radio_dash_blur_static = builder.get_object('radio_dash_blur_static')
        l_dash_blur = builder.get_object('l_dash_blur')
        
        if sw_dash_blur.get_active() == True:
            radio_dash_blur_smart.set_sensitive(True)
            radio_dash_blur_static.set_sensitive(True)
            l_dash_blur.set_sensitive(True)
        
        else:
            radio_dash_blur_smart.set_sensitive(False)
            radio_dash_blur_static.set_sensitive(False) 
            l_dash_blur.set_sensitive(False)
      
      # selective selection in unity-dash - part 2
      
    def on_radio_dash_color_cus_active_notify(self,widget,udata=None):
        color_dash_color_cus = builder.get_object('color_dash_color_cus')
        
        if radio_dash_color_cus.get_active() == True:
            color_dash_color_cus.set_sensitive(True)
            
        else:
            color_dash_color_cus.set_sensitive(False)
            
    # selective selection in unity-panel part 1
  
    def on_sw_appmenu_autohide_active_notify(self,widget,udata=None):
        spin_menu_visible = builder.get_object('spin_menu_visible')
        l_menu_visible = builder.get_object('l_menu_visible')
        
        if sw_appmenu_autohide.get_active() == True:
            spin_menu_visible.set_sensitive(True)
            l_menu_visible.set_sensitive(True)
        
        else:
            spin_menu_visible.set_sensitive(False)
            l_menu_visible.set_sensitive(False)
            
    # selective selection in unity-panel  part 2
  
    def on_sw_transparent_panel_active_notify(self,widget,udata=None):
        sc_panel_transparency = builder.get_object('sc_panel_transparency')
        l_transparent_panel = builder.get_object('l_transparent_panel')
        check_panel_opaque = builder.get_object('check_panel_opaque')
        
        if sw_transparent_panel.get_active() == True:
            sc_panel_transparency.set_sensitive(True)
            l_transparent_panel.set_sensitive(True)
            check_panel_opaque.set_sensitive(True)
        else:
            sc_panel_transparency.set_sensitive(False)
            l_transparent_panel.set_sensitive(False)
            check_panel_opaque.set_sensitive(False)
            
     # selective sensitivity in compiz - general
            
    def on_sw_compiz_zoom_active_notify(self,widget,udata=None):
        radio_zoom_type_standard = builder.get_object('radio_zoom_type_standard')
        radio_zoom_type_lg = builder.get_object('radio_zoom_type_lg')
        l_compiz_zoom_type = builder.get_object('l_compiz_zoom_type')
        
        if sw_compiz_zoom.get_active() == True:
            radio_zoom_type_standard.set_sensitive(True)
            radio_zoom_type_lg.set_sensitive(True)
            l_compiz_zoom_type.set_sensitive(True)
        
        else:
            radio_zoom_type_standard.set_sensitive(False)
            radio_zoom_type_lg.set_sensitive(False)                    
            l_compiz_zoom_type.set_sensitive(False)
            
    # selective sensitivity in compiz - windows spread
    
    def on_sw_windows_spread_active_notify(self,widget,udata=None):
        l_compiz_spacing = builder.get_object('l_compiz_spacing')
        l_additional = builder.get_object('l_additional')
        spin_compiz_spacing = builder.get_object('spin_compiz_spacing')
        check_overlay_emblem = builder.get_object('check_overlay_emblem')
        check_click_desktop = builder.get_object('check_click_desktop')
        
        if sw_windows_spread.get_active() == True:
            l_compiz_spacing.set_sensitive(True)
            l_additional.set_sensitive(True)
            spin_compiz_spacing.set_sensitive(True)
            check_overlay_emblem.set_sensitive(True)
            check_click_desktop.set_sensitive(True)
        
        else:
            l_compiz_spacing.set_sensitive(False)
            l_additional.set_sensitive(False)
            spin_compiz_spacing.set_sensitive(False)
            check_overlay_emblem.set_sensitive(False)
            check_click_desktop.set_sensitive(False)        


   # selective sensitivity in desktop settings
                
    def on_sw_desktop_icon_active_notify(self,widget,udata=None):
        check_desktop_home = builder.get_object('check_desktop_home')
        check_desktop_networkserver = builder.get_object('check_desktop_networkserver')
        check_desktop_trash = builder.get_object('check_desktop_trash')
        checK_desktop_devices = builder.get_object('check_desktop_devices')
        
        if sw_desktop_icon.get_active() == True:
            check_desktop_home.set_sensitive(True)
            check_desktop_networkserver.set_sensitive(True)
            check_desktop_trash.set_sensitive(True)
            checK_desktop_devices.set_sensitive(True)
        
        else:
            check_desktop_home.set_sensitive(False)
            check_desktop_networkserver.set_sensitive(False)   
            check_desktop_trash.set_sensitive(False)   
            checK_desktop_devices.set_sensitive(False)   
            
    # gtk search box
    
    # inserting text shows the secondary icon (stock-clear)
    
    def on_tool_entry_search_insert_text(self,text,length,position,udata):
    
        tool_entry_search = builder.get_object('tool_entry_search')
        
        # getting the text length to workaround some Gtk bug
        if tool_entry_search.get_text_length()+1:
            tool_entry_search.set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY,
                Gtk.STOCK_CLEAR)
            
        else:
            tool_entry_search.set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY, None) 

    def on_tool_entry_search_delete_text(self,start_pos,end_pos,udata):
        tool_entry_search = builder.get_object('tool_entry_search')
        
        # getting the text length to workaround some Gtk bug        
        
        if (tool_entry_search.get_text_length()-1) == 0:
            tool_entry_search.set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY, None)
            
    # clicking on secondary icon clearing text
     
    def on_tool_entry_search_icon_press(self, widget, icon, mouse_button):
       
        tool_entry_search = builder.get_object('tool_entry_search')
        
        if icon == Gtk.EntryIconPosition.SECONDARY:
            tool_entry_search.set_text("")
            tool_entry_search.set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY, None)
            
# Basic builder setting up
        
builder = Gtk.Builder()
builder.add_from_file("mechanig.glade")
builder.connect_signals(Handler())


# setting up switches that sensitivize things

sw_launcher_hidemode = builder.get_object('sw_launcher_hidemode')
sw_launcher_transparent = builder.get_object('sw_launcher_transparent')
radio_launcher_color_cus = builder.get_object('radio_launcher_color_cus')
sw_dash_blur = builder.get_object('sw_dash_blur')
radio_dash_color_cus = builder.get_object('radio_dash_color_cus')
sw_appmenu_autohide = builder.get_object('sw_appmenu_autohide')
sw_transparent_panel = builder.get_object('sw_transparent_panel')
sw_compiz_zoom = builder.get_object('sw_compiz_zoom')
sw_windows_spread = builder.get_object('sw_windows_spread')
sw_desktop_icon = builder.get_object('sw_desktop_icon')

# hide tabs of the notebook

builder.get_object('nb_mechanig').set_show_tabs(False)


# The main Mechanig window that needs to be shown
mechanig_main = builder.get_object('mechanig_main')

# Prevent resizing of the window
mechanig_main.set_resizable(False)

# This signal is emitted when you close the window,
# which triggers Gtk.main_quit, which tells the main Gtk loop to quit
mechanig_main.connect("delete-event", Gtk.main_quit)

# This is required, otherwise Gtk leaves the window hidden.
# Useful, like with our dummy "windows" that get reparented
mechanig_main.show_all()

# Runs the main loop
Gtk.main()
