# Cryptographic-System

This cryptographic system uses an encrypted alphabet. The encrypted alphabet is created by using a Caesar cipher on an original alphabet where the letters are represented by numerical values. The Caesar cipher will increase the value of each letter in the alphabet by a certain number, called the **Caesar Key**. By using this method, the plaintext letter ‘A’ may instead be perceived as the ciphertext letter ‘Z’ or ‘F’. This creates a pre-encrypted message to be entered in the encryption matrix.

**Ex 1:** 
	
	Plaintext: 27 18 39 39 48 = “H E L L O”
	Ciphertext:  39 30 51 51 60 = “L I P P S”

The second step in this cryptographic system is to encrypt the ciphertext by using a Matrix cipher. We denote the encryption matrix, the matrix containing the message to be encrypted, as **Y**, and the cipher key used is a 4x4 matrix called **Key**. *Y * Key* will give the encrypted cipher matrix which is called **ENC**. 

Initially, the size of Y is unknown and is determined by the length of the cipher text and the dimensions of Key. Since, *Y * Key = ENC*, the number of columns in Y must be equal to the number of rows in Key. The number of rows of the matrix Y is determined by the length of the ciphertext divided by the rows in the matrix Key. If the result of this division is a decimal, then ***always round up***.


**Ex 2:**

	The string “HELLO” has a length of 5.
	Since 5/4 = 1.25 is a decimal we round up, so the number of rows in Y is 2, and Y is a 2x4 matrix.

In order to decrypt the encrypted message, we use the inverse of the matrix Key:

	ENC * Inv_Key = DEC

Then convert the numeric values in DEC to obtain the ciphertext message and use the Caesar cipher key to decrypt the message.
