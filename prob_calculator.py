import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    contents = []
    for key, value in kwargs.items():
      for i in range(value):
        contents.append(key)
    self.contents = contents

  def draw(self, num_balls_drawn):
    if num_balls_drawn >= len(self.contents):
      return self.contents
    else:
      balls_drawn = []
      self.contents
      for i in range(num_balls_drawn):
        balls_drawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
      return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_success = 0
  succed = 0
  for i in range(0,num_experiments):
    hat_copy = copy.deepcopy(hat)
    pop_ball = hat_copy.draw(num_balls_drawn)
    pop_ball_dict = {}
    for ball in pop_ball:
      try:
        pop_ball_dict[ball] += 1
      except:
        pop_ball_dict.update({ball:1})
      
    
    try:
      for key, value in expected_balls.items():
        if pop_ball_dict[key] >= value:
          succed = 1
        else:
          succed = 0
          break
    except:
      succed = 0
      pass
    num_success += succed

  return num_success/num_experiments
