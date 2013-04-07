from BreakfastSerial import Led, Arduino, Component
import pyfirmata
import time

def read(neg, pos):
    """Reads in from the positive and negative end and outputs 1 or 0. """
    global ambient, tolerance
    x = getReading(pos, neg)
    if abs(x - AMBIENT) < TOLERANCE:
        return '0'
    else:
        return '1'

def getReading(neg, pos):
#    global leds
    global led2, led3
    # By default, output mode?
    #leds[neg]._pin._set_mode(pyfirmata.OUTPUT)
    #led2._pin._set_mode(pyfirmata.OUTPUT)
    #leds[pos]._pin._set_mode(pyfirmata.OUTPUT)
    #led3._pin._set_mode(pyfirmata.OUTPUT)
    #leds[neg].on()
    print "led2", led2.value
    print "led3", led3.value
    led2.on()
    print "led2", led2.value
    #leds[pos].off()
    led3.off()

    # Change to input mode
    #leds[neg].off()
    led2.off()
    #leds[neg]._pin._set_mode(pyfirmata.INPUT)
    #led2._pin._set_mode(pyfirmata.INPUT)
    #leds[neg]._pin.mode = pyfirmata.INPUT DEPRECATED

    # Read leak time
    j = 0
    for j in range(0, 31000):
        #if leds[neg].value == 0: 
        if led2._pin.value == 0:
            break
    return j


board = Arduino()
#leds = [Led(board, i) for i in range(2, 12)]
#leds[2].off()
#leds[3].on()
led2 = Led(board, 2)
led3 = Led(board, 3)
led2.off()
led3.on()
print "led3.value", led3.value
print "led3._pin.value", led3._pin.value
time.sleep(1)
TOLERANCE = 3100
#AMBIENT = getReading(2, 3) # TODO
while True:
    print getReading(2, 3)
    time.sleep(0.5)
