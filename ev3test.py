from ev3dev.ev3 import *
from time import sleep

#connect to motor C
mC = LargeMotor('outC')
#connect to touch sensor 1
ts = TouchSensor('in1')

#get rotation of motor and print
numbers=mC.position
print(numbers)


#start motar for bit
mC.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")


#play sound
Sound.speak('Hello, my name is skynet and I have come to take over the world!')$


#test button
touched = ts.value()
print(touched)
