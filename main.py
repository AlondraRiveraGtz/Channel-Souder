from PyQt5.QtWidgets import *
from VISTA.UI.ui_main import Ui_FrmMain
from VISTA.vSettings import Vsettings
from VISTA.vOpenFile import VopenFile

import sys

class Principal(QDialog):

    def __init__(self):
        super(Principal,self).__init__()
        self.principal = Ui_FrmMain()
        self.principal.setupUi(self)
        self.Vsetting = Vsettings()
        self.VopenFile = VopenFile()

        self.mensaje = QMessageBox(self)
        self.mensaje.setWindowTitle('Mensaje')

        #Botones Generales Record
        self.principal.btnSettings.clicked.connect(self.Vsetting.mostrar)
        self.principal.btnRec.clicked.connect(self.alertar)
        self.principal.pushButton_4.clicked.connect(self.alertar)

        #Botones Generales Replay
        self.principal.btnPlay.clicked.connect(self.alertar)
        self.principal.btnPause.clicked.connect(self.alertar)
        self.principal.btnOpenFile.clicked.connect(self.alertar)

        #Botones REC Grafica 1

        self.principal.rBtnMapRec1.clicked.connect(self.alertar)
        self.principal.rBtn3DRec1.clicked.connect(self.alertar)
        self.principal.rBtnPDPRec1.clicked.connect(self.alertar)
        self.principal.rBtnPSPRec1.clicked.connect(self.alertar) 
        self.principal.radioButton_20.clicked.connect(self.alertar)
        self.principal.radioButton_24.clicked.connect(self.alertar)

        #Botones REC Grafica 2

        self.principal.rBtnMapRec2.clicked.connect(self.alertar)
        self.principal.rBtn3DRec2.clicked.connect(self.alertar)
        self.principal.rBtnPDPRec2.clicked.connect(self.alertar)
        self.principal.radioButton_29.clicked.connect(self.alertar) 
        self.principal.radioButton_26.clicked.connect(self.alertar)
        self.principal.radioButton_30.clicked.connect(self.alertar) 

        #Botones Replay Grafica 1

        self.principal.rBtnMapRep1.clicked.connect(self.alertar) 
        self.principal.rBtn3DRep1.clicked.connect(self.alertar)
        self.principal.rBtnPDPRep1.clicked.connect(self.alertar)
        self.principal.rBtnPSPRep1.clicked.connect(self.alertar)  
        self.principal.radioButton_14.clicked.connect(self.alertar)
        self.principal.radioButton_18.clicked.connect(self.alertar)

        #Botones Replay Grafica 2

        self.principal.rBtnMapRep2.clicked.connect(self.alertar)
        self.principal.rBtn3DRep2.clicked.connect(self.alertar)
        self.principal.rBtnPDPRep2.clicked.connect(self.alertar)
        self.principal.rBtnPSPRep2.clicked.connect(self.alertar)  
        self.principal.radioButton_10.clicked.connect(self.alertar)
        self.principal.radioButton_7.clicked.connect(self.alertar)

    def alertar(self):
        self.mensaje.setIcon(QMessageBox.Warning)
        self.mensaje.setText('Elemento en construccion')
        self.mensaje.exec_()

if __name__ == "__main__": #Condicional que comprueba si ha sido ejecutado
    app = QApplication(sys.argv) #crea un objeto de aplicación (Argumentos de sys)
    ui = Principal()
    ui.show() #Método que muestra la ventana
    sys.exit(app.exec_()) #Inicia el ciclo de eventos y bloquea hasta que se cierre la aplicación