def power_supply(network, power_plants):
    print("Кол-во заводов", len(power_plants.keys()))
    if len(power_plants.keys()) == 0:
        output = list()
        for each in network:
            output.append(each[0])
            output.append(each[1])
        print(list(set(output)))
    else:
        plants = list(power_plants.keys())
        print("Название заводов", plants)
        network_array = network
        result_list = list()
        for each in network_array:
            for i in plants:
                print(each,i)
                if i in each:
                    print("%s in %s" % (i,each))
                    #plants[i] += str("-" + each[0] if each[0] != i else each[1])
                    #print(plants.index(i))
                    plants[plants.index(i)] += str("-" + each[0] if each[0] != i else "-" + each[1])
                    print("middle plantrs",plants)
            #network_array.pop(network_array.index(each))
    print("Конец", plants)
    #print("Конец",power_plants)
    return set([])
'''
if __name__ == '__main__':
    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['c2']), 'one blackout'
    assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3']), 'two blackout'
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]), 'no blackout'
    assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == set(['c0', 'c2']), 'weak power-plant'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == set([]), 'cooperation'
    assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
                         ['c5', 'c6'], ['c5', 'p7']],
                        {'p1': 1, 'p7': 1}) == set(['c3', 'c4', 'c6']), 'complex cities 1'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                         ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                       ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                       ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                      {'p0': 1, 'p12': 4, 'p8': 1}) == set(['c6', 'c7']), 'complex cities 2'
    assert power_supply([['c1', 'c2'], ['c2', 'c3']], {}) == set(['c1', 'c2', 'c3']), 'no power plants'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == set(['c3']), 'circle'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == set([]), 'more than enough'
    print("Looks like you know everything. It is time for 'Check'!")
'''

#power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4})
#power_supply([['c1', 'c2'], ['c2', 'c3']], {})
power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1})



