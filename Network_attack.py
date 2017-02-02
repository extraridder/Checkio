def capture(matrix):
    #print(matrix[0])
    time_period = 0
    infection_dict = {0:0}
    secure_hosts = list()
    f = lambda x: matrix[x][x]
    for i in range(0,len(matrix[0])):
        secure_hosts.append(f(i))
    #print(secure_hosts)
    # check connect to other hosts
    for each in range(len(matrix[0])):
        if matrix[0][each] == 1:
            #print("before",infection_dict)
            infection_dict[each] = matrix[each][each]
            #print("after",infection_dict)
    secure_hosts[1] -= 1
    print(secure_hosts)

    print(infection_dict)
    while len(set(infection_dict.values())) != 1:

        for i in list(infection_dict):
            if infection_dict[i] == 0:
                print("matrix[i]",i,matrix[i])
                for each in range(len(matrix[0])):
                    #print("loop",each,matrix[each][each])
                    #print(matrix[i])
                    if matrix[i][each] == 1:
                        print("loop", each, matrix[each][each])
                        print("before",infection_dict)
                        if each in infection_dict.keys():
                            print("key is in inf_dict")
                        else:
                            print("key is not in inf_dict")
                            infection_dict[each] = matrix[each][each]
        print("asdasd",infection_dict)
        for i in infection_dict.keys():
            if infection_dict[i] == 0:
                print(infection_dict[i], "=0")
            else:
                infection_dict[i] -= 1
        time_period += 1
        print(time_period)
        print("<===================================================>")

    print("Final time", time_period)




'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
'''
#capture([[0, 1, 0, 1, 0, 1], [1, 8, 1, 0, 0, 0], [0, 1, 2, 0, 0, 1], [1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 3, 1], [1, 0, 1, 0, 1, 2]])
#apture([[0, 1, 1], [1, 9, 1],[1, 1, 9]])
capture([[0,1,0],[1,9,1],[0,1,9]])