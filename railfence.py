def encrypt(plain_text):
	plain_text=plain_text.replace(" ","").upper()
	row1=""
	row2=""
	count=0
	for letter in plain_text:
		if count%2 is 0:
			row1+=letter
		else:
			row2+=letter
		count+=1	
	cipher_text=row1+row2
	return cipher_text		

def decrypt(cipher_text):
	middle=""
	part1=""
	part2=""
	if len(cipher_text)%2 is 1:
		part1=cipher_text[:len(cipher_text)/2]
		part2=cipher_text[(len(cipher_text)/2)+1:]
		middle=cipher_text[len(cipher_text)/2]
	else :
		part1=cipher_text[:len(cipher_text)/2]
		part2=cipher_text[len(cipher_text)/2:]
	print(part1,part2,middle)		
	plain_text=""
	for i in range(len(part1)):
		plain_text+=part1[i]
		plain_text+=part2[i]		
	plain_text+=middle
	return plain_text
	

plain_text=raw_input("Enter the plain text :")
cipher_text=encrypt(plain_text)
#print(cipher_text)
print("Encrypted Text : "+cipher_text)
ch=raw_input("Do you want to decrypt it?")
if ch=='y':
	print("Decrypted Text : "+decrypt(cipher_text))
