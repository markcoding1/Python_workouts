# For this exercise, write a Python function (pig_latin) that takes a string
#  as input, assumed to be an English word. The function should return the 
#  translation of this word into Pig Latin. You may assume that the word 
#  contains no capital letters or punctuation.

def pig_latin():
    sentence = input("enter your lowercase word to be translated to Pig Latin:")
    word_list = sentence.split()
    print(word_list)
    vowels = 'aeiou'
    translation = []
    for word in word_list:
        if word[0] in vowels:
            #word starts with a vowel 
            #add 'way to the end'
            word = word + 'way'
            #append the translated word to the end of the translation
            translation.append(word)
        else:
            #  move first letter to the end and add 'ay'

            #split the word into a list of letters, pop the first to put append on the end
            letters = list(word)
            first = letters.pop(0) 
            letters.append(first)
            #rejoin the list 
            word = "".join(letters)
            word = word + "ay"
            #append the translated word to the end of the translation
            translation.append(word)

    translation = " ".join(translation)        
    print(translation)        

pig_latin()    