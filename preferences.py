import subprocess
from PyQt4 import QtCore, QtGui
from ui_preferences import Ui_PreferencesDialog

class PreferencesDialog(QtGui.QDialog, Ui_PreferencesDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.setupUi(self)
        
        self.connect(self.selectButton, QtCore.SIGNAL('clicked()'), self.selectButtonClicked)
        self.connect(self.acceptButton, QtCore.SIGNAL('clicked()'), self.acceptButtonClicked)
        self.connect(self.cancelButton, QtCore.SIGNAL('clicked()'), self.cancelButtonClicked)
        self.connect(self.hackEntry, QtCore.SIGNAL('textChanged(QString)'), self.checkHack )

        self.initPreferences()

    def initPreferences(self):
        self.preferences = QtCore.QSettings('preferences.cfg', QtCore.QSettings.IniFormat)
        self.preferences.setIniCodec('UTF-8')
        self.hackEntry.setText(self.preferences.value('irivertool').toString())
    
    def checkHack(self):
        hackPath = self.hackEntry.text()
        cmd = ['python', hackPath, '-v']
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
        if result.startswith('irivertool'):
            self.versionLabel.setText(result[:-1])
        else:
            self.versionLabel.setText('ERROR')
    
    def selectButtonClicked(self):
        selectDialog = QtGui.QFileDialog()
        hackPath = selectDialog.getOpenFileName(self, 'Select irivertool...', '')
        self.hackEntry.setText(hackPath)
        self.checkHack()
                                                    
    def acceptButtonClicked(self):
        if str(self.versionLabel.text()).startswith('irivertool'):
            self.preferences.setValue('irivertool', self.hackEntry.text())
        
        self.preferences.sync()
        self.close()
    
    def cancelButtonClicked(self):
        self.close()