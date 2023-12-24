
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

dob_split = dob.split(".")

# use a try except statement to see if date and month are given as valid ints
try:
    # separate the date and month into two separate variables
    dob_split = dob.split(".")
    date = int(dob_split[0])
    month = int(dob_split[1]) - 1

# an error is thrown because either date or month cannot be parsed as an int
except:
    validInput = False


# ensuring that date and month are in  valid ranges
if not 0 < date <= 31:
    validInput = False
if not 0 < month <= 12:
    validInput = False

if validInput:
    firstSundayInMonth = int(code[month])
    dayInWeek = ((date + 7) - firstSundayInMonth) % 7
    weekDay = daysOfWeek[dayInWeek]

    print(weekDay)
else:
    print("Input is not valid")