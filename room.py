from random import randint

class Room(object):

  def __init__(self):
    self.description = self.get_description()
    self.creature = self.get_creature()
    self.exits = self.get_exits()
    self.walls = self.get_walls()

  def get_description(self):
    

  def get_exits(self):
    possible = [round(random.random()), round(random.random()), round(random.random()), round(random.random())]
    while sum(list(possible)) < 1:
      possible = [round(random.random()), round(random.random()), round(random.random()), round(random.random())]
    exits = {
        'N': possible[0],
        'S': possible[1],
        'E': possible[2],
        'W': possible[3]
        }
    return exits

  def get_walls(self):
    walls = {
        'N': 0,
        'S': 0,
        'E': 0,
        'W': 0
        }
    if self.exits['N'] == 0
      walls['N'] = 1
    if self.exits['S'] == 0
      walls['S'] = 1
    if self.exits['E'] == 0
      walls['E'] = 1
    if self.exits['W'] == 0
      walls['W'] = 1
    return walls

  def get_creature(self):
    moods = ['angry', 'sad', 'happy', 'disappointed', 'depressed']
    nouns = ['bear', 'lion', 'boy', 'girl', 'man', 'woman']
    return("There is a %s here that is very %s" % (random.choice(nouns), random.choice(moods)))
