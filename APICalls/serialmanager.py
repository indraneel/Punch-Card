import serial
import util
import sys

# Set up serial port and initial values
ser = serial.Serial('/dev/tty.usbserial', 9600)
TERMINATOR = 07		# Bell character is terminator character
output_string = ""	# String data to output

# Set up the output modes
output_mode = None			# By default, value will just be printed to console
MODE_TWITTER = 00			# Post a tweet to Twitter
MODE_NYTIMES = 01			# Generate a telegram from a New York Times article
MODE_TXTMSG = 02			# Send a text message

# Read bytes from the serial port
while 1:

	# Check that eight bytes are prepared for input
	if ser.inWaiting() >= 8:
		
		# Read in eight bytes from the serial port
		bytes = read(8)
		
		# Convert the eight 00 or 01 bytes to a number between 0 and 255
		input_value = gen_byte_from_array(bytes)
		
		# Determine the mode of operation
		if output_mode = None:
		
			# Enter Twitter mode
			if input_value == 00:
				output_mode = MODE_TWITTER
				print "Entering Twitter mode!"
				continue
				
			# Enter New York Times mode
			elif input_value == 01:
				output_mode = MODE_NYTIMES
				print "Entering New York Times mode!"
				continue
			
			# Enter email mode
			elif input_value == 02:
				output_mode = MODE_TXTMSG
				print "Entering text message mode!"
				continue
				
			# Error!
			else:
				print "Error! Invalid output mode specified."
				sys.exit()
		
		# Check for the terminator
		if input_value == TERMINATOR:
		
			# Perform some action based on the output mode
			print output_string
			output_string = ""
			
			# Reset the mode of operation
			output_mode = None
			continue
		
		# Append this character to the command string
		output_string = output_string + chr(input_value)
		