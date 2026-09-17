import requests
from bs4 import BeautifulSoup
#response = requests.get("https://aeon.co")
response1 = requests.get("https://git.new/amit-yadav-repo")
#print(response1.status_code)
#print(response1.headers)

url = "https://aeon.co"
response = requests.get(url=url)
soup = BeautifulSoup(response.text,"html.parser")
#print(soup)
print(soup.title)
print(soup.find_all("div").text)
