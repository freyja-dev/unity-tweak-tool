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

# This file contains the bindings to Gio.Settings
from gi.repository import Gio
import logging

logger=logging.getLogger('UnityTweakTool.backends.gsettings')

all_schemas             = frozenset(
                            Gio.Settings.list_schemas()
                        )
all_relocatable_schemas = frozenset(
                            Gio.Settings.list_relocatable_schemas()
                        )

GSettings = dict()


def is_valid(*,schema,key=None,path=None):
    if schema in all_schemas:
        if key is not None:
            return key in Gio.Settings(schema).list_keys()
        else:
            return True
    if schema in all_relocatable_schemas:
        if key is not None:
            assert path is not None, 'Relocatable schemas must be accompanied with path'
            return key in Gio.Settings(schema,path).list_keys()
        else:
            return True

# get_<type> and set_<type> are available for the following in Gio.Settings
VALID_TYPES=frozenset([
                'boolean',
                'int',
                'uint',
                'double',
                'string',
                'strv',
                'enum',
                'flags'
            ])

def get(*,schema,key,type,path=None):
    _suffix=':'+path if path is not None else ''
    try:
        _gs=GSettings[schema+_suffix]
    except KeyError as e:
        _gs=Gio.Settings(schema,path)
    return _gs.__getattr__('get_'+type)(key)

def set(*,schema,key,type,path=None,value):
    _suffix=':'+path if path is not None else ''
    try:
        _gs=GSettings[schema+_suffix]
    except KeyError as e:
        _gs=Gio.Settings(schema,path)
# TODO : check if value is legal, if possible.
    return _gs.__setattr__('set_'+type)(key,value)

