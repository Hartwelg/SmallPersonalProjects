import string

def encode(m, key):
    # c = ""
    # for i in range(len(key)):
    #     if (m[i] == "1" and key[i] == "1"):
    #         c += str(0)
    #     elif ((m[i] == "1" and key[i] == "0") or (m[i] == "0" and key[i] == "1")):
    #         c += str(1)
    #     else:
    #         c += str(0)
    # return c
    return int(m) ^ int(key)