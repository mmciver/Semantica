class Player(object):

  def __init__(self):
    self.name = self.get_name()
    self.experience = 12.3
    self.inventory = {}
    self.stats = self.get_stats()
    self.skills = self.get_skills()
    self.stat_points = 10
    self.skill_points = 10
    self.spend_stat_points()

  def get_name(self):
    name = input("What are you called? ")
    return name

  def get_stats(self):
    return {
        'STR': 1,
        'DEX': 1,
        'CON': 1,
        'INT': 1,
        'WIL': 1,
        'CHA': 1
        }

  def get_skills(self):
    return {
        'Inspection': 1
        }

  def spend_stat_points(self):
    self.print_stats()
    while self.stat_points > 0:
      spend = input("Assign a point to what stat? ").upper()
      if spend in self.stats:
        if int(self.stats[spend]) >= 5:
          print("%s is at maximum, you may not raise it any further" % spend)
        else:
          self.increase_stat(spend)
          self.stat_points -= 1
      else:
        print("Invalid stat %r selected, please try again" % spend)
      self.print_stats()

  def increase_stat(self, stat):
    self.stats[stat] += 0.1

    current_rank = int(self.stats[stat])
    next_rank = current_rank + 1
    purchased = int((self.stats[stat] - current_rank) * 10)

    if purchased == next_rank:
      self.stats[stat] = int(self.stats[stat]) + 1

  def print_stats(self):
    print("\nYour current stats are:")
    for s in ['STR', 'DEX', 'CON', 'INT', 'WIL', 'CHA']:
      print("%s: %s (%s of %s to level)" % (s, int(self.stats[s]), int(round((self.stats[s] - int(self.stats[s])) * 10, 0)), int(self.stats[s]) + 1))
    print("You have %s stat points to spend" % self.stat_points)

  def print_experience(self):
    print("\nYou have %s experience points" % int(self.experience))

  def spend_experience(self):
    prompt = "\n Spend options:\n  Stat Point (stat), 5 experience for 1 point\n  Skill Point (skill), 2 experience for 1 point\n  or quit to exit spending\n  > "
    self.print_experience()

    spend = input(prompt)
    while spend != "quit":
      if spend == "stat":
        if self.experience > 5:
          self.stat_points += 1
          self.experience -= 5
        else:
          print("You don't have enough experience to buy a Stat Point")

      elif spend == "skill":
        if self.experience > 2:
          self.skill_points += 1
          self.experience -= 2
        else:
          print("You don't have enough experience to buy a Skill Point")

      elif spend == "quit":
        return self.experience

      else:
        print("You have not provided a valid purchase request (stat, skill)")
      self.print_experience()
      spend = input(prompt)

