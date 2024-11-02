#Decryption
#Asal Rahbari
import sympy
import numpy as np
import random

#get needed inputs
dimension = int(input("Please enter the dimension of the key matrix :"))
CT = input("Please enter your text :")
key_matrix = []
for i in range(dimension):
    row = []
    for j in range(dimension):
        element = int(input(f"Enter element ({i+1},{j+1}): "))
        row.append(element)
    key_matrix.append(row)
#turn key into matrix
key = np.matrix(key_matrix)


def multiplicative_inverse(A, M):


    for i in range(0, M):
        if (A*i) % M == 1:
            return i
    # If we didn't find the multiplicative inverse in the loop above
    # then it doesn't exist for A under M
    return -1


matrix= sympy.Matrix(key_matrix)
#find the adjoint of matrix
adj=(matrix.adjugate()%26)

m=np.matrix(key_matrix)
#calculate the determinent
det=(round(np.linalg.det(m))%26)


mult_inverse=multiplicative_inverse(det, 26)

inv_m=(mult_inverse*adj)%26
#define a string for plain text
PT=""
alphabet = "abcdefghijklmnopqrstuvwxyz"
for index, i in enumerate(CT):
    values = []
    if index % dimension == 0:
        for j in range(0, dimension):
            if(index + j < len(CT)):
                values.append([alphabet.index(CT[index + j])])
            else:
                values.append([random.randint(0,25)])
        vector = np.matrix(values)
        vector = inv_m * vector
        vector %= 26
        for j in range(0, dimension):
            PT += alphabet[vector[j]]

print("The plain text is : "+ PT.upper())