import urllib.request
import nltk
from bs4 import BeautifulSoup

class BookReader(object):

  def __init__(self):
    #nltk.download()
    self.books = self.get_books()
    self.education()

  def education(self):
    pass

  def get_books(self):
    print("Getting books...")
    books = {}
    url = "http://www.gutenberg.org/browse/scores/top"
    with urllib.request.urlopen(url) as response:
      page =response.read()
      soup = BeautifulSoup(page, 'html.parser')

      links = soup.find_all('a')
      for link in links:
        if "/ebooks/" in link.get("href"):
          s = str(link)
          name = str[str.find(">"):str.find(" (")]
          stub = link.get("href")
          books[name] = stub

          #books.append(link.get("href"))
        else:
          continue

    print(books)
    return books


