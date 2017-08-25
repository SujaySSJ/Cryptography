import string
import random
from collections import OrderedDict
import itertools


table=[[" " for i in range(5)]for j in range(5)]
index={}
alphabet=string.ascii_uppercase
padding=""

def notPresent(letter):
    for sublist in table:
        for x in sublist:
            if x==letter:
                return False
    return True 

def saveRowColumn():
    global index
    for row,col in itertools.product(range(5),repeat=2):
        index[table[row][col]]=[row,col]
    index['J']=index['I']    


def fillTable(key):
    alphabet_j=alphabet.replace("J","")
    if(key==""):
        for i in range(5):
            for j in range(5):
                while True:
                    letter=random.choice(alphabet_j)
                    if notPresent(letter) is True:
                        table[i][j]=letter
                        break    
    else:
        key=list("".join(OrderedDict.fromkeys(key)))
        key_length=len(key)
        index=0
        for i in range(5):
            for j in range(5):
                if index<key_length:
                    #print("hello")
                    table[i][j]=key[index]
                    index+=1
                else:
                    while True:
                        letter=random.choice(alphabet_j)
                        if notPresent(letter) is True:
                            table[i][j]=letter
                            break
    saveRowColumn()
    return   

def printTable():
    for i in range(5):
        for j in range(5):
            print(table[i][j]),
        print 



def encrypt(plain_text):
    global table,padding
    cipher_text=""
    plain_text=plain_text.upper().replace(" ","")
    if 'X' not in plain_text:
        padding="X"
    else:
        diff=set(alphabet)-set(plain_text)
        if bool(diff) is True:
            padding=random.choice(list(diff))
        else:
            if len(plain_text)%2 is 1:
                print("Error cannot generate a padding character")
    
    new_plain_text=""
    for i in range(len(plain_text)-1):
        new_plain_text+=plain_text[i]
        if plain_text[i]==plain_text[i+1]:
            new_plain_text+=padding
    new_plain_text+=plain_text[-1]

    if len(new_plain_text)%2 is 1:
        new_plain_text+=padding
    
    plain_text=new_plain_text
    chunks,chunk_size=len(plain_text),2
    parts=[plain_text[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    
    for pair in parts:
        row1,col1=index[pair[0]]
        row2,col2=index[pair[1]]
        if row1==row2:
            cipher_text+=table[row1][(col1+1)%5]+table[row2][(col2+1)%5]
        elif col1==col2:
            cipher_text+=table[(row1+1)%5][col1]+table[(row2+1)%5][col2]
        else:
            cipher_text+=table[row1][col2]+table[row2][col1]

    return cipher_text                       

def decrypt(cipher_text):
    global table,padding
    plain_text=""
    chunks,chunk_size=len(cipher_text),2
    parts=[cipher_text[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    for pair in parts:
        row1,col1=index[pair[0]]
        row2,col2=index[pair[1]]
        if row1==row2:
            plain_text+=table[row1][(col1-1)%5]+table[row2][(col2-1)%5]
        elif col1==col2:
            plain_text+=table[(row1-1)%5][col1]+table[(row2-1)%5][col2]
        else:
            plain_text+=table[row1][col2]+table[row2][col1]
    return plain_text.replace(padding,"")

# if __name__=='__main__':
def main():
    plain_text=raw_input("Enter the plain text: ")
    ch=raw_input("Do you have the key ? ")
    key=""
    if ch is 'y':
        key=raw_input("Enter the key :")

    fillTable(key.replace(" ","").upper())    
    #printTable()
    cipher_text=encrypt(plain_text)
    print("Encrypted Text : "+cipher_text)
    ch=raw_input("Do you want to decrypt it?")
    if ch is 'y':
        print("Decrypted Text : "+decrypt(cipher_text))
    print(cipher_text)
    print(decrypt(cipher_text))

main()    