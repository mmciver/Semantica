from random import randint
import random

class Room(object):

  def __init__(self):
    self.description = self.get_description()
    self.creature = self.get_creature()
    self.exits = self.get_exits()
    self.walls = self.get_walls()

  def display(self):
    print(self.description)
    print(self.creature)
    print(self.display_exits())
    return 1

  def get_description(self):
    return "generic description"

  def get_exits(self):
    possible = [round(randint(0,1)), round(randint(0,1)), round(randint(0,1)), round(randint(0,1))]

    while sum(list(possible)) < 1:
      possible = [round(randint(0,1)), round(randint(0,1)), round(randint(0,1)), round(randint(0,1))]

    exits = {
        'North': possible[0],
        'South': possible[1],
        'East': possible[2],
        'West': possible[3]
        }
    return exits

  def display_exits(self):
    exits = []
    for e in self.exits:
      if self.exits[e] == 1:
        exits.append(e)
    return "You may go " + ", ".join(exits)


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

