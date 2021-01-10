import RandKey
import Dec
import Enc
import string

def main():
    m = input("input binary string to encode: ")
    key = RandKey.makeKey(len(m))
    ciphertext = Enc.encode(m, key)
    print("ciphertext is: " + str(ciphertext))
    print("\ndecrypting\n")
    plaintext = Dec.decode(ciphertext, key)
    print("plaintext is: " + str(plaintext))

if __name__ == "__main__":
    main()