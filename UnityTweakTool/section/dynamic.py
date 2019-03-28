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

from gi.repository import Gio

schema_list = Gio.Settings.list_schemas()

# in Ubuntu >15.04 org.gnome.settings-daemon.peripherals was moved to org.gnome.desktop.peripherals.
# lets check if we're using an older version and fix it if needed
if "org.gnome.desktop.peripherals" not in schema_list:
    touchpad_schema = 'settings-daemon'
else:
    touchpad_schema = 'desktop'


# Desktop feature was removed in nautilus >=3.28. So we use nemo to draw desktop icons.
#See https://bugs.launchpad.net/ubuntu/+source/unity/+bug/1814506
if "org.gnome.nautilus.desktop" not in schema_list:
    desktop_schema = 'org.nemo.desktop'
else:
    desktop_schema = 'org.gnome.nautilus.desktop'
