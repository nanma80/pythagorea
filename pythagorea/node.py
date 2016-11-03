import sympy

class Node():
  def __init__(self, coordinates):
    self.coordinates = coordinates
    self.x = self.coordinates[0]
    self.y = self.coordinates[1]

  def __str__(self):
    return "Node({})".format(self.coordinates)

  def __repr__(self):
    return self.__str__()

  def __cmp__(self, other):
    return cmp(self.coordinates, other.coordinates)

  def distance(self, other):
    return sympy.sqrt(self.square_distance(other))

  def square_distance(self, other):
    sq_distance = 0
    for coordinate_index in xrange(0, len(self.coordinates)):
      sq_distance += (self.coordinates[coordinate_index] - other.coordinates[coordinate_index]) ** 2
    return sq_distance
