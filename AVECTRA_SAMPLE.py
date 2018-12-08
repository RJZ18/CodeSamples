import requests
import datetime
from bs4 import BeautifulSoup
import re

# with requests.Session()as c:
#     serviceurl = 'https://netforum.avectra.com/eweb/DynamicPage.aspx?Site=KAAR&WebCode=IndResult&FromSearchControl=Yes'
#     payload = {'__EVENTTARGET':'ListControl_365f8b73-7c37-4008-8ac7-801e3d9f3a34','__EVENTARGUMENT':'0'}
#     c = requests.post(serviceurl, data=payload)
    #print(c.text)

serviceurl = 'https://netforum.avectra.com/eweb/DynamicPage.aspx?Site=KAAR&WebCode=IndResult&FromSearchControl=Yes'
payload = {'__EVENTTARGET':'ListControl_365f8b73-7c37-4008-8ac7-801e3d9f3a34','__EVENTARGUMENT':'0'}
c = requests.post(serviceurl, data=payload)

bs = BeautifulSoup(c.text, 'html.parser')
data = bs.find_all("td")

for linebreak in data[8].find_all('br'):
    linebreak.extract()

data2 = data[8].contents
# print(data2)
# print("Agent Name: " + data2[1].string)
# print("Company Name: " + data2[3].string)
# print("Address Line: " + data2[4].string)
# print("City, State, Zip: " + data2[5].string)
# print("Phone: " + data2[6].string)
# print("Fax: " + data2[7].string)


# if any("Phone:" in s for s in data2):
#     print(data2)
#     print(data2.index("11543 Kingston Pike"))

AgentName = data2[1].get_text()
CompanyName = data2[3].get_text()
AddressLine = data2[4]
CityStateZip = data2[5]
Phone = data2[6]
Fax = data2[7]
#Email = data2[9].get_text()
print(AgentName)
print(CompanyName)
print(AddressLine)
print(CityStateZip)
print(Phone)
print(Fax)
#print(Email)

# for content in data[4].contents:
#     print(content)
