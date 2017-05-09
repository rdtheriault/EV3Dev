import subprocess
subprocess.call("echo ev3-analog > /sys/class/lego-port/port1/mode", shell=True)
subprocess.call("echo lego-ev3-touch > /sys/class/lego-port/port1/set_device", shell=True)

from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('ttyAMA0:MA')


ts = TouchSensor('ttyAMA0:S2')
assert ts.connected, "Connect TouchSensor"

notTouched = 1

m.run_forever(speed_sp=300)
print(ts.value())
sleep(3)
while notTouched == 1:
 if ts.value() == 1:
  print(ts.value())
  m.stop()
  notTouched = 0
