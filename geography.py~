import room
import urllib.request
from bs4 import BeautifulSoup

class Geography(object):

  def __init__(self):
    self.books = self.get_books()
    self.geo = self.initialize_geo()
    self.current_room = self.geo[95050]

  def initialize_geo(self):
    rooms = {
        95050: room.Room(95050)
        }
    # need to generate the entire map on initialize, a recursive option should work, just have to pass back the rooms to add to the geography
    return rooms

  def get_current_room(self):
    return self.current_room

  def move(self, direction, from_id):
    print(self.current_room.exits)
    if direction in self.current_room.exits:
      print("You move to the %s" % direction)
      room_id = self.current_room.adjacent(direction)
      print("The room id you are moving to is %s" % room_id)
      self.geo[room_id] = room.Room(room_id, len(self.geo))
      print("The room exists as: %s" % self.geo[room_id])
      self.current_room = self.geo[room_id]
      print("There will be exits: \n >>  %s" % self.current_room.display_exits())
      print("There is a current geography of %s" % self.geo)
      print("moving to %s vs current of %s" % (self.geo[room_id].get_id(), self.current_room.get_id()))

    else:
      print("You may not move to the %s" % direction)

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

