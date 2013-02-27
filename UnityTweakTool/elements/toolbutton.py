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

import logging
logger=logging.getLogger('UnityTweakTool.elements.toolbutton')

class OverviewToolButton:
    def __init__(self,section,page,id,notebook):
        self.section=section
        self.id=id
        self.page=page
        self.notebook=notebook
        logger.debug('Initialised a toolbutton with id {self.id} in section {self.section} and page {self.page}'.format(self=self))

    def handler(self,*args,**kwargs):
        self.notebook.set_current_page(self.section)
        self.notebook.get_nth_page(self.section).set_current_page(self.page)
        logger.info('Handler for {self.id} executed'.format(self=self))

    def register(self,handler):
        handler['on_%s_clicked'%self.id]=self.handler
        logger.debug('Handler for {self.id} registered'.format(self=self))
