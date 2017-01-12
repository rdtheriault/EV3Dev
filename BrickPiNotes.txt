#Notes on using a BrickPi vs EV3

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
