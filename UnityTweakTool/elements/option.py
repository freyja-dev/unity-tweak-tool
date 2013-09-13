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

''' Generic option '''
from UnityTweakTool.backends import gsettings

#import logging
#logger=logging.getLogger('UnityTweakTool.elements.option')

class Option:
    ''' Generic class to be used for those options which
    are not straightforward to port. Will be removed in due time.'''
    def __init__(self,controlObj):
        self.handler=controlObj['handler']
        self.reset  =controlObj['reset']
        self.handlerid=controlObj['handlerid']
        self.refresh=controlObj['refresh']
    def register(self,handler):
        handler[self.handlerid]=self.handler

class HandlerObject:
    def __init__(self,ho):
        self.ho=ho
        def isHandler(attrname,ho=ho,prefix='on',suffix='reset_clicked'):
            return attrname.startswith(prefix) and \
                    not attrname.endswith(suffix) and \
                   callable(getattr(ho, attrname))
        def isResetHandler(attrname,ho=ho,prefix='on',suffix='reset_clicked'):
            return attrname.startswith(prefix) and \
                    attrname.endswith(suffix) and \
                   callable(getattr(ho, attrname))
        handlers = list(filter(isHandler, dir(ho)))
        self.hodict={key:getattr(ho,key) for key in handlers}
        reset_handlers = list(filter(isResetHandler,dir(ho)))
        self.hodict_reset={key:getattr(ho,key) for key in reset_handlers}
        self.register_tab=self.register
    def register(self,handler):
        handler.update(self.hodict)
        for key,val in self.hodict_reset.items():
            if key in handler:
                def reset_fix(*args,ported_reset=handler[key],old_reset=val,**kwargs):
                    old_reset(*args,**kwargs)
                    ported_reset(*args,**kwargs)
                handler[key]=reset_fix
            else:
                handler[key]=val
    def refresh(self):
        self.ho.refresh()
    def reset(self):
        self.ho.reset()
