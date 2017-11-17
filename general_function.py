import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from log_collection import Ui_myLogCollection
from am import ApplianceManager
from time import sleep

#This class defines functions needed for widgets
class GeneralFunctions(Ui_myLogCollection):
    ipfilename = "IPAddress.txt"
    username = "Admin"
    password = "Admin1!"
    def __init__(self, dialog):
        Ui_myLogCollection.__init__(self)
        self.setupUi(dialog)
        self.showBtn.clicked.connect(self.addIPAddrToListinCmbBox)
        self.getlogsBtn.clicked.connect(lambda: self.getLogsFromDevice(self.listIpAddrs))

    #This function reads IPAddress.tt file and displays in list view
    def addIPAddrToListinCmbBox(self):
        fh = open(self.ipfilename, "r")
        lines = fh.readlines()
        for line in lines:
            line = line.rstrip()
            self.listIpAddrs.addItem(line)

    #gets logs a=for selected ips
    def getLogsFromDevice(self, listwidget):
        selectedItems = self.listIpAddrs.selectedItems()
        sleep(2)
        while self.listIpAddrs.count() > 0:
            self.listIpAddrs.takeItem(0)

        for txt in selectedItems:
            txt1 = txt.text().rstrip()
            print("IP Address: " + txt1)
            am = ApplianceManager(txt1,self.username,self.password)
            file_name = am.get_log_files()
            self.listIpAddrs.addItem(file_name)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    general_function = GeneralFunctions(dialog)
    dialog.show()
    sys.exit(app.exec_())

