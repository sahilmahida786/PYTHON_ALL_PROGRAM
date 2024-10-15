# get request of url with request code.

# import requests  # type: ignore
# response = requests.get("https://www.google.com") #Enter url here.
# print(response.text) #smiple get a request.


# post request and code also request.
import requests
from bs4 import BeautifulSoup  
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/" #url
r = requests.get(url)
# print(r.text) #smiple get a request.
from bs4 import BeautifulSoup   # import Beautifulsoup 

soup = BeautifulSoup(r.text, 'html.parser') #var

print(soup.prettify()) #smiple get a request.

for heading in soup.find_all("footer"):# enter the any code resource.
    print(heading.text) # print of resource code like footer.


