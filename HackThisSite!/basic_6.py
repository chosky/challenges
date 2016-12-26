#!/usr/bin/python

"""Network Security Sam has encrypted his password. 
The encryption system is publically available and can be accessed with this form:"""

word = raw_input('Enter the to decrypt: ')

new_word = ''

for i in range(len(word)):
    new_word += chr(ord(word[i]) - i)

print new_word
