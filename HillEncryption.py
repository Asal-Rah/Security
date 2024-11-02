#Encryption
#Asal Rahbari
import numpy as np
import random

#get needed inputs
dimension = int(input("Please enter the dimension of the key matrix:"))
PT = input("Please enter your text :")
key_matrix = []
for i in range(dimension):
    row = []
    #get the elements of each row then add the row to the key matrix and move to the next row
    for j in range(dimension):
        element = int(input(f"Enter element ({i+1},{j+1}): "))
        row.append(element)
    key_matrix.append(row)
#turn key into matrix
key = np.matrix(key_matrix)


#alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

#define a string for cipher text
CT = ""

#generate vectors to start the encryption process

for index, i in enumerate(PT):
    values = []
    # Make bloc of N values
    length = len(PT)
    if index % dimension == 0:
        for j in range(0, dimension):
            if(index + j < length):
                values.append([alphabet.index(PT[index + j])])
                # print(f'if:{values}')
            else:
                values.append([random.randint(0,25)])
        #the actual encryption process
        vector = np.matrix(values)
        vector = key * vector
        vector %= 26
        for j in range(0, dimension):
            CT = CT + alphabet[vector.item(j)]

#print the cipher text
print("Cipher text is : "+ CT.upper())
