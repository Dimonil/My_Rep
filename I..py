import datetime
n = int(input())
year = int(input())
day_list = []

if year % 4 != 0 or year in (1800, 1900, 2100):
    count_day = 365
    d = {
        0: 0,
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
else:
    count_day = 366
    d = {
        0: 0,
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }



m = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12

}
s = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
_s = {
    0:"Monday",
    1:"Tuesday",
    2: "Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
}
all_day = [0 for i in range(7)]


day_list = []

for _ in range(n):
    day_list.append(input())
f_day = input()

x = s[f_day]

for _ in range(count_day):
    all_day[x] += 1
    x = (x+1) % 7



for date in day_list:
    day, month = date.split()
    day = int(day)
    count = 0
    for i in range(m[month]):
        count += d[i]


    count -= 1

    dif = (count + day) % 7
    res = (dif + s[f_day]) % 7
    #print(day, month, _s[res])
    all_day[res] -= 1


good = -1
bad = -1


for i in range(7):
    if good == -1:
        if all_day[i] == max(all_day):
            good = i
    if bad == -1:
        if all_day[i] == min(all_day):
            bad = i





for item in s:
    if s[item] == good:
        print(item, end=' ')
        break

for item in s:
    if s[item] == bad:
        print(item, end=' ')
        break







