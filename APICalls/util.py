# Receive four boolean values corresponding
# to light sensors (true is on, false is off)
# and compute a corresponding nibble
# b1 is farthest left punched hole
def gen_nibble(b1, b2, b3, b4):
	result = (b1 << 3)
	result = result + (b2 << 2)
	result = result + (b3 << 1)
	result = result + b4
	return result

# Receive eight boolean values corresponding
# to light sensors and compute a corresponding byte
# b1...b4 are top row with b1 farthest left
# b5...b8 are bottom row with b5 farthest left
def gen_byte(b1, b2, b3, b4, b5, b6, b7, b8):
	result = gen_nibble(b1, b2, b3, b4) << 4
	result = result + gen_nibble(b5, b6, b7, b8)
	return result

print gen_nibble(True, False, True, False)
print gen_nibble(False, False, True, False)
print gen_nibble(True, True, False, True)
print gen_byte(True, True, True, True, True, True, True, True)
print gen_byte(False, True, True, True, True, True, True, True)
print gen_byte(False, True, True, False, True, True, False, True)