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

    b = str(new_h), str(new_m).zfill(2)

    if b[0] not in ["10", "11", "12"]:
        a = '0' + ':'.join(b) + ' ' + period
    else:
        a = ':'.join(b) + ' ' + period

    return a
