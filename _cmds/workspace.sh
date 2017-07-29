#!/bin/sh

RATPOISON='/usr/bin/ratpoison'
CURGROUP=${RATPOISON} -c 'groups' | grep '*' | awk -F\* '{print $1}'
echo "`expr $CURGROUP + 1`"
