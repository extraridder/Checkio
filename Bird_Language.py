VOWELS = "aeiouy"

def translate(phrase):
    words = phrase.split()
    print(words)
    out = ""
    for each in words:
        print("Start each word",  len(each), each, out)
        if len(each) == 2:
            # print("len = 2")
            for i in range(0,len(each)):
                if each[i] not in VOWELS and each[i+1] in VOWELS:
                    # print("condition active")
                    out += each[i]
                    break
        elif len(each) == 3:
            #print("len 3")
            for i in range(0, len(each)):
                if (i == 0 or i == 1) and (each[i] not in VOWELS and each[i + 1] in VOWELS):
                    if each[i] not in VOWELS and each[i + 1] in VOWELS:
                        # print("condition active")
                        out += each[i]
                        break
                elif i == 0 and (each[i] in VOWELS and each[i] == each[i+1] == each[i+2]):
                    # print("trigger VOWEL len =3")
                    out += each[i]
        else:
            for i in range(0, len(each)):
                if i == 0:
                    if each[i] not in VOWELS and each[i+1] in VOWELS:
                        #print("condition active")
                        out += each[i]
                    elif each[i] in VOWELS and each[i] == each[i+1] == each[i+2]:
                        #print("condition active")
                        out += each[i]
                elif (i > 0) and i < len(each) - 3:
                    if each[i] not in VOWELS and each[i+1] in VOWELS:
                        #print("condition active")dfdfh
                        out += each[i]
                    elif each[i] in VOWELS and each[i] == each[i+1] == each[i+2] and each[i-1] not in VOWELS:
                        print("condition active")
                        out += each[i]
                elif i >= len(each) - 3:
                    if each[i] not in VOWELS and each[i+1] in VOWELS:
                        #print("condition active")
                        out += each[i]

        out += " "

    print(out)



    return phrase

#translate("yyyooouuu")
translate("hoooowe yyyooouuu duoooiiine")
'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
'''