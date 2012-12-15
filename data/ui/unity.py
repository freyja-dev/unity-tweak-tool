#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from gi.repository import Gtk,Gio

builder = Gtk.Builder()

builder.add_from_file("unity.ui")

unity = builder.get_object("unity_window")

unity.connect("delete-event", Gtk.main_quit)
unity.show_all()

Gtk.main()
