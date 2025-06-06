times_sum = int()
times_string = '1h 45m,360s,25m,30m 120s,2h 60s'

times_list = times_string.replace(',', ' ').split()

for time in times_list:
    if 'h' in time:
        times_sum += int(time[:-1]) * 60
    elif 'm' in time:
        times_sum += int(time[:-1])
    elif 's' in time:
        times_sum += int(time[:-1]) // 60

print(times_sum)
