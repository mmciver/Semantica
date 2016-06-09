import geography
import player

class Engine(object):

  def __init__(self):
    self.geography = geography.Geography()
    self.player = player.Player()
    self.command_loop()

  def command_loop(self):
    command = ""
    while command != "quit":
      command = input("\n> ").lower()
      self.take_action(command)
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