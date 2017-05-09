import subprocess
subprocess.call("echo ev3-analog > /sys/class/lego-port/port0/mode", shell=True)
subprocess.call("echo lego-nxt-touch > /sys/class/lego-port/port0/set_device", shell=True)

from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('ttyAMA0:MA')


ts = TouchSensor('ttyAMA0:S1')
assert ts.connected, "Connect TouchSensor"

notTouched = 1

while notTouched == 1:

        m.run_forever(speed_sp=300)
        if ts.value() == 1:
                m.stop()
                notTouched == 0
