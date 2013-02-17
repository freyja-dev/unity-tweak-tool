#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from . import gsettings
from UnityTweakTool.config.ui import ui

class values():

    def get_value(self, type, schema, key, key_list):
        if schema is not None:
            if gsettings.test_key(schema, key):
                attr = 'get_' + type
                return getattr(schema, attr)(key)
            else:
                print('%s key not present.' % key)
                self.ui.tooltip(key_list)
        else:
            print('%s schema not present.' % schema)

    def set_value(self, type, schema, key, setting):
        if schema is not None:
            if gsettings.test_key(schema, key):
                attr = 'set_' + type
                return getattr(schema, attr)(key, setting)
            else:
                print('%s key not present.' % key)
        else:
            print('%s schema not present.' % schema)

    def reset_value(self, schema, key):
        if schema is not None:
            if gsettings.test_key(schema, key):
                return schema.reset(key)
            else:
                print('%s key not present.' % key)
        else:
            print('%s schema not present.' % schema)
