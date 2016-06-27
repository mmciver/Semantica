from random import randint
import random

class Room(object):

  def __init__(self, room_id):
    self.room_id = room_id
    self.description = self.get_description()
    self.creature = self.get_creature()
    self.exits = self.make_exits('start')
    #self.walls = self.get_walls()

  def display(self):
    print("\n\n--------------")
    print(self.room_id)
    print(self.description)
    print(self.creature)
    print(self.display_exits())
    return 1

  def get_id(self):
    return self.room_id

  def get_description(self):
    return "generic description"

  def adjacent(self, direction):
    return self.exits[direction]

  def make_exits(self, path_from, rooms_length):
    possible = [round(randint(0,1)), round(randint(0,1)), round(randint(0,1)), round(randint(0,1))]

    while sum(list(possible)) < 1:
      possible = [round(randint(0,1)), round(randint(0,1)), round(randint(0,1)), round(randint(0,1))]

    exits = {}

    if path_from == 'south' or possible[0] == 1:
      exits['north'] = rooms_length
      rooms_length += 1

    if path_from == 'west' or possible[1] == 1:
      exits['east'] = rooms_length
      rooms_length += 1

    if path_from == 'north' or possible[2] == 1:
      exits['south'] = rooms_length
      rooms_length += 1

    if path_from == 'east' or possible[3] == 1:
      exits['west'] = rooms_length
      rooms_length += 1

    return exits

  def display_exits(self):
    exits = []
    for e in self.exits:
      exits.append(e)
    return "You may go " + ", ".join(exits)

  def exits(self):
    return self.exits

  def get_walls(self):
    walls = {
        'North': 0,
        'South': 0,
        'East': 0,
        'West': 0
        }

    if self.exits['North'] == 0:
      walls['North'] = 1

    if self.exits['South'] == 0:
      walls['South'] = 1

    if self.exits['East'] == 0:
      walls['East'] = 1

    if self.exits['West'] == 0:
      walls['West'] = 1

    return walls

  def get_creature(self):
    moods = ['angry', 'sad', 'happy', 'disappointed', 'depressed']
    nouns = ['bear', 'lion', 'boy', 'girl', 'man', 'woman']
    return("There is a %s here that is very %s" % (random.choice(nouns), random.choice(moods)))

