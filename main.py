import numpy as np
import time
import agentConstructor
import plotly.graph_objects as go


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

# # NEW for plotting: x-axis
plot_time_stamp = [] # list containing the x-axis of the plot (time)
counter = 0

while running:
  
  last_frame_time = StepTime(last_frame_time)  # makes loop controllable in realtime

  # TODO: increase each agent's phase and SendFlash if phase >= 1

  # TODO: send agent flashes to connected neighbors

  # TODO: generate new graph for random connectivity every 10 sec
  
  
  # # NEW PLOT DATA
  
  # TODO: insert this line: for each agent that fired, append the current timestamp with this line
  plot_time_stamp.append(counter / Params.fps)

  
  # plot_agent is a list containing all the agents that fired this iteration
  if (counter % 500 == 0 and counter > 0 ):
    fig = go.Figure(data=go.Scatter(x=plot_time_stamp, y=plot_agent, mode='markers',
                                    marker=dict(size=4.5, color="Blue", opacity=0.6)))
    fig.show()

  counter += 1
