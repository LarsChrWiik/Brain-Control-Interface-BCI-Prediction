import sys
import numpy as np
import pyqtgraph as pg

from PyQt5.QtCore import QCoreApplication,QThread
from PyQt5.QtGui import QIcon, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QVBoxLayout, QErrorMessage
from PyQt5.QtWidgets import QCalendarWidget, QColorDialog, QTextEdit, QFileDialog, QGraphicsView, QDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
from threading import Thread
from multiprocessing import Pool

from Wrapper import Wrapper
from Importer import Importer

# main window inherit from main window
class Window(QMainWindow):

    wrapper = Wrapper()

    def __init__(self):
        # use super to return parent object
        super(Window, self).__init__()
        self.setGeometry(50, 50, 650, 450)
        self.setWindowTitle("P300 Predictor")     # to change this file
        self.raw_signal = []


        # below for file menu
        File_Menu_Exit_Button = QAction("&Exit", self)
        File_Menu_Exit_Button.setShortcut("Ctrl+Q")
        # below for status bar
        File_Menu_Exit_Button.setStatusTip('Leave The App')
        File_Menu_Exit_Button.triggered.connect(self.close_application)


        File_Menu_Save_Button = QAction("&Save File", self)
        File_Menu_Save_Button.setShortcut("Ctrl+S")
        File_Menu_Save_Button.setStatusTip('Save File')
        #File_Menu_Save_Button.triggered.connect(self.file_save)

        # to add things to menu bar
        mainMenu = self.menuBar()
        # below name is 'File'
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(File_Menu_Save_Button)
        fileMenu.addAction(File_Menu_Exit_Button)
        self.home()

    def home(self):

        Function_Train_Button = QPushButton("Train", self)
        Function_Train_Button.clicked.connect(self.file_open)
        Function_Train_Button.resize(191,41)
        Function_Train_Button.move(420,100)

        Function_Predict_Button = QPushButton("Predict", self)
        Function_Predict_Button.clicked.connect(self.predict)
        Function_Predict_Button.resize(191,41)
        Function_Predict_Button.move(420,150)

        Function_Load_Button = QPushButton("Load", self)
        #Function_Load_Button.clicked.connect(self.close_application)
        Function_Load_Button.resize(191,41)
        Function_Load_Button.move(420,200)

        Function_Save_Button = QPushButton("Save", self)
        #Function_Save_Button.clicked.connect(self.close_application)
        Function_Save_Button.resize(191,41)
        Function_Save_Button.move(420,250)

        Function_Get_Statistics_Button= QPushButton("Get Statistics", self)
        Function_Get_Statistics_Button.clicked.connect(self.generate_graph)
        Function_Get_Statistics_Button.resize(191, 41)
        Function_Get_Statistics_Button.move(420, 300)

        label_1 = QLabel("P300 \nPredictor", self)
        label_1.setFont(QFont("Times", 40, QFont.Bold))
        label_1.resize(321, 201)
        label_1.move(30,30)

        label_3 = QLabel("Version 1.10", self)
        label_3.resize(171, 16)
        label_3.move(20, 330)

        label_4 = QLabel("(c) 2018", self)
        label_4.resize(171, 16)
        label_4.move(20, 350)

        label_5 = QLabel("University of Essex", self)
        label_5.resize(171, 16)
        label_5.move(20, 370)

        label_6 = QLabel("Essex, United Kingdom", self)
        label_6.resize(171, 16)
        label_6.move(20, 390)

        error_msg = QMessageBox()
        #error_msg.setIcon(QMessageBox.critical)
        error_msg.setWindowTitle("Error")
        error_msg.setDetailedText("")

        self.show()


    def worker(self,saved_file):
        """thread worker function"""
        self.wrapper.train(saved_file)
        return

    def file_open(self):
        # Let the user chose a file.
        # only allows mat files to be read in
        filename = QFileDialog.getOpenFileName(self, 'Open File', filter="*.mat")[0]

        if filename:

            # Make sure the user wants to use train.
            choice = QMessageBox.question(
              self,
               'Train',
               "Are you sure you want to train? If you click yes, the training might take long periods to train.",
               QMessageBox.Yes | QMessageBox.No
            )


            if choice == QMessageBox.Yes:
             # User wants to train.
                raw_data = Importer.mat(filename)

                self.wrapper.train(data_raw=raw_data, shrink_percent=0.75, verbose=True)

                # Statistics obtained from the data
                global raw_signal
                global filtered_signal
                global chunked_X
                global chunked_Y
                global accuracy
                raw_signal = self.wrapper.bciObject.preprocessor.preprocess_statistics.raw_signal
                filtered_signal = self.wrapper.bciObject.preprocessor.preprocess_statistics.filtered_signal
                chunked_X = self.wrapper.bciObject.preprocessor.preprocess_statistics.chunked_X
                chunked_Y = self.wrapper.bciObject.preprocessor.preprocess_statistics.chunked_Y
                accuracy = self.wrapper.bciObject.prediction_model.model_statistics.accuracy
                #print(accuracy)

                msg = QMessageBox(self)
                msg.resize(500, 400)
                msg.setText("The training accuracy is %.3f" % accuracy)
                msg.show()

            else:
                # User don't want to train.
                pass


    def predict(self):
        # Let the user chose a file.
        # only allows mat files to be read in
        filename = QFileDialog.getOpenFileName(self, 'Open File', filter="*.mat")[0]

        if filename:

            # Make sure the user wants to use train.
            choice = QMessageBox.question(
                 self,
                'Extract!',
                "Are you sure you want to run prediction? If you click yes, the prediction might take a long time to run",
                QMessageBox.Yes | QMessageBox.No
            )

            if choice == QMessageBox.Yes:
                # User wants to train.
                raw_data = Importer.mat(filename)
                raw_data = Importer.mat(filename)

                # Make data_raw smaller. (Should be removed in future versions).
                for row in raw_data:
                    raw_data[row] = raw_data[row][:1]

                prediction = self.wrapper.predict(raw_data, verbose=True)
                print(list(prediction))
            else:
                # User don't want to train.
                pass



    def generate_graph(self):
        # Check if variable is empty
        try:
            raw_signal
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            #msg.setInformativeText("No statistics found! Please run the training function button to generate statistics for the graph.")
            msg.setWindowTitle("Error")
        else:
            print("Generating Statistics Now")
            array_raw_signal = np.asarray(raw_signal)
            array_filtered_signal = np.asarray(filtered_signal)
            array_chunked_X = np.asarray(chunked_X)
            array_chunked_Y = np.asarray(chunked_Y)

            # plot for the 1st channel and 12th example only
            x1 = np.arange(array_raw_signal.shape[2])
            y1 = array_raw_signal[0][12]
            p1 = pg.plot(x1, y1, title='Raw Signal', labels={'left': ('Values'), 'bottom': ('Timesteps')},
                         enableMenu=True)
            p1.showGrid(x=True, y=True, alpha=0.3)
            p1.enableAutoScale()
            p1.showButtons()

            # plot for the 1st channel and 12th example only
            x2 = np.arange(array_filtered_signal.shape[2])
            y2 = array_filtered_signal[0][12]
            p2 = pg.plot(x2, y2, title='Filtered Signal', labels={'left': ('Values'), 'bottom': ('Timesteps')},
                         enableMenu=True)
            p2.showGrid(x=True, y=True, alpha=0.3)
            p2.enableAutoScale()
            p2.showButtons()

            x3 = np.arange(array_chunked_X.shape[2])
            y3 = array_chunked_X[0][12]
            p3 = pg.plot(x3, y3, title='Chunked_X', labels={'left': ('Values'), 'bottom': ('Timesteps')},
                         enableMenu=True)
            p3.showGrid(x=True, y=True, alpha=0.3)
            p3.enableAutoScale()
            p3.showButtons()


    def file_save(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def close_application(self):
        choice = QMessageBox.question(self, 'Exit!',
                                            "Are you sure you want to exit?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Exiting Now!")
            sys.exit()
        else:
            pass


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()