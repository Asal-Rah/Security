#Encryption
#Asal Rahbari
import random
#get the key from user
key = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for c in alphabet:
    key[c] = input("Enter the substitution for {}: ".format(c))
#get the plaintext
PT = input("Please enter your text :")
#encryption process
def subs_encrypt(PT, key):
    CT = ""
    for i in PT:
        if i.isalpha():
            i = i.lower()
            CT =  CT + key[i]
        else:
            CT = CT + i
    return CT


print("The cipher text is :" ,subs_encrypt(PT, key))