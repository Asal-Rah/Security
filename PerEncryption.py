#Encryption
#Asal Rahbari
#get the plaintext and key from user
PT_input = input("Please enter your text :")
order_of_per = list(map(int,input("enter your permutation's order(use space between numbers):").split()))
order = []
for i in range(len(order_of_per)) :
    if order_of_per[i] == " " :
        pass
    else :
        order+=[int(order_of_per[i])]
PT = PT_input.replace(" ", "")
length = len(PT) - len(order)
remainder_char = PT[-length:]
def permute(string, order):
    str=''
    CT = str.join([string[i] for i in order])
    return CT
def encrypt(string, order):
    CT = permute(string, order)
    return  CT

#print the results
if length == 0  :
   CT = encrypt(PT,order)
   print("The ciphertext is :", CT)
#where key length is smaller than plaintext length
elif length > 0 :
    r = len(PT) % len(order)
    nums = len(PT) // len(order)
    blocks = []
    c = ''
    if ( r == 0 ) :
       blocks = [PT[i:i+len(order)] for i in range(0, len(PT), len(order))]
       for j in range(nums):
           c += encrypt(blocks[j],order)
       print("The ciphertext is :" , c)
    else :
       blocks = [PT[i:i + len(order)] for i in range(0, len(PT), len(order))]
       re = len(order) - r
       blocks[len(blocks)-1] = blocks[len(blocks) -1 ] + PT[:re]
       for j in range(nums+1):
           c += encrypt(blocks[j],order)
       print("The ciphertext is :" , c)

#when key is larger than plaintext
else :
    r = len(order) % len(PT)
    nums = len(order) // len(PT)
    if(r == 0) :
        PT = PT * nums
        c = encrypt(PT,order)
        print("The ciphertext is :", c)
    else :
         PT = PT * nums
         PT = PT + PT[:r]
         c = encrypt(PT , order)
         print("The ciphertext is : ", c)
