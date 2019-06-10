import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MainGUI
import Download
import time

from PyQt5.QtCore import Qt, QThread, pyqtSignal

class MyThread(QThread):
    change_perc = pyqtSignal(int)
    change_lab = pyqtSignal(str)
    def run(self):
        Download.CreatePath()
        t = open("CardsDB.txt")
        ln = 0
        for ch in t:
            start = time.time()
            ln=ln+1

            ch = ch.rstrip('\n')
            if ch != "":
                size = Download.Download(ch+".jpg")

            end = time.time()
            elapsedtime = end - start

            linevar = 13636 - ln
            speed = 0
            if type(size) != type(None):
                try:
                    speed = ((int(size)/1024)/elapsedtime)
                except ZeroDivisionError:
                    pass
            percentage = 100 - round((linevar*50)/6815)
            if percentage > 99 and linevar !=0:
                    percentage = 99
            if ch != "":
                if speed == 0:
                    progr = "Skipping "+ch+".jpg"+"! Already Exists..."
                    print(progr)
                else:
                    progr = "Downloading "+ch+".jpg"+" @"+str(round(speed))+"kb/s "+str(linevar)+" cards left..."
                    print(progr)
                time.sleep(0.001)
                self.change_perc.emit(percentage)
                self.change_lab.emit(progr)
                #self.progressBar.setValue(percentage)
        print("Task Completed ! Check you pics folder.")
        t.close()

class MainUiClass(QtWidgets.QMainWindow, MainGUI.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

        DEFAULT_STYLE = r"""QProgressBar{border: 2px solid grey;border-radius: 5px;text-align: center}"""
        self.progressBar.setStyleSheet(DEFAULT_STYLE)

        self.downloadBtn.clicked.connect(self.startProgressBar)
        self.psBtn.clicked.connect(self.pauseProgram)
        
    
    def startProgressBar(self):
        self.downloadBtn.setEnabled(False)
        self.thread = MyThread()
        self.thread.change_perc.connect(self.setProgressVal)
        self.thread.change_lab.connect(self.setProgressLab)
        self.thread.start()
    
    def setProgressLab(self, st):
        self.progressLabel.setText(st)

    def setProgressVal(self, val):
        self.progressBar.setValue(val)

    def pauseProgram(self):
        PAUSE_STYLE = r"""QProgressBar{border: 2px solid grey;border-radius: 5px;text-align: center} QProgressBar::chunk {background-color: #ffdc00}"""
        self.progressBar.setStyleSheet(PAUSE_STYLE)
        self.progressLabel.setText("Cancelling...")
        time.sleep(2)
        QtGui.QGuiApplication.exit()
        

if __name__ == '__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()