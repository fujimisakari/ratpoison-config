#!/bin/bash

RATMENU='/usr/bin/ratmenu'
RATPOISON='/usr/bin/ratpoison'
FG='Orange'
BG='#1A1A1A'

(printf "${RATMENU} -fg '${FG}' -bg '${BG}' -align 'left' -style dreary -label 'choice_windows' ";
    ${RATPOISON} -c "windows %s %n %t" | while read x y z; do
        if [ "$x" = "*" ]; then
            printf "'%s*%s' '${RATPOISON} -c \"select %s\"' " "$y" "$z" "$y"
        else
            printf "'%s-%s' '${RATPOISON} -c \"select %s\"' " "$y" "$z" "$y"
        fi
    done;) | sh
