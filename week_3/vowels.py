word = input("Enter a word: ")
vowels=['a','e','i','o','u']

words = [word[0:x] + y + word[x+1:len(word)] for x in range(len(word)) for y in vowels if word[x] in vowels and word[x] != y]

print(words)
