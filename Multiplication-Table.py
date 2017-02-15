def checkio(first, second):
    a = "{0:b}".format(first)
    b = "{0:b}".format(second)
    #print(a,b)
    for i in a:
        c1, c2, c3 = "", "", ""
        for y in b:
            print("{0} ==== {1}".format(i,y))
            print(str(int(i) & int(y)))
            print(str(int(i) | int(y)))
            print(str(int(i) ^ int(y)))
            c1 += str(int(i) & int(y))
            c2 += str(int(i) | int(y))
            c3 += str(int(i) ^ int(y))
        print(c1, c2, c3)
    return 1


'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
'''
checkio(4, 6)