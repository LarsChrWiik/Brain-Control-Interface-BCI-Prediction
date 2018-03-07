import sys
from PyQt4 import QtGui, QtCore

# main window inherit from main window
class Window(QtGui.QMainWindow):

    def __init__(self):
        # use super to return parent object
        super(Window, self).__init__()
        self.setGeometry(50, 50, 650, 450)
        self.setWindowTitle("Brain Scanner!")
        #self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        # below for file menu
        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        # below for status bar
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        
        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        # to add things to menu bar
        mainMenu = self.menuBar()
        # below name is 'File'
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        self.home()

    def home(self):
        btn1 = QtGui.QPushButton("Train", self)
        btn1.clicked.connect(self.file_open)
        btn1.resize(191,41)
        btn1.move(420,100)

        btn2 = QtGui.QPushButton("Predict", self)
        btn2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn2.resize(191,41)
        btn2.move(420,150)

        btn3 = QtGui.QPushButton("Load", self)
        btn3.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn3.resize(191,41)
        btn3.move(420,200)

        btn4 = QtGui.QPushButton("Save", self)
        btn4.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn4.resize(191,41)
        btn4.move(420,250)

        btn5 = QtGui.QPushButton("Get Statistics", self)
        btn5.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn5.resize(191,41)
        btn5.move(420,300)

        # below for progress bar
        #self.progress = QtGui.QProgressBar(self)
        #self.progress.setGeometry(200, 80, 250, 20)

        #self.btn = QtGui.QPushButton("Download",self)
        #self.btn.move(200,120)
        #self.btn.clicked.connect(self.download)

        label_1 = QtGui.QLabel("Product \n  Name", self)
        label_1.setFont(QtGui.QFont("Times", 40, QtGui.QFont.Bold))
        label_1.resize(321, 201)
        label_1.move(30,30)

        label_2 = QtGui.QLabel("Insert Product Logo Here", self)
        label_2.resize(200, 16)
        label_2.move(20, 310)

        label_3 = QtGui.QLabel("Version ......", self)
        label_3.resize(171, 16)
        label_3.move(20, 330)

        label_4 = QtGui.QLabel("(c) 2018 - ....", self)
        label_4.resize(171, 16)
        label_4.move(20, 350)

        label_5 = QtGui.QLabel("University of Essex", self)
        label_5.resize(171, 16)
        label_5.move(20, 370)

        label_6 = QtGui.QLabel("Essex, United Kingdom", self)
        label_6.resize(171, 16)
        label_6.move(20, 390)



        self.show()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        self.editor()

        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Are you sure you want to train?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            with file:
                text = file.read()
                self.textEdit.setText(text)
        else:
            pass

        #with file:
        #    text = file.read()
        #    self.textEdit.setText(text)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Are you sure you want to exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()