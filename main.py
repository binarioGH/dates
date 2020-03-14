#-*-coding: utf-8-*-



def get_date_in_days(date):
	date = date.strip().split("/")
	try:
		years = int(date[-1])
		months = int(date[0])
		days = int(date[1])
	except:
		return -1
	else:
		total_days = 0
		total_days += years * 365
		total_days += int(years / 4)
		if years%4 == 0 and months <= 2:
			total_days -= 1
		for mnth in range(1, months):
			if mnth % 2 == 1 and mnth != 2:
				#print("*")
				total_days += 31
			elif mnth == 2:
				total_days += 28
			else:
				#print("!")
				total_days += 30

		total_days += days
		return total_days

def get_day_of_the_week(days):
	week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
	return week[days%7]

def main():
	date = ""
	while date != "exit":
		date = input("Input a date (mm/dd/yyyy):")
		days = get_date_in_days(date)
		if days == -1 or date == "exit":
			continue
		day = get_day_of_the_week(days)
		print("{} was a {}.".format(date, day))

if __name__ == '__main__':
	main()



	