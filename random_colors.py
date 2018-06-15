#!/usr/bin/python
from phue import Bridge
import time
import random

#
# for i in range(0,1):
# 	print(i)
# 	time.sleep(3)


b = Bridge('192.168.0.100') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
b.connect()

#b.set_light(3, 'bri',10)
# for i in range(0,5):
# 	b.set_light(3, 'bri',10)
# 	time.sleep(0.5)

lights = b.get_light_objects()
lights[0].brightness = 2
lights[1].brightness = 1

lights[0].xy = [0,1]
lights[1].xy = [1,0]
#
# for i in range(0,1000000):
# 	lights[0].xy = [random.random(),random.random()]
# 	time.sleep(0.5)
#





#
# lights = b.get_light_objects()
#
# for light in lights:
# 	light.brightness = 10
# 	light.xy = [random.random(),random.random()]
