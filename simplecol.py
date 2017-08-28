import string
alphabet=string.ascii_uppercase
padding=""
def getTable(plain_text,key):
    row_size=0
    col_size=0
    l=len(plain_text)
    if key:
        col_size=len(key)
        row_size=len(plain_text)/col_size
        key=[(int(x)-1) for x in key]
    else:
        i=0
        while row_size*col_size<l:
            if i%2 is 1: 
                row_size=row_size+1
            else:
                col_size=col_size+1
            i=i+1
        key=[x for x in range(col_size)]

    table=[["" for i in range(col_size)]for j in range(row_size)]
    i=0
    global padding
    if "X" not in plain_text:
        padding="X"
    else:
        diff=set(alphabet)-set(plain_text)
        padding=diff.pop()
    return table,row_size,col_size,key

def encrypt(plain_text,key=""):
    plain_text=plain_text.replace(" ","").upper()
    table,row_size,col_size,key=getTable(plain_text,key)
    i=0
    l=len(plain_text)
    for row in range(row_size):
        for col in range(col_size):
            if i<l:
                table[row][col]=plain_text[i]
                i=i+1
            else:
                table[row][col]=padding
    cipher_text=""
    for col in key:
        for row in range(row_size):
            cipher_text+=table[row][col]
    return cipher_text        

def decrypt(cipher_text,key=""):
    plain_text=""
    table,row_size,col_size,key=getTable(cipher_text.replace(padding,""),key)
    i=0
    l=len(cipher_text)
    for col in key:
        for row in range(row_size):
            table[row][col]=cipher_text[i]
            i=i+1
    for row in range(row_size):
        for col in range(col_size):
            plain_text+=table[row][col] 
    return plain_text.replace(padding,"")

plain_text=raw_input("Enter plain text :")
ch=raw_input("Do you have a key? :")
key=""
if ch is 'y':
    key=raw_input("Enter the key")
cipher_text=encrypt(plain_text,key)
print(cipher_text)
ch=raw_input("Do you want to decrypt?")
if ch is 'y':
     print("Decrypted Text: "+decrypt(cipher_text,key))
