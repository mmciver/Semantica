import random
import room
import urllib.request
from bs4 import BeautifulSoup

class Geography(object):

  def __init__(self):
    self.books = self.get_books()
    self.all_rooms = {}
    self.areas = {}
    self.houses = {}
    self.roads = {}
    self.paths = {}
    self.initialize_geo()
    self.build_exits()
    self.random_room()

  def initialize_geo(self):
    num_areas = random.randint(1,5)
    num_houses = random.randint(8,15)
    num_paths = random.randint(5,10)
    num_roads = random.randint(2,3)

    print("Building %s Areas..." % num_areas)
    while num_areas > 0:
      self.build_area()
      num_areas -= 1

    print("Building %s Houses..." % num_houses)
    while num_houses > 0:
      self.build_house()
      num_houses -= 1

    print("Building %s Roads..." % num_roads)
    while num_roads > 0:
      self.build_road()
      num_roads -= 1

    while num_paths > 0:
      #self.build_path()
      num_paths -= 1

  def random_room(self):
    self.current = self.all_rooms[random.choice(list(self.all_rooms.keys()))]

  def coord(self, coords):
    if type(coords) is dict:
      return ("%s %s" % (coords['x'], coords['y']))
    elif type(coords) is str:
      c = coords.split()
      return {
          'x': int(c[0]),
          'y': int(c[1])
          }

  def build_area(self):
    names = ['A freshly plowed field', 'A corn field', 'A wheat field', 'A shady grove', 'A sunny meadow']
    n = random.choice(names)
    while n in self.areas:
      n = random.choice(names)
    self.areas[n] = {}
    area_xr = random.randint(4,7)
    area_yr = random.randint(4,7)
    area_xc = self.r()
    area_yc = self.r()

    area_nl = area_xc + area_xr
    area_sl = area_xc - area_xr
    area_el = area_yc + area_yr
    area_wl = area_yc - area_yr

    x = area_wl
    y = area_sl
    while x <= area_el:
      while y <= area_nl:
        c = ("%s %s" % (x, y) )
        if c not in self.all_rooms:
          r = room.Room( c, 'area', n )
          self.all_rooms[c] = r
          self.areas[n][c] = r
        y += 1
      y = area_sl
      x += 1
    print("  > %s has been built with %s rooms" % (n, len(self.areas[n]) ) )

  def build_house(self):
    names = ['Weatherby', 'Hill House', 'Northshire Cottage', 'Donnovar Manor', 'Trillhelm', "Joe's Shack", 'An abandoned mill', 'Greyview', 'Elsinor Cottage', 'Overgrown ruins', 'A store house', 'A workshop', 'A barn', 'A house', 'A cottage']
    n = random.choice(names)
    while n in self.areas:
      n = random.choice(names)
    self.houses[n] = {}
    area_xr = random.randint(1,2)
    area_yr = random.randint(1,2)
    area_xc = self.r()
    area_yc = self.r()

    area_nl = area_xc + area_xr
    area_sl = area_xc - area_xr
    area_el = area_yc + area_yr
    area_wl = area_yc - area_yr

    start = self.coord("%s %s" % (area_sl, area_wl) )

    x = area_wl
    y = area_sl
    while x <= area_el:
      while y <= area_nl:
        c = ("%s %s" % (x, y) )
        if c not in self.all_rooms:
          r = room.Room( c, 'house', n )
          self.all_rooms[c] = r
          self.houses[n][c] = r
        y += 1
      y = area_sl
      x += 1
    print("  > %s has been built with %s rooms" % (n, len(self.houses[n]) ) )

  def build_road(self):
    names = ['The London Road', 'A well kept road', 'The North Road']
    n = random.choice(names)
    while n in self.areas:
      n = random.choice(names)
    self.roads[n] = {}
    route = random.randint(1,4)
    if route == 1: #from south to north
      x = self.r()
      y = -99
      ndir = list('nnnnnnwe')
    elif route == 2: #from east to west
      x = 99
      y = self.r()
      ndir = list('wwwwwwns')
    elif route == 3: #from north to south
      x = self.r()
      y = 99
      ndir = list('ssssssew')
    elif route == 4: #from west to east
      x = -99
      y = self.r()
      ndir = list('eeeeeens')

    l = ""
    op = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    while x < 100 and x > -100 and y < 100 and y > -100:
      c = ("%s %s" % (x, y) )
      if c not in self.all_rooms:
        r = room.Room( c, 'road', n )
        self.all_rooms[c] = r
        self.roads[n][c] = r

      nx = random.choice(ndir)
      while op[nx] == l:
        nx = random.choice(ndir)

      if nx == 'n':
        y += 1
      elif nx == 's':
        y -= 1
      elif nx == 'e':
        x += 1
      elif nx == 'w':
        x -= 1

      l = nx
    print("  > %s has been built with %s rooms" % (n, len(self.roads[n]) ) )

  def build_path(self):
    pass

  def r(self):
    return random.randint(0, 200) - 100

  def get_current(self):
    return self.current

  def build_exits(self):
    print("Building Exits...")
    for r in self.all_rooms:
      c = self.coord(r)
      check = [
          ['East', "%s %s" % ( c['x'] + 1, c['y'] + 0 )],
          ['North', "%s %s" % ( c['x'] + 0, c['y'] + 1 )],
          ['South', "%s %s" % ( c['x'] + 0, c['y'] - 1 )],
          ['West', "%s %s" % ( c['x'] - 1, c['y'] + 0 )],
          ]
      for q in check:
        if q[1] in self.all_rooms:
          i = q[1]
          d = q[0]
          n = self.all_rooms[q[1]].get_name()
          self.all_rooms[r].add_exit(i, d, n)

  def display_map(self, room_id):
    c = self.coord(room_id)
    cx = c['x']
    cy = c['y']

    mx = cx - 5
    my = cy + 5

    while my > cy - 6:
      r = []
      while mx < cx + 6:
        if mx == cx and my == cy:
          r.append("@")
        else:
          r.append(self.get_map_icon("%s %s" % (mx, my)))
        mx += 1
      print("".join(r))
      mx = cx -5
      my -= 1

  def get_map_icon(self, room_id):
    if room_id in self.all_rooms:
      if self.all_rooms[room_id].get_type() == 'house':
        return "#"
      elif self.all_rooms[room_id].get_type() == 'road':
        return "-"
      elif self.all_rooms[room_id].get_type() == 'area':
        return "+"
    else:
      return " "

  def move(self, direction, from_id):
    c = self.coord(from_id)
    possible = {
        'north': "%s %s" % ( c['x'] + 0, c['y'] + 1 ),
        'south': "%s %s" % ( c['x'] + 0, c['y'] - 1 ),
        'east': "%s %s" % ( c['x'] + 1, c['y'] + 0 ),
        'west': "%s %s" % ( c['x'] - 1, c['y'] + 0 ),
        }
    if possible[direction] in self.all_rooms:
      print("moving %s" % direction)
      self.current = self.all_rooms[possible[direction]]
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

