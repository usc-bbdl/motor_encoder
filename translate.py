#This function maps degrees to pulse length
#pulseRange(value,minDegrees,MaxDegrees,Min pulse length out of 4096, max pulse length out of 4096)
def pulseRange(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

#print translate(180,0,180,102.4,512),// output should be 512.

