import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor, QFont 
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog



from Wrapper import Wrapper
from Importer import Importer

wrapper = Wrapper()

# main window inherit from main window
class Window(QMainWindow):

    def __init__(self):
        # use super to return parent object
        super(Window, self).__init__()
        self.setGeometry(50, 50, 650, 450)
        self.setWindowTitle("Brain Scanner!")
        #self.setWindowIcon(QIcon('pythonlogo.png'))
        
        # below for file menu
        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        # below for status bar
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openFile = QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        
        saveFile = QAction("&Save File", self)
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
        btn1 = QPushButton("Train", self)
        btn1.clicked.connect(self.file_open)
        btn1.resize(191,41)
        btn1.move(420,100)

        btn2 = QPushButton("Predict", self)
        btn2.clicked.connect(self.close_application)
        btn2.resize(191,41)
        btn2.move(420,150)

        btn3 = QPushButton("Load", self)
        btn3.clicked.connect(self.close_application)
        btn3.resize(191,41)
        btn3.move(420,200)

        btn4 = QPushButton("Save", self)
        btn4.clicked.connect(self.close_application)
        btn4.resize(191,41)
        btn4.move(420,250)

        btn5 = QPushButton("Get Statistics", self)
        btn5.clicked.connect(self.close_application)
        btn5.resize(191,41)
        btn5.move(420,300)

        # below for progress bar
        #self.progress = QtGui.QProgressBar(self)
        #self.progress.setGeometry(200, 80, 250, 20)

        #self.btn = QtGui.QPushButton("Download",self)
        #self.btn.move(200,120)
        #self.btn.clicked.connect(self.download)

        label_1 = QLabel("Product \n  Name", self)
        label_1.setFont(QFont("Times", 40, QFont.Bold))
        label_1.resize(321, 201)
        label_1.move(30,30)

        label_2 = QLabel("Insert Product Logo Here", self)
        label_2.resize(200, 16)
        label_2.move(20, 310)

        label_3 = QLabel("Version ......", self)
        label_3.resize(171, 16)
        label_3.move(20, 330)

        label_4 = QLabel("(c) 2018 - ....", self)
        label_4.resize(171, 16)
        label_4.move(20, 350)

        label_5 = QLabel("University of Essex", self)
        label_5.resize(171, 16)
        label_5.move(20, 370)

        label_6 = QLabel("Essex, United Kingdom", self)
        label_6.resize(171, 16)
        label_6.move(20, 390)



        self.show()

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        #print(name)
        #file = open(name,'r')

        #self.editor()

        choice = QMessageBox.question(self, 'Extract!',
                                            "Are you sure you want to train?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print(name)
            lol = Importer.mat(name)
            print(lol)
            wrapper.train(lol)

        else: 
            pass
        
        print('Training completed')
        
        #    with file:
        #        text = file.read()
        #        self.textEdit.setText(text)
        #else:
        #    pass

        #with file:
        #    text = file.read()
        #    self.textEdit.setText(text)

    def file_save(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    #def editor(self):
    #    self.textEdit = QtGui.QTextEdit()
    #    self.setCentralWidget(self.textEdit)

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def close_application(self):
        choice = QMessageBox.question(self, 'Extract!',
                                            "Are you sure you want to exit?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()