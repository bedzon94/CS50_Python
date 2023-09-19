#Decalre list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#Loop forver
while True:
    #Take user input for the program
    date = input("Date: ")
    try:
        #Split input with / into month, day and year
        month, day, year = date.split("/")
        if int(month) <= 12 and int(month) >= 1 and int(day) <= 31 and int(day) >= 1:
            break
    except:
        try:
            #Split input formatted as Month Day, Year
            b_month, b_day, year = date.split(" ")
            #Repeat line 19 if b_day does not end with comma
            if not b_day.endswith(","):
                continue
            #Get index of month in list
            for i in range(len(months)):
                if b_month == months[i]:
                    month = i + 1
            day = b_day.replace(",", "")
            if int(month) <= 12 and int(month) >= 1 and int(day) <= 31 and int(day) >= 1:
                break
        except:
            pass

#Print result & don't forget to rstrip white space from instances with whitespace
print(f"{year.rstrip()}-{int(month):02}-{int(day):02}")
