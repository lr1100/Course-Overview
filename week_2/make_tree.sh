#!/bin/bash
#Create File Structure
mkdir s1
mkdir s1/s3
echo "I love bash scripting" > s1/s3/conf.txt
mkdir s1/s2
touch s1/s2/text_analyzer1.py
mkdir s1/s2/Advanced
touch s1/s2/Advanced/text_analyzer2.py

#Write text_analyzer1 python code
echo -e 'words = input("Input a string: ").lower()\n' > s1/s2/text_analyzer1.py
echo -e 'vowels = ["a","e","i","o","u"]' >> s1/s2/text_analyzer1.py
echo -e 'total_vowels = 0\n' >> s1/s2/text_analyzer1.py
echo -e 'for vowel in vowels:' >> s1/s2/text_analyzer1.py
echo -e '\ttotal_vowels += words.count(vowel)' >> s1/s2/text_analyzer1.py
echo -e 'if(total_vowels != 0):' >> s1/s2/text_analyzer1.py
echo -e '\tprint("vowels: " + str(total_vowels))' >> s1/s2/text_analyzer1.py
echo -e 'else:' >> s1/s2/text_analyzer1.py
echo -e '\tprint("there are no vowels in the input string")' >> s1/s2/text_analyzer1.py
echo -e '\texit(0)\n' >> s1/s2/text_analyzer1.py
echo -e 'for character in words:' >> s1/s2/text_analyzer1.py
echo -e '\tif(character in vowels):' >> s1/s2/text_analyzer1.py
echo -e '\t\tprint("first vowel: " + character)' >> s1/s2/text_analyzer1.py
echo -e '\t\tif(words.index(character) != len(words) - 1):' >> s1/s2/text_analyzer1.py
echo -e '\t\t\tprint("character immediately after first vowel: " + words[words.index(character) + 1])' >> s1/s2/text_analyzer1.py
echo -e '\t\telse:' >> s1/s2/text_analyzer1.py
echo -e '\t\t\tprint("first vowel is the last character")' >> s1/s2/text_analyzer1.py
echo -e '\t\tbreak' >> s1/s2/text_analyzer1.py

#Write text_analyzer2 python code
echo -e 'vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}\n' > s1/s2/Advanced/text_analyzer2.py
echo -e 'words = input("Input a string: ").lower()\n' >> s1/s2/Advanced/text_analyzer2.py
echo -e 'for character in words:' >> s1/s2/Advanced/text_analyzer2.py
echo -e '\tif(character in vowels):' >> s1/s2/Advanced/text_analyzer2.py
echo -e '\t\tvowels[character] += 1\n' >> s1/s2/Advanced/text_analyzer2.py
echo -e 'print(vowels)' >> s1/s2/Advanced/text_analyzer2.py
