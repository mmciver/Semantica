import geography
import player

class Engine(object):

  def __init__(self):
    #self.player = player.Player()
    self.map_matrix = geography.Geography()
    self.current_room = self.map_matrix.geo[95050]
    self.command_loop()

  def command_loop(self):
    command = ""
    while command != "quit":
      print(self.current_room.display())
      command = input("\n> ").lower()
      self.process_command(command)
      #self.take_action(command)
    exit()

  def process_command(self, command):
    if command in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
      if command == 'n':
        command = 'north'
      elif command == 'e':
        command = 'east'
      elif command == 's':
        command = 'south'
      elif command == 'w':
        command = 'west'
      self.map_matrix.move(command)
      self.current_room = self.map_matrix.get_current_room()

    elif command == 'search':
      pass

    elif command in ['i', 'inv', 'inventory']:
      print("You currently have these items:")
      for i in self.player.inventory.keys():
        print(i)

    elif command == 'stats':
      self.player.print_stats()
      self.player.print_experience()

    elif command == 'xp':
      self.player.print_experience()

    elif command == 'spend xp':
      self.player.spend_experience()

    elif command == 'spend stat':
      self.player.spend_stat_points()

    elif command == 'spend skill':
      self.player.spend_skill_points()

    elif command.startswith("get"):
      pass

    elif command.startswith("drop"):
      pass

    elif command.startswith("talk"):
      pass

    elif command.startswith("search"):
      pass

    elif command.startswith("look"):
      pass

    else:
      print("Invalid command, please try again.")


