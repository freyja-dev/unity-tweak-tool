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

'''This file contains the bindings to Gio.Settings'''
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


def is_valid(*,schema,path=None,key=None):
    '''
    Check if the given schema,path,key,type combination is valid. All arguments are keyword-only. path is used to instantiate Gio.Settings only if schema is relocatable. Relocatable schemas are expected to be accompanied by path.
    '''
    logger.debug('Checking if schema %s with path %s has key %s',schema,path,key)
    if schema in all_schemas:
        logger.debug('Ignoring path for static schema')
        if key is not None:
            try:
                _gs=GSettings[schema]
            except KeyError as e:
                _gs=Gio.Settings(schema)
            return key in _gs.list_keys()
        else:
            return True
    if schema in all_relocatable_schemas:
        if key is not None:
            assert path is not None, 'Relocatable schemas must be accompanied with path'
            try:
                _gs=GSettings[schema]
            except KeyError as e:
                _gs=Gio.Settings(schema,path)
            return key in _gs.list_keys()
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
    '''
    Getter that calls appropriate function on Gio.Settings depending on type. The schema,path,key,type combination is expected to be valid. Uses cache wherever possible.
    '''
    logger.debug('Attempting to get key %s of type %s from schema %s with path %s',key,type,schema,path)
    _gskey=schema+(':'+path if path is not None else '')
    try:
        _gs=GSettings[_gskey]
        logger.debug('Using cached Settings object for %s',_gskey)
    except KeyError as e:
        logger.debug('Cache miss for Settings object %s',_gskey)
        _gs=Gio.Settings(schema,path)
        GSettings[_gskey]=_gs
    return _gs.__getattribute__('get_'+type)(key)

def set(*,schema,key,type,path=None,value):
    '''
    Setter that calls appropriate function on Gio.Settings depending on the type. The schema,path,key,type combination is expected to be valid, and the value must be of the proper type. Uses cache wherever possible.
    '''
    logger.debug('Attempting to set key %s of type %s from schema %s with path %s to value %s',key,type,schema,path,value)
    _gskey=schema+(':'+path if path is not None else '')
    try:
        _gs=GSettings[_gskey]
        logger.debug('Using cached Settings object for %s',_gskey)
    except KeyError as e:
        logger.debug('Cache miss for Settings object %s',_gskey)
        _gs=Gio.Settings(schema,path)
        GSettings[_gskey]=_gs
# TODO : check if value is legal, if possible.
    return _gs.__getattribute__('set_'+type)(key,value)

def reset(*,schema,key,path=None):
    ''' Reset the given key. schema,path,key combination is expected to be valid. '''
    logger.debug('Attempting to reset key %s from schema %s with path %s',key,schema,path)
    _gskey=schema+(':'+path if path is not None else '')
    try:
        _gs=GSettings[_gskey]
        logger.debug('Using cached Settings object for %s',_gskey)
    except KeyError as e:
        logger.debug('Cache miss for Settings object %s',_gskey)
        _gs=Gio.Settings(schema,path)
        GSettings[_gskey]=_gs
    _gs.reset(key)

