import sys
from CanvasDessin import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Dessin(QMainWindow):
    def __init__(self, parent = None) :
        super(QMainWindow,self).__init__()
        
        self.cvsDessin=CanvasDessin()
        self.setCentralWidget(self.cvsDessin)
        menu = self.menuBar()
        fileMenu = menu.addMenu("Colors")

        changeCouleur = QAction ("Change color ...", self)
        changeCouleur.setToolTip("Change the color")
        changeCouleur.triggered.connect(self.chgeCouleur)
        fileMenu.addAction(changeCouleur)

        self.changeEpaisseur=QSlider(Qt.Horizontal)
        self.changeEpaisseur.setMinimum(0)
        self.changeEpaisseur.setMaximum(40)
        self.changeEpaisseur.valueChanged.connect(self.valueChange)

        self.effaceDessin = QPushButton("Bouton qui efface")
        self.effaceDessin.clicked.connect(self.Erase)


        toolBar = QToolBar("File")
        self.addToolBar(toolBar)
        toolBar.addAction(changeCouleur)
        toolBar.addWidget(self.effaceDessin)
        toolBar.addWidget(self.changeEpaisseur)

    def chgeCouleur(self):
        color=QColorDialog()
        res=color.getColor()
        self.cvsDessin.changeCouleur(res)
        
    def chgeEpaisseur(self):
        self.epaisseur=self.value()
        self.cvsDessin.changeEpaisseur(epaisseur)

        

    def valueChange(self):
       size = self.changeEpaisseur.value()
       self.cvsDessin.changeEpaisseur(size)


    def Erase(self):
        print("efface le dessin")
        self.cvsDessin.effacer()



def main(args):
  app=QApplication(args)
  main =Dessin()
  main.show()
  sys.exit(app.exec_())
    
if __name__ == "__main__":
  main(sys.argv)