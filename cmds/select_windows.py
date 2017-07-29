#! /usr/bin/env python
# coding: utf-8

from commands import getoutput
from os import system

fg_col = 'Orange'
bg_col = '#1A1A1A'

ratmenu_cmd = ['ratmenu']
ratmenu_cmd.append('-fg "{}"'.format(fg_col))
ratmenu_cmd.append('-bg "{}"'.format(bg_col))
ratmenu_cmd.append('-align "left"')
ratmenu_cmd.append('-style dreary')
ratmenu_cmd.append('-label "select windows"')
ratmenu_cmd.append('"=== select windows ===" ""')

windows_list = getoutput('ratpoison -c "windows %s %n %t"').split('\n')
for wdata in [w.split(' ', 2) for w in windows_list]:
    if wdata[0] == '*':
        ratmenu_cmd.append('"{}*{}"'.format(wdata[1], wdata[2]))
    else:
        ratmenu_cmd.append('"{}-{}"'.format(wdata[1], wdata[2]))
    ratmenu_cmd.append('"ratpoison -c \'select {}\'"'.format(wdata[1]))

system(' '.join(ratmenu_cmd))
