def tringle_number(x):
    a,i=0,1
    array=list()
    while x >= a:
        array.append(a)
        a += i
        i += 1
        #print(array)
    array.pop(0)
    return array

def checkio(number):
    a = tringle_number(number)
    print(a)
    result_list = list()

    print(result_list)
    return [number // 2, number - number // 2]

#These "asserts" using only for self-checking and not necessary for auto-testing
'''
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
'''
checkio(371)