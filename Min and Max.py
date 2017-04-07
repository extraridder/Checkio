def min(*args, **kwargs):
    if args:
        pass
    if kwargs:
        pass
    a = args[0]
    for each in args:
        if a > each:
            a = each
    key = kwargs.get("key", None)
    print(key)
    print(a)
    return a


def max(*args, **kwargs):
    if kwargs:
        print("key",kwargs)
        f = kwargs['key']
    if args:
        print(type(args))
        if args[0] > args[1]:
            print("ASDf")
        for i in args:
            print(i)
            for each in i:
                pass
                #print(f(each))


'''
if args:
        for each in args:
            if isinstance(each, (list, set, str)):
                print("Object is iterable")
                print(tuple(each))
            else:
                print("object is not iterable")
                print(each)
if args:
        a = args[0]
        for each in args:
            if a < each:
                a = each
        print(a)
        return a
    if kwargs:
        pass
    print(type(args))
    print(sorted(map(abs, list(args))))
    a = args[0]
    for each in args:
        if a < each:
            a = each
    #key = kwargs.get("key", None)
    print(key)
    print(a)
    return a
'''

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
'''
#max(3, 2,1,2,3,4,5,6,7)
#min(3, 2,1,2,3,4,5,6,7,-1)
#max([1, 2, 0, 3, 4])
#max([[1, 2], [3, 4], [9, 0]], key=1)
#max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])
max("hello")
#a = [1, 2]
#f = lambda x: x[2]
#print(f(a))
