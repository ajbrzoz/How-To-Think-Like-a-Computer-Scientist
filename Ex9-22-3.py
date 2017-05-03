# Exercise 9.22.3

# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text
# - perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

# Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text
# and then keeps track of how many are the letter ‘e’.

import string


def eee(quote):
    quote = quote.lower()
    chars = 0
    e_count = 0
    for c in quote:
        if c in string.ascii_lowercase:
            chars += 1
        if c == 'e':
            e_count += 1

    ratio = round(100 * (e_count / chars), 1)

    print("Your text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(chars, e_count, ratio))


phrase = "Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your " \
         "text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the " \
         "text like this"

eee(phrase)
