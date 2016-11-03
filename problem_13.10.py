#!/usr/bin/env python

from pythagorea import *

grid = Grid(90)

node0 = Node((0, 0))

for node1 in grid.nodes:
  for node2 in grid.nodes:
    if node0 < node1 and node1 < node2:
      sides = sorted([
        node0.distance(node1),
        node0.distance(node2),
        node2.distance(node1),
      ])
      
      if sympy.sqrt(34) not in sides:
        continue
      
      if sides[0] != sides[1] and sides[1] != sides[2]:
        continue

      print node0, node1, node2, sides
