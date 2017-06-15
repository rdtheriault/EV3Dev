##This program makes a "mouth" chomp when a light object is placed infront of it.

#!/usr/bin/env python3 from ev3dev.ev3 import * from time import sleep m = LargeMotor('outB')
# Connect EV3 color sensor and check connected.
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
m = LargeMotor('outB')
cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode='COL-REFLECT'

chomp = 0

while chomp<3:
        if cl.value()>20:
                chomp = chomp + 1
                for x in range(0, 3):
                        sleep(.25)
                        m.run_to_rel_pos(position_sp=70, speed_sp=200, stop_action="hold")
                        sleep(.25)
                        m.run_to_rel_pos(position_sp=-55, speed_sp=200, stop_action="hold")

# I get max 80 with white paper, 3mm separation 
# and 5 with black plastic, same separation
