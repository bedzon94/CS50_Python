from datetime import date
import sys
import inflect

w = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")

    print(mins_lived(year, month, day))



def mins_lived(year, month, day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"
    tday = date.today()
    date_diff = tday - dt
    mins = int(date_diff.total_seconds() / 60)
    result = w.number_to_words(mins, andword="") + " minutes"
    return result.capitalize()


if __name__ == "__main__":
    main()
