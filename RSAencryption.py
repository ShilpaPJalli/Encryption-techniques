
# Description: Using the RSA encryption technique to create an encryption
#              program to encrypt text.

from primes import *
import caesar
import playfair
import random, time, os


def encrypt():
    # generating a prime numbers list
    prime_list = primes(1000)

    # choosing two random prime numbers from the list
    p = prime_list[random.randint(0, len(prime_list)-1)]
    q = prime_list[random.randint(0, len(prime_list)-1)]

    # n will be the modulus for the public and private keys
    n = p*q

    # calculating the totient
    m = (p - 1)*(q - 1)

    # choosing an integer e which is between 1 and the totient.
    # e must also be coprime to the totient, so choosing only prime
    # numbers inside that range would guarantee that e is coprime.
    e_list = primes(1000)
    e = e_list[random.randint(0, len(e_list)-1)]

    # choosing a number d such that e*d has a remainder 1 when it is
    # divided by m.
    for d in range(2, 1000000):
        if (e*d)%m == 1:
            break

    # here, you take the user input and convert each character into
    # its appropriate ASCII number
    message = input("\nEnter message to encrypt: ")

    # the following list will contain all the ASCII numbers of the message
    ascii_list = [ord(char) for char in message]

    # the following list will contain all the encrypted values of each ASCII number
    enc_list = [(a**e)%n for a in ascii_list]

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""
    for encryption in enc_list:
        a = random.randint(13221, 561651616) # just generating random numbers between key mashed numbers
        # concatenating a sequence of numbers and a letter into the final encrypted string
        encrypted_string += str(encryption * a) + "<>" + str(a) + alphabet[encryption%26] + "<>"
    fname = str(e) + " " + str(n) + ".txt"
    print(encrypted_string, file=open(fname, 'w'))
    print("\nYour message has been encrypted in a text file with format 'e n.txt'".format(fname))
    print("Please keep note of the public keys: e = {0} end n = {1}".format(e, n))
    # check for '__this_folder_is_totally_not_suspicious__' folder
    # this folder will contain the private keys ... but .. shhh... you didn't need to know that
    if not os.path.isdir("__this_folder_is_totally_not_suspicious__"):
        os.mkdir("__this_folder_is_totally_not_suspicious__")
    store_priv = open("__this_folder_is_totally_not_suspicious__/" + fname, "w")
    print("{0} {1}".format(d, n), file=store_priv)

def decrypt():
    fname = input("\nPlease enter the two public keys 'e' and 'n' separated by a space: ").split()
    e = fname[0]
    n = fname[1]
    enc_data = open(e + " " + n + ".txt", "r").read()
    decryption = ""

    # enc_list is a list of all the encrypted characters of the message
    # that are separated by '<>'
    enc_list = enc_data.split("<>")

    # go to the '...totally_not_suspicious__' folder and extract private keys
    p_k = open("__this_folder_is_totally_not_suspicious__/" + e + " " + n + ".txt", "r").read().split()
    d = int(p_k[0])
    n = int(n) # this n is from the main encrypted file

    print("\n------------------------")
    print("    START DECRYPTION    ")
    print("------------------------\n")

    # every two elements represents one character
    for x in range(0, len(enc_list)-1, 2):
        # the first number a is the main encrypted number and b is the
        # multiplier. here, the appended letter at the end of the second
        # number is being removed
        a, b = int(enc_list[x]), int(enc_list[x+1][:len(enc_list[x+1])-1])
        #print(a, b)
        encryption = a // b
        #print(encryption)
        decryption += chr((encryption**d)%n)
    print(decryption)

    print("\n------------------------")
    print("     END DECRYPTION     ")
    print("------------------------")   

def main():
    output=""
    print("\n")
    print("Welcome, this program uses RSA, Caesar cipher and Playfair cipher techniques to Encryption and Decryption the message")
   # print("using public and private keys.\n")
    #print("\n")
    print("Enter your choice: yes or no")
    if input("'caesar': ")[:2]== "ye":

        if input("'encrypt' or 'decrypt': ")[:2]== "en":
            text = input("Enter message to encrypt: ")

            key =int(input("entr key: "))
            output = "".join(caesar.enc(list(text.upper()), key))
        else:
            cipher = input("entr cipher txt to decrypt: ")
            key=int(input("entr key: "))
            output = "".join(caesar.dec(list(cipher.upper()), key))

        print(output)

       # caesar.enc(text,)
    elif input("'rsa': ")[:2]== "ye":
        if input("'encrypt' or 'decrypt': ")[:2]== "en":
            encrypt()
        else:
            decrypt()
    elif input("'playfair': ")[:2]== "ye":

        if input("'encrypt' or 'decrypt': ")[:2] == "en":
            text = input("Enter message to encrypt: ")

            key = (input("entr key: "))
            output = playfair.enc(text.upper(), key.upper())
        else:
            cipher = input("entr cipher txt to decrypt: ")
            key = (input("entr key: "))
            output = playfair.dec(cipher.upper(), key.upper())
        print(output)
    return output
main()
