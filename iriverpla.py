#!/usr/bin/env python

import os
import sys
import subprocess
from PyQt4 import QtCore, QtGui
from ui_iriverpla import Ui_MainWindow
import preferences

class IriverPLA_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)

        self.statusBar.showMessage('Select device.')

        self.connect(self.rootPathSelButton, QtCore.SIGNAL('clicked()'), self.rootPathSelClicked)
        self.connect(self.addButton, QtCore.SIGNAL('clicked()'), self.addClicked)
        self.connect(self.delButton, QtCore.SIGNAL('clicked()'), self.delClicked)
        self.connect(self.saveListButton, QtCore.SIGNAL('clicked()'), self.saveListClicked)
        self.connect(self.clearListButton, QtCore.SIGNAL('clicked()'), self.clearListClicked)
        self.connect(self.createButton, QtCore.SIGNAL('clicked()'), self.createClicked)
        self.connect(self.quitButton, QtCore.SIGNAL('clicked()'), self.quitClicked)

        self.connect(self.actionCreate_PLA, QtCore.SIGNAL('triggered()'), self.createClicked)
        self.connect(self.actionOpen_list, QtCore.SIGNAL('triggered()'), self.actionOpenListTriggered)
        self.connect(self.actionSave_list, QtCore.SIGNAL('triggered()'), self.saveListClicked)
        self.connect(self.actionClear_list, QtCore.SIGNAL('triggered()'), self.clearListClicked)
        self.connect(self.actionPreferences, QtCore.SIGNAL('triggered()'), self.actionPreferencesTriggered)
        self.connect(self.actionIriverPLA_Help, QtCore.SIGNAL('triggered()'), self.actionIriverPLAHelpTriggered)
        self.connect(self.actionAbout_iriverPLA, QtCore.SIGNAL('triggered()'), self.actionAboutIriverPLATriggered)
        self.connect(self.actionAbout_Qt, QtCore.SIGNAL('triggered()'), self.actionAboutQtTriggered)
        self.connect(self.actionExit, QtCore.SIGNAL('triggered()'), self.quitClicked)

        self.initPreferences()
        self.initRootTree()

    def initPreferences(self):
        self.preferences = QtCore.QSettings('preferences.cfg', QtCore.QSettings.IniFormat)
        self.preferences.setIniCodec('UTF-8')
        self.rootPath = self.preferences.value('root').toString()
        self.rootPathEntry.setText(self.rootPath)

    def initRootTree(self):
        self.treeFSM = QtGui.QFileSystemModel()
        self.treeMI = QtCore.QModelIndex()
        self.treeFSM.setRootPath(self.rootPath)
        self.treeMI = self.treeFSM.index(self.rootPath)

        self.musicTreeView.setModel(self.treeFSM)
        for i in range(1, 4):
            self.musicTreeView.hideColumn(i)
        self.musicTreeView.setRootIndex(self.treeMI)
        
        self.offList = []
        self.listModel = QtGui.QStringListModel()
        self.strList = QtCore.QStringList()
        self.listModel.setStringList(self.strList)
        self.musicListView.setModel(self.listModel)

    
    def rootPathSelClicked(self):
        rootPathDialog = QtGui.QFileDialog()

        self.rootPath = rootPathDialog.getExistingDirectory(self, 'Select directory...', '/', QtGui.QFileDialog.ShowDirsOnly)
        self.rootPathEntry.setText(self.rootPath)
        
        self.preferences.setValue('root', self.rootPath)
        self.preferences.sync()
        
        self.initRootTree()

    def addClicked(self):
        curInd = self.musicTreeView.currentIndex()
        path = self.treeFSM.filePath(curInd)        # Get file path QString
        path = path.toUtf8()                        # Convert to UTF-8
        path = str(path)                            # Convert to Python string
        path = path.decode('utf-8')                    # Decode from UTF-8
        name = self.treeFSM.fileName(curInd)
        name = name.toUtf8()
        name = str(name)
        name = name.decode('utf-8')
        if self.treeFSM.isDir(curInd):
            for root, subDirs, files in os.walk(path):
                for file in files:
                    if (file.find('.mp3')) != -1 or (file.find('.flac')) != -1:
                        track = os.path.join(root, file)
                        track = track.replace(self.rootPath, '\\')
                        track = track.replace('/', '\\')
                        track = track.replace('\\\\', '\\')
                        offset = len(track) - len(file) +1
                        self.strList.append(str(offset)+' | '+track)
                        self.listModel.setStringList(self.strList)
        elif path.find('.mp3') != -1:
            track = path.replace(self.rootPath, '\\')
            track = track.replace('/', '\\')
            track = track.replace('\\\\', '\\')
            offset = len(track) - len(name) +1
            self.strList.append(str(offset)+' | '+track)
            self.listModel.setStringList(self.strList)

    def delClicked(self):
        pass

    def saveListClicked(self):
        listDialog = QtGui.QFileDialog()
        listPath = listDialog.getSaveFileName(self, 'Save file...', '')
        f = open(listPath, 'w')
        curStrList = self.listModel.stringList()
        counter = 0
        for line in curStrList:
            counter += 1
            if counter == len(curStrList):
                f.write(line.toUtf8())
            else:
                f.write(line.toUtf8()+'\n')
        f.close()
    
    def clearListClicked(self):
        self.strList.clear()
        self.listModel.setStringList(self.strList)

    def createClicked(self):
        playlistName = self.playlistEntry.text()
        playlistName = playlistName.toUtf8()
        playlistName = str(playlistName)
        playlistName = playlistName.decode('utf-8')
        playlistPath = os.path.join(str(self.rootPath), 'Playlists')
        playlistTotal = os.path.join(playlistPath, playlistName)
        playlistTotal = os.path.normpath(playlistTotal)
#        self.playlistEntry.setText(playlistTotal)    
        
        tmpListPath = os.path.normpath(os.path.join(str(self.rootPath), 'list.tmp'))
        f = open(tmpListPath, 'w')
        curStrList = self.listModel.stringList()
        counter = 0
        for line in curStrList:
            counter += 1
            if counter == len(curStrList):
                f.write(line.toUtf8())
            else:
                f.write(line.toUtf8()+'\n')
        f.close()
                
#        cmd = ['python', '../hack-0.2.2a.py', '-l', tmpListPath, '-o', playlistTotal]
        irivertool = self.preferences.value('irivertool').toString()
        irivertool = str(irivertool)
        cmd = ['python', irivertool, '-l', tmpListPath, '-o', playlistTotal]
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
        result = str(result)
        result = result.decode('utf-8')
        self.statusBar.showMessage(result)
        QtGui.QMessageBox.information(self, 'Information', result)

    def quitClicked(self):
        QtGui.qApp.quit()


    def actionOpenListTriggered(self):
        openDialog = QtGui.QFileDialog()
        openPath = openDialog.getOpenFileName(self, 'Open file...', '')
        f = open(openPath, 'r')
        data = f.read()
        f.close()
        self.strList.append(unicode(data))
        self.listModel.setStringList(self.strList)
    
    def actionPreferencesTriggered(self):
        self.prefDialog = preferences.PreferencesDialog()
        self.prefDialog.setModal(True)
        self.prefDialog.show()
    
    def actionIriverPLAHelpTriggered(self):
        QtGui.QMessageBox.information(self, 'Help', 'To do...')
    
    def actionAboutIriverPLATriggered(self):
        QtGui.QMessageBox.information(self, 'About', 'To do...')
    
    def actionAboutQtTriggered(self):
        QtGui.qApp.aboutQt()


app_version = 'iriverPLA'# v0.2.1 for GNU/Linux'
app = QtGui.QApplication(sys.argv)
#app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
window = IriverPLA_Window()
window.setWindowTitle(app_version)
window.show()

sys.exit(app.exec_())
