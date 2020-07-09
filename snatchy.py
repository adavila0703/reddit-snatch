import requests
import bs4

request = requests.get('https://www.reddit.com/login/')
reddit_soup = bs4.BeautifulSoup(request.text, 'lxml')

# username reddit_soup.select('input')[9]['name']
# password reddit_soup.select('input')[10]['name']
# token print(reddit_soup.select('input')[2])

session = requests.Session()

# Create the payload
payload = {'_username':'',
          '_password':''
         }

# Post the payload to the site to log in
s = session.post("http://www.reddit.com/login/", data=payload)

# Navigate to the next page and scrape the data
s = session.get('')

soup = bs4.BeautifulSoup(s.text, 'lxml')
print(soup)

