import string
import random
import math
alphabet=string.ascii_uppercase
index={}
padding=""
for i,letter in zip(range(26),alphabet):
	index[letter]=i

def encrypt(plain_text,key):
	plain_text=plain_text.replace(" ","").upper()
	key=key.upper()
	global padding
	if "X" not in plain_text:
		padding="X"
	else:
		diff=set(alphabet)-set(plain_text)
		padding=diff.pop()

	g=int(math.ceil(float(len(plain_text))/len(key)))
	for i in range(g*len(key)-len(plain_text)):
		plain_text+=padding
	
	cipher_text=""
	i=0
	for letter in plain_text:
		total=index[letter]+index[key[i]]
		i=(i+1)%len(key)
		if total>25:
			total=total-25
		cipher_text+=index.keys()[index.values().index(total)]
	return cipher_text

def decrypt(cipher_text,key):
	plain_text=""
	key=key.upper()
	i=0
	for letter in cipher_text:
		diff=index[letter]-index[key[i]]
		i=(i+1)%len(key)
		if diff<0:
			diff=diff+25
		plain_text+=index.keys()[index.values().index(diff)]
	return plain_text.replace(padding,"")	


plain_text=raw_input("Enter plain text :")
key=raw_input("Enter the key :")
cipher_text=encrypt(plain_text,key)
print("Encrypted Text : "+cipher_text)
ch=raw_input("Do you want to decrypt it?")
if ch is 'y':
	print("Decrypted Text : "+decrypt(cipher_text,key))