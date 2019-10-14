import math
import numpy as np


#
# Initialization of the encryption and decryption dictionaries. alpha_encrypt will return the value of a letter,
#  alpha_decrypt will return the letter associated with a value.
#
alpha_encrypt = {' ': 0, 'A': 3, 'B': 6, 'C': 9, 'D': 12, 'E': 15, 'F': 18, 'G': 21, 'H': 24, 'I': 27, 'J': 30, 'K': 33,
                 'L': 36, 'M': 39, 'N': 42, 'O': 45, 'P': 48, 'Q': 51, 'R': 54, 'S': 57, 'T': 60, 'U': 63, 'V': 66,
                 'W': 69, 'X': 72, 'Y': 75, 'Z': 78, ',': 81, '.': 84, '?': 87, '!': 90, "'": 93, '-': 96, '0': 99,
                 '1': 102, '2': 105, '3': 108, '4': 111, '5': 114, '6': 117, '7': 120, '8': 123, '9': 126}
alpha_decrypt = {0: ' ', 3: 'A', 6: 'B', 9: 'C', 12: 'D', 15: 'E', 18: 'F', 21: 'G', 24: 'H', 27: 'I', 30: 'J', 33: 'K',
                 36: 'L', 39: 'M', 42: 'N', 45: 'O', 48: 'P', 51: 'Q', 54: 'R', 57: 'S', 60: 'T', 63: 'U', 66: 'V',
                 69: 'W', 72: 'X', 75: 'Y', 78: 'Z', 81: ',', 84: '.', 87: '?', 90: '!', 93: "'", 96: '-', 99: '0',
                 102: '1', 105: '2', 108: '3', 111: '4', 114: '5', 117: '6', 120: '7', 123: '8', 126: '9'}

#
# Initialization of the Matrix encryption key. MATRIX_KEY is final and should not be changed.
#
MATRIX_KEY = [
    [2, 3, 6, 7],
    [1, 4, 5, 2],
    [6, 7, 3, 2],
    [9, 10, 2, 3]
]

#
# Initialization of the empty matrices.
#
Y = []  # The encryption matrix that will hold the values of the message
ENC = []  # The encrypted matrix. ENC = Y * MATRIX_KEY
DEC = []  # The decrypted matrix. DEC = ENC * inv_matrix_key


CAESAR_KEY = 12  # The key used for the caesar cipher. CAESAR_KEY is final and should not be changed.
max_value = alpha_encrypt['9'] + CAESAR_KEY  # The largest possible value of a character in the alphabet
string = input("Enter a message: ").upper()  # Get the message as input from the user

#
# Row and Column configuration.
#
x_rows = len(MATRIX_KEY)  # The number of rows in MATRIX_KEY
x_cols = len(MATRIX_KEY[0])  # The number of columns in MATRIX_KEY
y_rows = math.ceil(len(string) / x_rows)  # The number of rows needed for matrix Y to fit the length of the string
y_cols = x_rows  # The number of columns in matrix Y needs to be equal to the number of rows in MATRIX_KEY
entries_in_y = y_rows * x_cols  # The number of total entries in matrix Y


#
# Encrypt the message by using the caesar cipher then the encryption matrix Y
#
# return ENC
#
def encryption(s):

    # Caesar cypher initialization. Increment the values of alpha_encrypt by 3, creating a caesar cipher.
    for x in alpha_encrypt:
        alpha_encrypt[x] = (alpha_encrypt[x] + CAESAR_KEY) % max_value

    # While the number of characters in s is less than the number of entries in ENC, create spaces to fill the gaps.
    while len(s) < entries_in_y:
        s = s + ' '

    # For the number of characters in s, place the value of each character in their proper places in Y.
    char_count = 0
    for i in range(y_rows):
        Y.append([])
        for j in range(y_cols):
            Y[i].append(alpha_encrypt[s[char_count]])
            char_count += 1

    # Matrix multiplication on Y * MATRIX_KEY = ENC
    for i in range(len(Y)):
        ENC.append([])
        for j in range(len(MATRIX_KEY[0])):
            e = 0
            for c in range(len(MATRIX_KEY)):
                e += Y[i][c] * MATRIX_KEY[c][j]
            ENC[i].append(e)

    return ENC


#
# Decrypt the message from the ENC matrix, using the INV_MATRIX_KEY and the caesar_key.
#
# return decrypted_message
#
def decryption(enc_mat):

    #  Initialization of the MATRIX_KEY inverse
    inv_matrix_key = np.linalg.inv(MATRIX_KEY)

    # Initialization of the decrypted message
    decrypted_message = ''

    # Matrix multiplication on enc_mat * INV_MATRIX_KEY = D
    for i in range(len(enc_mat)):
        DEC.append([])
        for j in range(len(inv_matrix_key[0])):
            d = 0
            for c in range(len(inv_matrix_key)):
                d += enc_mat[i][c] * inv_matrix_key[c][j]
            DEC[i].append(round(d))

    # For each of the values in DEC, use the caesar_key to find the original values and decrypt the message
    for i in range(len(DEC)):
        for j in range(len(DEC[0])):
            DEC[i][j] = (DEC[i][j] - CAESAR_KEY) % max_value
            decrypted_message += alpha_decrypt[DEC[i][j]]

    return decrypted_message


# The following lines will encrypt the string and print the encrypted matrix ENC to the screen, then decrypt ENC and
#  print the decrypted matrix DEC and the original message to the screen.
print("The encryption matrix = {}".format(encryption(string)))
message = decryption(ENC)
print("The decrypted matrix = {}".format(DEC))
print("The decrypted message = {}".format(message))


