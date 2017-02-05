import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )

def work_with_inf_dict(x,y,z=0,tmp=None):
    for i in list(x):
        if z != 0 and tmp != None:
            tmp_dict = dict()
            if i == 1:
                for each in range(len(y[0])):
                    if y[i][each] == 1:
                        #print("loop", each, y[each][each])
                        #print("before", x)
                        if each in x.keys():
                            #print("key is in inf_dict")
                            continue
                        else:
                            print("!!!key is not in inf_dict!!!!")
                            tmp_dict[each] = y[each][each]
                            print(tmp_dict)
                            return tmp_dict
        if x[i] == 0:
            for each in range(len(y[0])):
                if y[i][each] == 1:
                    if each in x.keys():
                        continue
                    else:
                        x[each] = y[each][each]
    return x

def capture(matrix):
    logging.info("Start script: {}".format(__name__))
    time_period = 0
    infection_dict = {0:0}
    tmp_dict = dict()
    logging.info("Adding item in infection_dictionary: {}".format(__name__))

    for each in range(len(matrix[0])):
        if matrix[0][each] == 1:
            infection_dict[each] = matrix[each][each]
    print("inf_dict and set",infection_dict,set(infection_dict.values()))

    while len(set(infection_dict.values())) != 1:

        work_with_inf_dict(infection_dict, matrix)
        print("inf_dict---->",infection_dict)



        print("asdasd",infection_dict)
        for i in infection_dict.keys():
            if infection_dict[i] == 0:
                print(infection_dict[i], "=0")
            else:
                infection_dict[i] -= 1
        time_period += 1
        print(time_period)
        print("set",set(infection_dict.values()),"inf_dict",infection_dict)
        if set(infection_dict.values()) == {0}:
            logging.info("set == 0: {}".format(__name__))
            print("set == 0")
            tmp_dict = work_with_inf_dict(infection_dict, matrix, z=1, tmp=1)
            print("tmp_dict---->", tmp_dict)
            infection_dict.update(tmp_dict)
            print(infection_dict)
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
#capture([[0, 1, 1], [1, 9, 1],[1, 1, 9]])
#capture([[0,1,0],[1,9,1],[0,1,9]])
capture([[0,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[0,1,2,1,0,0,0,0,0,0],[0,0,1,3,1,0,0,0,0,0],[0,0,0,1,4,1,0,0,0,0],[0,0,0,0,1,5,1,0,0,0],[0,0,0,0,0,1,6,1,0,0],[0,0,0,0,0,0,1,7,1,0],[0,0,0,0,0,0,0,1,8,1],[0,0,0,0,0,0,0,0,1,9]])