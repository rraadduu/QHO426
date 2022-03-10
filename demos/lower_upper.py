word = input("Enter a word: ")
for letter in word:
  if ord(letter) >= 97 and ord(letter) <= 122: # check ascii table 'ord'
    print(chr(ord(letter)-32), end = "") # transform lower case to uper case. end = "" prints word horizontaly. chr capitalize letters
  else:
    print(letter, end = "") #for first letter to be in first line

#######print(word.upper()) # specific method to print lower words to upper words
#######print(word.lower()) # specific method to print upper words to lower words