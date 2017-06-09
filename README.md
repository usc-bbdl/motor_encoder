# motor_encoder
Contains classes that allow the motors to be moved and encoders to be read.



Additional Information:
To understand how pulse lengths allow control of servos visit: https://www.youtube.com/watch?v=ddlDgUymbxc&t=185s&index=15&list=PLKgqFZFLmrATtqQgirSF6pDOexzkuzEmG

0deg ;.5ms pulse width time
neutral or 90deg ; 1.5ms pulse width time
180deg ; 2.5ms pulse width time

***If you need to calculate pulse-width in microseconds, you can do that by first figuring out how long
each cycle is. That would be 1/freq where freq is the PWM frequency you set. For 1000 Hz,
that would be 1 millisecond. Then divide by 4096 to get the time per tick, eg 1 millisecond / 4096 =
~0.25 microseconds. If you want a pulse that is 10 microseconds long, divide the time by time-per-tick
(10us / 0.25 us = 40) then turn on at tick 0 and turn off at tick 40. (source:Adafruit manual).

Example:
.0005/((1/50)/4096) = 102.4 pulse width
.0015/((1/50)/4096) = 307.2
.0025/((1/50)/4096) = 512

Note: When you set the servos that we have to 180 degrees or 512 pulse width, the motors move to a position greater than 180. It seems like the motors need to be calibrated and a number lower than 512 needs to be given to generate 180 degrees. Good luck.
