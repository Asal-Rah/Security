#Decryption algorithm
#Asal Rahbari
CT = input("Please enter your text : ")
key = int(input("Please enter your key: "))
#define a function to perform the decryption process
def shift_decrypt(K , CT):
    PT = ""
    for i in CT:
        if i.isalpha():
            num = ord(i) - K
            if num < ord('a'):
                num = num + 26
            ans = chr(num)
            PT += ans

    PT = PT.upper()
    return PT
PT = shift_decrypt(key,CT)
print("The plaintext is:", PT)