import room
import urllib.request
from bs4 import BeautifulSoup

class Geography(object):

  def __init__(self):
    self.books = self.get_books()
    self.geo = self.initialize_geo()
    self.current_room = self.geo['00000000']

  def initialize_map(self):
    rooms = {
        '00000000': room.Room()
        }

  def current_room(self):
    return self.current_room

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

