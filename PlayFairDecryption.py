#Decryption
#Asal Rahbari
CT = input("Please enter your text :")
KEY = input("Please enter your key :")

#define a function to gerenate the 5*5 square
#considering I and J the same
def generate_square_of_size_5(key):
    key = key.replace(" ", "").upper()
    square = ""
    str = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    #fill in the square properly
    for letter in key:
        if letter not in square and letter != "J":
            square = square + letter
    for letter in str:
        if letter not in square:
            square = square + letter
    return square
#define a function to convert the text into pairs
def divide_text_to_pairs(text):
    pairs = []
    text = text.upper().replace(" ", "").replace("J", "I")
    for i in range(0, len(text), 2):
        try:
            if text[i] == text[i + 1]:
                pairs.append(text[i] + "X")
            else:
                pairs.append(text[i] + text[i + 1])
        except IndexError:
                pairs.append(text[i] + "X")
    return pairs
#now the encryption process begins
def decrypt(PT, KEY):
    key_square = generate_square_of_size_5(KEY)
    pairs = divide_text_to_pairs(PT)
    CT = ""
    for pair in pairs:
        row1, column1 = divmod(key_square.index(pair[0]), 5)
        row2, column2 = divmod(key_square.index(pair[1]), 5)
        multiple1 = row1 * 5
        multiple2 = row2 * 5

        if row1 == row2:
              CT = CT + key_square[multiple1 + (column1 - 1) % 5]
              CT = CT + key_square[multiple2 + (column2 - 1) % 5]
        elif column1 == column2:
              CT = CT + key_square[((row1 - 1) % 5) * 5 + column1]
              CT = CT + key_square[((row2 - 1) % 5) * 5 + column2]
        else:
              cl2 = column2 - column1
              CT = CT + key_square[multiple1 + column2]
              CT = CT + key_square[multiple2 + column1]
    return CT

ciphertext = decrypt(CT, KEY)
print("The cipher text is : " , ciphertext)