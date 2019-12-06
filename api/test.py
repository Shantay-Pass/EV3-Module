#!/usr/bin/env python3
from controller_ev3 import move, rotate, pause, say

move(50, 300)
rotate(50, 90)
pause(5)
move(50, 300)
say("Test complete")