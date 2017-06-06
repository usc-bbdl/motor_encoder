import RPi.GPIO as GPIO
import time

class Encoder:	
	def __init__(self,A_pin,B_pin,numberOfEncoders,ppr): #Constructor
		#import the GPIO and time package
		self.A_pin = A_pin
		self.B_pin = B_pin
		self.ppr = ppr
		self.numberOfEncoders = numberOfEncoders
		GPIO.setmode(GPIO.BOARD)
		for i in range(numberOfEncoders):
        		GPIO.setup(self.A_pin[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        		GPIO.setup(self.B_pin[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.count_prev = 0.0
        	self.count2_prev = 0.0

        	self.lastModeA = []
        	self.lastModeB = []
        	self.curModeA = []
        	self.curModeB = []
        	self.count = []
        	self.count_last = []
		self.countInDeg = []
		for i in range(numberOfEncoders):  # initializing
                	self.lastModeA.append(0)
                	self.lastModeB.append(0)
                	self.curModeA.append(0)
                	self.curModeB.append(0)
                	self.count.append(0)
                	self.count_last.append(0)
			self.countInDeg.append(0)
	        self.A_prev = 0
	        self.time_ = 0.0
	        self.dt = 0.001
        	self.change =0
	def __del__(self): # Destructor
		GPIO.cleanup()
		print("Destructor was called fellow Trojan!")
		
	def encoderReader(self): # Function that reads encoders
		self.change = 0
		for c in range(self.numberOfEncoders):
			self.curModeA[c] = GPIO.input(self.A_pin[c])
                	self.curModeB[c] = GPIO.input(self.B_pin[c])
   			if(self.curModeA[c] != self.lastModeA[c]):
				if(self.curModeA[c] ==0):
					if(self.curModeB[c]==0):
						self.count[c]= self.count[c] - 1.0
					else:
						self.count[c]=self.count[c] + 1.0
				else:						
					if(self.curModeB[c] == 0):
						self.count[c]=self.count[c] + 1.0
					else:
						self.count[c]=self.count[c] - 1.0
			if (self.curModeB[c] != self.lastModeB[c]):
				if(self.curModeB[c] == 0):
        				if(self.curModeA[c] == 0):
          					self.count[c] = self.count[c] + 1.0
       					else:
         					self.count[c] = self.count[c] - 1.0
				else:
        				if(self.curModeA[c]== 0):
         					self.count[c] = self.count[c] - 1.0
					else:	
						self.count[c] = self.count[c] + 1.0 

			self.lastModeA[c] = self.curModeA[c]
			self.lastModeB[c] = self.curModeB[c]

			if(self.count[c] != self.count_last[c]):
				self.change = 1
		if(self.change == 1):					
			for c in range(self.numberOfEncoders):
				self.count_last[c] = self.count[c] 
				self.time_=self.time_+self.dt
				self.countInDeg[c] = ((self.count[c]/self.ppr)*360)/4
		return self.countInDeg

