from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from title import Ui_MainWindow as mainWindow
from challenges_selector import Ui_MainWindow as challengesWindow
from challenge1 import Ui_MainWindow as challenge1Window
from challenge2 import Ui_MainWindow as challenge2Window
from challenge3 import Ui_MainWindow as challenge3Window
from challenge4 import Ui_MainWindow as challenge4Window
from challenge4 import Ui_MainWindow as challenge5Window
from challenge4 import Ui_MainWindow as challenge6Window
from challenge4 import Ui_MainWindow as challenge7Window
from challenge4 import Ui_MainWindow as challenge8Window
from challenge4 import Ui_MainWindow as challenge9Window
from challenge4 import Ui_MainWindow as challenge10Window
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
        self.pushButton_5.clicked.connect(self.open_chal4) # "challenge 4"
        

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
        
    def open_chal4(self):
        self.chal4Window = Chal4Window()
        self.chal4Window.show()
        self.close()
    
    def open_chal5(self):
        self.chal5Window = Chal5Window()
        self.chal5Window.show()
        self.close()

    def open_chal6(self):
        self.chal6Window = Chal6Window()
        self.chal6Window.show()
        self.close()
    
    def open_chal7(self):
        self.chal7Window = Chal7Window()
        self.chal7Window.show()
        self.close()
    
    def open_chal8(self):
        self.chal8Window = Chal8Window()
        self.chal8Window.show()
        self.close()
    
    def open_chal9(self):
        self.chal9Window = Chal9Window()
        self.chal9Window.show()
        self.close()
    def open_chal10(self):
        self.chal10Window = Chal10Window()
        self.chal10Window.show()
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


class Chal4Window(QMainWindow, challenge4Window):
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
        self.launchSpeedLineEdit.setVisible(not checked)
        self.launchAngleLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.launchHeightLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal4ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                            float(self.launchAngleLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.launchHeightLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal4ProjPath, [float(self.launc)])
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


class Chal5Window(QMainWindow, challenge5Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.uSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.hSlider.setVisible(False)
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
        self.hSlider.setVisible(checked)
        self.XSlider.setVisible(checked)
        self.YSlider.setVisible(checked)
        self.uLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.hLineEdit.setVisible(not checked)
        self.XLineEdit.setVisible(not checked)
        self.YLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal5ProjPath, [float(self.uLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.hLineEdit.text()),
                                                            float(self.XLineEdit.text()),
                                                            float(self.YLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal5ProjPath, [float(self.launc)])
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


class Chal6Window(QMainWindow, challenge6Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.uSlider.setVisible(False)
        self.hSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.thetaSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.uSlider.setVisible(checked)
        self.hSlider.setVisible(checked)
        self.gSlider.setVisible(checked)
        self.thetaSlider.setVisible(checked)
        self.uLineEdit.setVisible(not checked)
        self.hLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.thetaLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal6ProjPath, [float(self.uLineEdit.text()),
                                                            float(self.hLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.thetaLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal6ProjPath, [float(self.launc)])
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


class Chal7Window(QMainWindow, challenge7Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.uSlider.setVisible(False)
        self.gSlider.setVisible(False)
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
        self.uLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal7ProjPath, [float(self.uLineEdit.text()),
                                                            float(self.gLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal7ProjPath, [float(self.launc)])
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


class Chal8Window(QMainWindow, challenge8Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.uSlider.setVisible(False)
        self.CSlider.setVisible(False)
        self.thetaSlider.setVisible(False)
        self.hSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.maxBouncesSlider.setVisible(False)
        self.timeSetpSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.uSlider.setVisible(checked)
        self.CSlider.setVisible(checked)
        self.thetaSlider.setVisible(checked)
        self.hSlider.setVisible(checked)
        self.gSlider.setVisible(checked)
        self.maxBouncesSlider.setVisible(checked)
        self.timeSetpSlider.setVisible(checked)
        self.uLineEdit.setVisible(not checked)
        self.CLineEdit.setVisible(not checked)
        self.thetaLineEdit.setVisible(not checked)
        self.hLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.maxBouncesLineEdit.setVisible(not checked)
        self.timeSetpLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal8ProjPath, [float(self.uLineEdit.text()),
                                                            float(self.CLineEdit.text()),
                                                            float(self.thetaLineEdit.text()),
                                                            float(self.hLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.maxBouncesLineEdit.text()),
                                                            float(self.timeSetpLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal8ProjPath, [float(self.launc)])
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


class Chal9Window(QMainWindow, challenge9Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.thetaSlider.setVisible(False)
        self.uSlider.setVisible(False)
        self.hSlider.setVisible(False)
        self.gSlider.setVisible(False)
        self.DSlider.setVisible(False)
        self.CSASlider.setVisible(False)
        self.dASlider.setVisible(False)
        self.MSlider.setVisible(False)
        self.timeStepSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.thetaSlider.setVisible(checked)
        self.uSlider.setVisible(checked)
        self.hSlider.setVisible(checked)
        self.gSlider.setVisible(checked)
        self.DSlider.setVisible(checked)
        self.CSASlider.setVisible(checked)
        self.dASlider.setVisible(checked)
        self.MSlider.setVisible(checked)
        self.timeStepSlider.setVisible(checked)
        
        self.thetaLineEdit.setVisible(not checked)
        self.uLineEdit.setVisible(not checked)
        self.hLineEdit.setVisible(not checked)
        self.gLineEdit.setVisible(not checked)
        self.DLineEdit.setVisible(not checked)
        self.CSALineEdit.setVisible(not checked)
        self.dALineEdit.setVisible(not checked)
        self.MLineEdit.setVisible(not checked)
        self.timeStepLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.chal9ProjPath, [float(self.thetaLineEdit.text()),
                                                            float(self.uLineEdit.text()),
                                                            float(self.hLineEdit.text()),
                                                            float(self.gLineEdit.text()),
                                                            float(self.DLineEdit.text()),
                                                            float(self.CSALineEdit.text()),
                                                            float(self.dALineEdit.text()),
                                                            float(self.MLineEdit.text()),
                                                            float(self.timeStepLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.chal9ProjPath, [float(self.launc)])
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


class Chal10Window(QMainWindow, challenge10Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.back) # "back"

        # sliders and line edits
        self.slider_mode_on = False
        self.sliderModeCheckBox.toggled.connect(self.slider_mode)
        self.uSlider.setVisible(False)
        self.orbitTimeSlider.setVisible(False)
        self.RSlider.setVisible(False)
        self.mSlider.setVisible(False)
        self.timeStepSlider.setVisible(False)
        self.simulationLengthSlider.setVisible(False)

        # generate graph
        self.pushButton.clicked.connect(self.generateGraph)

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def slider_mode(self, checked):
        self.slider_mode_on = checked
        self.uSlider.setVisible(checked)
        self.orbitTimeSlider.setVisible(checked)
        self.RSlider.setVisible(checked)
        self.mSlider.setVisible(checked)
        self.timeStepSlider.setVisible(checked)
        self.simulationLengthSlider.setVisible(checked)
        
        self.uLineEdit.setVisible(not checked)
        self.orbitTimeLineEdit.setVisible(not checked)
        self.RLineEdit.setVisible(not checked)
        self.mLineEdit.setVisible(not checked)
        self.timeStepLineEdit.setVisible(not checked)
        self.simulationLengthLineEdit.setVisible(not checked)

    def generateGraph(self):
        try:
            if not self.slider_mode_on:
                self.plot(chals.plt_sphere, [float(self.uLineEdit.text()),
                                                            float(self.orbitTimeLineEdit.text()),
                                                            float(self.RLineEdit.text()),
                                                            float(self.mLineEdit.text()),
                                                            float(self.timeStepLineEdit.text()),
                                                            float(self.simulationLengthLineEdit.text())])
            else:
                self.plot(self.graphLayout, chals.plt_sphere, [float(self.launc)])
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