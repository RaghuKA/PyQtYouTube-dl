from __future__ import unicode_literals
import os
from PyQt5 import QtWidgets, QtCore, QtGui, uic
import sys
from PyQt5.QtCore import QObject, QProcess, QUrl, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QAction, QPushButton, QVBoxLayout, QMessageBox, QToolTip
import functools 
import operator
from shutil import which
try:
    import youtube_dl
    is_youtubedl_installed = True
except ImportError as e:
    is_youtubedl_installed = False
import importlib.util

glob_ui_file = "yTGui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(glob_ui_file)

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")
    
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
 
    def flush(self):
        pass  
    
class mywindow(QtWidgets.QMainWindow, Ui_MainWindow,Logger):
    def __init__(self, dloadIpFile="", dloadDestDir="",prc=""):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
      
        self.setupUi(self)
        self.comboBox_VideoQuality.addItem("First item") #add item
        self.comboBox_VideoQuality.addItem("Second item")
        self.comboBox_VideoQuality.addItem("Third item")
        
        self.dloadIpFile = dloadIpFile
        self.dloadDestDir = dloadDestDir
        self.prc=prc
                              
        self.BrowseInputButton.clicked.connect(self.openFileNameDialog)
        self.BrowseDloaddirButton.clicked.connect(self.openFileNameDialog2)
        self.DloadVidsButton.clicked.connect(self.DownloadVideos)
        
        self.actionAbout.triggered.connect(self.openAction)
        
    def startProgress(self,prc):
        self.prc = 0
        for self.prc in range(0,101):
            self.prc += 0.0001
            self.progBar.setValue(self.prc)    
        
    def openAction(self):
        link = "https://github.com/RaghuKA/PyQtYoutube-dl"
        msg = "<a href='%s'>gitHub</a>" % link +"<br>RaghuKA"+"<br>arkumar38@outlook.com"
        QMessageBox.about(self, "PyQtYouTube-dl", msg)
                         
    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        self.FilePathField.setText (fileName)
        self.dloadIpFile = fileName
        self.Log.insertPlainText('Input file specified as '+ self.dloadIpFile +'\n')
           
    def openFileNameDialog2(self):
        DloadDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.DloadDirPath.setText (DloadDir)
        self.dloadDestDir = DloadDir
        self.Log.insertPlainText('Download destination directory chosen as '+ self.dloadDestDir +'\n')

    def DownloadVideos(self):
        if(is_youtubedl_installed == True):
            self.status_label.setText ("All okay! youtube-dl is installed")
            self.Log.insertPlainText('youtube-dl is installed check complete\n')
            if os.path.exists(self.dloadDestDir):
                os.chdir(self.dloadDestDir)
                with open (self.dloadIpFile, 'r') as fh:     #Take test input file as 'Download_inputs1.txt'
                    fh_list = fh.readlines ()
                    number_of_links = len(fh_list)
                    self.Log.insertPlainText('Number of total download links is '+ str(number_of_links) + '\n')
                                                       
                for i in range (len (fh_list)):
                    video_link = fh_list[i].split (',') [0].strip()
                    custom_name = fh_list[i].split (',') [1].strip()
                    self.Log.insertPlainText('Processing download link ' + str(i+1) +' of total '+ str(number_of_links) + '\n')   
                    ydl_opts = {
                        'outtmpl': custom_name,
                        'format': 'webm', 
                        'keepvideo': True,                   
                        'audioquality': '1',
                        'writedescription': True,
                    }
                    sys.stdout = Logger()
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_link])
                    
                    prc= float(100/number_of_links)
                    print(prc)
                    pc=0
                    for i in range(0,number_of_links):
                        pc=pc+prc
                        self.startProgress(pc)
                self.Log.insertPlainText('Download finished \n')
            else:
                print('The directory does not exist')
        else:
            self.status_label.setText ("The package youtube-dl is not installed. Install the package using pip install youtube_dl. Cannot download videos!")
          
if __name__ == "__main__":    
    app = QtWidgets.QApplication (sys.argv)
    window = mywindow ()
    window.show ()
    sys.exit (app.exec_())
        
            
