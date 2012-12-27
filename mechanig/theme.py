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
# This file is a part of Mechanig
#
# Mechanig is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# Mechanig is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>

import os, os.path

from gi.repository import Gtk, Gio

from .ui import ui
from . import settings
from . import gsettings

class Themesettings ():
    def __init__(self, container):
        '''Handler Initialisations.
        Obtain all references here.'''
        self.builder = Gtk.Builder()
        self.glade = (os.path.join(settings.UI_DIR, 
                                    'theme.ui'))
        self.container = container
# TODO : Use os module to resolve to the full path.
        self.builder.add_from_file(self.glade)
        self.ui = ui(self.builder)
        self.page = self.ui['nb_themesettings']
        self.page.unparent()
        self.builder.connect_signals(self)

        self.builder.connect_signals(self)
        self.refresh()

#=====================================================================#
#                                Helpers                              #
#=====================================================================#


    def refresh(self):
        self.ui['font_default'].set_font_name(gsettings.font.get_string('font-name'))
        self.ui['font_document'].set_font_name(gsettings.font.get_string('document-font-name'))
        self.ui['font_monospace'].set_font_name(gsettings.font.get_string('monospace-font-name'))
        self.ui['font_window_title'].set_font_name(gsettings.titlefont.get_string('titlebar-font'))
        
        antialiasing = gsettings.antialiasing.get_string('antialiasing')
        if antialiasing == 'none':
            self.ui['cbox_antialiasing'].set_active(0)
        elif antialiasing == 'grayscale':
            self.ui['cbox_antialiasing'].set_active(1)
        elif antialiasing == 'rgba':
            self.ui['cbox_antialiasing'].set_active(2)
            
        hinting = gsettings.antialiasing.get_string('hinting')
        if hinting == 'none':
            self.ui['cbox_hinting'].set_active(0)
        elif hinting == 'slight':
            self.ui['cbox_hinting'].set_active(1)
        elif hinting == 'medium':
            self.ui['cbox_hinting'].set_active(2)
        elif hinting == 'full':
            self.ui['cbox_hinting'].set_active(3)
        
        self.ui['spin_textscaling'].set_value(gsettings.font.get_double('text-scaling-factor'))
      
# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
# Dont trust glade to pass the objects properly.            |
# Always add required references to init and use them.      |
# That way, mechanig can resist glade stupidity.            |
# Apologies Gnome devs, but Glade is not our favorite.      |
#___________________________________________________________/


#-----BEGIN: Theme settings------


#-----Font settings--------

    def on_font_default_font_set(self, widget):
        gsettings.font.set_string('font-name', self.ui['font_default'].get_font_name())
    
    def on_font_document_font_set(self, widget):
        gsettings.font.set_string('document-font-name', self.ui['font_document'].get_font_name())
    
    def on_font_monospace_font_set(self, widget):
        gsettings.font.set_string('monospace-font-name', self.ui['font_monospace'].get_font_name())
        
    def on_font_window_title_font_set(self, widget):
        gsettings.titlefont.set_string('titlebar-font', self.ui['font_window_title'].get_font_name())
        
    def on_cbox_antialiasing_changed(self, widget):
        mode = self.ui['cbox_antialiasing'].get_active()
        if mode == 0:
            gsettings.antialiasing.set_string('antialiasing', "none")
        elif mode == 1:
            gsettings.antialiasing.set_string('antialiasing', "grayscale")
        elif mode == 2:
            gsettings.antialiasing.set_string('antialiasing', "rgba")

    def on_cbox_hinting_changed(self, widget):
        mode = self.ui['cbox_hinting'].get_active()
        if mode == 0:
            gsettings.antialiasing.set_string('hinting', "none")
        elif mode == 1:
            gsettings.antialiasing.set_string('hinting', "slight")
        elif mode == 2:
            gsettings.antialiasing.set_string('hinting', "medium")
        elif mode == 3:
            gsettings.antialiasing.set_string('hinting', "full")
            
    def on_spin_textscaling_value_changed(self, widget):
        gsettings.font.set_double('text-scaling-factor', self.ui['spin_textscaling'].get_value())

    def on_b_theme_font_reset_clicked(self, widget):
        gsettings.font.reset('font-name')
        gsettings.font.reset('document-font-name')
        gsettings.font.reset('monospace-font-name')
        gsettings.titlefont.reset('titlebar-font')
        gsettings.antialiasing.reset('antialiasing')
        gsettings.antialiasing.reset('hinting')
        gsettings.font.reset('text-scaling-factor')
        self.refresh()
        
if __name__ == '__main__':
# Fire up the Engines
    Themesettings()
