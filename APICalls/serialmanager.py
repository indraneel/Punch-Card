import serial
import util
import sys
import api_twitter

# Set up serial port and initial values
ser = serial.Serial('/dev/tty.usbserial', 9600)
TERMINATOR = 07		# Bell character is terminator character
output_string = ""	# String data to output

# Set up the output modes
output_mode = None
MODE_TWITTER = 01			# Post a tweet to Twitter
MODE_NYTIMES = 02			# Generate a telegram from a New York Times article
MODE_TXTMSG = 03			# Send a text message
MODE_GMAIL = 04				# Send an email
MODE_CONSOLE = 06			# Output text to console

# Read bytes from the serial port
while 1:

	# Check that eight bytes are prepared for input
	if ser.inWaiting() >= 8:
		
		# Read in eight bytes from the serial port
		bytes = read(8)

		# Convert chars '0' or '1' to 00 or 01
		for i in range(len(bytes)):
			if bytes[i] != '0' and bytes[i] != '1':
				print "Invalid byte read from serial port: ", bytes[i], "!"
				sys.exit()
			bytes[i] = bytes[i] - '0'
		
		# Convert the eight 00 or 01 bytes to a number between 0 and 255
		input_value = gen_byte_from_array(bytes)
		
		# Skip the null character
		if input_value == 00:
			continue
		
		# Determine the mode of operation
		if output_mode == None:
		
			# Enter Twitter mode
			if input_value == 01:
				output_mode = MODE_TWITTER
				print "Entering Twitter mode!"
				setup_twitter()
				continue
				
			# Enter New York Times mode
			elif input_value == 02:
				output_mode = MODE_NYTIMES
				print "Entering New York Times mode!"
				continue
			
			# Enter text message mode
			elif input_value == 03:
				output_mode = MODE_TXTMSG
				print "Entering text message mode!"
				continue
			
			# Enter gmail mode
			elif input_value == 04:
				output_mode = MODE_GMAIL
				print "Entering gmail mode!"
				continue
			
			# Enter console mode
			elif input_value == 06:
				output_mode = MODE_CONSOLE
				print "Entering console mode!"
				continue
				
			# Exit the program
			elif input_value == TERMINATOR:
				print "Exiting program..."
				sys.exit()
				
			# Error!
			else:
				print "Error! Invalid output mode specified."
				sys.exit()
		
		# Check for the terminator
		if input_value == TERMINATOR:
		
			# Perform some action based on the output mode
			if output_mode == MODE_TWITTER:
				post_tweet(output_string)
			
			# Reset the output string
			output_string = ""
			sys.stdout.write('\n')
			
			# Reset the mode of operation
			output_mode = None
			continue
		
		# Append this character to the command string
		output_string = output_string + chr(input_value)
		
		# If this is console mode, output the character
		sys.stdout.write(chr(input_value));
		