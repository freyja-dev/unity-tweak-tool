#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio

builder = Gtk.Builder()

builder.add_from_file("desktop.ui")

desktop = builder.get_object("desktop_window")

desktop.connect("delete-event", Gtk.main_quit)
desktop.show_all()

Gtk.main()
