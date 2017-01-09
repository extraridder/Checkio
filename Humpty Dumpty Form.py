import math
def checkio(height, width):
    pi = 3.14159265359
    if height/2 == width/2:
        S = 4 * pi * (height/2) ** 2
        V = (4/3) * pi * (height/2) ** 3
    elif height/2 > width/2:
        e = (- (width/2) ** 2 + (height/2)** 2) ** 0.5 / (width/2)
        print(e)
        S = 2 * pi * (height/2) * (height/2 + (width/2 * math.asin(e)/e))
        V = (4 / 3) * pi * (width/2) * (height / 2) ** 2
    elif height/2 < width/2:
        pass
    print(round(V,2),round(S,2))
    #return [V, S]

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