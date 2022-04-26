# Khaled Adad

#ceasar cypher

from operator import indexOf

message = input("Enter a string to encrypt: ")
shift = input("Enter the number of charcters to shift by (integer): ")

def Ceasar(message, shift):
    # assuming shift will not be less than 0 or greater than 25
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    first_half = alphabet[shift:]
    second_half = alphabet[:shift]

    cipher = first_half + second_half
    enc = ""

    for i in message:
        if i.upper() in alphabet:
            idx = message.index(i)
            enc += cipher[idx]

    print("message")
    print(enc)

Ceasar(message,shift)