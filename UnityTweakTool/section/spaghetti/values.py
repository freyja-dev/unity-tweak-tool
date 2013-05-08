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

from . import gsettings
from UnityTweakTool.config.ui import ui

class values():

    def get_value(self, type, schema, key, key_list):
        if schema is not None:
            if gsettings.test_key(schema, key):
                attr = 'get_' + type
                return getattr(schema, attr)(key)
            else:
                print('%s key not present.' % key)
                self.ui.tooltip(key_list)
        else:
            print('%s schema not present.' % schema)

    def set_value(self, type, schema, key, setting):
        if schema is not None:
            if gsettings.test_key(schema, key):
                attr = 'set_' + type
                return getattr(schema, attr)(key, setting)
            else:
                print('%s key not present.' % key)
        else:
            print('%s schema not present.' % schema)

    def reset_value(self, schema, key):
        if schema is not None:
            if gsettings.test_key(schema, key):
                return schema.reset(key)
            else:
                print('%s key not present.' % key)
        else:
            print('%s schema not present.' % schema)
