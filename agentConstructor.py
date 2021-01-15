import numpy as np
import random
import time

class Agent():
  def __init__(self, id, Params):
    self.time = 0
    self.id = id
    self.delta = 1 / Params.natural_frequency
    self.time_cur = random.uniform(0, self.delta) # random time initialization
    self.phi = self.time_cur / self.delta  # the phase [0 to 1]
    self.timestep = 1 /Params.fps # size of step in time


  def process_flash(self):
    """
    processes incoming flash
    """

    raise NotImplementedError

  def check_time(self):
      """
      updates time, and checks if phase at end of cycle time
      """

      raise NotImplementedError
