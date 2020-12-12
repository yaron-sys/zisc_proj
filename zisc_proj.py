#!/usr/bin/env python3

from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button

from time import sleep
#from signal import pause

def ledPWMStart(pinNum, sleepTimeSec):
	"""
	ledpwm.value = 0  # off
	ledpwm.value = 0.5  # half brightness
	ledpwm.value = 1  # full brightness 
	"""
	ledpwm = PWMLED(pinNum)
	pwmVal = [x * 0.1 for x in range(0, 10)]
	while True:
		for val in pwmVal:
			ledpwm.value = val
			sleep(sleepTimeSec/2)
		#ledpwm.pulse()
		#pause()
		
def ledStart(pinNum, sleepTimeSec):
	led = LED(pinNum)
	while True:
		led.on()
		sleep(sleepTimeSec)
		led.off()
		sleep(sleepTimeSec)
	#led.blink()
	#pause()

def buttonStart():
	button = Button(2)
	led = LED(17)
	
	while True:
		if button.is_pressed:
			print("Button is pressed")
			led.on()
		else:
			print("Button is not pressed")
			led.off()
	
def main():
	#ledPWMStart(17,1)
	#ledStart(17,1)
	#buttonStart()
	pass
	
if __name__ == "__main__":
    # execute only if run as a script
    #main()
	  print("hello world")
