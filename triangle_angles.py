import math
def value_cos_func(x,y,z):
    print("{0} ** 2 + {1} ** 2 - {2} ** 2  / 2 * {0} * {1}".format(x,y,z))
    return (x ** 2 + y ** 2 - z ** 2 ) / (2 * x * y)
def round_degrees(x):
    while x >= 180:
        x -= 180
    return x

def round_radians(x):
    while x >= 3.14:
        x -= 3.14
    return x

def checkio(a, b, c):
    if a == b == c:
        print([60, 60, 60])
        return [60, 60, 60]
    else:
        result = list()
        for each in ((a,b,c),(b,c,a),(a,c,b)):
            print(each)
            print(value_cos_func(*each))
            #print(int(round(math.degrees(math.acos(value_cos_func(*each))),0)))
            if abs(value_cos_func(*each)) > 1:
                return [0, 0, 0]
            else:
                result.append(int(round(math.degrees(math.acos(value_cos_func(*each))),0)))
        print(result)
        if sum(result) != 180:
            return [0, 0, 0]
        elif 0 in result:
            print([0, 0, 0])
            return [0, 0, 0]
        else:
            print(list(sorted(result)))
            return list(sorted(result))
'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
'''

#checkio(3, 4, 5)
#checkio(4, 4, 4)
#checkio(2, 2, 5)
#checkio(11, 20, 30)
checkio(10, 20, 30)