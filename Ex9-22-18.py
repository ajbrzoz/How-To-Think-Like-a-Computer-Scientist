# Exercises 9.22.18

# Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted
# for another to garble the message. For example A -> Q, B -> T, C -> G etc. your function should take two
# parameters, the message you want to encrypt, and a string that represents the mapping of the 26 letters in the
# alphabet. Your function should return a string that is the encrypted version of the message.


import string


def substitution_cipher(oldstr):
    newstr = ""
    for c in oldstr:
        if (c in string.digits) or (c in string.punctuation) or c == ' ':
            newstr += c
        elif c == 'Z':
            c = 'A'
            newstr += c
        elif c == 'z':
            c = 'z'
            newstr += c
        else:
            newstr += chr(ord(c)+1)
    return newstr
