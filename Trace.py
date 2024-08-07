import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Trace:
  def __init__(self, point, width, color) :
    self.points = []
    self.width = width
    self.color = color
    self.points.append(point)
    
  def addPoints(self,point):
    self.points.append(point)

  def getPoints(self):
    return self.points

  def getColor(self):
    return self.color

  def getWidth(self):
    return self.width

if __name__ == "__main__":
  a = Trace((2,0),5,"rouge")
  a.addPoints((1,2))
  a.addPoints((2,5))
  a.addPoints((3,6))
  b = a.getPoints()

  for i in range(3):
    print(b[i][0],b[i][1],a.getColor())