M = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368}
def checkio(opacity):
    limit = 10000
    year = 0
    if limit == opacity:
        print(opacity, year)
        return 0
    while True:
        year += 1
        if year in M:
            limit -= year
        else:
            limit += 1
        if limit == opacity:
            break
    print(limit, year)
    return year

'''
 assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
'''

checkio(9999)