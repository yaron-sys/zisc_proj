#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
from signal import pause

led = LED(17)
while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)

#led.blink()
#pause()
