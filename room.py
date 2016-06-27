from random import randint
import random

class Room(object):

  def __init__(self, room_id):
    self.room_id = room_id
    self.coordinates = [int(str(room_id)[1:2]), int(str(room_id)[3:4])]
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

  def get_adjacent_ids(self):
    return self.exits.keys()


  def make_exits(self, path_from):
    possible = [round(randint(0,1)), round(randint(0,1)), round(randint(0,1)), round(randint(0,1))]

    while sum(list(possible)) < 1:
      possible = [round(randint(0,1)), round(randint(0,1)), round(randint(0,1)), round(randint(0,1))]

    exits = {
        'north': -1,
        'east': -1,
        'south': -1,
        'west': -1
        }

    #north
    if path_from


#iterate each direction
#if there is a room in the direction and it also has an exit in this direction, make the exit and link (covers progression)
#if the coordinates would result in a number less than 0 or greater than 99, don't make the exit
#if I want 'pathing' with a greater chance to continue in a given direction of motion, then I have to check the above points
#against all directions first before randomizing the remaining directions.
#better idea .. from the 'start' pick a type of room: open, path, enclosed, and that sets the randomization criteria



    for e in exits:
      print(e)
      if int(str(self.room_id)[1:2]) 

      jumblefluff += 1
    #north

    if path_from == 'south':
      exits['north'] = self.room_id + 100

    if path_from == 'west':
      exits['east'] = self.room_id + 1

    if path_from == 'north':
      exits['south'] = self.room_id - 100

    if path_from == 'east':
      exits['west'] = self.room_id - 1



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

