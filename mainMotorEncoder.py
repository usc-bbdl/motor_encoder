import encoderReaderFunction
import motorPosition
import time

#Encoder([PinA1,PinA2],[PinB1,PinB2],numberOfEncoders,pulsesPerRevolution)
d = encoderReaderFunction.Encoder([11,15],[13,16],2,500) # calls constructor, initializing all variables
m = motorPosition.Motor(50,0,180,150,500) # Motor(freq,minDeg,maxDeg,minPulseLength,maxPulseLength), initializes motor class
f = open("encoder.txt","w") # opens or create file to write to.

try:
	while(1):
		encoderReadings = d.encoderReader() # calls function that reads encoder and returns count list with the count
		m.position([0,1,2],[encoderReadings[0],encoderReadings[1],encoderReadings[0]]) #position([pin1,pin2,pin3], [list])
		#pin numbers come from adafruit board.
        	if(d.change ==1): #Only prints value when there is a change
                	print str(encoderReadings) + '\n'
			f.write(str(encoderReadings) + '\n')
except KeyboardInterrupt:
	f.close()
	print "Program Ended Trojan!"	
	
