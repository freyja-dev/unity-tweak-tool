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
import UnityTweakTool.config.data as data
from gi.repository import Gtk, Gio

class SkeletonPage ():
    def __init__(self, ui,id):
        self.builder = Gtk.Builder()
        self.ui = os.path.join(data.get_data_path(),ui)
        self.builder.add_from_file(self.ui)
        self.page = self.builder.get_object(id)
        self.page.unparent()
        self.registered=False
        self.elements=set()

    def register(self):
        assert self.registered is False
        handler={}
        for element in self.elements:
            element.register(handler)
        self.builder.connect_signals(handler)
        self.registered=True

    def reset(self):
        for element in self.elements:
            element.reset()
