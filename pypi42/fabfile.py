#!/usr/bin/env python

from fabric.api import *
from fabric.colors import *
from fabric.decorators import *
from fabric.contrib import *
from fabtools import *


def test():
    with settings(host_string='localhost', user='scalp'):
        run('uname')
