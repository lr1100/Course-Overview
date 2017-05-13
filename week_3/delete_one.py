word = input("Enter a word: ")

words = [word[0:x] + word[y:len(word)] for x in range(len(word)) for y in range(x+1, len(word))]


print(words)
