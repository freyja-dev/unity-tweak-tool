#! /usr/bin/python

import compizconfig
from gi.repository import Gdk

screen= Gdk.Screen.get_default()
n = screen.get_number()
context = compizconfig.Context(n)
print context.CurrentProfile.Name
