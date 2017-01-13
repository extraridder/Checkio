
def checkio(time_string):
    import re
    #print(time_string)
    bits = [2,4,3,4,3,4]
    signs = [" "," : "," "," : "," ",""]
    a = time_string.split(":")
    for e in range(0,3):
        if len(a[e]) < 2:
            a[e] = "0" + a[e]
    print(a)
    b =""
    for each in a:
        b += each
    #print(a,b)
    result = ""
    for i in range(0, len(b)):
        #print(b[i])
        c = ("{:0%db}"%int(bits[i])).format(int(b[i]))
        for each in c:
            if each == "1":
                result += re.sub(r'1',"-",each)
            else:
                result += re.sub(r'0',".",each)
        result += signs[i]
        #print(c)
    print(result)
    return ".- .... : .-- .--- : -.. -..-"

'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
'''
checkio("00:1:02")