#This program has the EV3 listen for a button push then let you know if you have the right size coin
#You will probably need to run GetRotation.py script to get the "size" of the coin, but uncommenting the print() in this should work as well
#You can find the robot build on https://www.khanacademy.org/science/electrical-engineering/lego-robotics/lego-coin-detector/v/lego-nxt-coin-detector
#Final note, you will need to start everything up with the "leg" of the detector in the same position everytime. 
#The rotation sets itself to zero when the system starts up so make sure to get the "size" reading from the same point

#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

mC = LargeMotor('outC')
num=mC.position
btn = Button()

while True:
  # Checks if any button is pressed.
  if btn.any():
    num=mC.position
    if num == 100:                                                    #100 should be replaced with rotation for given coin
      Sound.speak('This is the coin you are looking for').wait()
      #print(num)
    else:
      Sound.speak('This is not the coin you are looking for').wait()
      #print(num)
  else:
    # Check for button press every 0.01 second
    sleep(0.01)
    
    
#you could also add elif num == 150: yada yada for different coin sizes and then change the wording to "this is a nickel" "this is a penny"
