from __future__ import unicode_literals
import youtube_dl
import os

from PyQt5 import QtWidgets, QtCore, QtGui, uic
#from PyQt5_learn_Pyuic5_Edit import Ui_MainWindow
import sys
import model
from PyQt5.QtCore import QUrl,QObject,pyqtSlot #, QStringList
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout #, QWidget
#from gi.overrides.Pango import Layout
import functools 
import operator


glob_ui_file = "yTGui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(glob_ui_file)

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, download_inputFile_location_string="", download_destination_folder=""):   
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.ui.comboBox_VideoQuality.addItem("First item") #add item
        self.ui.comboBox_VideoQuality.addItem("Second item")
        
        self.download_inputFile_location_string = download_inputFile_location_string
        self.download_destination_folder = download_destination_folder
        self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
     
        self.ui.pushButton_Browse_for_DownloadFolder.clicked.connect(self.openFileNameDialog2)
        self.ui.pushButton_DownloadVideos.clicked.connect(self.DownloadVideos)

    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        print(fileName)
        self.download_inputFile_location_string = fileName
     
    def openFileNameDialog2(self):
        DownloadFolderName = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory'))
        self.download_destination_folder = DownloadFolderName
 
    def DownloadVideos(self):
        with open(self.download_inputFile_location_string) as f:
            my_list = list(f)
        print(my_list)
        #ydl_opts = {}
        
        # ydl_opts = {
        # 'download_archive': 'YOUR_PATH_HERE',
        # 'format': 'bestaudio/best',
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192',
        #     }],
        # }
        ydl_opts = {
            'format': 'bestaudio/best',  # choice of quality
            'extractaudio': True,        # only keep the audio
            'format': "mkv",        # convert to mp3
            'outtmpl': '%(id)s',         # name the file the ID of the video
            'noplaylist': True,          # only download single song, not playlist
            #'listformats': True,         # print a list of the formats to stdout and exit
        }   
    # ydl_opts = {
    #     #'download_archive': 'self.download_destination_folder',
    #     'merge-output-format': 'mp4',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         #'audio-format': 'mp3',
    #         'preferredquality': '192',
    #         }],
    # }
        os.chdir(self.download_destination_folder)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(my_list)        


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())