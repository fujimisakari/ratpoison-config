#! /bin/sh
if [ -s $HOME/.xkb/keymap/mykbd ]; then
  sleep 1
  xkbcomp -I$HOME/.xkb $HOME/.xkb/keymap/mykbd $DISPLAY
fi
