from node import *

class Grid(object):
  def __init__(self, angle):
    self.angle = angle
    if angle == 60:
      self.nodes = self.nodes_60()
    elif angle == 90:
      self.nodes = self.nodes_90()
    else:
      raise "Angle not supported. Angle == {}".format(angle)
  
  def nodes_90(self):
    nodes = []
    for x in xrange(0, 7):
      for y in xrange(0, 7):
        nodes.append(Node((x, y)))
    return nodes

  def nodes_60(self):
    raise "Not implemented"
