#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	output= ""

	# traverse text using
	for i in range(len(text)):
		ele= text[i]

		# Encrypt uppercase characters
		if (ele.isupper()):
			output += chr((ord(ele) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			output += chr((ord(ele) + s - 97) % 26 + 97)

	return output


#decryption technique
def decrypt(text,s):
	output = ""
	s=26-s
	# traverse text
	for i in range(len(text)):
		ele= text[i]

		# Encrypt uppercase characters
		if (ele.isupper()):
			output += chr((ord(ele) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			output += chr((ord(ele) + s - 97) % 26 + 97)

	return output

#check the above function
text = "CIPHER"
shift = 5
print("Text : " + text)
print("Shift : " + str(shift))
print("Encrypted Text Cipher: " + encrypt(text,shift))
print("Decrypted Text Cipher: " + decrypt(encrypt(text,shift),shift))
