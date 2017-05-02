def piglatin(word):
    word = word.lower()
    ay = word[:1] + "ay"
    return (word[1:] + ay).title()

names = input("Enter your name: ").split()
for name in names:
    print("%s " % piglatin(name), end='')
