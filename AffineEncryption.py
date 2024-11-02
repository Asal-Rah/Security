#Encryption
#Asal Rahbari
PT = input("Please enter your text :")
keys = input("PLease enter your keys :")


def get_char(z , x , y):
    return chr((x * (ord(z) - ord('a')) + y) % 26 + ord('a'))

def affine_encrypt(PT,x,y):

    PT = PT.lower().replace(' ', '')
    CT = ''
    for a in PT:
        if a.isalpha():
            CT =  CT + get_char(a,x,y)
        else:
            CT = CT + a
    return CT
x = int(keys[0])
y = int(keys[1])
print("The cipher text is :" , affine_encrypt(PT,x,y))