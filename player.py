class Player(object):

  def __init__(self):
    self.name = self.get_name()
    self.stats = self.get_stats()

  def get_name(self):
    name = input("What are you called? ")
    return name

  def get_stats(self):
    points = 10
    stats = {
        'STR': 1,
        'DEX': 1,
        'CON': 1,
        'INT': 1,
        'WIL': 1,
        'CHA': 1
        }
    print("Your stats are currently %r" % stats)
    while points > 0:
      print("You have %s points remaining to spend" % points)
      spend = input("Assign a point to what stat? ")
      if spend in stats:
        stats = self.increase_stat(stats, spend)
        points -= 1
      else:
        print("Invalid stat %r selected, please try again" % spend)
      print("Your stats are currently %r" % stats)

    return stats

  def increase_stat(self, stats, stat):
    stats[stat] += 0.1

    current_rank = int(stats[stat])
    next_rank = current_rank + 1
    purchased = int((stats[stat] - current_rank) * 10)

    if purchased == next_rank:
      stats[stat] = int(stats[stat]) + 1

    return stats

