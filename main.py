from PyQt5.QtWidgets import *
from VISTA.UI.ui_main import Ui_FrmMain
from VISTA.vSettings import Vsettings
from VISTA.vOpenFile import VopenFile

import sys

class Principal(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.ui = Ui_FrmMain()
        self.Vsetting = Vsettings()
        self.VopenFile = VopenFile()
        self.ui.setupUi(self)
        
        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        #Botones Generales Record
        self.ui.btnSettings.clicked.connect(self.Vsetting.mostrar)
        self.ui.btnRec.clicked.connect(self.alertar)
        self.ui.pushButton_4.clicked.connect(self.alertar)

        #Botones Generales Replay
        self.ui.btnPlay.clicked.connect(self.alertar)
        self.ui.btnPause.clicked.connect(self.alertar)
        self.ui.btnOpenFile.clicked.connect(self.alertar)

        #Botones REC Grafica 1

        self.ui.rBtnMapRec1.clicked.connect(self.alertar)
        self.ui.rBtn3DRec1.clicked.connect(self.alertar)
        self.ui.rBtnPDPRec1.clicked.connect(self.alertar)
        self.ui.rBtnPSPRec1.clicked.connect(self.alertar) 
        self.ui.radioButton_20.clicked.connect(self.alertar)
        self.ui.radioButton_24.clicked.connect(self.alertar)

        #Botones REC Grafica 2

        self.ui.rBtnMapRec2.clicked.connect(self.alertar)
        self.ui.rBtn3DRec2.clicked.connect(self.alertar)
        self.ui.rBtnPDPRec2.clicked.connect(self.alertar)
        self.ui.radioButton_29.clicked.connect(self.alertar) 
        self.ui.radioButton_26.clicked.connect(self.alertar)
        self.ui.radioButton_30.clicked.connect(self.alertar) 

        #Botones Replay Grafica 1

        self.ui.rBtnMapRep1.clicked.connect(self.alertar) 
        self.ui.rBtn3DRep1.clicked.connect(self.alertar)
        self.ui.rBtnPDPRep1.clicked.connect(self.alertar)
        self.ui.rBtnPSPRep1.clicked.connect(self.alertar)  
        self.ui.radioButton_14.clicked.connect(self.alertar)
        self.ui.radioButton_18.clicked.connect(self.alertar)

        #Botones Replay Grafica 2

        self.ui.rBtnMapRep2.clicked.connect(self.alertar)
        self.ui.rBtn3DRep2.clicked.connect(self.alertar)
        self.ui.rBtnPDPRep2.clicked.connect(self.alertar)
        self.ui.rBtnPSPRep2.clicked.connect(self.alertar)  
        self.ui.radioButton_10.clicked.connect(self.alertar)
        self.ui.radioButton_7.clicked.connect(self.alertar)

        self.show()

    def alertar(self):
        self.mensaje.setIcon(QMessageBox.Warning)
        self.mensaje.setText('Elemento en construccion')
        self.mensaje.exec_()

def main():
    app = QApplication(sys.argv)
    ventana = Principal()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()