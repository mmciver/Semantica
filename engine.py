import geography
import player

class Engine(object):

  def __init__(self):
    self.player = player.Player()
    self.map_matrix = geography.Geography()
    self.current_room = self.map_matrix.geo['00000000']
    self.commands = self.build_command_list()
    self.command_loop()

  def command_loop(self):
    command = ""
    while command != "quit":
      print(self.current_room.display())
      command = input("\n> ").lower()
      self.process_command()
      #self.take_action(command)
    exit()

  def take_action(self, action):
    if action in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
      self.move(action)

    elif action == 'search':
      pass

    elif action in ['i', 'inv', 'inventory']:
      print("You currently have these items:")
      for i in self.player.inventory.keys():
        print(i)

    elif action == 'stats':
      self.player.print_stats()
      self.player.print_experience()

    elif action == 'xp':
      self.player.print_experience()

    elif action == 'spend xp':
      self.player.spend_experience()

    elif action == 'spend stat':
      self.player.spend_stat_points()

    elif action == 'spend skill':
      self.player.spend_skill_points()

    elif action.startswith("get"):
      pass

    elif action.startswith("drop"):
      pass

    elif action.startswith("talk"):
      pass

    elif action.startswith("search"):
      pass

    elif action.startswith("look"):
      pass

    else:
      print("Invalid command, please try again.")


  def process_command(self):
    if self.command in self.commands:
      pass

  def build_command_list(self):
    return {
        'n': self.map_matrix.move('north'),
        'north': self.map_matrix.move('north'),
        'e': self.map_matrix.move('east'),
        'east': self.map_matrix.move('east'),
        'w': self.map_matrix.move('west'),
        'west': self.map_matrix.move('west'),
        's': self.map_matrix.move('south'),
        'south': self.map_matrix.move('south'),
        'l': print(self.current_room.display()),
        'look': print(self.current_room.display()),
        'stats': '',

      }

