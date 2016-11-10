import decimal
def format_number(number, decimals=0,base=1000):
    print("format_number",number)
    if base != 1000:
        while abs(number) >= 1024.0:
            print("format_number number=", number)
            number /= 1024.0
    print("format_number final number=", number)
    print(('{:.%sf}' % str(decimals)).format(number))
    return ('{:.%sf}' % str(decimals)).format(number)

def round_number(number ,base=1000,powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    for i in range(1,9):
        if abs(number) < base:
            return 0
            break
        elif abs(number) >= 10 ** (3 + 3 * (i - 1)) and (abs(number) < 10 ** (3 + 3 * i)):
            return powers[i],number/(10 ** (3 + 3 * (i - 1)))
            break
        else:
            continue


def friendly_number(number, base=1000, decimals=0, suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    print(number, base)
    result = ""
    step = round_number(number)
    digit = format_number(number,decimals,base)
    print(step,digit)
    b = format_number(step[1],decimals)
    #print(format_number(step[1],decimals))
    result += b
    result += step[0]

    print(result)
    # return str(number)


def sizeof_fmt(num, suffix='B'):
    print(abs(num),type(num))
    print(float(abs(num)) < 1024.0)
    for i in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        print(i, num)
        if abs(num) < 1024.0:
            print("%3.1f%s%s" % (num, i, suffix))
            return "%3.1f%s%s" % (num, i, suffix)
        num /= 1024.0
    print("%.1f%s%s" % (num, 'Yi', suffix))
    return "%.1f%s%s" % (num, 'Yi', suffix)



#round_number(100000 * 10**9)
number,i = 102400000000,2
#sizeof_fmt(number, suffix='B')
#print(abs(number) >= 10 ** (3 + 3 * (i -1))) and (abs(number) <= 10 ** (3 + 2 * i))
#print(10 ** (3 + 3 * i))
#friendly_number(number, base=1000, decimals=4, suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'])

decimal.getcontext().prec = 3
print(decimal.Decimal(1000000.0)/decimal.Decimal(1024))
print(round(976.5625,1))
#friendly_number(102) == '102', '102'
#friendly_number(10240) == '10k', '10k'
#friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
#friendly_number(12461, decimals=1) == '12.5k', '12.5k'
friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'