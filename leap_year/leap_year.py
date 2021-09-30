LEAP_YEAR = 'Високосный год'
NOT_LEAP_YEAR = 'Не високосный год'

currentYear = int(input())

# check del on 4 = check_four

if currentYear % 4 == 0:
    check_four = 1
else:
    check_four = 0

# check del on 100 = check_hundred

if currentYear % 100 == 0:
    check_hundred = 1
else:
    check_hundred = 0

# check del on 400 = check_four_hundred

if currentYear % 400 == 0:
    check_four_hundred = 1
else:
    check_four_hundred = 0

# main check leap

if (check_hundred and (not(check_four)) or check_four_hundred):
    result = LEAP_YEAR
else:
    result = NOT_LEAP_YEAR

print(result)
