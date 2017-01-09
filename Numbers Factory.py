import functools
def checkio(number):
    simple_number = [2, 3, 4, 5, 6, 7, 8, 9]
    n = number
    b = list()
    #print(set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    a = list(set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    print(a, len(a))
    print(type(a))
    i = 0
    while i <= len(a) - 1:
        print(i, a[i])
        if a[i] > 9:
            i += 1
        else:
            b.append(a[i])
            i += 1
    print(b)
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


'''
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
'''

checkio(20)
