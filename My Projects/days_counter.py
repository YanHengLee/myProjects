dates = input().split('),')
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

# strip off unnecessary strings
for i in range(2):
    dates[i] = dates[i].strip()
    dates[i] = dates[i].strip("(")
    dates[i] = dates[i].strip(")")
    dates[i] = list(map(int, dates[i].split(",")))


# to identify leap year
def isleap(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return 1
    return 0


# switch date so the first date will always be ahead of the second date
if dates[0][0] > dates[1][0]:
    temp = dates[0]
    dates[0] = dates[1]
    dates[1] = temp
elif dates[0][0] == dates[1][0]:
    if dates[0][1] > dates[1][1]:
        temp = dates[0]
        dates[0] = dates[1]
        dates[1] = temp
    elif dates[0][1] == dates[1][1]:
        if dates[0][2] > dates[1][2]:
            temp = dates[0]
            dates[0] = dates[1]
            dates[1] = temp

# count the days
if dates[0][0] == dates[1][0] and dates[0][1] == dates[1][1]:
    days = dates[1][2] - dates[0][2]
else:
    years = dates[1][0] - dates[0][0]
    days += month_list[dates[0][1] - 1] - dates[0][2]
    if days < 0:
        days = 0
    for i in range(dates[0][1], dates[1][1] + 12 * years):
        days += month_list[i % 12]
    days = days - month_list[dates[1][1] - 1] + dates[1][2]

# if leap year add a day
if dates[0][1] <= 2:
    if isleap(dates[0][1]):
        if dates[0][2] < 29:
            days += 1
if dates[1][0] > dates[0][0]:
    t = 0
    if dates[1][1] > 2:
        t = 1
    for i in range(dates[0][0] + 1, dates[1][0] + t):
        if isleap(i):
            days += 1

print("The total number of days:", days)
