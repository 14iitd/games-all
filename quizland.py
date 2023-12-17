import requests
from bs4 import BeautifulSoup
f=open('trivia.txt','a')
# Define the base URL
base_url = "https://quizzlandanswers.com/en/{}/which-animal-can-go-longer-than-a-camel-without-water"

# Iterate through the range of i values (1 to 100000)
for i in range(1312, 100001):
    url = base_url.format(i)

    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific content based on the class names
        q = soup.find('h1')
        li_element = soup.findAll('li', class_='question-breadcrumb')[1]

        # Extract and print the text content
        if q:
            print(f"Span element content for URL {i}:")
            x=q.get_text(strip=True)
            cat=li_element.get_text(strip=True)
            l=x+"##"+cat
            print(l)
            f.write(l+'\n')
    else:
        print(f"Failed to fetch data for URL {i}. Status code: {response.status_code}")

#
# import requests
# from bs4 import BeautifulSoup
#
# # Define the base URL
# base_url = "https://quizzlandanswers.com/en/{}/which-animal-can-go-longer-than-a-camel-without-water"
#
# f=open('trivia.txt')
# # Iterate through the range of i values (1 to 100000)
# for i in range(1, 100001):
#     url = base_url.format(i)
#
#     # Make a GET request to the URL
#     response = requests.get(url)
#
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Find and extract specific elements or perform operations on the parsed content
#         # For example, find all h1 tags and print their text
#         h1_tags = soup.find_all('h1')
#         print(f"=== H1 tags for URL {i} ===")
#         for tag in h1_tags:
#             f.write(tag.get_text())
#     else:
#         print(f"Failed to fetch data for URL {i}. Status code: {response.status_code}")
