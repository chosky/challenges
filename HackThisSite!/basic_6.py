#!/usr/bin/python

"""Basic Level 6"""

word = raw_input('Enter the to decrypt: ')

new_word = ''

for i in range(len(word)):
    new_word += chr(ord(word[i]) - i)

print new_word
