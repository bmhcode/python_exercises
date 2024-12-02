import datetime # type: ignore
now = datetime.datetime.now()
birthday = int(input('Enter your birthday : '))
# year = now.year
age = now.year - birthday
print('your age is : ', age)


