def probability(dice_number, sides, target):
    dict_probability = {}
    c = 0
    for i in range(1, dice_number + 1):
        if i == 1:
            for each in range(1, sides + 1):
                dict_probability[each] = round((1/sides), 4)
        else:
            temp_dict = {}
            for each in dict_probability.keys():
                for ii in range(1, sides + 1):
                    if (each + ii) in temp_dict.keys():
                        temp_dict[each + ii] += (dict_probability[each] * (1 / sides))
                    elif (each + ii) not in temp_dict.keys():
                        temp_dict[each + ii] = dict_probability[each] * (1 / sides)
            dict_probability = temp_dict
    if target in dict_probability:
        return dict_probability[target]
    else:
        return round(0.0000, 4)


probability(2, 6, 3)
probability(2, 6, 4)
probability(2, 6, 7)
probability(2, 3, 5)
probability(2, 3, 7)
probability(7, 6, 7)
probability(10, 10, 50)
probability(1,2,999)