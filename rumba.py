#this code should make the robot bounce off walls and turn, like a rumba

#!/usr/bin/env python3
# So program can be run from Brickman

from ev3dev.ev3 import *
from time import sleep   #sleep(1)
m = LargeMotor('outB')
m2 = LargeMotor('outC')

while True:
  ts = TouchSensor('in1')
  ts2 = TouchSensor('in2')
  #run both
  m.run_forever(speed_sp=900)
  m2.run_forever(speed_sp=900)
  #if right touched:
  if ts.value() ==1:
    #while touched
    while ts.value() ==1:
      #run left both back left faster
      m.run_forever(speed_sp=-950)
      m2.run_forever(speed_sp=-300)
      sleep(1)

    #if left touched:
    elif ts2.value() ==1:
      while ts2.value() ==1:
        #run both back right faster
        m.run_forever(speed_sp=-300)
        m2.run_forever(speed_sp=-950)
        sleep(1)

    #elif both touched:
    elif ts2.value() ==1 and ts.value() ==1:
      while ts2.value() ==1 and ts.value() ==1:
        #run both back left faster
        m.run_forever(speed_sp=-950)
        m2.run_forever(speed_sp=-300)
        sleep(1)
