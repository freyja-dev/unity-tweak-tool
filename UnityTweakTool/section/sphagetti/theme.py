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
#   Angel Araya <al.arayaq@gmail.com>
#
# Description:
#   A One-stop configuration tool for Unity.
#
# Legal Stuff:
#
# This file is a part of Unity Tweak Tool
#
# Unity Tweak Tool is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# Unity Tweak Tool is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>

import os, os.path

from gi.repository import Gtk, Gio

from UnityTweakTool.config.ui import ui
from . import unitytweakconfig
from . import gsettings

class Themesettings ():
    def __init__(self, builder):
        self.ui=ui(builder)
        self.gtkthemestore=Gtk.ListStore(str,str)
        self.windowthemestore=self.gtkthemestore
        self.ui['tree_gtk_theme'].set_model(self.gtkthemestore)
        self.ui['tree_window_theme'].set_model(self.windowthemestore)

        # Get all themes
        systhdir='/usr/share/themes'
        systemthemes=[(theme.capitalize(),os.path.join(systhdir,theme)) for theme in os.listdir(systhdir) if os.path.isdir(os.path.join(systhdir,theme))]
        try:
            uthdir=os.path.expanduser('~/.themes')
            userthemes=[(theme.capitalize(),os.path.join(uthdir,theme)) for theme in os.listdir(uthdir) if os.path.isdir(os.path.join(uthdir,theme))]
        except OSError as e:
            userthemes=[]
        allthemes=systemthemes+userthemes
        allthemes.sort()
        required=['gtk-2.0','gtk-3.0','metacity-1']
        self.gtkthemes={}
        self.windowthemes={}
        for theme in allthemes:
            if all([os.path.isdir(os.path.join(theme[1],req)) for req in required]):
                iter=self.gtkthemestore.append(theme)
                themename=os.path.split(theme[1])[1]
                self.gtkthemes[themename]={'iter':iter,'path':theme[1]}
                self.windowthemes[themename]={'iter':iter,'path':theme[1]}

        self.iconthemestore=Gtk.ListStore(str,str)
        self.cursorthemestore=Gtk.ListStore(str,str)
        self.ui['tree_icon_theme'].set_model(self.iconthemestore)
        self.ui['tree_cursor_theme'].set_model(self.cursorthemestore)

        sysithdir='/usr/share/icons'
        systemiconthemes= [(theme.capitalize(),os.path.join(sysithdir,theme)) for theme in os.listdir(sysithdir) if os.path.isdir(os.path.join(sysithdir,theme))]
        to_be_hidden=[('Loginicons','/usr/share/icons/LoginIcons'),('Unity-webapps-applications','/usr/share/icons/unity-webapps-applications')]
        for item in to_be_hidden:
            try:
                systemiconthemes.remove(item)
            except ValueError as e:
                pass
        try:
            uithdir=os.path.expanduser('~/.icons')
            usericonthemes=[(theme.capitalize(),os.path.join(uithdir,theme)) for theme in os.listdir(uithdir) if os.path.isdir(os.path.join(uithdir,theme))]
        except OSError as e:
            usericonthemes=[]
        allithemes=systemiconthemes+usericonthemes
        allithemes.sort()
        self.iconthemes={}
        self.cursorthemes={}
        for theme in allithemes:
            iter=self.iconthemestore.append(theme)
            themename=os.path.split(theme[1])[1]
            self.iconthemes[themename]={'iter':iter,'path':theme[1]}
            if os.path.isdir(os.path.join(theme[1],'cursors')):
                iter=self.cursorthemestore.append(theme)
                self.cursorthemes[themename]={'iter':iter,'path':theme[1]}

        self.matchthemes=True

#=====================================================================#
#                                Helpers                              #
#=====================================================================#


    def refresh(self):

        # System theme
        gtkthemesel=self.ui['tree_gtk_theme'].get_selection()
        gtktheme=gsettings.gnome('desktop.interface').get_string('gtk-theme')

        # FIXME: Workaround to fix LP bug: #1098845
        try:
            gtkthemesel.select_iter(self.gtkthemes[gtktheme]['iter'])

        # TODO: This except part should do something more.
        except KeyError:
            gtkthemesel.unselect_all()

        # Window theme
        windowthemesel=self.ui['tree_window_theme'].get_selection()
        windowtheme=gsettings.gnome('desktop.wm.preferences').get_string('theme')

        # FIXME: Workaround to fix LP bug: #1146122
        try:
            windowthemesel.select_iter(self.windowthemes[windowtheme]['iter'])

        # TODO: This except part should do a lot more.
        except KeyError:
            windowthemesel.unselect_all()    

        # Icon theme
        iconthemesel=self.ui['tree_icon_theme'].get_selection()
        icontheme=gsettings.gnome('desktop.interface').get_string('icon-theme')

        # FIXME: Workaround to fix potential bug
        try:
            iconthemesel.select_iter(self.iconthemes[icontheme]['iter'])

        except KeyError:
            iconthemesel.unselect_all()

        # Cursor theme
        cursorthemesel=self.ui['tree_cursor_theme'].get_selection()
        cursortheme=gsettings.gnome('desktop.interface').get_string('cursor-theme')

        # FIXME: Workaround to fix LP bug: #1097227

        try:
            cursorthemesel.select_iter(self.cursorthemes[cursortheme]['iter'])
        # TODO: except part should make sure the selection is deselected.
        except KeyError:
            cursorthemesel.unselect_all()

        # Cursor size
        self.ui['check_cursor_size'].set_active(True if gsettings.interface.get_int('cursor-size') is 48 else False)

        # ===== Fonts ===== #

        # Fonts
        self.ui['font_default'].set_font_name(gsettings.interface.get_string('font-name'))
        self.ui['font_document'].set_font_name(gsettings.interface.get_string('document-font-name'))
        self.ui['font_monospace'].set_font_name(gsettings.interface.get_string('monospace-font-name'))
        self.ui['font_window_title'].set_font_name(gsettings.wm.get_string('titlebar-font'))

        # Antialiasing
        if gsettings.antialiasing.get_string('antialiasing') == 'none':
            self.ui['cbox_antialiasing'].set_active(0)
        elif gsettings.antialiasing.get_string('antialiasing') == 'grayscale':
            self.ui['cbox_antialiasing'].set_active(1)
        elif gsettings.antialiasing.get_string('antialiasing') == 'rgba':
            self.ui['cbox_antialiasing'].set_active(2)

        # Hinting
        if gsettings.antialiasing.get_string('hinting') == 'none':
            self.ui['cbox_hinting'].set_active(0)
        elif gsettings.antialiasing.get_string('hinting') == 'slight':
            self.ui['cbox_hinting'].set_active(1)
        elif gsettings.antialiasing.get_string('hinting') == 'medium':
            self.ui['cbox_hinting'].set_active(2)
        elif gsettings.antialiasing.get_string('hinting') == 'full':
            self.ui['cbox_hinting'].set_active(3)

        # Scaling
        self.ui['spin_textscaling'].set_value(gsettings.interface.get_double('text-scaling-factor'))

    # ===== Window Controls ===== #

    # Button layout
    def refresh_window_controls(self):

        dependants = ['radio_left',
                    'radio_right']
        if gsettings.wm.get_string('button-layout') == 'close,minimize,maximize:':
            self.ui['radio_left'].set_active(True)
            self.ui['check_show_menu'].set_active(False)
        elif gsettings.wm.get_string('button-layout') == ':minimize,maximize,close':
            self.ui['radio_right'].set_active(True)
            self.ui['check_show_menu'].set_active(False)
        else:
            return
        del dependants

    # Show menu
    def refresh_window_menu_check(self):
        if 'menu' in gsettings.wm.get_string('button-layout'):
            self.ui['check_show_menu'].set_active(True)
        else:
            self.ui['check_show_menu'].set_active(False)

# TODO : Find a clever way or set each one manually.
# Do it the dumb way now. BIIIG refactoring needed later.


#-----BEGIN: Theme settings------

# These check for nonetype and return since for some bizzare reason Gtk.quit destroys
# the selection object and then calls these callbacks. This is a temporary fix to LP:1096964

    # System Theme
    def on_treeselection_gtk_theme_changed(self,udata=None):
        gtktreesel = self.ui['tree_gtk_theme'].get_selection()
        if gtktreesel is None:
            return
        gtkthemestore,iter = gtktreesel.get_selected()
        if self.matchthemes:
            self.ui['treeselection_window_theme'].select_iter(iter)
        themepath=gtkthemestore.get_value(iter,1)
        theme=os.path.split(themepath)[1]
        gsettings.interface.set_string('gtk-theme',theme)

    def on_treeselection_window_theme_changed(self,udata=None):
        windowtreesel = self.ui['tree_window_theme'].get_selection()
        if windowtreesel is None:
            return
        windowthemestore,iter = windowtreesel.get_selected()
        if self.matchthemes:
            self.ui['treeselection_gtk_theme'].select_iter(iter)
        themepath=windowthemestore.get_value(iter,1)
        theme=os.path.split(themepath)[1]
        gsettings.wm.set_string('theme',theme)

    # Icon theme
    def on_tree_icon_theme_cursor_changed(self,udata=None):
        icontreesel = self.ui['tree_icon_theme'].get_selection()
        if icontreesel is None:
            return
        iconthemestore,iter = icontreesel.get_selected()
        themepath=iconthemestore.get_value(iter,1)
        theme=os.path.split(themepath)[1]
        gsettings.interface.set_string('icon-theme',theme)

    def on_check_show_incomplete_toggled(self,udata=None):
    # TODO
        print('To do')

    def on_b_theme_system_reset_clicked(self, widget):
        gsettings.interface.reset('gtk-theme')
        gsettings.wm.reset('theme')
        self.refresh()

#----- End: Theme settings------

#----- Begin: Icon settings--------

    def on_b_theme_icon_reset_clicked(self, widget):
        gsettings.interface.reset('icon-theme')
        self.refresh()

#----- End: Icon settings------

#----- Begin: Cursor settings--------

    # Cursor
    def on_tree_cursor_theme_cursor_changed(self,udata=None):
        cursortreesel= self.ui['tree_cursor_theme'].get_selection()
        if cursortreesel is None:
            return
        cursorthemestore,iter = cursortreesel.get_selected()
        themepath=cursorthemestore.get_value(iter,1)
        theme=os.path.split(themepath)[1]
        gsettings.interface.set_string('cursor-theme',theme)

    # Cursor Size
    def on_check_cursor_size_toggled(self, widget, udata = None):
        if self.ui['check_cursor_size'].get_active() == True :
            gsettings.interface.set_int('cursor-size', 48)
        else:
            gsettings.interface.set_int('cursor-size', 24)

    def on_b_theme_cursor_reset_clicked(self, widget):
        gsettings.interface.reset('cursor-theme')
        gsettings.interface.reset('cursor-size')
        self.refresh()

#----- End: Cursor settings------
#----- Begin: Window control settings--------

    def on_radio_left_toggled(self, button, udata = None):

        if self.ui['radio_left'].get_active() == True:
            if 'menu' in gsettings.wm.get_string('button-layout'):
                value = 'close,minimize,maximize:' + 'menu'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value
            else:
                value = 'close,minimize,maximize:'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value
        else:
            if 'menu' in gsettings.wm.get_string('button-layout'):
                value = 'menu' + ':minimize,maximize,close'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value
            else:
                value = ':minimize,maximize,close'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value

    def on_radio_right_toggled(self, button, udata = None):

        if self.ui['radio_right'].get_active() == True:
            if 'menu' in gsettings.wm.get_string('button-layout'):
                value = 'menu' + ':minimize,maximize,close'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value

            else:
                value = ':minimize,maximize,close'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value
        else:
            if 'menu' in gsettings.wm.get_string('button-layout'):
                value = 'close,minimize,maximize:' + 'menu'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value
            else:
                value = 'close,minimize,maximize:'
                gsettings.wm.set_string('button-layout', value)
                self.refresh_window_menu_check()
                del value

    def on_check_show_menu_toggled(self, button, udata = None):

        if gsettings.wm.get_string('button-layout').endswith(':'):
            value = gsettings.wm.get_string('button-layout') + 'menu'
            gsettings.wm.set_string('button-layout', value)
            del value
        elif gsettings.wm.get_string('button-layout').startswith(':'):
            value = 'menu' + gsettings.wm.get_string('button-layout')
            gsettings.wm.set_string('button-layout', value)
            del value
        else:
            if 'menu' in gsettings.wm.get_string('button-layout'):
                value = str(gsettings.wm.get_string('button-layout')).replace('menu', '')
                gsettings.wm.set_string('button-layout', value)
            else:
                return

    def on_b_theme_window_controls_reset_clicked(self, widget):
        self.ui['check_show_menu'].set_active(False)
        gsettings.wm.set_string('button-layout', 'close,minimize,maximize:')
        self.refresh_window_menu_check()
        self.refresh_window_controls()

#----- End: Window control settings--------
