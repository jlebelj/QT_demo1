# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Pop_lst_e = QtWidgets.QListView(Dialog)
        self.Pop_lst_e.setGeometry(QtCore.QRect(50, 31, 301, 201))
        self.Pop_lst_e.setObjectName("Pop_lst_e")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
