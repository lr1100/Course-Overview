#TODO: period is off in output



def is_consonant(letter):
    """Checks to see if a letter is a consonant or not"""
    vowels = ('a', 'e', 'i', 'o', 'u')
    if letter not in vowels:
        return True
    else:
        return False

def to_piglatin(word):
    """Changes the word to piglatin
       Example: Leon -> eonLay"""
    piglatin_word = word
    #Loop through all letters and get there position
    for i,letter in enumerate(word):
        #Move all consonants to the end of the word
        if is_consonant(letter):
            piglatin_word = piglatin_word[1:] + word[i]
        #Found first vowel, break from loop
        else:
            break

    return piglatin_word + "ay"

def main():
    words = input("Enter a word or a sentence ending in a period: ")
    words = words.split()

    #Check to see if the last word has a period, meaning it's a sentence
    if "." in words[-1]:
        piglatin = ""
        #Remove the period in the last word
        words[-1] = words[-1][:-1]
        #Change each word to piglatin
        for word in words:
            piglatin += to_piglatin(word.lower()) + " "

        print(piglatin[0].upper() + piglatin[1:] + ".")


    #Only a single word
    else:
        print(to_piglatin(words[0].lower()).title())


if __name__ == "__main__":
    main()
