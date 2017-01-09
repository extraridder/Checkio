import math
def checkio(a, b, c):
    if a == b == c:
        return [60, 60, 60]
    else:
        result = list()
        print((b * b + c * c - a * a ) / 2 * b * c)
        #print(math.acos((b ** 2 + c ** 2 - a ** 2) / 2 * b * c) * (180 / math.pi))
        a1 = 0.5
        print(a1, math.acos(a1))
        #result.append(str(math.acos((b ** 2 + c ** 2 - a ** 2) / 2 * b * c) * (180 / )))
        #result.append(int(math.acos((a ** 2 + c ** 2 - b ** 2) / 2 * a * c) * (180 / 180)))
        #result.append(int(math.acos((b ** 2 + a ** 2 - c ** 2) / 2 * b * a) * (180 / 180)))
        print(result)
        #replace this for solution
        return [0, 0, 0]
'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
'''

checkio(3, 4, 5)