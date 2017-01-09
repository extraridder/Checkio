import datetime

import calendar
#my_date = datetime.date.today()
#print(my_date,type(my_date))
#print(calendar.day_name[my_date.weekday()])
#print(datetime.datetime.strftime('2012-02-10' , '%Y-%m-%d'))
#d = datetime.datetime.strptime('2007-07-18 10:03:19', '%Y-%m-%d %H:%M:%S')
#day_string = d.strftime('%Y-%m-%d')
#print(day_string)
a = "2007-07-18"
#print(datetime.date(2101,month=12,day=2),type(datetime.date(2101,month=12,day=2)))

def most_frequent_days(year):
    result = list()
    week = ('Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
    a = {0: 0,1: 0 ,2: 0,3: 0,4: 0,5 : 0,6 : 0}
    #print(a[0])
    day = datetime.date(year,month=1,day=1)
    #print(day,type(day))
    #cal_day = calendar.day_name[day.weekday()]
    cal_day = day.strftime("%w")
    #print(cal_day,type(cal_day),calendar.day_name[day.weekday()])
    a[int(cal_day)] += 1
    #print(a)
    while day !=  datetime.date(year,month=12,day=31):
        one_day = datetime.timedelta(days=1)
        day += one_day
        #print(cal_day, type(cal_day), calendar.day_name[day.weekday()])
        cal_day = day.strftime("%w")
        a[int(cal_day)] += 1
    #one_day = datetime.timedelta(days=1)
    #next_day = day + one_day
    #print(next_day,type(next_day))
    #print(next_day.strftime("%w"),calendar.day_name[next_day.weekday()])
    print(a)
    #a = {0: 52, 1: 52, 2: 52, 3: 52, 4: 53, 5: 53, 6: 52}
    max_value = max(a,key=lambda i: a[i])
    max_value = a[max_value]
    #print(max_value, type(max_value))
    b = list()
    for i in range(0,len(a.keys())):
        #print(a[i])
        if int(a[i]) == int(max_value):
            #print("true",list(a.keys())[1])
            b.append(list(a.keys())[i])
    print(b)
    c = list()
    for each in b:
        if 0 in b:
            c.insert(0,week[each])
        else:
            c.append(week[each])
    print(c)

'''
def most_frequent_days(year):
    a = dict()
    first_day = "%s-01-01" % (year)
    first_ = datetime.datetime.strptime('20070718', '%Y%m%d')
    print(first_,type(first_))
    first_day = first_.strftime('%Y%m%d')
    #first_day_datetime = datetime.strftime(first_day,"%Y-%m-%d")
    print(first_day,type(first_day))
    #print(calendar.day_name[datetime(first_day.weekday())])
    """
        List of most frequent days of the week in the given year
    """
    return ['Monday']

    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
'''
most_frequent_days(328)