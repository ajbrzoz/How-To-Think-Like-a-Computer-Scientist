# Exercise 9.22.21

# Write a function called rot13 that uses the Caesar cipher to encrypt a message. The Caesar cipher works like
# a substitution cipher but each character is replaced by the character 13 characters to ‘its right’ in the alphabet.
# So for example the letter a becomes the letter n. If a letter is past the middle of the alphabet then the counting
# wraps around to the letter a again, so n becomes a, o becomes b and so on.

import string


def rot13(mess):
    ciphered = ""
    for char in mess:
        if char in string.ascii_lowercase:
            if ord(char) % 26 in range(6, 19):
                ciphered += chr(ord(char) - 13)
            else:
                ciphered += chr(ord(char) + 13)
        elif char in string.ascii_uppercase:
            if ord(char) % 26 in range(0, 13):
                ciphered += chr(ord(char) - 13)
            else:
                ciphered += chr(ord(char) + 13)
        else:
            ciphered += char
    return ciphered
