from _datetime import datetime

user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# convert string to date
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

# calculate how many days from now till deadline
time_till = deadline_date - today_date

# get only the days
print(f"The time remaining for your goal: {goal} is {time_till.days} days")

# get only the hours and to convert to integer we add int
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"The time remaining for your goal: {goal} is {hours_till} hours")

# get only the seconds and to convert to integer we add int
seconds_till = int(time_till.total_seconds() / 60)
print(f"The time remaining for your goal: {goal} is {seconds_till} seconds")


# Result on run
# Enter your goal with a deadline separated by a colon
# learn python:12.02.2022
# The time remaining for your goal: learn python is 124 days
# The time remaining for your goal: learn python is 2983 hours
# The time remaining for your goal: learn python is 178994 seconds
