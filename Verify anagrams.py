def verify_anagrams(first_word, second_word):
    print(first_word,second_word)
    f = list()
    s = list()
    for each in first_word:
        if each != " ":
            f.append(each.lower())
    for each in second_word:
        if each != " ":
            s.append(each.lower())
    print(sorted(f),sorted(s))
    return True if sorted(f) == sorted(s) else False


'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

'''
#verify_anagrams("Kyoto", "Tokyo")
verify_anagrams("Programming", "Gram Ring Mop")