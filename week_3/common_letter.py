#Enter words to compare
word1 = input("Enter one word: ")
word2 = input("Enter another word: ")

common_letters = []

#iterate through letters of first word
for letter in word1:
    #check if letter is in word 2
    if letter in word2:
        common_letters.append(letter)

print(''.join(sorted(common_letters)))
