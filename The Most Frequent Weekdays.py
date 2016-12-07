from datetime import date
import calendar
my_date = date.today()
print(my_date)
print(calendar.day_name[my_date.weekday()])

def most_frequent_days(year):
    a = dict
    first_day = "%s-01-01" % (year)
    print(first_day)
    print(calendar.day_name[calendar.weekday("%s,%s,%s".format())])
    """
        List of most frequent days of the week in the given year
    """
    return ['Monday']


'''
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
'''
most_frequent_days(2399)