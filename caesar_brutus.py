#!/usr/bin/python3
def encrypt(plaintext,n):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if(char == ' '):
            ciphertext += ' '
        else:
            if(char.isupper()):
                ciphertext += chr((ord(char) + n-65)% 26 + 65)
            else: ciphertext += chr((ord(char) + n - 97)% 26 + 97)
    return ciphertext
def dec(plaintext,n):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if(char == ' '):
            ciphertext += ' '
        else:
            if(char.isupper()):
                ciphertext += chr((ord(char) + -n-65)% 26 + 65)
            else: ciphertext += chr((ord(char) + -n - 97)% 26 + 97)
    return ciphertext
print("1.Encrypt\n2.Decrypt\n3.Bruteforce")

try:
	choice = int(input(": "))

	if(choice == 1):
		plaintext = input("Input plaintext: ")
		n = int(input("n: "))
		print("Ciphertext: " + encrypt(plaintext,n))

	elif(choice == 2):
		ciphertext = input("Input ciphertext: ")
		n = int(input("n: "))
		print("Plaintext: " + dec(ciphertext,n))
		
	elif(choice == 3):
		ciphertext = input("Input ciphertext: ")
		print("Bruteforcing possible phrases")
		for i in range(26):
			print("n: " + str(i) + " | " + str(dec(ciphertext,i)))

except:
	print("Invalid input")
