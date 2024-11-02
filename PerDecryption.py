#Decryption
# Asal Rahbari
#get the ciphertext and key from user
CT_input = input("Please enter your text :")
order_of_per = list(map(int,input("enter your permutation's order (use space between numbers) :").split()))
order = []
for i in range(len(order_of_per)) :
    if order_of_per[i] == " " :
        pass
    else :
        order+=[int(order_of_per[i])]
CT = CT_input.replace(" ", "")
length = len(CT) - len(order)
remainder_part = CT[-length:]
def permute(order , ct):
    str =''
    PT = str.join([ct[i] for i in order])
    return PT

def permutation_decrypt(order , str):
    #get the inverse order of permutation
    inverse_order = [0] * len(order)
    length = len(order)
    for i in range(length):
        inverse_order[order[i]] = i
    PT = permute(inverse_order,str)
    return PT
#print the results
if length == 0 :
        PT = permutation_decrypt(order,CT)
        print("The plaintext is :",PT)
else :
    PT =''
    nums = len(CT) // len(order)
    blocks = [CT[i:i + len(order)] for i in range(0, len(CT), len(order))]
    for i in range(nums) :
        PT += permutation_decrypt(order , blocks[i])
    print("The plaintext is :", PT)




