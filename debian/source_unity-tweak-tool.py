import os
from os import path

import apport
from apport.hookutils import *


def add_info(report):
    if apport.packaging.is_distro_package(report['Package'].split()[0]):
        report['CrashDB'] = '{"impl":"launchpad", "distro" : "ubuntu" }
    else:
        report['CrashDB'] = '{"impl": "launchpad", "project": "unity-tweak-tool"}'
