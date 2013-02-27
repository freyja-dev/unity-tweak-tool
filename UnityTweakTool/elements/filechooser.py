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

''' Definitions for FileChooser element. '''
import UnityTweakTool.config.data as data
from gi.repository import Gtk
import os

import logging
logger=logging.getLogger('UnityTweakTool.elements.filechooser')

class FileChooser:
    def __init__(self,controlObj):
        ''' Initialise a FileChooser element from a dictionary'''
        self.builder = Gtk.Builder()
        self.ui = os.path.join(data.get_data_path(),'filechooser-theme.ui')
        self.builder.add_from_file(self.ui)
        self.widget=self.builder.get_object('themeselector')
        self.builder.connect_signals(self)
    def run(self):
        self.widget.run()
    def on_button_cancel_clicked(self,*args,**kwargs):
        logger.info('Theme selection cancelled by user')
        self.widget.destroy()
    def on_button_install_clicked(self,*args,**kwargs):
        logger.debug('Install clicked')
        file=self.widget.get_filename()
        if file is None:
            return
        logger.info('Attempting to install %s'%file)
        logger.warn('Unimplemented logic')
        # TODO : Get file name and do the installation
        self.widget.destroy()

