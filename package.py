# -*- coding: utf-8 -*-

name = u'gaa_to_delete'

version = '1.0.0'

description = u''

authors = [u'Gabriel AKPO-ALLAVO']

tools = []

requires = []

build_requires = ['python-2']

def commands():
    global env
    env.PATH.append('{this.root}/python')

def pre_commands():
    pass

def post_commands():
    pass

help = []

timestamp = 1699054017

format_version = 2

build_command = "python {root}/build.py {install}"

_data = {}
