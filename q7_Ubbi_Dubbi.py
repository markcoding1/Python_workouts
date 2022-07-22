#In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. 
# Thus milk becomes mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am).

def ubbi_dubbi():
    vowels = 'aeiou'
    new_word = []
    word = input('which word do you want to translate into ubbi dubbi?: ' )
    #split the word into a list of letters
    letters = list(word)
    #iterate the list adding each letter to the new_word list identifying vowels and prefacing them with 'ub' 
    for letter in letters:
        if letter  not in vowels:
            new_word.append(letter)
        else:
            new_word.append('ub')
            new_word.append(letter)
    new_word = "".join(new_word)
    return(new_word)

print(ubbi_dubbi())