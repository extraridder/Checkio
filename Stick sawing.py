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
    for each in a:
        sum = each
        temp_list = list()
        temp_list.append(each)
        print(a.index(each),temp_list)
        for i in range(a.index(each)+1,len(a)):
            if sum >= number:
                print("sum",sum)
                if sum == number:
                    result_list.append(temp_list)
                break
            else:
                sum += a[i]
                temp_list.append(a[i])
        print("END of loop",each,temp_list)

    print(result_list)
    print(max(result_list,key=len) if len(result_list) > 0 else [])
    return max(result_list,key=len) if len(result_list) > 0 else []

#These "asserts" using only for self-checking and not necessary for auto-testing
'''
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
'''
checkio(100)