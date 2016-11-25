def checkio(expression):
    brackets_1 = list("[{(")
    brackets_2 = list("]})")
    a=list()
    str_a = ""
    #print(brackets_1)
    #print(brackets_2)
    for each in expression:
        if each in brackets_1 or each in brackets_2:
            a.append(each)
    for i in range(0,len(a)):
        print(a[i])
        if a[i] in brackets_2 and a[i] in brackets_1:
            if






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