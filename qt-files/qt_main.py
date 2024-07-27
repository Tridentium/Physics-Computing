from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from title import Ui_MainWindow as mainWindow
from challenges_selector import Ui_MainWindow as challengesWindow
from challenge1 import Ui_MainWindow as challenge1Window
from challenge2 import Ui_MainWindow as challenge2Window
from challenge3 import Ui_MainWindow as challenge3Window
import sys
import Testing as chals
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# title
class MainWindow(QMainWindow, mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton_3.clicked.connect(self.open_challenges) # "challenges"
    
    def open_challenges(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()


# challenges
class ChallengesWindow(QMainWindow, challengesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"
        self.pushButton_2.clicked.connect(self.open_chal1) # "challenge 1"
        self.pushButton_3.clicked.connect(self.open_chal2) # "challenge 2"
        self.pushButton.clicked.connect(self.open_chal3) # "challenge 3"
        

    def back(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.close()

    def open_chal1(self):
        self.chal1Window = Chal1Window()
        self.chal1Window.show()
        self.close()

    def open_chal2(self):
        self.chal2Window = Chal2Window()
        self.chal2Window.show()
        self.close()
        
    def open_chal3(self):
        self.chal3Window = Chal3Window()
        self.chal3Window.show()
        self.close()


# challenge 1
class Chal1Window(QMainWindow, challenge1Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.launchSpeedSlider.setVisible(False)
        self.launchAngleSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.launchHeightSlider.setVisible(False)
        self.timeStepSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.launchSpeedSlider.setVisible(checked)
        self.launchAngleSlider.setVisible(checked)
        self.gSlider.setVisible(checked)
        self.launchHeightSlider.setVisible(checked)
        self.timeStepSlider.setVisible(checked)
        self.launchSpeedLineEdit.setVisible(not checked)
        self.launchAngleLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.launchHeightLineEdit.setVisible(not checked)
        self.timeStepLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal1ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                            float(self.launchAngleLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.launchHeightLineEdit.text()),
                                                            float(self.timeStepLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal1ProjPath, [float(self.launc)])
        except: # invalid input
            pass

    def plot(self, function, data):
        try:
            self.fig.clear()
            self.graphLayout.removeWidget(self.canvas)
            self.graphLayout.update()
        except:
            pass

        self.fig = Figure(figsize = (5, 5), 
                        dpi = 100) 
        self.plot1 = self.fig.add_subplot(111)
        function(self.plot1, *data)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.graphLayout.addWidget(self.canvas)   
        self.canvas.draw()


# challenge 2
class Chal2Window(QMainWindow, challenge2Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.launchSpeedSlider.setVisible(False)
        self.launchAngleSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.launchHeightSlider.setVisible(False)
        self.timeStepSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.launchSpeedSlider.setVisible(checked)
        self.launchAngleSlider.setVisible(checked)
        self.gSlider.setVisible(checked)
        self.launchHeightSlider.setVisible(checked)
        self.timeStepSlider.setVisible(checked)
        self.launchSpeedLineEdit.setVisible(not checked)
        self.launchAngleLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.launchHeightLineEdit.setVisible(not checked)
        self.timeStepLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal2ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                            float(self.launchAngleLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.launchHeightLineEdit.text()),
                                                            float(self.timeStepLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal2ProjPath, [float(self.launc)])
        except Exception as error:
            print("An exception occurred:", type(error).__name__)
            pass
        
        
    def plot(self, function, data):
        try:
            self.fig.clear()
            self.graphLayout.removeWidget(self.canvas)
            self.graphLayout.update()
        except:
            pass

        self.fig = Figure(figsize = (5, 5), 
                        dpi = 100) 
        self.plot1 = self.fig.add_subplot(111)
        function(self.plot1, *data)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.graphLayout.addWidget(self.canvas)   
        self.canvas.draw()
        
        
class Chal3Window(QMainWindow, challenge3Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.uSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.launchHeightSlider.setVisible(False)
        self.timeStepSlider.setVisible(False)
        self.XSlider.setVisible(False)
        self.YSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.uSlider.setVisible(checked)
        self.gSlider.setVisible(checked)
        self.launchHeightSlider.setVisible(checked)
        self.timeStepSlider.setVisible(checked)
        self.XSlider.setVisible(checked)
        self.YSlider.setVisible(checked)
        self.uLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.launchHeightLineEdit.setVisible(not checked)
        self.timeStepLineEdit.setVisible(not checked)
        self.XLineEdit.setVisible(not checked)
        self.YLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal3ProjPath, [float(self.uLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.launchHeightLineEdit.text()),
                                                            float(self.timeStepLineEdit.text()),
                                                            float(self.XLineEdit.text()),
                                                            float(self.YLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal3ProjPath, [float(self.launc)])
        except Exception as error:
            print("An exception occurred:", type(error).__name__)
            pass     

    def plot(self, function, data):
        try:
            self.fig.clear()
            self.graphLayout.removeWidget(self.canvas)
            self.graphLayout.update()
        except:
            pass

        self.fig = Figure(figsize = (5, 5), 
                        dpi = 100) 
        self.plot1 = self.fig.add_subplot(111)
        function(self.plot1, *data)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.graphLayout.addWidget(self.canvas)   
        self.canvas.draw()









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("BPhO Computational Challenge 2024")
    window.show()
    sys.exit(app.exec_())