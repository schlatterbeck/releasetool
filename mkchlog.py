#!/usr/bin/env python3

import sys
import re

state = 'start'
for line in sys.stdin :
    line = line.rstrip ()
    if line == 'Changes' :
        state = 'changelog'
    if line.startswith ('Version') and state == 'changelog' :
        state = 'start_notes'
        if sys.argv [1] == 'sf-release-focus' :
            rf = line.split (':') [1].strip ()
            print (rf)
        continue
    if not line :
        if state == 'notes' :
            state = 'start_changes'
            continue
        elif state == 'changes' :
            break
    if line and state.startswith ('start_') :
        state = state [6:]
    if sys.argv [1] == state :
        print (line)
