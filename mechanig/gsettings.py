#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gio,  Gdk

def plugin(plugin):
    schema = 'org.compiz.'+plugin
    path = '/org/compiz/profiles/unity/plugins/'+plugin+'/'
    return Gio.Settings(schema = schema,  path = path)

def unity(child = None):
    schema = 'com.canonical.Unity'
    schema = schema+'.'+child if child else schema
    return Gio.Settings(schema)

def canonical(child):
    schema = 'com.canonical.'+child
    return Gio.Settings(schema)

def compiz(child):
    schema = 'org.compiz.'+child
    return Gio.Settings(schema)

def gnome(child):
    schema = 'org.gnome.'+child
    return Gio.Settings(schema)

def color_to_hash(c):
    """Convert a Gdk.Color or Gdk.RGBA object to hex representation"""
    if isinstance(c, Gdk.Color):
        return "#{:02x}{:02x}{:02x}ff".format(*map(lambda x: round(x*255), [c.red_float, c.green_float, c.blue_float]))
    if isinstance(x, Gdk.RGBA):
        return "#{:02x}{:02x}{:02x}{:02x}".format(*map(lambda x: round(x*255), [c.red, c.green, c.blue, c.alpha]))
    # If it is neither a Gdk.Color object nor a Gdk.RGBA objcect, 
    raise NotImplementedError

# GSettings objects go here

unityshell = plugin('unityshell')
desktop = gnome('nautilus.desktop')
background = gnome('desktop.background')
launcher = unity('Launcher')
power = canonical('indicator.power')
session = canonical('indicator.session')
datetime = canonical('indicator.datetime')
font = gnome('desktop.interface')
titlefont = gnome('desktop.wm.preferences')
antialiasing = gnome('settings-daemon.plugins.xsettings')
opengl = plugin('opengl')
core = plugin('core')
scale = plugin('scale')
expo = plugin('expo')
move = plugin('move')
zoom = plugin('ezoom')
grid = plugin('grid')
