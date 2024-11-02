#Attack against shift cipher
#Asal Rahbari
CT = input("Please enter the text you want to attack : ")

def attack (CT):
    #try all possible keys to find the appropriate plaintext
    #in this case there are only 26 possibilities for the key
    PT = " "
    for key in range(26):
        PT = ""
        for i in CT:
            if i.isalpha():
                num = ord(i) - key
                if num < ord('a'):
                    num = num + 26
                ans = chr(num)
                PT  = PT + ans
        print("The found key is : ", key , " and the plaintext is : " , PT)

attack(CT)