import requests
from bs4 import BeautifulSoup
from datetime import datetime

# webs crap amount of money
url = "https://www.ratujemyzwierzaki.pl/ami-zanim-odejde"

result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")

element = soup.find('span', class_="amount")

value = element.get_text(strip=True)

# format value
if value[-2:] == "zł":
    value=value[:-2]

value=value.replace(" ", "")


# get time
current_datatime = datetime.now()

formatted_datatime = current_datatime.strftime("%Y-%m-%d %H:%M:%S")


# save to file
path= "ratujemy_zwierzaki_tracker.csv"

line=formatted_datatime + ", " + value + "\n"

with open(path, "a") as file:
    file.write(line)
