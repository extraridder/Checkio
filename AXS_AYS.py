import os, re
path = "[[[[[[[[["
lst=os.listdir(path)
print(lst)


a = ""
f = open(']]]]]]]]]]', 'r')
for each in f:
    #print(each)
    m = re.split(", ",each)
    #print(m[4].split("=")[1],":",m[6].split("=")[1],"/",m[7].split("=")[1])
    a = a + m[4].split("=")[1] + str(" : ") + m[6].split("=")[1] + str(" / ") + m[7].split("=")[1]

print(a)