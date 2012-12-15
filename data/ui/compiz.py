#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio

builder = Gtk.Builder()

builder.add_from_file("compiz.ui")

compiz = builder.get_object("compiz_window")

compiz.connect("delete-event", Gtk.main_quit)
compiz.show_all()

Gtk.main()
