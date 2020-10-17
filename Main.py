from PyQt5.QtCore import QDir, Qt, QUrl,QRect

from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction,QScrollArea,QDesktopWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtGui,QtWidgets
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5 import QtCore, QtGui, QtWidgets




#_____________________________________________________________________________________________________           
class Anomaly2(QMainWindow):

    def __init__(self, parent=None):
        super(Anomaly1, self).__init__(parent)
        self.setStyleSheet("""QWidget {
                background: rgb(255, 255, 255);
                background: #FAFAFA;
                background: #F2F2F2;
            }
        """)

        self.setWindowTitle("Accueil") 
        self.controle = QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('./icon/acceuil.png'))

        self.l=QLabel(self)
        pix=QPixmap("./icon/anomly2.png")
        self.l.setPixmap(pix)
        self.l.setAlignment(Qt.AlignCenter)
        self.l.setGeometry(0,0,1500, 900)
        

        self.labelTitre=QLabel(self)
        self.labelTitre.setGeometry(480,150,100, 100)
        self.labelTitre.setFixedSize(900,100)
        self.labelTitre.setText("Détection d'anomalies")


        self.labelTitre.setStyleSheet(''' 
  QLabel      {	 color: #3D3E3E; font-family: 'Raleway',sans-serif;
   font-size: 48px; font-weight: 500; 
   line-height: 72px; margin: 0 0 24px; 
  text-align: center; text-transform: uppercase; 

}''')
        self.labelTitre.setStyleSheet(''' 
  QLabel      {	 color: #3D3E3E; 
   font-size: 48px; font-weight: 500; 

}''')
        


        """
        self.lancer = QPushButton('Lancer la détection', self)
        self.lancer.setEnabled(False)
        #self.lancer.clicked.connect(self.lancerDetection)
        self.controle.addWidget(self.lancer)

        widCentre=QWidget(self)
        widCentre.setGeometry(0,0,1500, 900)
        #widCentre.setLayout(self.controle)
        self.l=QLabel(widCentre)
        pix=QPixmap("anomly2.png")
        self.l.setPixmap(pix)
        self.l.setAlignment(Qt.AlignCenter)
        """

        self.layoutBoutton=QHBoxLayout(self)
        self.setGeometry(0, 0, 1500, 900)
        #qtRectangle = self.frameGeometry()
        #centerPoint = QDesktopWidget().availableGeometry().center()
        #qtRectangle.moveCenter(centerPoint)
        #self.move(qtRectangle.topLeft())

        width = QDesktopWidget().screenGeometry().width()
        height = QDesktopWidget().screenGeometry().height()
        x=(width - self.width()) / 2.0;
        y=(height - self.height()) / 2.0;
        self.setGeometry(x,y,self.width(),self.height())
        #screenGeometry.width()

        
        self.b1=QPushButton(self)
        self.b1.setIcon(QIcon("t.png"))
        self.b1.setFixedSize(290,70)
        self.b1.setText("Traitement général")
        self.b1.setGeometry(990,700,100,200)
        self.b1.clicked.connect(self.openGeneral)


        self.b1.setStyleSheet(''' 
  QPushButton      {	
font-size:20px;
color:white;
background:#2196F3;
padding:20px;
border-radius:1px;
}
QPushButton:hover{
font-size:20px;
color:black;
background:#6eb9f7
;
padding:20px;
border-radius:1px;

}''')
        

        self.b2=QPushButton(self)
        self.b2.setIcon(QIcon("t.png"))
        self.b2.setFixedSize(290,70)
        self.b2.setText("Traitement de rail ")
        self.b2.setGeometry(200,700,100,200)
        self.b2.clicked.connect(self.openRail)


        self.b2.setStyleSheet(''' 
  QPushButton      {	
font-size:20px;
color:white;
background:#2196F3;
padding:20px;
border-radius:1px;
}
QPushButton:hover{
font-size:20px;
color:black;
background:#6eb9f7
;
padding:20px;
border-radius:1px;

}''')

        self.layoutBoutton.addWidget(self.b1)
        self.layoutBoutton.addWidget(self.b2)
        

    def openRail(self):
        from traitementRail import Rail

        self.window=QtWidgets.QMainWindow()
        self.ui=Rail()
        #self.ui.setupUi(self.window)
        self.hide()
        #MainWindow.hide()
        self.ui.setFixedSize(1500, 900)
        self.ui.show()

    def openGeneral(self):
        
        from traitementGeneral import General

        self.window=QtWidgets.QMainWindow()
        self.ui=General()
        self.hide()
        self.ui.setFixedSize(1500, 900)
        self.ui.show()

    





        

if __name__ == '__main__':
    k=1
    app = QApplication(sys.argv)

    player = Anomaly2()
    
    player.setFixedSize(1500, 900)
    player.show()
    sys.exit(app.exec_())
        
