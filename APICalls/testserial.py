import serial
import sys

ser = serial.Serial('/dev/tty.usbserial', 9600)

while 1:
	while ser.inWaiting() > 0:
		byte = ser.read()
		sys.stdout.write(byte)
		