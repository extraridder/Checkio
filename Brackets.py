import re
def checkio(expression):
    brackets_1 = list("[{(")
    brackets_2 = list("]})")
    a=list()
    for each in expression:
        if each in brackets_1 or each in brackets_2:
            a.append(each)
    #print(a)
    str_a = "".join(a)
    #print(str_a)
    patt_1 = "[]"
    patt_2 = "{}"
    patt_3 = "()"
    i = 0
    while len(str_a) > 0:
        if patt_1 in str_a:
            #print("find []")
            str_a = re.sub("\[\]", '', str_a)
            #print(str_a)
        elif patt_2 in str_a:
            #print("find {}")
            str_a = re.sub("\{\}", '', str_a)
            #print(str_a)
        elif patt_3 in str_a:
            #print("find ()")
            str_a = re.sub("\(\)", '', str_a)
            #print(str_a)
        #print(str_a)
        i += 1
        if len(str_a) == 0:
            break
        if i > 1000:
            break
    if len(str_a) > 0:
        return False
    else:
        return True

    #print(a)
    #print("".join(a))
    #str_a = "".join(a)
    #print(str_a[3])




'''
       # return True or False
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
'''

checkio("((5+3)*2+1)")
checkio("{[(3+1)+2]+}")
checkio("(3+{1-1)}")
checkio("2+3")