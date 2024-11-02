#Decryption
#Asal Rahbari
#get the key from user
key = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for c in alphabet:
    key[c] = input("Enter the substitution for {}: ".format(c))
#generate the inverse key for decryption
inverse_key = {}
for c in alphabet:
    inverse_key[key[c]] = c
# get the cipher text
CT = input("Please enter your text :")
#Decryption process
def subs_deccrypt(CT, key):
    PT = ""
    for j in CT:
        if j.isalpha():
            j = j.lower()
            PT =  PT + key[j]
        else:
            PT = PT + j
    return PT
print("The plain text is : ", subs_deccrypt(CT,inverse_key))