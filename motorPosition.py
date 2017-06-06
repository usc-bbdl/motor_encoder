from __future__ import division
import time
import translate 

# Import the PCA9685 module.
import Adafruit_PCA9685

class Motor:
	def __init__(self,freq,degMin,degMax,servo_min,servo_max):
		# Initialise the PCA9685 using the default address (0x40).
		self.pwm = Adafruit_PCA9685.PCA9685()
		print "contructor worked trojan"
		# Configure min and max servo pulse lengths
		self.servo_min = int(servo_min)   # Min pulse length out of 409
		self.servo_max =int(servo_max)  # Max pulse length out of 4096
		self.degMin = degMin
		self.degMax = degMax
		# Set frequency to 60hz, good for servos.
		self.pwm.set_pwm_freq(freq) 

	def position(self,pins, posVector): #Both input arguments need to be explicit list.
		for c in range(len(posVector)):
			#pulseRange maps degress into pulse length
			d = translate.pulseRange(posVector[c], self.degMin, self.degMax, self.servo_min, self.servo_max)
			self.pwm.set_pwm(pins[c],0,int(d))
#			print "function worked trojan"
