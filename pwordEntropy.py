import re
import math
import string

def main():
    #get password from user
    print("Password can contain a-z, A-Z, 0-9, no spaces")
    pw = input("Enter password: ")
    #character set = a-z + A-Z + 0-9
    CS = 26 + 26 + 10
    #max. length will be 48 characters
    ML = 48
    #password length
    plen = len(pw)
    #if password length is longer than max length, say so and exit
    if (plen > ML):
        print ("password is too long")
        return 0
    #if password contains non-alphanumeric characters, say so and exit
    elif (not pw.isalnum()):
        print("non-alphanumeric character(s) in password")
        return 0
    else:
        #entropy = log2(possibly combinations)
        ent = math.log2(pow(CS, plen))
        #time to guess (number of guesses to 50% probability) = 2^ent-1
        ttg = math.ceil(pow(2, ent-1))
        print ("Password is: \n'" + pw + "',\nEntropy is:\n" + str(ent) + " bits,\nexpected brute force guesses is: \n" + str(ttg) + " guesses")
        return 0

if __name__ == '__main__':
    main()