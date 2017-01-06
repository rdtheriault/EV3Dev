#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

mC = LargeMotor('outC')
numbers=mC.position

while True:
        numbers=mC.position
        print(numbers)
        sleep(1)
