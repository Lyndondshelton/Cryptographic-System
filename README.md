# Cryptographic-System

The goal of this project is to create a cryptographic system that can encrypt a message by using a Matrix Cipher. First, the system uses an encrypted alphabet to encrypt the message before it is entered in the Matrix Cipher. The *"encrypted alphabet"* is created by using a Caesar cipher on a *"plaintext alphabet"* where the letters are represented by numerical values. The Caesar cipher will increase the value of each letter in the alphabet by a certain number; this number is called the **Caesar Key**. By using this method, the plaintext letter *‘A’* may instead be perceived as the ciphertext letter *‘Z’* or *‘F’*. This creates a pre-encrypted message to be entered in the **encryption matrix**.

**Ex 1:** 
	
	We send the message "Hello":
	
	cipher key = 12
	
	Plaintext: 27 18 39 39 48 = “H E L L O”
	Ciphertext:  39 30 51 51 60 = “L I P P S”

The Encryption Matrix will contain the values of the letters in the ciphertext message. We denote the encryption matrix as **Y**, and the matrix cipher key used is a 4x4 matrix called **Key**. *Y * Key* will give the desired Encrypted Matrix which is called **ENC**. The value of the previously defined Caesar Key is determined by *multiplying the number of rows in **Key** by the difference in values between letters in the alphabet.*

**Ex 2:**
	
	Caesar key is initially unknown. Choose two adjacent letters in the alphabet:

	a = Value of ‘A’= 5 
	b = Value of ‘B’= 7
	Caesar Key = (number of rows in KEY) * (b – a) = 4 * (7 – 5) = 8 


Initially, the size of Y is unknown and is determined by *the length of the cipher text and the dimensions of Key*. Since, *Y * Key = ENC*, the number of columns in Y must be equal to the number of rows in Key. The number of rows of the matrix Y is determined by the length of the ciphertext divided by the rows in the matrix Key. If the result of this division is a decimal, then ***always round up***.


**Ex 3:**

	The string “HELLO” has a length of 5.
	Since 5/4 = 1.25 is a decimal we round up, so the number of rows in Y is 2, and Y is a 2x4 matrix.

In order to decrypt the encrypted message, we use the inverse of the matrix Key:

	ENC * Inv_Key = DEC

Then convert the numeric values in DEC by using the Encrypted Alphabet to obtain the ciphertext message, then use the Caesar Key to decrypt the message.
