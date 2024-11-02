#Decryption
#Asal Rahbari
CT = input("Please enter your text :")
keys = input("Please enter your keys :")
#find the gcd
def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b % a, a)
        return (g, x - (b // a) * y, y)
#define a function to calculate the multiplicative inverse of the first given key in the mod 26

def multiplicative_inverse(x , y):
    a, z, t = gcd(x , y)
    if a != 1:
        raise Exception("The given number doesn't have inverse in mod 26 ")
    else:
        return z % y

def affine_decrypt(CT, a, b):

    mod = 26
    PT = ""
    inverse = multiplicative_inverse(a, mod)
    for i in CT:
        if i.isalpha():
            i = i.lower()
            ans = chr(((inverse * (ord(i) - ord('a') - b)) % 26 ) + ord('a'))
            PT  =  PT + ans
        else:
            PT = PT + i
    return PT
x = int(keys[0])
y = int(keys[1])
PT = affine_decrypt(CT , x , y)
print ( "The plaintext is :" , PT)