#! /bin/sh

RATPOISON='/usr/bin/ratpoison'
$RATPOISON -c windows | grep "^[0-9]*\*"
