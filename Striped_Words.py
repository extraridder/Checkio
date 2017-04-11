VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    # print(text)
    a = list()
    c = 0
    if " " in text:
        a = text.split(" ")
    elif "," in text:
        a = text.split(",")
    elif "." in text:
        a = text.split(".")
    for each in a:
        print("<=====================================================>")
        print(each)
        if len(each) % 2 == 0:
            i = 0
            err = 0
            while i >= len(each) - 1:
                #print((each[i].upper() in CONSONANTS and each[i + 1].upper() in VOWELS) == True ,(each[i].upper() in VOWELS and each[i + 1].upper() in CONSONANTS) == True)
                if (each[i].upper() in CONSONANTS and each[i + 1].upper() in VOWELS) or (each[i].upper() in VOWELS and each[i + 1].upper() in CONSONANTS):
                    pass
                else:
                    err += 1
                i += 2
            if err == 0:
                c += 10
        else:
            continue
    print(c)

#checkio("My name is ...")
#checkio("Hello world")
checkio("A quantity of striped words.")
#checkio("Dog,cat,mouse,bird.Human.")

'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
'''

