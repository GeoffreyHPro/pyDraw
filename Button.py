from ButtonModel import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CanvasButton(QWidget) :
    defaultCol=QColor(Qt.lightGray)
    
    hoverCol=QColor(80, 137, 162)
    pressCol=QColor(83, 170, 207)

        
    def __init__(self, parent = None) :
        super(CanvasButton,self).__init__()
        self.bbox = QRect(10,10,100,80)
        self.setMouseTracking(True)
        
        self.cursorOver=False
        self.isPress=False
        
        self.b=ButtonModel()
        
        
    def mouseMoveEvent(self, event):
#        print("testMove")
        
        if self.cursorOnEllipse(event.pos()):
            cursorOver=True
            self.b.Enter(self.b.state)
            
        else:
            cursorOver=False
            self.b.Leave(self.b.state)
        self.update()
#        print(cursorOver)
#        print(self.b.state)
        
    def mousePressEvent(self, event):
        self.isPress=True
#        print("testPress")
        self.b.Press(self.b.state)
        self.update()
#       print(self.b.state)
       
    def mouseReleaseEvent(self, event):
#        print("testRelease")
        self.isPress=False    
        self.b.Release(self.b.state)
        self.update()
#        print(self.b.state)
    
    def paintEvent(self,event):
        painter=QPainter(self)
        if self.b.state==1:
            painter.setBrush(CanvasButton.defaultCol)
        elif self.b.state==3:
            painter.setBrush(CanvasButton.pressCol)
        elif self.b.state==2:
            painter.setBrush(CanvasButton.hoverCol)
            
        painter.drawEllipse(self.bbox)
        
        
    def cursorOnEllipse(self, point):
        ellipse=QRegion(self.bbox,QRegion.Ellipse)
        return ellipse.contains(point)
            


def main(args):
    app=QApplication(args)
    main=QMainWindow()
    button = CanvasButton()
    main.setCentralWidget(button)
    button.show()
    main.show()
    sys.exit(app.exec_())
        
    
if __name__ == "__main__":
    main(sys.argv)