# Colocar 0 no início quando hora < 10
# Colocar argumento "dias da semana"

def add_time(start, duration):
    time = start.split()
    hour = time[0]
    period = time[1]

    start_h, start_m = hour.split(':')
    dur_h, dur_m = duration.split(':')
    new_h = int(start_h) + int(dur_h)
    new_m = int(start_m) + int(dur_m)

    if new_m > 59:
        new_m -= 60
        new_h += 1

    if new_h > 12:
        new_h -= 12
        if period == "PM":
            period = "AM"
        else:
            period = "PM"

    b = str(new_h), str(new_m)

    a = ':'.join(b) + ' ' + period

    if b[0] in range(1, 9):
        a += '0'

    #c = ' '.join(a, period)

    return a

print("x1:", add_time("02:10 PM", "03:25"))
print("x2:", add_time("11:10 PM", "03:25"))
print("x3:", add_time("02:40 PM", "03:25"))
