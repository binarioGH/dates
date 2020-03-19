#-*-coding: utf-8-*-

from tkinter import *


def do_all(date):
	return get_day_of_the_week(get_date_in_days(date))

def get_date_in_days(date):
	date = date.strip().split("/")
	try:
		years = int(date[-1])
		months = int(date[0])
		days = int(date[1])
	except:
		return -1
	else:
		months30 = (4, 6, 7, 9, 11)
		if years < 0:
			return -1
		if months > 12 or months < 0:
			return -1
		if months in months30 and days > 30:
			return -1
		elif months == 2:
			if years % 4 == 0 and days > 29:
				return -1
			elif years % 4 != 0 and days > 28:
				return -1
		else:
			if days > 31:
				return -1
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

def console_mode():
	date = ""
	while date != "exit":
		date = input("Input a date (mm/dd/yyyy):")
		days = get_date_in_days(date)
		if date == "exit":
			continue
		elif days == -1:
			print("{} is an Invalid date.".format(date))
			continue
		day = get_day_of_the_week(days)
		print("{} was a {}.".format(date, day))

def main():
	MBG = "#FCDFD8"
	root = Tk()
	root.geometry("500x500")
	root.title("Get da date")
	mframe = Frame(root, bg=MBG)
	mframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	title = Label(mframe, bg=MBG, text="Input a date!", fg="black", font=("Courier", 18))
	title.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
	inputDate = Entry(mframe, font=("Courier", 20))
	inputDate.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.1)
	send = Button(mframe, text="Check!", font=("Courier", 18), command=lambda:result.config(text=do_all(inputDate.get())))
	send.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1)
	result = Label(mframe,bg=MBG,text="", font=("Courier", 40))
	result.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

	root.mainloop()

if __name__ == '__main__':
	main()
	#console_mode()



	