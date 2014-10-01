# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Thu Jan  5 22:41:49 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName(_fromUtf8("PreferencesDialog"))
        PreferencesDialog.resize(470, 279)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabInterface = QtGui.QWidget()
        self.tabInterface.setObjectName(_fromUtf8("tabInterface"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabInterface)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.langLabel = QtGui.QLabel(self.tabInterface)
        self.langLabel.setObjectName(_fromUtf8("langLabel"))
        self.verticalLayout.addWidget(self.langLabel)
        self.langComboBox = QtGui.QComboBox(self.tabInterface)
        self.langComboBox.setObjectName(_fromUtf8("langComboBox"))
        self.verticalLayout.addWidget(self.langComboBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tabInterface, _fromUtf8(""))
        self.tabSystem = QtGui.QWidget()
        self.tabSystem.setObjectName(_fromUtf8("tabSystem"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabSystem)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radioButton = QtGui.QRadioButton(self.tabSystem)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.tabSystem)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_4.addWidget(self.radioButton_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.hackLabel = QtGui.QLabel(self.tabSystem)
        self.hackLabel.setObjectName(_fromUtf8("hackLabel"))
        self.verticalLayout_3.addWidget(self.hackLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.hackEntry = QtGui.QLineEdit(self.tabSystem)
        self.hackEntry.setObjectName(_fromUtf8("hackEntry"))
        self.horizontalLayout_4.addWidget(self.hackEntry)
        self.selectButton = QtGui.QPushButton(self.tabSystem)
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.horizontalLayout_4.addWidget(self.selectButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.versionLabel = QtGui.QLabel(self.tabSystem)
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.verticalLayout_3.addWidget(self.versionLabel)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.checkBox = QtGui.QCheckBox(self.tabSystem)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_4.addWidget(self.checkBox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabSystem, _fromUtf8(""))
        self.tabOther = QtGui.QWidget()
        self.tabOther.setObjectName(_fromUtf8("tabOther"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tabOther)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget.addTab(self.tabOther, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cancelButton = QtGui.QPushButton(PreferencesDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.acceptButton = QtGui.QPushButton(PreferencesDialog)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.horizontalLayout_3.addWidget(self.acceptButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.langLabel.setText(QtGui.QApplication.translate("PreferencesDialog", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInterface), QtGui.QApplication.translate("PreferencesDialog", "Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("PreferencesDialog", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.hackLabel.setText(QtGui.QApplication.translate("PreferencesDialog", "Hack:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("PreferencesDialog", "version", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("PreferencesDialog", "Linux", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSystem), QtGui.QApplication.translate("PreferencesDialog", "System", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOther), QtGui.QApplication.translate("PreferencesDialog", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.acceptButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))

