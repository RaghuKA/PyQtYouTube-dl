from __future__ import unicode_literals
import youtube_dl
import os
from PyQt5 import QtWidgets, QtCore, QtGui, uic
import sys
from PyQt5.QtCore import QUrl,QObject,pyqtSlot 
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout 
import functools 
import operator

glob_ui_file = "yTGui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(glob_ui_file)

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, dloadIpFile="", dloadDestDir=""):   
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.comboBox_VideoQuality.addItem("First item") #add item
        self.comboBox_VideoQuality.addItem("Second item")
        self.dloadIpFile = dloadIpFile
        self.dloadDestDir = dloadDestDir
        
        self.BrowseInputButton.clicked.connect(self.openFileNameDialog)
        self.BrowseDloaddirButton.clicked.connect(self.openFileNameDialog2)
        self.DloadVidsButton.clicked.connect(self.DownloadVideos)

    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        print(fileName)
        self.FilePathField.setText (fileName)
        self.dloadIpFile = fileName
     
    def openFileNameDialog2(self):
        DloadDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        print(DloadDir)
        self.DloadDirPath.setText (DloadDir)
        self.dloadDestDir = DloadDir
 
    def DownloadVideos(self):
        with open(self.dloadIpFile) as f:
            my_list = list(f)
        print(my_list)
        ydl_opts = {}
       
        os.chdir(self.dloadDestDir)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(my_list)        

if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    window = mywindow ()
    window.show ()
    sys.exit (app.exec_())