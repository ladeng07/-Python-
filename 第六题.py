time = input().split(('-'))
time = time[:-1] + time[-1].split()
weeks=time[3]
time.pop(3)
time = list(map(int,time))
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weeks=week[(week.index(weeks)+time[3]) % 7]

def output_day(year,month):
    if month in (4,6,9,11):
        return 30
    elif month == 2:
        if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31
        
        
def main(time):
	month_day=output_day(time[0],time[1])
	if time[2] +time[3] <= month_day:
		time[2] = time[2] + time[3]
		return tuple(time[:-1])
		
	else:
		if time[1] == 12:
			time[0] += 1
			time[1] = 1
			time[3] = time[3] - month_day
			return main(time)
		else:
			time[1] += 1
			time[3] = time[3] - month_day
			return main(time)

print('%d-%d-%d ' % main(time) + weeks)