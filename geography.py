import room
import urllib.request
from bs4 import BeautifulSoup

class Geography(object):

  def __init__(self):
    self.books = self.get_books()

  def initialize_map(self):
    rooms = {
        '00000000': room.Room()
        }

  def get_books(self):
    print("Getting books...")
    books = []
    url = "http://www.gutenberg.org/browse/scores/top"
    with urllib.request.urlopen(url) as response:
      page =response.read()
      soup = BeautifulSoup(page, 'html.parser')

      links = soup.find_all('a')
      for link in links:
        if "/ebooks/" in link.get("href"):
          books.append(link.get("href"))
        else:
          continue

