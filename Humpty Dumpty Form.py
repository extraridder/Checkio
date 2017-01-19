import math
def checkio(height, width):
    pi = math.pi
    e = 2.71828183
    a, b = width/2,height/2
    if b == a:
        v = 4 * pi * a ** 3 / 3
        s = 4 * pi * a ** 2
    elif b > a:
        print(math.log(e))
        v
    elif height/2 < width/2:
        pass
    #print(round(v,2),round(s,2))
    # return [v, s]

'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
'''
checkio(4, 2)
#checkio(2, 2)
#checkio(2, 4)