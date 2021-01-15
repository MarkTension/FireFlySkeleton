import numpy as np
import time
import agentConstructor

"""
This is a simulation for firefly synchronisation
Ermentraut algorithm and general algorothm are largely based on Firefly-inspired Heartbeat Synchronization in Overlay Networks, 
http://www.cs.unibo.it/babaoglu/courses/cas06-07/papers/pdf/fireflies.pdf . 
Adapted for discrete time simulation

"""


class Params:
  """
  parameters for simulation
  """
  fps = 60  # frames per second (simulation speed)
  num_agents = 200  # 800 works well
  natural_frequency = 1  # natural frequency of an agent
  num_neighbors = 30  # how many neighbors for each agent # 30 often converges
  epsilon = 0.02

# TODO: generate adjacency matrix / graph for agent connectivity

# initialize agents with ID and simulation parameters
agents = []
for i in range(Params.num_agents):
  agents.append(agentConstructor.Agent(i, Params))

# control timeflow in realtime
def StepTime(last_frame_time):
  currentTime = time.time()
  sleepTime = 1. / Params.fps - (currentTime - last_frame_time)
  if sleepTime > 0:
    time.sleep(sleepTime)
  else:
    last_frame_time = time.time()
  return last_frame_time


"""
environment
"""
running = True
last_frame_time = time.time()
# empty numpy array for environmental state
ids = np.arange(0, Params.num_agents)


while running:
  last_frame_time = StepTime(last_frame_time)  # makes loop controllable in realtime

  # TODO: increase each agent's phase and SendFlash if phase >= 1

  # TODO: send agent flashes to connected neighbors

  # TODO: generate new graph for random connectivity every 10 sec

