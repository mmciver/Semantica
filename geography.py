import os
import random
import math
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
    self.road_coord_list = []
    self.paths = {}
    self.initialize_geo()
    self.build_exits()
    self.random_room()

  def initialize_geo(self):
    num_areas = random.randint(1,5)
    num_houses = random.randint(8,15)
    num_paths = random.randint(5,10)
    num_roads = random.randint(2,3)

    print("Building %s Roads..." % num_roads)
    while num_roads > 0:
      self.build_road()
      num_roads -= 1

    print("Building Areas...")
    while len(self.all_rooms) < 4000:
      self.build_area()

    print("Building %s Houses..." % num_houses)
    while num_houses > 0:
      self.build_house()
      num_houses -= 1


    while num_paths > 0:
      #self.build_path()
      num_paths -= 1

  def random_room(self):
    self.current = self.all_rooms[random.choice(list(self.all_rooms.keys()))]

  def closest_road_coord(self, c):
    closest_id = ""
    closest_dist = 999
    ox = c[0]
    oy = c[1]
    for z in self.road_coord_list:
      qx = z[0]
      qy = z[1]
      d = math.hypot(qx-ox, qy-oy)
      if d < closest_dist:
        closest_dist = d
        closest_id = z
    return [closest_dist, closest_id]

  def build_area(self):
    names = ['A freshly plowed field', 'A corn field', 'A wheat field', 'A shady grove', 'A sunny meadow']
    n = "%s %s" % (random.choice(names), len(self.areas))
    self.areas[n] = {}
    xr = random.randint(4,7)
    yr = random.randint(4,7)
    xc = self.r()
    yc = self.r()

    close = self.closest_road_coord((xc, yc))
    while close[0] < 20:
      xc = self.r()
      yc = self.r()
      close = self.closest_road_coord((xc, yc))

    center = (xc, yc)

    nl = yc + yr
    sl = yc - yr
    el = xc + xr
    wl = xc - xr

    x = wl
    y = nl
    while y >= sl:
      while x <= el:
        c = (x, y)
        if c in self.all_rooms:
          if self.all_rooms[c].get_type() == 'path':
            r = room.Room( c, 'area', n )
            self.all_rooms[c] = r
            self.areas[n][c] = r
        else:
          r = room.Room( c, 'area', n )
          self.all_rooms[c] = r
          self.areas[n][c] = r
        x += 1
      x = wl
      y -= 1
    print("  > %s has been built with %s rooms" % (n, len(self.areas[n]) ) )
    self.build_path((xc, yc), close[1], "Path to %s" % n)

  def build_house(self):
    names = ['Weatherby', 'Hill House', 'Northshire Cottage', 'Donnovar Manor', 'Trillhelm', "Joe's Shack", 'An abandoned mill', 'Greyview', 'Elsinor Cottage', 'Overgrown ruins', 'A store house', 'A workshop', 'A barn', 'A house', 'A cottage']
    n = random.choice(names)
    while n in self.areas:
      n = random.choice(names)
    self.houses[n] = {}
    xr = random.randint(1,2)
    yr = random.randint(1,2)
    xc = self.r()
    yc = self.r()

    close = self.closest_road_coord((xc, yc))
    while close[0] < 9:
      xc = self.r()
      yc = self.r()
      close = self.closest_road_coord((xc, yc))

    nl = yc + yr
    sl = yc - yr
    el = xc + xr
    wl = xc - xr

    x = wl
    y = sl
    while x <= el:
      while y <= nl:
        c = (x, y)
        r = room.Room( c, 'house', n )
        self.all_rooms[c] = r
        self.houses[n][c] = r
        y += 1
      y = sl
      x += 1
    print("  > %s has been built with %s rooms" % (n, len(self.houses[n]) ) )
    self.build_path((xc, yc), close[1], "Path to %s" % n)

  def build_road(self):
    names = ['The London Road', 'A well kept road', 'The North Road']
    n = random.choice(names)
    while n in self.roads:
      n = random.choice(names)
    self.roads[n] = {}
    route = random.randint(1,4)
    if route == 1: #from south to north
      x = self.r()
      y = -99
      ndir = list('nnnnnnnnnwe')
    elif route == 2: #from east to west
      x = 99
      y = self.r()
      ndir = list('wwwwwwwwwns')
    elif route == 3: #from north to south
      x = self.r()
      y = 99
      ndir = list('sssssssssew')
    elif route == 4: #from west to east
      x = -99
      y = self.r()
      ndir = list('eeeeeeeeens')

    l = ""
    op = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    while x < 100 and x > -100 and y < 100 and y > -100:
      c = (x, y)
      self.display_map(c)
      if c not in self.all_rooms:
        r = room.Room( c, 'road', n )
        self.all_rooms[c] = r
        self.roads[n][c] = r
        self.road_coord_list.append(c)

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

  def build_path(self, s, e, n):
    c = s
    steps = []

    #destination minus current
    v = [-1, -1] #default heads west and south
    if s[0] < e[0]: #head east
      v[0] = 1

    if s[1] < e[1]: #head north
      v[1] = 1

    xd = (v[0], 0)
    yd = (0, v[1])
    xs = [xd] * abs(e[0] - s[0])
    ys = [yd] * abs(e[1] - s[1])
    steps = xs + ys
    random.shuffle(steps)

    while len(steps) > 0:
      c = (c[0] + steps[0][0], c[1] + steps[0][1])
      self.display_map(c)
      print(n)
      if c not in self.all_rooms:
        r = room.Room( c, 'path', n )
        self.all_rooms[c] = r
        self.road_coord_list.append(c)
      steps.pop(0)


  def r(self):
    return random.randint(0, 200) - 100

  def get_current(self):
    return self.current

  def build_exits(self):
    print("Building Exits...")
    for c in self.all_rooms:
      check = [
          ['East', ( c[0] + 1, c[1] + 0 )],
          ['North', ( c[0] + 0, c[1] + 1 )],
          ['South', ( c[0] + 0, c[1] - 1 )],
          ['West', ( c[0] - 1, c[1] + 0 )],
          ]
      for q in check:
        if q[1] in self.all_rooms:
          i = q[1]
          d = q[0]
          n = self.all_rooms[q[1]].get_name()
          self.all_rooms[c].add_exit(i, d, n)

  def display_map(self, room_id):
    os.system('cls')
    print(room_id)
    xsize = 80
    ysize = 30
    cx = room_id[0]
    cy = room_id[1]

    mx = cx - xsize
    my = cy + ysize

    while my >= cy - ysize:
      r = []
      while mx <= cx + xsize:
        if mx == cx and my == cy:
          r.append("@")
        else:
          r.append(self.get_map_icon((mx, my)))
        mx += 1
      print("".join(r))
      mx = cx - xsize
      my -= 1

  def get_map_icon(self, room_id):
    if room_id in self.all_rooms:
      if self.all_rooms[room_id].get_type() == 'house':
        return "#"
      elif self.all_rooms[room_id].get_type() == 'road':
        return "*"
      elif self.all_rooms[room_id].get_type() == 'area':
        return "+"
      elif self.all_rooms[room_id].get_type() == 'path':
        return "."
      else:
        print("\n\nError: Room Type not found: %s" % self.all_rooms[room_id].get_type())
        exit()
    else:
      return " "

  def move(self, direction, c):
    possible = {
        'north': ( c[0] + 0, c[1] + 1 ),
        'south': ( c[0] + 0, c[1] - 1 ),
        'east': ( c[0] + 1, c[1] + 0 ),
        'west': ( c[0] - 1, c[1] + 0 ),
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

