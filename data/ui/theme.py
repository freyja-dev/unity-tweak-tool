#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio

builder = Gtk.Builder()

builder.add_from_file("theme.ui")

theme = builder.get_object("theme_window")

theme.connect("delete-event", Gtk.main_quit)
theme.show_all()

Gtk.main()
