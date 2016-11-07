VOWELS = "aeiouy"

def translate(phrase):
    words = phrase.split()
    print(words)
    out = ""
    for each in words:
        print("Start each word",  len(each), each, out)

        for i in range(0, len(each)):
            if i == 0:
                if each[i] not in VOWELS and each[i + 1] in VOWELS:
                    out += each[i]
                elif each[i] in VOWELS and each[i-1] not in VOWELS:
                    continue
            elif i > 0 and i < len(each) - 2:
                if each[i] in VOWELS and each[i-1] not in VOWELS:
                    continue
                elif 1:
                    pass




            '''
            print("Start next elem",i, each[i], len(each), each,  out )
            if each[i] not in VOWELS and each[i + 1] in VOWELS:
                print("not Vowel st",i, each[i], len(each), each, out)
                out += each[i]
                print("not Vowel end",i, each[i], len(each), each, out)
            elif i == (len(each) - 2):
                out += " "
            elif each[i] in VOWELS and (each[i]== each[i+1]==each[i+2]):
                print("Vowel st",i, each[i], len(each), each, out)
                out += each[i]
                print("Vowel end",i, each[i], len(each), each, out)
            else:
                print("else")
                continue
            '''
            '''
            if i == (len(each) - 1):
                print("last element st",i, each[i], len(each), each, out)
                out += " "
                print("last eleent end",i, each[i], len(each), each, out)
            '''
    print(out)



    return phrase


translate("hoooowe yyyooouuu duoooiiine")
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
'''