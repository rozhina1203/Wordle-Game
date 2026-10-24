import random

global guessed
guessed = ['', '', '', '']
word = list()

alphabet = {'a':1, 'b':1, 'c':1, 'd':1, 'e':1, 'f':1, 'g':1, 'h':1, 'i':1, 'j':1, 'k':1, 'l':1, 'm':1, 
            'n':1, 'o':1, 'p':1, 'q':1, 'r':1, 's':1, 't':1, 'u':1, 'v':1, 'w':1, 'x':1, 'y':1, 'z':1}

def promising(txt, i, contain, ans):
    if txt[i] == '-':
        if ans[i] in alphabet:
            alphabet.pop(ans[i])
    
    if txt[i] == '+':
        contain.append((ans[i]))

    if txt[i] == '=':
        guessed[i] = ans[i]
        if ans[i] in alphabet:
            alphabet.pop(ans[i])
    
    return contain
    

def guessword(word, i, c, ans, txt):
    if len(word) == 4 or i < 0:
        return word
    
    contain = promising(txt, i, c, ans)

    word = guessword(word, i-1, c, ans, txt)
    if len(contain) != 0:
        if contain[0] not in word:
            word.clear()
        word.append(contain[0])
        if len(word) == 4:
            contain.pop(0)
        return word   
     
    else:
        keys = alphabet.keys()

        for j in keys:
            if len(word) == 0:       
                word.append(j)
                break
            else:
                check = True
                for k in word:
                    if k == j:
                        check = False
                if check:
                    word.append(j)
                    break
    return word

contain = []
wordle = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(4))
print(wordle)
count = 9

while count > 0:
    inp = input('user input:')
    newword = guessword(word, 3, contain, wordle, inp)
    wordle = ''.join(newword)
    if guessed[0] != '' and guessed[1] != '' and guessed[2] != '' and guessed[3] != '':
        print('Tha answer is:', ''.join(guessed))
        break
    
    elif count > 0:
        print(''.join(newword))
        print(f"{count} number of guesses left.")
        word.clear()
    
    elif count == 0:
       print("I can't guess the word!")
    count -= 1