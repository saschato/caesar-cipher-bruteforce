import sys
import string

def shift(key,char):
    chars = string.ascii_uppercase
    if not char in chars:
        return char
    else:
        index = chars.find(char)
        return chars[(index-key)%26]

if __name__ == "__main__":
    ciphertext = input("\n [+] enter ciphertext: ").upper()
    print("\n")

    for key in range(1,26):
        try:
            new_string = ""
            for char in ciphertext:
                new_string += shift(key,char)

            print(" [-] ", new_string," - key: ", key)
            input()
        except KeyboardInterrupt:
            print("\n\n")
            print(" [+] ", new_string," - key: ", key)
            sys.exit()
