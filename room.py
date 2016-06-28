from random import randint
import random

class Room(object):

  def __init__(self, room_id, type_of, belongs_to):
    self.room_id = room_id
    self.room_type = type_of
    self.room_parent = belongs_to
    self.name = self.get_name()
    self.description = self.get_description()
    self.creature = self.get_creature()
    self.exits = {}

  def display(self):
    print("\n\n--------------")
    print(self.room_id)
    print(self.description)
    print(self.creature)
    print(self.display_exits())
    return 1

  def get_id(self):
    return self.room_id

  def get_type(self):
    return self.room_type

  def get_parent(self):
    return self.room_parent

  def get_description(self):
    return self.parent

  def get_name(self):
    return self.get_parent()

  def add_exit(self, room_id, room_name):
    self.exits[room_id] = room_name
    pass



  def display_exits(self):
    for e in self.exits:
      print("")

  def get_exits(self):
    return self.exits

