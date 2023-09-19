import requests
import sys

api_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
dump = api_response.json()

#Check if sys args in not less than 2 and handle errors
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif (sys.argv[1]).isalpha():
    sys.exit("Command-line argument is not a number")
else:
    #Get keys of current bitcoin rate from coindesk
    arg = float(sys.argv[1])
    results = dump["bpi"]["USD"]["rate"]
    final = results.replace(",", "")
    amount = float((sys.argv[1])) * float(final)
    print(f"${amount:,.4f}")
