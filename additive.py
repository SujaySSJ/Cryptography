def encrypt(plain_text,shift):
	plain_text=plain_text.replace(" ","").upper()
	cipher_text=""
	for letter in plain_text:
		cipher_text+=chr((ord(letter)-65+shift)%26+65)
	return cipher_text


def decrypt(cipher_text,shift):
	plain_text=""
	for letter in cipher_text:
		plain_text+=chr((ord(letter)-65-shift)%26+65)
	return plain_text


plain_text=raw_input("Enter the plain text : ")
shift=input("Enter the shift : ")%26
cipher_text=encrypt(plain_text,shift)
print("Encrypted Text : "+cipher_text)
ch=raw_input("Do you want to decrypt it?")
if ch=='y':
	print("Decrypted Text : "+decrypt(cipher_text,shift))
