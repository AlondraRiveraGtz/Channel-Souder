from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from VISTA.UI.ui_main import Ui_FrmMain
from VISTA.vSettings import Vsettings
from VISTA.vOpenFile import VopenFile
import pandas as pd
import folium # pip install folium
import matplotlib.pyplot as plt
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import sys
import io

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
        self.ui.pushButton_4.clicked.connect(self.saveFile)

        #Botones Generales Replay
        self.ui.btnPlay.clicked.connect(self.alertar)
        self.ui.btnPause.clicked.connect(self.alertar)
        self.ui.btnOpenFile.clicked.connect(self.getCSV)

        #Botones REC Grafica 1

        self.ui.rBtnMapRec1.clicked.connect(self.viewMap)
        self.ui.rBtn3DRec1.clicked.connect(self.alertar)
        self.ui.rBtnPDPRec1.clicked.connect(self.alertar)
        self.ui.rBtnPSPRec1.clicked.connect(self.alertar) 
        self.ui.radioButton_20.clicked.connect(self.alertar)
        self.ui.radioButton_24.clicked.connect(self.alertar)

        #Botones REC Grafica 2

        self.ui.rBtnMapRec2.clicked.connect(self.viewMap)
        self.ui.rBtn3DRec2.clicked.connect(self.alertar)
        self.ui.rBtnPDPRec2.clicked.connect(self.alertar)
        self.ui.radioButton_29.clicked.connect(self.alertar) 
        self.ui.radioButton_26.clicked.connect(self.alertar)
        self.ui.radioButton_30.clicked.connect(self.alertar) 

        #Botones Replay Grafica 1

        self.ui.rBtnMapRep1.clicked.connect(self.viewMap) 
        self.ui.rBtn3DRep1.clicked.connect(self.alertar)
        self.ui.rBtnPDPRep1.clicked.connect(self.alertar)
        self.ui.rBtnPSPRep1.clicked.connect(self.alertar)  
        self.ui.radioButton_14.clicked.connect(self.alertar)
        self.ui.radioButton_18.clicked.connect(self.alertar)

        #Botones Replay Grafica 2

        self.ui.rBtnMapRep2.clicked.connect(self.viewMap)
        self.ui.rBtn3DRep2.clicked.connect(self.alertar)
        self.ui.rBtnPDPRep2.clicked.connect(self.plot)
        self.ui.rBtnPSPRep2.clicked.connect(self.alertar)  
        self.ui.radioButton_10.clicked.connect(self.alertar)
        self.ui.radioButton_7.clicked.connect(self.alertar)

        self.show()

    def alertar(self):
        self.mensaje.setIcon(QMessageBox.Warning)
        self.mensaje.setText('Elemento en construccion')
        self.mensaje.exec_()

    def getCSV(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '')
        if filePath != "":
            print ("Dirección",filePath) 
            self.df = pd.read_csv(str(filePath))

    def plot(self):
        self.df.plot()
        print(self.df)
        plt.show()
        
    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
    
    def viewMap(self):
        coordinate = (20.628269,-103.284029)
        m = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=15,
        	location=coordinate
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)
        #switch(self.ui.)
        
        if self.ui.rBtnMapRec1.isChecked():
            self.ui.WRecG1.setHtml(data.getvalue().decode())
        if self.ui.rBtnMapRec2.isChecked():
            self.ui.WRecG2.setHtml(data.getvalue().decode())
        if self.ui.rBtnMapRep1.isChecked():
            self.ui.WRepG1.setHtml(data.getvalue().decode())
        if self.ui.rBtnMapRep2.isChecked():
            self.ui.WRepG2.setHtml(data.getvalue().decode())
        #self.addWidget(webView)

def main():
    app = QApplication(sys.argv)
    ventana = Principal()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()