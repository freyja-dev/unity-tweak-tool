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

# List of all subpackages that can be imported using
# from UnityTweakTool import *
__all__=['backends','config','elements']

import logging

logger=logging.getLogger('UnityTweakTool')
logger.setLevel(logging.DEBUG)

# TODO : give a sensible logfile name.
_fh=logging.FileHandler(logfile)
_fh.setLevel(logging.DEBUG)

_formatter=logging.Formatter('%(asctime)s - %(levelname)-8s :: %(name)s - %(funcName)s - %(message)s')

_fh.setFormatter(_formatter)
logger.setHandler(_fh)

del _fh, _formatter
