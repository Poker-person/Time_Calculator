D = ["Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday", "Sunday"]

#def add_time(start, duration):
#    x = start.split()
#    hour_start = x[0]
#    period_start = x[1]



#    return new_time

start = "02:10 PM"
duration = "03:25"

time = start.split()
hour = time[0]
period = time[1]

start_h, start_m = hour.split(':')
dur_h, dur_m = duration.split(':')

hourn = duration.split()
print("Start:", hour, period, "Duration:", dur_h, dur_m)

#hour_out = int(hour_spl[0]) + int(dur_spl[0])

#print("output:", hour_out)

new_h = int(start_h) + int(dur_h)
new_m = int(start_m) + int(dur_m)
b = str(new_h), str(new_m)
a = ':'.join(b) + ' ' + period

print(a)
