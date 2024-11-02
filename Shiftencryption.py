#Encryption
#Asal Rahbari
PT = input("Please enter your text: ")
key = int(input("Please enter your key: "))
#define a function to perform the encryption process
def shift_encryption(K , PT):
    CT = ""
    for i in PT:
        if i.isalpha():
            num = ord(i) + K
            if num > ord('z'):
                num = num - 26
            ans = chr(num)
            CT = CT + ans
    CT = CT.upper()
    return CT

CT = shift_encryption(key,PT)
print("The ciphertext is: ", CT)