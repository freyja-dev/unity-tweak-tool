import os
from os import path

from apport.hookutils import *

def add_info(report):
    report['CrashDB'] = '{"impl": "launchpad", "project": "unity-tweak-tool"}'
