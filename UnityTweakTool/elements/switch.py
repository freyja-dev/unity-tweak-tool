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

''' Definitions for Switch element. '''
from UnityTweakTool.backends import gsettings

import logging
logger=logging.getLogger('UnityTweakTool.elements.switch')

class Switch:
    def __init__(self,controlObj):
        ''' Initialise a switch from a controlObj dictionary '''
        self.id         = controlObj['id']
        self.builder    = controlObj['builder']
        self.ui         = controlObj['builder'].get_object(controlObj['id'])
        self.schema     = controlObj['schema']
        self.path       = controlObj['path']
        self.key        = controlObj['key']
        self.type       = controlObj['type']
        self.map        = controlObj['map']
        self.invmap     = dict([ (v,k) for (k,v) in self.map.items() ])
        self.dependants = controlObj['dependants']
        self.disabled   = False
        try:
            assert gsettings.is_valid(
                schema=self.schema,
                path=self.path,
                key=self.key
                )
        except AssertionError as e:
            self.disabled = True
        logger.debug('Initialised a switch with id {self.id} to control key {self.key} of type {self.type} in schema {self.schema} with path {self.path}'.format(self=self))

    def register(self,handler):
        ''' Register handler on a handler object '''
        handler['on_%s_active_notify'% self.id]=self.handler
        logger.debug('Handler for {self.id} registered'.format(self=self))

    def refresh(self):
        ''' Refresh the UI querying the backend '''
        logger.debug('Refreshing UI display for {self.id}'.format(self=self))
        if self.disabled:
            self.ui.set_sensitive(False)
            return
        self.active=self.map[
                gsettings.get(
                    schema=self.schema,
                    path  =self.path,
                    key   =self.key,
                    type  =self.type
                    )
                ]
        self.ui.set_active(self.active)
        self.handledependants()

    def handler(self,*args,**kwargs):
        ''' Handle notify::active signals '''
        if self.disabled:
            return
        self.active=self.ui.get_active()
        gsettings.set(
            schema=self.schema,
            path=self.path,
            key=self.key,
            type=self.type,
            value=self.invmap[self.active]
            )
        self.handledependants()
        logger.info('Handler for {self.id} executed'.format(self=self))

    def reset(self):
        ''' Reset the controlled key '''
        if self.disabled:
            return
        gsettings.reset(schema=self.schema,path=self.path,key=self.key)
        logger.debug('Key {self.key} in schema {self.schema} and path {self.path} reset.'.format(self=self))

    def handledependants(self):
        status = False if self.disabled else self.active
        for element in self.dependants:
            self.builder.get_object(element).set_sensitive(status)
