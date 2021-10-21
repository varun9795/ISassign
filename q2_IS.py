#affine cipher


# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
#function to find modular inverse
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# Affine cipher encryption formula:
# C = (a * P + b) mod 26, where C is cipher text, a is key1, text is plaintext, b is key2.
def encrypt(text,a,b):
	output = ""

	# looping through text
	for i in range(len(text)):
		ele = text[i]

		# Encrypt uppercase eleacters
		if (ele.isupper()):
			output += chr((a*(ord(ele)-65)+b) % 26 + 65)

		# Encrypt lowercase eleacters
		else:
			output += chr((a*(ord(ele)-97)+b)  % 26 + 97)

	return output

# Formula for Affine decryption:
# P = a^-1 (C - b) mod 26, where text is plaintext, a is key1, C is cipher text and b is key2.
def decrypt(text,a,b):
    output =""

    # traverse text
    for i in range(len(text)):
        ele=text[i]
        # decrypt uppercase characters
        if (ele.isupper()):
            output += chr((modinv(a,26)*((ord(ele)-65)-b)) % 26 + 65)
        else:
            output += chr((modinv(a,26)*((ord(ele)-97)-b)) % 26 + 97)
    
    return output

#check the above function
text = "AFFINECIPHER"
# taking hardcoded two key
a= 17
b=20
print("Text : " + text)
print("Key : " + str(a)+" "+str(b))
res=encrypt(text,a,b)
print("EnCrypt using Affine Cipher: " + res)
print("DeCrypt using Affine Cipher: " + decrypt("UBBAHKCAPJKX",a,b))
