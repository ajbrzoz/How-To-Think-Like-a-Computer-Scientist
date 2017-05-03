# Exercise 12.7.17

# Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical
# listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in
# Wonderland. (You can obtain a free plain text version of the book, along with many others, from
# http://www.gutenberg.org.)

book = open('http://www.gutenberg.org/cache/epub/11/pg11.txt', 'r')

words = {}

wordlist = sorted(book.read().split())
for n in wordlist:
    words[n] = wordlist.count(n)

for k in wordlist.keys():
    print(k, wordlist[k])
