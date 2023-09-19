import sys
import pyfiglet
from pyfiglet import Figlet

#Checks leng of CDL args
if len(sys.argv) == 1:
    letter = input("Letter: ")
    result = pyfiglet.figlet_format(letter)
    print(result)

#Checks for CDL args and scans through second args in a Figlet font list
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in Figlet().getFonts()):
    letter = input("Letter: ")
    result = pyfiglet.figlet_format(letter, font = sys.argv[2])
    print(result)
else:
    #Displays error message
    sys.exit("Invalid usage")
