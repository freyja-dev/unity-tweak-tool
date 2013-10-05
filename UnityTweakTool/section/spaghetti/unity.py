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

from gi.repository import Gtk, Gdk

from UnityTweakTool.config.ui import ui
from . import unitytweakconfig
from . import gsettings
from .values import values

class Unitysettings ():
    def __init__(self, builder):
        self.ui = ui(builder)


        if Gdk.Screen.get_default().get_n_monitors() == 1:
            dependants = ['l_launcher_visibility',
                          'radio_launcher_visibility_all',
                          'radio_launcher_visibility_primary',
                          'l_notifications',
                          'radio_active_monitor',
                          'radio_all_monitors']
            self.ui.unsensitize(dependants)

#=====================================================================#
#                                Helpers                              #
#=====================================================================#
    def refresh(self):
        '''Reads the current config and refreshes the displayed values'''
        # Colour
        color = gsettings.unityshell.get_string('background-color')
        if color.endswith('00'):
            self.ui['radio_launcher_color_cham'].set_active(True)
            self.ui.unsensitize(['color_launcher_color_cus'])
        else:
            self.ui['radio_launcher_color_cus'].set_active(True)
            self.ui.sensitize(['color_launcher_color_cus'])
        valid, gdkcolor = Gdk.Color.parse(color[:-2])
        if valid:
            self.ui['color_launcher_color_cus'].set_color(gdkcolor)
        del color, valid, gdkcolor

        # Show Desktop
        self.ui['sw_show_desktop'].set_active(True if 'unity://desktop-icon' in gsettings.launcher.get_strv('favorites') else False)

        # ====== Dash Helpers ===== #
        # Run Command History
        dependants = ['b_clear_run_history']
        if gsettings.runner.get_strv('history') == '[]':
            self.ui.unsensitize(dependants)
            self.ui['b_clear_run_history'].set_active(False)
        else:
            self.ui.sensitize(dependants)
        del dependants


        # ====== Panel Helpers ====== #
         # Default Player
        interested_players = gsettings.sound.get_strv('interested-media-players')
        preferred_players = gsettings.sound.get_strv('preferred-media-players')

        for player in interested_players:
            self.ui['cbox_default_player'].append_text(player.capitalize())
# Sanity check for LP:1219318. Ideally we need checkboxes to cover all cases.
            if len(preferred_players)>0:
                if preferred_players[0] in interested_players:
                    self.ui['cbox_default_player'].set_active(interested_players.index(preferred_players[0]))

        # ====== Unity Switcher helpers ====== #
        # Window Switcher accelerators
        model = self.ui['list_unity_switcher_windows_accelerators']

        alt_tab_forward = gsettings.unityshell.get_string('alt-tab-forward')
        iter_alt_tab_forward = model.get_iter_first()
        model.set_value(iter_alt_tab_forward, 1, alt_tab_forward)

        alt_tab_prev = gsettings.unityshell.get_string('alt-tab-prev')
        iter_alt_tab_prev = model.iter_next(iter_alt_tab_forward)
        model.set_value(iter_alt_tab_prev, 1, alt_tab_prev)

        alt_tab_forward_all = gsettings.unityshell.get_string('alt-tab-forward-all')
        iter_alt_tab_forward_all = model.iter_next(iter_alt_tab_prev)
        model.set_value(iter_alt_tab_forward_all, 1, alt_tab_forward_all)

        alt_tab_prev_all = gsettings.unityshell.get_string('alt-tab-prev-all')
        iter_alt_tab_prev_all = model.iter_next(iter_alt_tab_forward_all)
        model.set_value(iter_alt_tab_prev_all, 1, alt_tab_prev_all)

        alt_tab_next_window = gsettings.unityshell.get_string('alt-tab-next-window')
        iter_alt_tab_next_window = model.iter_next(iter_alt_tab_prev_all)
        model.set_value(iter_alt_tab_next_window, 1, alt_tab_next_window)

        alt_tab_prev_window = gsettings.unityshell.get_string('alt-tab-prev-window')

        iter_alt_tab_prev_window = model.iter_next(iter_alt_tab_next_window)
        model.set_value(iter_alt_tab_prev_window, 1, alt_tab_prev_window)

        del model

        # Launcher switcher accelerators
        model = self.ui['list_unity_switcher_launcher_accelerators']

        launcher_switcher_forward = gsettings.unityshell.get_string('launcher-switcher-forward')
        iter_launcher_switcher_forward = model.get_iter_first()
        model.set_value(iter_launcher_switcher_forward, 1, launcher_switcher_forward)

        launcher_switcher_prev = gsettings.unityshell.get_string('launcher-switcher-prev')
        iter_launcher_switcher_prev = model.iter_next(iter_launcher_switcher_forward)
        model.set_value(iter_launcher_switcher_prev, 1, launcher_switcher_prev)

        del model, launcher_switcher_forward, iter_launcher_switcher_forward, launcher_switcher_prev, iter_launcher_switcher_prev


        # ====== Unity Webapps helpers ===== #
        # Preauthorized domains
        self.ui['check_preauthorized_amazon'].set_active(True if 'amazon.ca' in gsettings.webapps.get_strv('preauthorized-domains') else False)
        self.ui['check_preauthorized_ubuntuone'].set_active(True if 'one.ubuntu.com' in gsettings.webapps.get_strv('preauthorized-domains') else False)

        # ====== Unity additional helpers ======= #
        model = self.ui['list_unity_additional_accelerators']

        show_hud = gsettings.unityshell.get_string('show-hud')
        iter_show_hud = model.get_iter_first()
        model.set_value(iter_show_hud, 1, show_hud)

        show_launcher = gsettings.unityshell.get_string('show-launcher')
        iter_show_launcher = model.iter_next(iter_show_hud)
        model.set_value(iter_show_launcher, 1, show_launcher)

        execute_command = gsettings.unityshell.get_string('execute-command')
        iter_execute_command = model.iter_next(iter_show_launcher)
        model.set_value(iter_execute_command, 1, execute_command)

        keyboard_focus = gsettings.unityshell.get_string('keyboard-focus')
        iter_keyboard_focus = model.iter_next(iter_execute_command)
        model.set_value(iter_keyboard_focus, 1, keyboard_focus)

        panel_first_menu = gsettings.unityshell.get_string('panel-first-menu')
        iter_panel_first_menu = model.iter_next(iter_keyboard_focus)
        model.set_value(iter_panel_first_menu, 1, panel_first_menu)

        del model, show_hud, iter_show_hud, show_launcher, iter_show_launcher, execute_command, iter_execute_command, keyboard_focus, iter_keyboard_focus, panel_first_menu, iter_panel_first_menu


# ===== BEGIN: Unity settings =====
# ----- BEGIN: Launcher -----
    def on_radio_launcher_color_cus_toggled(self, widget, udata = None):
        dependants = ['color_launcher_color_cus']
        color = self.ui['color_launcher_color_cus'].get_color()
        colorhash = gsettings.color_to_hash(color)
        if self.ui['radio_launcher_color_cus'].get_active():
            self.ui.sensitize(dependants)
            gsettings.unityshell.set_string('background-color', colorhash)
        else:
            self.ui.unsensitize(dependants)
            gsettings.unityshell.set_string('background-color', colorhash[:-2]+'00')


    def on_sw_show_desktop_active_notify(self, widget, udata = None):
        fav = gsettings.launcher.get_strv('favorites')
        desktop = 'unity://desktop-icon'
        if self.ui['sw_show_desktop'].get_active():
            if desktop not in fav:
                fav.append(desktop)
                gsettings.launcher.set_strv('favorites', fav)
        else:
            if desktop in fav:
                fav.remove(desktop)
                gsettings.launcher.set_strv('favorites', fav)
        del desktop

    def on_b_unity_launcher_reset_clicked(self, widget):
        gsettings.unityshell.reset('background-color')
        gsettings.unityshell.reset('panel-opacity')

        # Launcher items
        fav = gsettings.launcher.get_strv('favorites')
        desktop = 'unity://desktop-icon'
        if desktop in fav:
            fav.remove(desktop)
            gsettings.launcher.set_strv('favorites', fav)
        del desktop
        del fav

        self.refresh()

# ----- END: Launcher -----

# ----- BEGIN: Dash -----
    def on_b_clear_run_history_clicked(self, widget):
        gsettings.runner.reset('history')
#----- END: Dash -------

#----- BEGIN: Panel -----
    def on_cbox_default_player_changed(self, widget, udata = None):
        combobox_text = self.ui['cbox_default_player'].get_active_text()
        gsettings.sound.set_strv('preferred-media-players', [combobox_text.lower()])

    def on_b_unity_panel_reset_clicked(self, widget):
        gsettings.sound.reset('preferred-media-players')

        self.refresh()

#----- END: Panel -----

#----- BEGIN: Switcher -----
    # keyboard widgets in unity-windows-switcher

    def on_craccel_unity_switcher_windows_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_unity_switcher_windows_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        # Python has no switch statement, right?

        if path == '0':
            gsettings.unityshell.set_string('alt-tab-forward', accel)
        elif path == '1':
            gsettings.unityshell.set_string('alt-tab-prev', accel)
        elif path == '2':
            gsettings.unityshell.set_string('alt-tab-forward-all', accel)
        elif path == '3':
            gsettings.unityshell.set_string('alt-tab-prev-all', accel)
        elif path == '4':
            gsettings.unityshell.set_string('alt-tab-next-window', accel)
        elif path == '5':
            gsettings.unityshell.set_string('alt-tab-prev-window', accel)

    def on_craccel_unity_switcher_windows_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_unity_switcher_windows_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, 'Disabled')
        if path == '0':
            gsettings.unityshell.set_string('alt-tab-forward', 'Disabled')
        elif path == '1':
            gsettings.unityshell.set_string('alt-tab-prev', 'Disabled')
        elif path == '2':
            gsettings.unityshell.set_string('alt-tab-forward-all', 'Disabled')
        elif path == '3':
            gsettings.unityshell.set_string('alt-tab-prev-all', 'Disabled')
        elif path == '4':
            gsettings.unityshell.set_string('alt-tab-next-window', 'Disabled')
        elif path == '5':
            gsettings.unityshell.set_string('alt-tab-prev-window', 'Disabled')

    # keyboard widgets in unity-launcher-switcher

    def on_craccel_unity_switcher_launcher_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        model = self.ui['list_unity_switcher_launcher_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)
        # Python has no switch statement, right?

        if path == '0':
            gsettings.unityshell.set_string('launcher-switcher-forward', accel)
        else:
            gsettings.unityshell.set_string('launcher-switcher-prev', accel)

    def on_craccel_unity_switcher_launcher_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_unity_switcher_launcher_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, 'Disabled')
        if path == '0':
            gsettings.unityshell.set_string('launcher-switcher-forward', 'Disabled')
        else:
            gsettings.unityshell.set_string('launcher-switcher-prev', 'Disabled')

    def on_b_unity_switcher_reset_clicked(self, widget):
        gsettings.unityshell.reset('alt-tab-forward')
        gsettings.unityshell.reset('alt-tab-prev')
        gsettings.unityshell.reset('alt-tab-forward-all')
        gsettings.unityshell.reset('alt-tab-prev-all')
        gsettings.unityshell.reset('alt-tab-next-window')
        gsettings.unityshell.reset('alt-tab-prev-window')
        gsettings.unityshell.reset('launcher-switcher-forward')
        gsettings.unityshell.reset('launcher-switcher-prev')
        self.refresh()

#----- END: Switch -----

#----- BEGIN: Webapps -----
    # Preauthorized domains - Amazon
    def on_check_preauthorized_amazon_toggled(self, widget):
        if self.ui['check_preauthorized_amazon'].get_active() == False:
            preauthorized = gsettings.webapps.get_strv('preauthorized-domains')
            amazonca = 'amazon.ca'
            if amazonca in preauthorized:
                amazonlist = ['amazon.ca', 'amazon.cn', 'amazon.com', 'amazon.co.uk', 'amazon.de', 'amazon.es', 'amazon.fr', 'amazon.it', 'www.amazon.ca', 'www.amazon.cn', 'www.amazon.com', 'www.amazon.co.uk', 'www.amazon.de', 'www.amazon.es', 'www.amazon.fr', 'www.amazon.it']
                for amazon in amazonlist:
                    preauthorized.remove(amazon)
                    gsettings.webapps.set_strv('preauthorized-domains', preauthorized)
            elif amazonca not in preauthorized:
                pass
        else:
            preauthorized = gsettings.webapps.get_strv('preauthorized-domains')
            amazonca = 'amazon.ca'
            if amazonca not in preauthorized:
                amazonlist = ['amazon.ca', 'amazon.cn', 'amazon.com', 'amazon.co.uk', 'amazon.de', 'amazon.es', 'amazon.fr', 'amazon.it', 'www.amazon.ca', 'www.amazon.cn', 'www.amazon.com', 'www.amazon.co.uk', 'www.amazon.de', 'www.amazon.es', 'www.amazon.fr', 'www.amazon.it']
                for amazon in amazonlist:
                    preauthorized.append(amazon)
                    gsettings.webapps.set_strv('preauthorized-domains', preauthorized)
            elif amazonca in preauthorized:
                pass

    # Preauthorized domains - Ubuntu One
    def on_check_preauthorized_ubuntuone_toggled(self, widget):
        if self.ui['check_preauthorized_ubuntuone'].get_active() == False:
            preauthorized = gsettings.webapps.get_strv('preauthorized-domains')
            ubuntuone = 'one.ubuntu.com'
            if ubuntuone in preauthorized:
                preauthorized.remove(ubuntuone)
                gsettings.webapps.set_strv('preauthorized-domains', preauthorized)
            elif ubuntuone not in preauthorized:
                pass
        else:
            preauthorized = gsettings.webapps.get_strv('preauthorized-domains')
            ubuntuone = 'one.ubuntu.com'
            if ubuntuone not in preauthorized:
                preauthorized.append(ubuntuone)
                gsettings.webapps.set_strv('preauthorized-domains', preauthorized)
            elif ubuntuone in preauthorized:
                pass

    # Reset button
    def on_b_unity_webapps_reset_clicked(self, widget):
        gsettings.webapps.reset('preauthorized-domains')
        self.refresh()

#----- END: Webapps -----

#----- BEGIN: Additional -----
    # keyboard widgets in unity-additional

    def on_craccel_unity_additional_accel_edited(self, craccel, path, key, mods, hwcode, model = None):
        # Glade has a habit of swapping arguments. beware.
        model = self.ui['list_unity_additional_accelerators']
        accel = Gtk.accelerator_name(key, mods)
        titer = model.get_iter(path)
        model.set_value(titer, 1, accel)

        # Python has no switch statement, right?

# You are right, jokerdino. Python has no switch statement.
# That is against OOP principles. -jpm

        if path == '0':
            gsettings.unityshell.set_string('show-hud', accel)
        elif path == '1':
            gsettings.unityshell.set_string('show-launcher', accel)
        elif path == '2':
            gsettings.unityshell.set_string('execute-command', accel)
        elif path == '3':
            gsettings.unityshell.set_string('keyboard-focus', accel)
        else:
            gsettings.unityshell.set_string('panel-first-menu', accel)

    def on_craccel_unity_additional_accel_cleared(self, craccel, path, model = None):
        model = self.ui['list_unity_additional_accelerators']
        titer = model.get_iter(path)
        model.set_value(titer, 1, 'Disabled')
        if path == '0':
            gsettings.unityshell.set_string('show-hud', 'Disabled')
        elif path == '1':
            gsettings.unityshell.set_string('show-launcher', 'Disabled')
        elif path == '2':
            gsettings.unityshell.set_string('execute-command', 'Disabled')
        elif path == '3':
            gsettings.unityshell.set_string('keyboard-focus', 'Disabled')
        else:
            gsettings.unityshell.set_string('panel-first-menu', 'Disabled')

    def on_b_unity_additional_reset_clicked(self, widget):
        gsettings.unityshell.reset('shortcut-overlay')
        gsettings.unityshell.reset('show-hud')
        gsettings.unityshell.reset('show-launcher')
        gsettings.unityshell.reset('execute-command')
        gsettings.unityshell.reset('keyboard-focus')
        gsettings.unityshell.reset('panel-first-menu')
        self.refresh()

#----- END: Additional -----

