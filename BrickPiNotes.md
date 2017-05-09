#Notes on using a BrickPi vs EV3

##Main Source
Here is the offical side by side info http://www.ev3dev.org/docs/platform-comparison/

--Sensor Issues

https://github.com/ev3dev/ev3dev/issues/374

https://github.com/ev3dev/ev3dev/issues/529

http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/brickpi.html#input-ports


##Start up using screen
Mine hangs up at UTMP, you can use ALT F2 to get to tty2 and still run the programs (so far I can only use the screen)

I was informed you can run the following commands to get to tty1

```
sudo systemctl stop brickman.service
sudo systemctl disable brickman.service
```

Also found I needed to 

```
sudo nano /boot/flash/config.txt
```

and uncomment out the brickpi settings, did three not sure if all are needed at this point

##Outputs and Inputs
Have to define them first
```
OUTPUT_A = 'ttyAMA0:MA'
OUTPUT_B = 'ttyAMA0:MB'
OUTPUT_C = 'ttyAMA0:MC'
OUTPUT_D = 'ttyAMA0:MD'

INPUT_1 = 'ttyAMA0:S1'
INPUT_2 = 'ttyAMA0:S2'
INPUT_3 = 'ttyAMA0:S3'
INPUT_4 = 'ttyAMA0:S4'
```

Example
```
from EV3dev.ev3 import *

outC = 'ttyAMA0:MC'
mC = LargeMotor(outC)
```

##Network
I found that ifconfig did not work for me so I had to use
```
ip addr show
```


##More Input info
Have to define them first (so far)
```
import subprocess
subprocess.call("echo ev3-analog > /sys/class/lego-port/port0/mode", shell=True)
subprocess.call("echo lego-ev3-touch > /sys/class/lego-port/port0/set_device", shell=True)

from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('ttyAMA0:MA')

ts = TouchSensor('ttyAMA0:S1')
assert ts.connected, "Connect TouchSensor"

while True:

        m.run_forever(speed_sp=300)
        if ts.value() == 1:
                m.stop()
```
From Bash
```
echo ev3-analog > /sys/class/lego-port/port0/mode
echo lego-ev3-touch > /sys/class/lego-port/port0/set_device
```
