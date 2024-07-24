import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('h1', {'id': 'firstHeading'}).text

content = ''
for paragraph in soup.find_all('p'):
    content += paragraph.text

print(f"Title: {title}\n")
print("Content:\n", content)

headings = ''
for heading in soup.find_all(['h2', 'h3']):
    headings += heading.text.strip() + '\n'

print("\nHeadings:\n", headings)

references = ''
for ref in soup.find_all('cite', {'class': 'citation'}):
    references += ref.text.strip() + '\n'

print("\nReferences:\n", references)
