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

''' Definitions for ResetButton element. '''
from UnityTweakTool.backends import gsettings

import logging
logger=logging.getLogger('UnityTweakTool.elements.resetbutton')

class ResetButton:
    def __init__(self,controlObj):
        ''' Initialise a ResetButton from a controlObj dictionary '''
        self.id         = controlObj['id']
        self.tab        = controlObj['tab']
        logger.debug('Initialised a ResetButton with id {self.id}'.format(self=self))

    def register(self,handler):
        ''' Register handler on a handler object '''
        handler['on_%s_clicked'% self.id]=self.handler
        logger.debug('Handler for {self.id} registered'.format(self=self))

    def handler(self,*args,**kwargs):
        ''' Handle clicked signals '''
        self.tab.reset()
        self.tab.refresh()
        logger.info('Handler for {self.id} executed'.format(self=self))

# The following are required to allow RB to be considered just like any other element
    def reset(self):
        pass
    def refresh(self):
        pass
