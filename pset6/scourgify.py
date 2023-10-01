import csv
import sys


if len(sys.argv) == 3:
    if sys.argv[-1].endswith(".csv") and sys.argv[1].endswith(".csv"):
        try:
            with open (sys.argv[1]) as input_file:
                reader = csv.DictReader(input_file)
                with open(sys.argv[-1], "w") as output_file:
                    writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
                    writer.writeheader()

                    for row in reader:
                        name = row["name"]
                        house = row["house"]
                        last, first = name.split(", ")
                        writer.writerow({"first":first, "last":last, "house":house})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    else:
        sys.exit("not a csv file")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")


