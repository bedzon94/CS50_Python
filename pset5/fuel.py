def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))




def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            div = x / y
            if x > y:
                fraction = input("Fraction: ")
                continue
            else:
                percentage = int(div * 100)
                return percentage

        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")











if __name__ == "__main__":
    main()
