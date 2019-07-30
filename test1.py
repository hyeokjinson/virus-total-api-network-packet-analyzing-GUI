# DemoForm2.py
#!/usr/bin/env python
# coding: utf-8 
#module sys
#from (built-in)
import os,subprocess
import sys
import ctypes
import time
import threading
import socket 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("DemoForm2.ui")[0]
subprocess.Popen('python connect.py')
subprocess.Popen('python VT_Domain_Scanner_py3.py')

       
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.viewer=QListWidget()
       

    def firstClick(self):
       
       r=open('log.txt','r')
       while True:
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))
        self.listWidget.addItem(r.read(1000))

        
        break
        
       
    def secondClick(self):
        
        
        
        self.label_2.setText("패킷을 읽고있습니다.")
        
        
    def thirdClick(self):
       
        t = open('results.csv', mode='rt', encoding='utf-8')
        self.label_3.setText(t.read())
        
        t.close()
    def fourClick(self):
        os.system("python bandwidthgraph.py")
    def resultClick(selif):
        os.system("python VT_Domain_Scanner_py3.py")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show() 
    app.exec_()