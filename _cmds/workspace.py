#! /usr/bin/env python
# coding: utf-8

from commands import getoutput
from os import system

curgroup = getoutput('ratpoison -c "groups" | grep "*" | awk -F* \'{print $1}\'')
system('echo "`expr {} + 1`"'.format(curgroup))
