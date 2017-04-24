import math
def checkio(height, width):
    pi = math.pi
    e = 2.71828183
    a, b = width/2,height/2
    if b == a:
        v = round(4 * pi * a ** 3 / 3,2)
        s = round(4 * pi * a ** 2,2)
        print([v,s])
        return [v,s]
    elif a > b:
        e1 = ((a ** 2 - b ** 2) ** 0.5) / a
        s = round(2 * pi * a * a * (1 + ((1 - e1 **2) * math.atanh(e1) / e1 )),2)
        v = round((4 * pi / 3) * a * a * b,2)
        print([v,s])
        return [v, s]
    elif a < b:
        e1 = ((b ** 2 - a ** 2) ** 0.5) / b
        s = round(2 * pi * a * a * (1 + (b * math.asin(e1) / (e1 * a) )), 2)
        v = round((4 * pi / 3) * a * a * b, 2)
        print([v,s])
        return [v, s]
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
checkio(2, 2)
checkio(2, 4)