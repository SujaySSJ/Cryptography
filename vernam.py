import string
import random
alphabet=string.ascii_uppercase
index={}
for i,letter in zip(range(26),alphabet):
	index[letter]=i

def encrypt(plain_text):
	plain_text=plain_text.replace(" ","").upper()
	cipher_text=""
	for letter in plain_text:
		total=index[letter]+index[random.choice(alphabet)]
		if total>25:
			total=total-25
		cipher_text+=index.keys()[index.values().index(total)]
	return cipher_text



plain_text=raw_input("Enter plain text :")
cipher_text=encrypt(plain_text)
print("Encrypted Text : "+cipher_text)