def add_time(start, duration, weekday=None):
    # Split input
    time = start.split()
    hour = time[0]
    period = time[1]
    x = 0
    D = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split 'split' result and calculate 'start + duration'
    start_h, start_m = hour.split(':')
    dur_h, dur_m = duration.split(':')
    new_h = int(start_h) + int(dur_h)
    new_m = int(start_m) + int(dur_m)

    # Format timer to advance 1 hour every 60 minutes
    if new_m > 59:
        new_m -= 60
        new_h += 1

    newhh = new_h

    # Same as above to hours // also calculate new period
    while new_h > 12:
        new_h -= 12

    while newhh > 11:
        newhh -= 12
        period = 'PM' if period == 'AM' else 'AM'
        x += 1

    # Workaround for 'next day' string
    if x % 2 != 0:
        if time[1] == "PM":
            x += 1
        else:
            x -= 1

    y = x / 2

    b = str(new_h), str(new_m).zfill(2)

    a = ':'.join(b) + ' ' + period

    # Calculate weekday based on input and period cycle
    if weekday:
        day = D.index(weekday.title())
        day_out = int((day + y) % 7)
        a += ',' + ' ' + str(D[day_out])


    # Adds 'next day' or 'n days later' based on period cycle done above
    if y == 1:
        a += " (next day)"

    if y > 1:
        a += f" ({int(y)} days later)"

    return a
