#! /usr/bin/env python
# coding: utf-8

import sys

from commands import getoutput
from os import system

system('ratpoison -c only')

windows_count = getoutput('ratpoison -c windows | wc -l | sed -e "s/[ ]*//g"')
i = 2
while i <= int(windows_count):
    fc = int(windows_count) / 2
    if i <= fc:
        system('ratpoison -c vsplit')
    else:
        system('ratpoison -c hsplit')
    system('ratpoison -c focus; ratpoison -c focus')
    i += 1

current_windows = getoutput('ratpoison -c windows | grep "^[0-9]*\*" | awk -F* \'{print $1}\'')
system('ratpoison -c "select {}"'.format(current_windows))

if 'fs' in sys.argv:
    system('ratpoison -i -c fselect')
    system('ratpoison -c only')
else:
    system('ratpoison -i -c "windows"')
