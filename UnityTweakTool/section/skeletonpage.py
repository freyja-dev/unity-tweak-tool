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
import UnityTweakTool.config.data as data
from UnityTweakTool.elements.resetbutton import ResetButton
from gi.repository import Gtk, Gio

class Section ():
    def __init__(self, ui,id):
        self.builder = Gtk.Builder()
        self.builder.set_translation_domain('unity-tweak-tool')
        self.ui = os.path.join(data.get_data_path(),ui)
        self.builder.add_from_file(self.ui)
        self.page = self.builder.get_object(id)
        self.page.unparent()
        self.handler={}
    def add_page(self,page):
        page.register_tab(self.handler)
        page.refresh()
    def register(self):
        self.builder.connect_signals(self.handler)

class Tab():
    def __init__(self,elements):
        self.registered=False
        self.elements=elements

    def register_tab(self,handler):
        assert self.registered is False
        for element in self.elements:
            element.register(handler)
        self.registered=True
    def enable_restore(self,id):
        self.elements.append(ResetButton({'id':id,'tab':self}))
    def reset(self):
        for element in self.elements:
            element.reset()
    def refresh(self):
        for element in self.elements:
            element.refresh()
