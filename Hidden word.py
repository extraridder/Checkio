def checkio(text, word):
    #print(text,word,sep="\n\n")
    a = text.replace(" ","").lower().split("\n")
    print(a)
    print(a[0],word[0],word[0] in a[0],(a[1].index(str(word[0])) + 1) if word[0] in a[1] else "not found")
    for each in a:
        i = a.index(each)+1
        if word[0] in a[i-1]:
            pass
    #print(a[0].index(word[0]))
    return [1, 1, 1, 4]


'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
'''
checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten")

