

def largest_histogram(histogram):
    if len(histogram) == 1:
        print(histogram[0])
        return histogram[0]
    else:
        result_list = list()
        i = min(histogram)
        while True:
            if i == max(histogram):
                break
            else:




    print(histogram)

    return max(histogram)

'''
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
'''

largest_histogram([5])
largest_histogram([5, 3])
largest_histogram([1, 1, 4, 1])
largest_histogram([1, 1, 3, 1])
largest_histogram([2, 1, 4, 5, 1, 3, 3])