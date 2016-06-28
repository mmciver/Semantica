from random import randint
import random

class Room(object):

  def __init__(self, room_id, type_of, belongs_to):
    self.room_id = room_id
    self.room_type = type_of
    self.room_parent = belongs_to
    self.name = belongs_to
    self.description = self.get_description()
    self.exits = {}

  def display(self):
    print(self.room_id)
    print(self.name)
    for e in sorted(self.exits, key=self.exits.get):
      print(self.exits[e] )

  def get_id(self):
    return self.room_id

  def get_type(self):
    return self.room_type

  def get_parent(self):
    return self.room_parent

  def get_description(self):
    return self.room_parent

  def get_name(self):
    return self.get_parent()

  def add_exit(self, room_id, direction, room_name):
    self.exits[room_id] = "%s: %s" % (direction, room_name)
    pass

  def get_exits(self):
    return self.exits

