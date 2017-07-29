#! /usr/bin/env python
# coding: utf-8

import sys
import re

from commands import getoutput
from os import system

fg_col = 'Orange'
bg_col = '#1A1A1A'

group_list = getoutput('ratpoison -c groups').split('\n')

filst_group_num = re.search(r'^\d+', group_list[0])
system('ratpoison -c "gselect {}"'.format(filst_group_num.group()))

# スクリプト引数によって、gmergeからgmove挙動を変更する
action_type = 'gmerge'
if 'gmove' in sys.argv:
    action_type = sys.argv[1]

ratmenu_cmd = ['ratmenu']
ratmenu_cmd.append('-fg "{}"'.format(fg_col))
ratmenu_cmd.append('-bg "{}"'.format(bg_col))
ratmenu_cmd.append('-align "left"')
ratmenu_cmd.append('-style dreary')
ratmenu_cmd.append('-label "group Action"')
ratmenu_cmd.append('"=== {} ===" ""'.format(action_type))

for group in group_list:
    # groupリスト作成
    num = re.search(r'^\d+', group)
    ratmenu_cmd.append('"{}" \'ratpoison -c "{} {}"\''.format(group, action_type, num.group()))

    # groupに紐づいてるwindowリスト作成
    windows_list = getoutput('ratpoison -c windows | sed -e "s/^/   /"').split('\n')
    for w in windows_list:
        ratmenu_cmd.append('"{}" ""'.format(w))
    system('ratpoison -c gnext')

# グループを元に戻す
current_group_num_list = [re.search(r'^\d+', g) for g in group_list if re.search(r'^[0-9]*\*', g)]
system('ratpoison -c "gselect {}"'.format(current_group_num_list[0].group()))

# ratmenuの作成
system(' '.join(ratmenu_cmd))
