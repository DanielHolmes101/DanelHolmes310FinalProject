from bs4 import BeautifulSoup
import requests


#finds wikipedia link about subject, returns false otherwise


def extract_search_term(subject):
 
  # create headers based off computers specifications
  headers = {
      'User-agent':
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
  }
  # general search params
  params = {
    "q": subject + 'Wikipedia',
    "gl": "us",
    "hl": "en",
    "num": "100"
  }
  # parse html for wikipedia link
  html = requests.get("https://www.google.com/search", headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')
  for result in soup.select('.tF2Cxc')[:15]:
    
    title = result.select_one('.DKV0Md').text
    link = result.select_one('.yuRUbf a')['href']
    word = 'Wikipedia'
   # return the link
    if word in title:

     return link
    else: 
     return False
