def ip_range_check(x):
    mask = 1
    mask_f = 0
    for ii in range(0,32):
        tmp_mask = x[0][:mask]
        for each in x:
            if str(each).startswith(tmp_mask) == False:
                mask_f += 1
                break
        if mask_f > 0:
            break
        mask += 1
    return mask -1,x[0][:mask-1]+"0"*(32-mask+1)


def checkio(data):
    import re
    array_bin = list()
    for each in data:
        a = each.split(".")
        str_a = ""
        for i in a:
            str_a += "".join("{:08b}".format(int(i)))
        array_bin.append(str_a)
    #print(array_bin)
    mask_f,mask_f1 = ip_range_check(array_bin)
    #print(mask_f,mask_f1)
    str_result =""
    while len(mask_f1) > 0:
        tmp = mask_f1[:8]
        #print(tmp, int(tmp,2),len(mask_f1))
        str_result += str(int(tmp,2))
        str_result += "."
        mask_f1 = mask_f1[8:]
    str_result = str_result[:-1] + "/" + str(mask_f)
    #print(str_result)

    return str_result




'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
'''
checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"])
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"])
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"])
ip1 = '192.168.1.1'
#print('.'.join([bin(int(x)+256)[3:] for x in ip1.split('.')]))

ip1 = "10101100000100000000110100000000"
#print("{0:10d}".format(int(ip1)))