#Given that a year has 365 days, 52 weeks, 12 months
#we need to how many days, weeks and months we have left till we become 90 years old
age = input("Enter your current age: ")
age_int = int(age)
age_in_mon = age_int * 12
age_in_weeks = age_int * 52
age_in_days = age_int * 365
y90_in_mon = 90 * 12
y90_in_weeks = 90 * 52
y90_in_days = 90 * 365
left_mon = y90_in_mon - age_in_mon
left_weeks = y90_in_weeks - age_in_weeks
left_days = y90_in_days - age_in_days
print(f"You have {left_days} Days, {left_weeks} Weeks and {left_mon} Months left.")



