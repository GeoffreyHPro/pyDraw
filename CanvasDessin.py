import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Trace import *

class CanvasDessin(QWidget):
    
    
    def __init__(self, parent = None) :
        super(QWidget,self).__init__()
        self.setMinimumSize(300,300)
        self.traces = []
        self.setMouseTracking(True)
        self.isPress=False
        self.position = 0

        self.couleur=QColor(0,0,0,255)
        self.epaisseur=1
        self.painter = []
             
    
    def mouseMoveEvent(self, event):
        if self.isPress==True:
          self.traces[self.position].addPoints(event.pos())
        self.update()
        

    def mousePressEvent(self, event):
        self.isPress=True
        self.depart=event.pos()
        self.traces.append(Trace(event.pos(),self.epaisseur,self.couleur))
        self.update()

       
    def mouseReleaseEvent(self, event):
        self.isPress=False
        self.position = self.position + 1
        self.update()



    def paintEvent(self, event):
        painter = QPainter(self)
        for i in range(0,len(self.traces)):
            self.painter.append(QPainterPath())
            points = self.traces[i].getPoints()     
            color = self.traces[i].getColor()
            epaisseur = self.traces[i].getWidth()
            self.painter[i].moveTo(points[0]) 

            for j in range(1,len(points)):
              self.painter[i].lineTo(points[j])
            pen = QPen()
            pen.setColor(color)
            pen.setWidth(epaisseur)
            painter.setPen(pen)
            painter.drawPath(self.painter[i])
        self.painter = []
        

    def changeCouleur(self,couleur):
        self.couleur = couleur
        
    def changeEpaisseur(self,epaisseur):
        self.epaisseur = epaisseur

    def effacer(self):
        self.position = 0
        self.traces = []
        self.painter = []