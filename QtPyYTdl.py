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
        self.FilePathField.setText (fileName)
        self.dloadIpFile = fileName
           
    def openFileNameDialog2(self):
        DloadDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.DloadDirPath.setText (DloadDir)
        self.dloadDestDir = DloadDir
 
    def DownloadVideos(self):
        if os.path.isdir(self.dloadDestDir):
            os.chdir(self.dloadDestDir)
        else:
            print('The directory does not exist')

        with open (self.dloadIpFile, 'r') as fh:     #Take test input file as 'Download_inputs1.txt'
            fh_list = fh.readlines ()
        
        for i in range (len (fh_list)):
            video_link = fh_list[i].split (',') [0].strip()
            custom_name = fh_list[i].split (',') [1].strip()
                  
            ydl_opts = {
                'outtmpl': custom_name,
                'format': 'webm', 
                'keepvideo': True,                   
                'audioquality': '1',
                'writedescription': True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_link])
          
if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    window = mywindow ()
    window.show ()
    sys.exit (app.exec_())