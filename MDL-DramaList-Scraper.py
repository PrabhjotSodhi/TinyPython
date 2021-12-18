import requests
from bs4 import BeautifulSoup
import csv

url = 'https://mydramalist.com/dramalist/7899245'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
table_raw = soup.find('table', {"id": "list_2"})

headers = []
for i in table_raw.find_all('th')[1:]:
    header = i.text.strip()
    try:
        int(header)
    except:
        headers.append(header)


wordlist = ["Korean","Drama","Movie"]
for row in table_raw.find_all('tr'):
    raw_data = row.find_all('td')
    data_text = [i.text.strip() for i in raw_data]
    data_text[1] = "Completed"
    title = data_text[0].split()[:-2]
    title = " ".join(title)
    data_text[0] = title
    with open("data.csv", "a", newline='') as data_file:
        write_file = csv.writer(data_file, delimiter=",")
        write_file.writerow(data_text)