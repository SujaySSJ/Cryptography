import string
import math
alphabet=string.ascii_uppercase
padding=""
def getTable(plain_text,key):
    row_size=0
    col_size=0
    l=len(plain_text)
    if key:
        col_size=len(key)
        row_size=int(math.ceil(float(len(plain_text))/col_size))
        key=[(int(x)-1) for x in key]
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
    ntable=[["" for i in range(col_size)]for j in range(row_size)]
    for ncol,col in zip(range(col_size),key):
        for row in range(row_size):
            ntable[row][ncol]=table[row][col]   
    cipher_text=""
    for col in key:
        for row in range(row_size):
            cipher_text+=ntable[row][col]
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
    ntable=[["" for i in range(col_size)]for j in range(row_size)]
    for col,ncol in zip(key,range(col_size)):
        for row in range(row_size):
            ntable[row][col]=table[row][ncol]
    for row in range(row_size):
        for col in range(col_size):
            plain_text+=ntable[row][col] 
    return plain_text.replace(padding,"")

plain_text=raw_input("Enter plain text :")
key=raw_input("Enter the key :")
cipher_text=encrypt(plain_text,key)
print(cipher_text)
ch=raw_input("Do you want to decrypt?")
if ch is 'y':
     print("Decrypted Text: "+decrypt(cipher_text,key))
