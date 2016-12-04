def checkio(data):
    print(len(data))
    S = 0
    for i in range(0, len(data)):
        print(i,data[i])
        if i == len(data)-1:
            S += (data[i][0]+data[0][0])*(data[i][1]-data[0][1])
        else:
            S += (data[i][0] + data[i+1][0]) * (data[i][1] - data[i+1][1])
    print(round(S/2,1) if str(round(S/2,1))[-1] != 0 else S/2)
    return abs(round(S/2,1)) if str(round(S/2,1))[-1] != 0 else abs(S/2)

'''
    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
'''
checkio([[1, 1], [9, 9], [9, 1]])
checkio([[4, 10], [7, 1], [1, 4]])
checkio([[1, 2], [3, 8], [9, 8], [7, 1]])
checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]])
checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]])
checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]])
checkio([[3,7],[6,7],[7,4],[7,1],[4,1],[2,3],[4,5]])