import string

def decode(m, key):
    # p = ""
    # for i in range(len(key)):
    #     if (m[i] == "1" and key[i] == "1"):
    #         p += str(0)
    #     elif ((m[i] == "1" and key[i] == "0") or (m[i] == "0" and key[i] == "1")):
    #         p += str(1)
    #     else:
    #         p += str(0)
    # return p
    return int(m) ^ int(key)