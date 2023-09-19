def main():
    time = input("What time is it ?")
    time = convert(time)

#Compares input time to determine timing of food
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    else:
        print()

#Converts time corresponding number of hours
def convert(t = 0.0):
    hours, minutes = t.split(":")
    hr = float(hours)
    min = float(minutes) / 60
    tme = round(hr + min, 2)
    return(tme)


if __name__ == "__main__":
    main()
