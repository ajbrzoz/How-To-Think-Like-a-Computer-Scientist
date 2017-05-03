# Exercise 10.30.23

# Count how many words in a list have length 5.


def count_words5(ll):
    return len([n for n in ll if len(n) == 5])
