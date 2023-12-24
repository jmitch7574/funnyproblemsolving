
# Our secret code, the date of the first sunday of each month  
code = "743752741631"

# A list containing the days of the week
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# User input
dob = input("When is your date of birth (format dd.mm)? ")

# checks
validInput = True
if "." not in dob:
    validInput = False

if validInput:
    dob_split = dob.split(".")
    date = int(dob_split[0])
    month = int(dob_split[1]) - 1

    firstSundayInMonth = int(code[month])
    dayInWeek = ((date + 7) - firstSundayInMonth) % 7
    weekDay = daysOfWeek[dayInWeek]

    print(weekDay)
