import requests

url = "https://companyenrichment.abstractapi.com/v1/?api_key=91ed2d597df9426ea51610c6307fee37&domain="

domain = input("Please enter Company domain: ").lower()
response = requests.get(f"{url}{domain}")

dump = response.json()

name = dump["name"]
domain = dump["domain"]
founded_year = dump["year_founded"]
industry = dump["industry"]
employees = dump["employees_count"]
locality = dump["locality"]
country = dump["country"]
linkedin = dump["linkedin_url"]

print(f"Name: {name}")
print(f"Domain: {domain}")
print(f"Year founded: {founded_year}")
print(f"Industry: {industry}")
print(f"Number of Employees: {employees}")
print(f"HQ location: {locality}")
print(f"Country: {country}")
print(f"LinkedIn profile URL: https://www.{linkedin}")
print()

