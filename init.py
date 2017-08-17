#! /usr/bin/env python
# -*- coding:utf-8 -*-

from os import system

DOTFILES_LIST = ['.xkb', '.conkyrc', '.ratpoisonrc', '.Xresources']

for dotfile in DOTFILES_LIST:
    system('ln -sf ~/.ratpoison-config/{} ~/.'.format(dotfile))
