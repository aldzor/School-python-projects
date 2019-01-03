#a program to calculate the time until "Vappu 2019"

import datetime
from datetime import datetime

def dateDiffInSeconds(date1, date2):
	timedelta = date2 - date1
	return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

countdown_date = datetime.strptime('2018-04-30 00:00:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print('Wabuun aikaa %d päivää, %d tuntia, %d minuuttia, %d sekuntia, mutta wabu ei lobu.' % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, countdown_date)))
