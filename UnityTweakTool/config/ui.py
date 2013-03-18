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

class ui():
    def __init__(self, builder):
        self.builder = builder
    def __getitem__(self, obj):
        return self.builder.get_object(obj)
    def sensitize(self, list):
        for item in list:
            self.__getitem__(item).set_sensitive(True)
    def unsensitize(self,list):
        for item in list:
            self.__getitem__(item).set_sensitive(False)
    def tooltip(self, list):
        for item in list:
            tooltip = "Schema / key missing for this widget."
            self.unsensitize(list)
            self.__getitem__(item).set_tooltip_text(tooltip)
            self.__getitem__(item).set_tooltip_markup(tooltip)
