# Khaled Adad

#ceasar cypher

def main():
    message = input("Enter message: ")
    shift = int(input("Enter shift amount: "))
    encryptedMsg = Ceasar(message, shift)
    print(message)
    print(encryptedMsg)

def Ceasar(message, shift):
    # assuming shift will not be less than 0 or greater than 25
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    first_half = alphabet[shift:]
    second_half = alphabet[:shift]

    cipher = first_half + second_half
    enc = ""
    print(f'alphabet: {alphabet}')
    print(f'cipher: {cipher}')

    for i in message:
        if i.upper() in alphabet:
            idx = alphabet.index(i)
            enc += cipher[idx]
        else:
            enc += i

    return enc

main()