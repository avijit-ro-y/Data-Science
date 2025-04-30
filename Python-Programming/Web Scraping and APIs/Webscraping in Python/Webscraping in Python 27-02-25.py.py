#------------------------------------------------------------------Web Scraping------------------------------------------------------------------
#Web scraping is the automated process of extracting information from websites. Instead of manually copying and pasting data, web scrapers collect and structure the data in a systematic way. 

# Web scraping involves four key steps:
# Sending a request – A request is sent to a website's server to fetch the web page's content.
# Receiving a response – The server responds with the page’s HTML code.
# Parsing the HTML – The received HTML is analyzed to find the required data.
# Extracting and structuring the data – The data is cleaned, formatted, and stored in a usable format (CSV, JSON, database, etc.).

#------------------------------------------------------------------The requests Library------------------------------------------------------------------
# requests is a Python library used to send HTTP requests to websites.
# It helps retrieve web pages' HTML content using functions like requests.get(url).text.
import requests

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

#------------------------------------------------------------------Parsing a Page with BeautifulSoup------------------------------------------------------------------
# BeautifulSoup is a Python library that helps extract data from HTML.
# It converts HTML into a parseable format to locate specific elements.
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

#------------------------------------------------------------------Finding All Instances of a Tag at Once------------------------------------------------------------------
# Using soup.find_all(tag_name), we can extract all occurrences of a particular HTML tag.
all_paragraphs = soup.find_all('a')  # Finds all <p> tags
for p in all_paragraphs:
    print(p.text)  # Prints the text inside each paragraph
    
#------------------------------------------------------------------Searching for Tags by Class and ID------------------------------------------------------------------
#Tags can be filtered using their class or id attributes.
specific_div = soup.find("div", class_="popup-container")
print(specific_div)  # Prints content inside div with class="content"

#------------------------------------------------------------------Using CSS Selectors------------------------------------------------------------------
import pandas as pd

titles = soup.select("h1, h2, h3")  # Finds all headings
for title in titles:
    print(title.text)


  # Store in a DataFrame
df = pd.DataFrame({"Headings": [title.text.strip() for title in titles]})

# Save to CSV (optional)
df.to_csv("headings.csv", index=False)
print(df)