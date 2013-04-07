import serial
import util

# Set up serial port and initial values
ser = serial.Serial('/dev/tty.usbserial', 9600)
TERMINATOR = 7		# Bell character is terminator character
output_string = ""	# String data to output

# Read bytes from the serial port
while 1:
	if ser.inWaiting() >= 8:
		bytes = read(8)
		input_value = gen_byte_from_array(bytes)
		if input_value == TERMINATOR:
			print output_string
			output_string = ""
			continue
		output_string = output_string + input_value