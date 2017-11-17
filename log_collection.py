# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_collection.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myLogCollection(object):
    def setupUi(self, myLogCollection):
        myLogCollection.setObjectName("myLogCollection")
        myLogCollection.resize(520, 315)
        self.buttonBox = QtWidgets.QDialogButtonBox(myLogCollection)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.showBtn = QtWidgets.QPushButton(myLogCollection)
        self.showBtn.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.showBtn.setObjectName("showBtn")
        self.listIpAddrs = QtWidgets.QListWidget(myLogCollection)
        self.listIpAddrs.setGeometry(QtCore.QRect(130, 10, 371, 101))
        self.listIpAddrs.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listIpAddrs.setSelectionRectVisible(True)
        self.listIpAddrs.setObjectName("listIpAddrs")
        self.getlogsBtn = QtWidgets.QPushButton(myLogCollection)
        self.getlogsBtn.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.getlogsBtn.setObjectName("getlogsBtn")

        self.retranslateUi(myLogCollection)
        self.buttonBox.accepted.connect(myLogCollection.accept)
        self.buttonBox.rejected.connect(myLogCollection.reject)
        QtCore.QMetaObject.connectSlotsByName(myLogCollection)

    def retranslateUi(self, myLogCollection):
        _translate = QtCore.QCoreApplication.translate
        myLogCollection.setWindowTitle(_translate("myLogCollection", "Log Collection"))
        self.showBtn.setText(_translate("myLogCollection", "Show IPs"))
        self.getlogsBtn.setText(_translate("myLogCollection", "Get Logs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myLogCollection = QtWidgets.QDialog()
    ui = Ui_myLogCollection()
    ui.setupUi(myLogCollection)
    myLogCollection.show()
    sys.exit(app.exec_())

