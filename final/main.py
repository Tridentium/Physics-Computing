# BPhO Computational Challenge 2024 - Modelling Projectiles
# By Mantas Robinson and Bert Chun Chang

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from title import Ui_MainWindow as mainWindow
from challenges_selector import Ui_MainWindow as challengesWindow
from challenge1 import Ui_MainWindow as challenge1Window
from challenge1_info import Ui_MainWindow as challenge1InfoWindow
from challenge2 import Ui_MainWindow as challenge2Window
from challenge2_info import Ui_MainWindow as challenge2InfoWindow
from challenge3 import Ui_MainWindow as challenge3Window
from challenge3_info import Ui_MainWindow as challenge3InfoWindow
from challenge4 import Ui_MainWindow as challenge4Window
from challenge4_info import Ui_MainWindow as challenge4InfoWindow
from challenge5 import Ui_MainWindow as challenge5Window
from challenge5_info import Ui_MainWindow as challenge5InfoWindow
from challenge6 import Ui_MainWindow as challenge6Window
from challenge6_info import Ui_MainWindow as challenge6InfoWindow
from challenge7 import Ui_MainWindow as challenge7Window
from challenge7_info import Ui_MainWindow as challenge7InfoWindow
from challenge8 import Ui_MainWindow as challenge8Window
from challenge8_info import Ui_MainWindow as challenge8InfoWindow
from challenge9 import Ui_MainWindow as challenge9Window
from challenge9_info import Ui_MainWindow as challenge9InfoWindow
from extension import Ui_MainWindow as extensionWindow
from extension_info import Ui_MainWindow as extensionInfoWindow
from extension_code_info import Ui_MainWindow as extensionCodeInfoWindow
import sys
import Testing as chals
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# Title
class MainWindow(QMainWindow, mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        
        self.challengesButton.clicked.connect(self.open_challenges)
        self.exitButton.clicked.connect(self.exit_application)
    
    def open_challenges(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def exit_application(self):
        self.close()


# Challenge Selector
class ChallengesWindow(QMainWindow, challengesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0) 
        self.setWindowTitle("Challenges")

        self.backButton.clicked.connect(self.back)
        self.chal1Button.clicked.connect(self.open_chal1)
        self.chal2Button.clicked.connect(self.open_chal2)
        self.chal3Button.clicked.connect(self.open_chal3)
        self.chal4Button.clicked.connect(self.open_chal4)
        self.chal5Button.clicked.connect(self.open_chal5)
        self.chal6Button.clicked.connect(self.open_chal6)
        self.chal7Button.clicked.connect(self.open_chal7)
        self.chal8Button.clicked.connect(self.open_chal8)
        self.chal9Button.clicked.connect(self.open_chal9)
        self.extensionButton.clicked.connect(self.open_ext)
        

    def back(self):
        self.mainWindow = MainWindow()
        self.mainWindow.setWindowTitle("BPhO Computational Challenge 2024")
        self.mainWindow.show()
        self.close()

    def open_chal1(self):
        self.chal1Window = Chal1Window()
        self.chal1Window.setWindowTitle("Challenge 1")
        self.chal1Window.show()
        self.close()

    def open_chal2(self):
        self.chal2Window = Chal2Window()
        self.chal2Window.setWindowTitle("Challenge 2")
        self.chal2Window.show()
        self.close()
        
    def open_chal3(self):
        self.chal3Window = Chal3Window()
        self.chal3Window.setWindowTitle("Challenge 3")
        self.chal3Window.show()
        self.close()
        
    def open_chal4(self):
        self.chal4Window = Chal4Window()
        self.chal4Window.setWindowTitle("Challenge 4")
        self.chal4Window.show()
        self.close()
    
    def open_chal5(self):
        self.chal5Window = Chal5Window()
        self.chal5Window.setWindowTitle("Challenge 5")
        self.chal5Window.show()
        self.close()

    def open_chal6(self):
        self.chal6Window = Chal6Window()
        self.chal6Window.setWindowTitle("Challenge 6")
        self.chal6Window.show()
        self.close()
    
    def open_chal7(self):
        self.chal7Window = Chal7Window()
        self.chal7Window.setWindowTitle("Challenge 7")
        self.chal7Window.show()
        self.close()
    
    def open_chal8(self):
        self.chal8Window = Chal8Window()
        self.chal8Window.setWindowTitle("Challenge 8")
        self.chal8Window.show()
        self.close()
    
    def open_chal9(self):
        self.chal9Window = Chal9Window()
        self.chal9Window.setWindowTitle("Challenge 9")
        self.chal9Window.show()
        self.close()

    def open_ext(self):
        self.chal10Window = ExtWindow()
        self.chal10Window.setWindowTitle("Extension")
        self.chal10Window.show()
        self.close()


# Challenge 1
class Chal1Window(QMainWindow, challenge1Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.launchAngleLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 100)
        self.launchSpeedSlider.setValue(25)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(20)

        self.launchAngleSlider.setRange(0, 90)
        self.launchAngleSlider.setValue(45)
        self.launchAngleSlider.valueChanged.connect(self.updateAngleLabel)
        self.launchAngleSlider.valueChanged.connect(self.generateGraph)
        self.updateAngleLabel(45)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 200)
        self.launchHeightSlider.setValue(2)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(2)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.launchAngleLineEdit.textChanged.connect(self.updateAngleLabel)
        self.launchAngleLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal1InfoWindow = Chal1InfoWindow()
        self.chal1InfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateAngleLabel(self, value):
        try:
            self.launchAngleSlider.setValue(int(value))
            self.launchAngleSliderLabel.setText(str(value) + "°")
        except: # invalid input
            self.launchAngleSlider.setValue(0)
            self.launchAngleSliderLabel.setText("Invalid input from text input mode")

        self.launchAngleLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.launchAngleSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.launchAngleSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.launchAngleLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge1Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.challenge1Path, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
        except: # invalid input
            self.plot(chals.challenge1Path, [0, 0, 0, 0, 0])

    def plot(self, function, data):
        try:
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

# Challenge 1 info
class Chal1InfoWindow(QMainWindow, challenge1InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal1Window = Chal1Window()
        self.chal1Window.show()
        self.close()


# Challenge 2
class Chal2Window(QMainWindow, challenge2Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.launchAngleLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 100)
        self.launchSpeedSlider.setValue(25)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(20)

        self.launchAngleSlider.setRange(0, 90)
        self.launchAngleSlider.setValue(45)
        self.launchAngleSlider.valueChanged.connect(self.updateAngleLabel)
        self.launchAngleSlider.valueChanged.connect(self.generateGraph)
        self.updateAngleLabel(45)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 200)
        self.launchHeightSlider.setValue(2)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(2)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.launchAngleLineEdit.textChanged.connect(self.updateAngleLabel)
        self.launchAngleLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal2InfoWindow = Chal2InfoWindow()
        self.chal2InfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateAngleLabel(self, value):
        try:
            self.launchAngleSlider.setValue(int(value))
            self.launchAngleSliderLabel.setText(str(value) + "°")
        except: # invalid input
            self.launchAngleSlider.setValue(0)
            self.launchAngleSliderLabel.setText("Invalid input from text input mode")

        self.launchAngleLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.launchAngleSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.launchAngleSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.launchAngleLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge2Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.challenge2Path, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
                
            analytics = chals.challenge2Path(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSliderLabel.text()[0:-5]),
                                            float(self.launchHeightSlider.value()),
                                            float(self.timeStepSlider.value()))
            self.rangeLabel.setText("Range: " + str(round(analytics[0], 5)) + " m")
            self.apogeeLabel.setText("Apogee: (" + str(round(analytics[1], 5)) + " m, " + str(round(analytics[2], 5)) + " m)")
            self.flightTimeLabel.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")

        except Exception as error: # invalid input
            # print(error)
            self.plot(chals.challenge2Path, [0, 0, 0, 0, 0])

    def plot(self, function, data):
        try:
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

# Challenge 2 info
class Chal2InfoWindow(QMainWindow, challenge2InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal2Window = Chal2Window()
        self.chal2Window.show()
        self.close()

        
# Challenge 3
class Chal3Window(QMainWindow, challenge3Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.XLineEdit.setVisible(False)
        self.YLineEdit.setVisible(False)
        self.launchSpeedLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.XSlider.setRange(0, 2000)
        self.XSlider.setValue(1000)
        self.XSlider.valueChanged.connect(self.updateXLabel)
        self.XSlider.valueChanged.connect(self.generateGraph)
        self.updateXLabel(1000)

        self.YSlider.setRange(0, 2000)
        self.YSlider.setValue(300)
        self.YSlider.valueChanged.connect(self.updateYLabel)
        self.YSlider.valueChanged.connect(self.generateGraph)
        self.updateYLabel(300)

        self.launchSpeedSlider.setRange(0, 300)
        self.launchSpeedSlider.setValue(150)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(150)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 300)
        self.launchHeightSlider.setValue(0)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(0)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.XLineEdit.textChanged.connect(self.updateXLabel)
        self.XLineEdit.textChanged.connect(self.generateGraph)
        self.YLineEdit.textChanged.connect(self.updateYLabel)
        self.YLineEdit.textChanged.connect(self.generateGraph)
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal3InfoWindow = Chal3InfoWindow()
        self.chal3InfoWindow.show()
        self.close()
        
    def updateXLabel(self, value):
        try:
            self.XSlider.setValue(int(value))
            self.XSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.XSlider.setValue(0)
            self.XSliderLabel.setText("Invalid input from text input mode")

        self.XLineEdit.setText(str(value))

    def updateYLabel(self, value):
        try:
            self.YSlider.setValue(int(value))
            self.YSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.YSlider.setValue(0)
            self.YSliderLabel.setText("Invalid input from text input mode")

        self.YLineEdit.setText(str(value))

    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.XSlider.setVisible(not checked)
        self.YSlider.setVisible(not checked)
        self.launchSpeedSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.XSliderLabel.setVisible(not checked)
        self.YSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.XLineEdit.setVisible(checked)
        self.YLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge3Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text()),
                                                float(self.XLineEdit.text()),
                                                float(self.YLineEdit.text())])
            else:
                self.plot(chals.challenge3Path, [float(self.launchSpeedSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value()),
                                                float(self.XSlider.value()),
                                                float(self.YSlider.value())])
                
            analytics = chals.challenge3Path(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.gSliderLabel.text()[0:-5]),
                                            float(self.launchHeightSlider.value()),
                                            float(self.timeStepSlider.value()),
                                            float(self.XSlider.value()),
                                            float(self.YSlider.value()))
            self.minLaunchSpeedLabel.setText("Min. Launch Speed: " + str(round(analytics[0], 5)) + " ms⁻¹")
            self.minSpeedAngleLabelRad.setText("Min. Speed Angle: " + str(round(analytics[1], 5)) + " rad")
            self.minSpeedAngleLabelDeg.setText("Min. Speed Angle: " + str(round(analytics[2], 5)) + "°")
            self.projFlightTime.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")
            self.highAngleRad.setText("Angle: " + str(round(analytics[4], 5)) + " rad")
            self.highAngleDeg.setText("Angle: " + str(round(analytics[5], 5)) + "°")
            self.highFlightTime.setText("Flight Time: " + str(round(analytics[6], 5)) + " s")
            self.lowAngleRad.setText("Angle: " + str(round(analytics[7], 5)) + " rad")
            self.lowAngleDeg.setText("Angle: " + str(round(analytics[8], 5)) + "°")
            self.lowFlightTime.setText("Flight Time: " + str(round(analytics[9], 5)) + " s")

        except Exception as error: # invalid input
            self.plot(chals.challenge2Path, [0, 0, 0, 0, 0])

    def plot(self, function, data):
        try:
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

# Challenge 3 info
class Chal3InfoWindow(QMainWindow, challenge3InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal3Window = Chal3Window()
        self.chal3Window.show()
        self.close()


class Chal4Window(QMainWindow, challenge4Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.launchAngleLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 100)
        self.launchSpeedSlider.setValue(10)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(10)

        self.launchAngleSlider.setRange(0, 90)
        self.launchAngleSlider.setValue(60)
        self.launchAngleSlider.valueChanged.connect(self.updateAngleLabel)
        self.launchAngleSlider.valueChanged.connect(self.generateGraph)
        self.updateAngleLabel(60)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 200)
        self.launchHeightSlider.setValue(2)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(2)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.launchAngleLineEdit.textChanged.connect(self.updateAngleLabel)
        self.launchAngleLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal4InfoWindow = Chal4InfoWindow()
        self.chal4InfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateAngleLabel(self, value):
        try:
            self.launchAngleSlider.setValue(int(value))
            self.launchAngleSliderLabel.setText(str(value) + "°")
        except: # invalid input
            self.launchAngleSlider.setValue(0)
            self.launchAngleSliderLabel.setText("Invalid input from text input mode")

        self.launchAngleLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.launchAngleSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.launchAngleSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.launchAngleLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge4Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.challenge4Path, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
                
            analytics = chals.challenge4Path(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSliderLabel.text()[0:-5]),
                                            float(self.launchHeightSlider.value()),
                                            float(self.timeStepSlider.value()))
            
            self.rangeLabel.setText("Range: " + str(round(analytics[0], 5)) + " m")
            self.apogeeLabel.setText("Apogee: (" + str(round(analytics[1], 5)) + " m, " + str(round(analytics[2], 5)) + " m)")
            self.flightTimeLabel.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")
            self.rangeLabel_2.setText("Range: " + str(round(analytics[4], 5)) + " m")
            self.apogeeLabel_2.setText("Apogee: (" + str(round(analytics[5], 5)) + " m, " + str(round(analytics[6], 5)) + " m)")
            self.flightTimeLabel_2.setText("Time of Flight: " + str(round(analytics[7], 5)) + " s")

        except Exception as error: # invalid input
            print(error)
            self.plot(chals.challenge4Path, [1, 0, 1, 1, 1])

    def plot(self, function, data):
        try:
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

# Challenge 4 info
class Chal4InfoWindow(QMainWindow, challenge4InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal4Window = Chal4Window()
        self.chal4Window.show()
        self.close()


# Challenge 5
class Chal5Window(QMainWindow, challenge5Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.XLineEdit.setVisible(False)
        self.YLineEdit.setVisible(False)
        self.launchSpeedLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.XSlider.setRange(0, 2000)
        self.XSlider.setValue(1000)
        self.XSlider.valueChanged.connect(self.updateXLabel)
        self.XSlider.valueChanged.connect(self.generateGraph)
        self.updateXLabel(1000)

        self.YSlider.setRange(0, 2000)
        self.YSlider.setValue(300)
        self.YSlider.valueChanged.connect(self.updateYLabel)
        self.YSlider.valueChanged.connect(self.generateGraph)
        self.updateYLabel(300)

        self.launchSpeedSlider.setRange(0, 300)
        self.launchSpeedSlider.setValue(150)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(150)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 300)
        self.launchHeightSlider.setValue(0)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(0)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.XLineEdit.textChanged.connect(self.updateXLabel)
        self.XLineEdit.textChanged.connect(self.generateGraph)
        self.YLineEdit.textChanged.connect(self.updateYLabel)
        self.YLineEdit.textChanged.connect(self.generateGraph)
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal5InfoWindow = Chal5InfoWindow()
        self.chal5InfoWindow.show()
        self.close()
        
    def updateXLabel(self, value):
        try:
            self.XSlider.setValue(int(value))
            self.XSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.XSlider.setValue(1)
            self.XSliderLabel.setText("Invalid input from text input mode")

        self.XLineEdit.setText(str(value))

    def updateYLabel(self, value):
        try:
            self.YSlider.setValue(int(value))
            self.YSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.YSlider.setValue(1)
            self.YSliderLabel.setText("Invalid input from text input mode")

        self.YLineEdit.setText(str(value))

    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.XSlider.setVisible(not checked)
        self.YSlider.setVisible(not checked)
        self.launchSpeedSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.XSliderLabel.setVisible(not checked)
        self.YSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.XLineEdit.setVisible(checked)
        self.YLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge5Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text()),
                                                float(self.XLineEdit.text()),
                                                float(self.YLineEdit.text())])
            else:
                self.plot(chals.challenge5Path, [float(self.launchSpeedSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value()),
                                                float(self.XSlider.value()),
                                                float(self.YSlider.value())])

        except Exception as error: # invalid input
            self.plot(chals.challenge5Path, [1, 1, 1, 1, 1, 1])

    def plot(self, function, data):
        try:
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

# Challenge 5 info
class Chal5InfoWindow(QMainWindow, challenge5InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal5Window = Chal5Window()
        self.chal5Window.show()
        self.close()


class Chal6Window(QMainWindow, challenge6Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.launchAngleLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 100)
        self.launchSpeedSlider.setValue(10)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(10)

        self.launchAngleSlider.setRange(0, 90)
        self.launchAngleSlider.setValue(60)
        self.launchAngleSlider.valueChanged.connect(self.updateAngleLabel)
        self.launchAngleSlider.valueChanged.connect(self.generateGraph)
        self.updateAngleLabel(60)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 200)
        self.launchHeightSlider.setValue(2)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(2)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.launchAngleLineEdit.textChanged.connect(self.updateAngleLabel)
        self.launchAngleLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal6InfoWindow = Chal6InfoWindow()
        self.chal6InfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateAngleLabel(self, value):
        try:
            self.launchAngleSlider.setValue(int(value))
            self.launchAngleSliderLabel.setText(str(value) + "°")
        except: # invalid input
            self.launchAngleSlider.setValue(0)
            self.launchAngleSliderLabel.setText("Invalid input from text input mode")

        self.launchAngleLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.launchAngleSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.launchAngleSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.launchAngleLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge6Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.challenge6Path, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
                
            analytics = chals.challenge6Path(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSliderLabel.text()[0:-5]),
                                            float(self.launchHeightSlider.value()),
                                            float(self.timeStepSlider.value()))
            
            self.rangeLabel.setText("Range: " + str(round(analytics[0], 5)) + " m")
            self.apogeeLabel.setText("Apogee: (" + str(round(analytics[1], 5)) + " m, " + str(round(analytics[2], 5)) + " m)")
            self.flightTimeLabel.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")
            self.rangeLabel_2.setText("Max Range: " + str(round(analytics[4], 5)) + " m")
            self.apogeeLabel_2.setText("Apogee: (" + str(round(analytics[5], 5)) + " m, " + str(round(analytics[6], 5)) + " m)")
            self.flightTimeLabel_2.setText("Time of Flight: " + str(round(analytics[7], 5)) + " s")
            self.distanceLabel.setText("Distance: " + str(round(analytics[8], 5)) + "m")
            self.distanceLabel_2.setText("Max Distance: " + str(round(analytics[9], 5)) + "m")

        except Exception as error: # invalid input
            print(error)
            self.plot(chals.challenge6Path, [1, 0, 1, 1, 1])

    def plot(self, function, data):
        try:
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

# Challenge 6 info
class Chal6InfoWindow(QMainWindow, challenge6InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal6Window = Chal6Window()
        self.chal6Window.show()
        self.close()


# Challenge 7
class Chal7Window(QMainWindow, challenge7Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 300)
        self.launchSpeedSlider.setValue(10)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(10)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal7InfoWindow = Chal7InfoWindow()
        self.chal7InfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plotLeft(chals.challenge7PathLeft, [float(self.launchSpeedLineEdit.text()),
                                                    float(self.gLineEdit.text()),
                                                    float(self.timeStepLineEdit.text())])
                self.plotRight(chals.challenge7PathRight, [float(self.launchSpeedLineEdit.text()),
                                                    float(self.gLineEdit.text()),
                                                    float(self.timeStepLineEdit.text())])
            else:
                self.plotLeft(chals.challenge7PathLeft, [float(self.launchSpeedSlider.value()),
                                                    float(self.gSliderLabel.text()[0:-5]),
                                                    float(self.timeStepSlider.value())])
                self.plotRight(chals.challenge7PathRight, [float(self.launchSpeedSlider.value()),
                                                    float(self.gSliderLabel.text()[0:-5]),
                                                    float(self.timeStepSlider.value())])
        except: # invalid input
            pass

    def plotLeft(self, function, data):
        try:
            self.graphLayout.removeWidget(self.canvas)
            self.graphLayout.update()
        except:
            pass

        self.fig = Figure(figsize = (3, 3), 
                        dpi = 100) 
        self.plot1 = self.fig.add_subplot(111)
        function(self.plot1, *data)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.graphLayout.addWidget(self.canvas)   
        self.canvas.draw()

    def plotRight(self, function, data):
        try:
            self.graphLayout_2.removeWidget(self.canvas2)
            self.graphLayout_2.update()
        except:
            pass

        self.fig2 = Figure(figsize = (2, 3), 
                        dpi = 100) 
        self.plot2 = self.fig2.add_subplot(111)
        function(self.plot2, *data)
        self.canvas2 = FigureCanvasQTAgg(self.fig2)
        self.graphLayout_2.addWidget(self.canvas2)   
        self.canvas2.draw()

# Challenge 7 info
class Chal7InfoWindow(QMainWindow, challenge7InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal7Window = Chal7Window()
        self.chal7Window.show()
        self.close()


# Challenge 8
class Chal8Window(QMainWindow, challenge8Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.maxBouncesLineEdit.setVisible(False)
        self.restitutionCoefficientLineEdit.setVisible(False)
        self.launchSpeedLineEdit.setVisible(False)
        self.launchAngleLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)

        # set up sliders
        self.maxBouncesSlider.setRange(0, 100)
        self.maxBouncesSlider.setValue(6)
        self.maxBouncesSlider.valueChanged.connect(self.updateMaxBouncesLabel)
        self.maxBouncesSlider.valueChanged.connect(self.generateGraph)
        self.updateMaxBouncesLabel(6)

        self.restitutionCoefficientSlider.setRange(0, 100)
        self.restitutionCoefficientSlider.setValue(70)
        self.restitutionCoefficientSlider.valueChanged.connect(self.changedRestitutionCoefficientSlider)
        self.restitutionCoefficientSlider.valueChanged.connect(self.generateGraph)
        self.updateRestitutionCoefficientLabel(70, True)

        self.launchSpeedSlider.setRange(0, 100)
        self.launchSpeedSlider.setValue(5)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(5)

        self.launchAngleSlider.setRange(0, 90)
        self.launchAngleSlider.setValue(45)
        self.launchAngleSlider.valueChanged.connect(self.updateAngleLabel)
        self.launchAngleSlider.valueChanged.connect(self.generateGraph)
        self.updateAngleLabel(45)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 200)
        self.launchHeightSlider.setValue(10)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(10)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        # link lineedit labels to sliders
        self.maxBouncesLineEdit.textChanged.connect(self.updateMaxBouncesLabel)
        self.maxBouncesLineEdit.textChanged.connect(self.generateGraph)
        self.restitutionCoefficientLineEdit.textChanged.connect(self.changedRestitutionCoefficientLineEdit)
        self.restitutionCoefficientLineEdit.textChanged.connect(self.generateGraph)
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.launchAngleLineEdit.textChanged.connect(self.updateAngleLabel)
        self.launchAngleLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal8InfoWindow = Chal8InfoWindow()
        self.chal8InfoWindow.show()
        self.close()
    
    def updateMaxBouncesLabel(self, value):
        try:
            self.maxBouncesSlider.setValue(int(value))
            self.maxBouncesSliderLabel.setText(str(value))
        except: # invalid input
            self.maxBouncesSlider.setValue(0)
            self.maxBouncesSliderLabel.setText("Invalid input from text input mode")

        self.maxBouncesLineEdit.setText(str(value))

    def changedRestitutionCoefficientSlider(self, value):
        self.updateRestitutionCoefficientLabel(value, True)
    
    def changedRestitutionCoefficientLineEdit(self, value):
        self.updateRestitutionCoefficientLabel(value, False)

    def updateRestitutionCoefficientLabel(self, value, slider):
        if slider:
            value /= 100
        try:
            self.restitutionCoefficientSlider.setValue(int(float(value) * 100))
            self.restitutionCoefficientSliderLabel.setText(str(value))
        except: # invalid input
            self.restitutionCoefficientSlider.setValue(0)
            self.restitutionCoefficientSliderLabel.setText("Invalid input from text input mode")

        self.restitutionCoefficientLineEdit.setText(str(value))

    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateAngleLabel(self, value):
        try:
            self.launchAngleSlider.setValue(int(value))
            self.launchAngleSliderLabel.setText(str(value) + "°")
        except: # invalid input
            self.launchAngleSlider.setValue(0)
            self.launchAngleSliderLabel.setText("Invalid input from text input mode")

        self.launchAngleLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.maxBouncesSlider.setVisible(not checked)
        self.restitutionCoefficientSlider.setVisible(not checked)
        self.launchSpeedSlider.setVisible(not checked)
        self.launchAngleSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.maxBouncesSliderLabel.setVisible(not checked)
        self.restitutionCoefficientSliderLabel.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.launchAngleSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.maxBouncesLineEdit.setVisible(checked)
        self.restitutionCoefficientLineEdit.setVisible(checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.launchAngleLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge8Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.restitutionCoefficientLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.maxBouncesLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
                analytics = chals.challenge8Path(None,
                                                float(self.launchSpeedSlider.value()),
                                                float(self.restitutionCoefficientSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.maxBouncesSlider.value()),
                                                float(self.timeStepSlider.value()))
            else:
                self.plot(chals.challenge8Path, [float(self.launchSpeedSlider.value()),
                                                float(self.restitutionCoefficientSlider.value() / 100),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.maxBouncesSlider.value()),
                                                float(self.timeStepSlider.value())])
                analytics = chals.challenge8Path(None,
                                                float(self.launchSpeedSlider.value()),
                                                float(self.restitutionCoefficientSlider.value() / 100),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.maxBouncesSlider.value()),
                                                float(self.timeStepSlider.value()))
            self.flightTimeLabel.setText("Time of Flight for Max Number of Bounces: " + str(round(analytics, 5)) + " s")

        except Exception as error: # invalid input
            self.plot(chals.challenge8Path, [0,0,0,0,0,0,0])

    def plot(self, function, data):
        try:
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
            

# Challenge 8 info
class Chal8InfoWindow(QMainWindow, challenge8InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal8Window = Chal8Window()
        self.chal8Window.show()
        self.close()


# Challenge 9
class Chal9Window(QMainWindow, challenge9Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.launchAngleLineEdit.setVisible(False)
        self.gLineEdit.setVisible(False)
        self.launchHeightLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)
        self.dragCoefficientLineEdit.setVisible(False)
        self.CSALineEdit.setVisible(False)
        self.airDensityLineEdit.setVisible(False)
        self.massLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 100)
        self.launchSpeedSlider.setValue(25)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(20)

        self.launchAngleSlider.setRange(0, 90)
        self.launchAngleSlider.setValue(45)
        self.launchAngleSlider.valueChanged.connect(self.updateAngleLabel)
        self.launchAngleSlider.valueChanged.connect(self.generateGraph)
        self.updateAngleLabel(45)

        self.gSlider.setRange(1, 30)
        self.gSlider.setValue(10)
        self.gSlider.valueChanged.connect(self.updategLabel)
        self.gSlider.valueChanged.connect(self.generateGraph)
        self.updategLabel(9.81)

        self.setgButton.clicked.connect(self.setEarthg)
        self.setgButton.clicked.connect(self.generateGraph)

        self.launchHeightSlider.setRange(0, 200)
        self.launchHeightSlider.setValue(2)
        self.launchHeightSlider.valueChanged.connect(self.updateHeightLabel)
        self.launchHeightSlider.valueChanged.connect(self.generateGraph)
        self.updateHeightLabel(2)

        self.timeStepSlider.setRange(2, 500)
        self.timeStepSlider.setValue(2)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(2)

        self.dragCoefficientSlider.setRange(0, 200)
        self.dragCoefficientSlider.setValue(10)
        self.dragCoefficientSlider.valueChanged.connect(self.changedDragCoefficientSlider)
        self.dragCoefficientSlider.valueChanged.connect(self.generateGraph)
        self.changedDragCoefficientSlider(10)

        self.CSASlider.setRange(0, 500)
        self.CSASlider.setValue(80)
        self.CSASlider.valueChanged.connect(self.updateCSALabel)
        self.CSASlider.valueChanged.connect(self.generateGraph)
        self.updateCSALabel(80)

        self.airDensitySlider.setRange(0, 300)
        self.airDensitySlider.setValue(100)
        self.airDensitySlider.valueChanged.connect(self.changedAirDensitySlider)
        self.airDensitySlider.valueChanged.connect(self.generateGraph)
        self.changedAirDensitySlider(100)

        self.massSlider.setRange(0, 5000)
        self.massSlider.setValue(10)
        self.massSlider.valueChanged.connect(self.changedMassSlider)
        self.massSlider.valueChanged.connect(self.generateGraph)
        self.changedMassSlider(10)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.launchAngleLineEdit.textChanged.connect(self.updateAngleLabel)
        self.launchAngleLineEdit.textChanged.connect(self.generateGraph)
        self.gLineEdit.textChanged.connect(self.updategLabel)
        self.gLineEdit.textChanged.connect(self.generateGraph)
        self.launchHeightLineEdit.textChanged.connect(self.updateHeightLabel)
        self.launchHeightLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)
        self.dragCoefficientLineEdit.textChanged.connect(self.changedDragCoefficientLineEdit)
        self.dragCoefficientLineEdit.textChanged.connect(self.generateGraph)
        self.CSALineEdit.textChanged.connect(self.updateCSALabel)
        self.CSALineEdit.textChanged.connect(self.generateGraph)
        self.airDensityLineEdit.textChanged.connect(self.changedAirDensityLineEdit)
        self.airDensityLineEdit.textChanged.connect(self.generateGraph)
        self.massLineEdit.textChanged.connect(self.changedMassLineEdit)
        self.massLineEdit.textChanged.connect(self.generateGraph)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal9InfoWindow = Chal9InfoWindow()
        self.chal9InfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " ms⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateAngleLabel(self, value):
        try:
            self.launchAngleSlider.setValue(int(value))
            self.launchAngleSliderLabel.setText(str(value) + "°")
        except: # invalid input
            self.launchAngleSlider.setValue(0)
            self.launchAngleSliderLabel.setText("Invalid input from text input mode")

        self.launchAngleLineEdit.setText(str(value))

    def updategLabel(self, value):
        if value == 9.81:
            self.gSlider.valueChanged.disconnect(self.updategLabel)
            self.gSlider.setValue(10)
            self.gSlider.valueChanged.connect(self.updategLabel)
            self.gSliderLabel.setText("9.81 ms⁻²")
        else:
            try:
                self.gSlider.setValue(int(value))
                self.gSliderLabel.setText(str(value) + " ms⁻²")
            except: # invalid input
                self.gSlider.setValue(0)
                self.gSliderLabel.setText("Invalid input from text input mode")

        try:
            self.gLineEdit.textChanged.disconnect(self.updategLabel)
        except:
            pass
        self.gLineEdit.setText(str(value))
        self.gLineEdit.textChanged.connect(self.updategLabel)

    def updateHeightLabel(self, value):
        try:
            self.launchHeightSlider.setValue(int(value))
            self.launchHeightSliderLabel.setText(str(value) + " m")
        except: # invalid input
            self.launchHeightSlider.setValue(0)
            self.launchHeightSliderLabel.setText("Invalid input from text input mode")

        self.launchHeightLineEdit.setText(str(value))

    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " ms")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def changedDragCoefficientSlider(self, value):
        self.updateDragCoefficientLabel(value, True)
    
    def changedDragCoefficientLineEdit(self, value):
        self.updateDragCoefficientLabel(value, False)

    def updateDragCoefficientLabel(self, value, slider):
        if slider:
            value /= 100
        try:
            self.dragCoefficientSlider.setValue(int(float(value) * 100))
            self.dragCoefficientSliderLabel.setText(str(value))
        except: # invalid input
            self.dragCoefficientSlider.setValue(0)
            self.dragCoefficientSliderLabel.setText("Invalid input from text input mode")

        self.dragCoefficientLineEdit.setText(str(value))

    def updateCSALabel(self, value):
        try:
            self.CSASlider.setValue(int(value))
            self.CSASliderLabel.setText(str(value) + " cm²")
        except: # invalid input
            self.CSASlider.setValue(0)
            self.CSASliderLabel.setText("Invalid input from text input mode")

        self.CSALineEdit.setText(str(value))

    def changedAirDensitySlider(self, value):
        self.updateAirDensityLabel(value, True)
    
    def changedAirDensityLineEdit(self, value):
        self.updateAirDensityLabel(value, False)

    def updateAirDensityLabel(self, value, slider):
        if slider:
            value /= 100
        try:
            self.airDensitySlider.setValue(int(float(value) * 100))
            self.airDensitySliderLabel.setText(str(value) + " kgm⁻³")
        except: # invalid input
            self.airDensitySlider.setValue(0)
            self.airDensitySliderLabel.setText("Invalid input from text input mode")

        self.airDensityLineEdit.setText(str(value))

    def changedMassSlider(self, value):
        self.updateMassLabel(value, True)
    
    def changedMassLineEdit(self, value):
        self.updateMassLabel(value, False)

    def updateMassLabel(self, value, slider):
        if slider:
            value /= 100
        try:
            self.massSlider.setValue(int(float(value) * 100))
            self.massSliderLabel.setText(str(value) + " kg")
        except: # invalid input
            self.massSlider.setValue(0)
            self.massSliderLabel.setText("Invalid input from text input mode")

        self.massLineEdit.setText(str(value))

    def setEarthg(self):
        self.updategLabel(9.81)
        self.updategLabel(9.81)     # only running it once will make the label say "invalid input from text input mode"

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.launchAngleSlider.setVisible(not checked)
        self.gSlider.setVisible(not checked)
        self.launchHeightSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.dragCoefficientSlider.setVisible(not checked)
        self.CSASlider.setVisible(not checked)
        self.airDensitySlider.setVisible(not checked)
        self.massSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.launchAngleSliderLabel.setVisible(not checked)
        self.gSliderLabel.setVisible(not checked)
        self.launchHeightSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.dragCoefficientSliderLabel.setVisible(not checked)
        self.CSASliderLabel.setVisible(not checked)
        self.airDensitySliderLabel.setVisible(not checked)
        self.massSliderLabel.setVisible(not checked)
        self.setgButton.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.launchAngleLineEdit.setVisible(checked)
        self.gLineEdit.setVisible(checked)
        self.launchHeightLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)
        self.dragCoefficientLineEdit.setVisible(checked)
        self.CSALineEdit.setVisible(checked)
        self.airDensityLineEdit.setVisible(checked)
        self.massLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.challenge9Path, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text()),
                                                float(self.dragCoefficientLineEdit.text()),
                                                float(self.CSALineEdit.text()),
                                                float(self.airDensityLineEdit.text()),
                                                float(self.massLineEdit.text())])
                analytics = chals.challenge9Path(None,
                                                float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text()),
                                                float(self.dragCoefficientLineEdit.text()),
                                                float(self.CSALineEdit.text()),
                                                float(self.airDensityLineEdit.text()),
                                                float(self.massLineEdit.text()))
            else:
                self.plot(chals.challenge9Path, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value()),
                                                float(self.dragCoefficientSlider.value() / 100),
                                                float(self.CSASlider.value()),
                                                float(self.airDensitySlider.value() / 100),
                                                float(self.massSlider.value() / 100)])                
                analytics = chals.challenge9Path(None,
                                                float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSliderLabel.text()[0:-5]),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value()),
                                                float(self.dragCoefficientSlider.value() / 100),
                                                float(self.CSASlider.value()),
                                                float(self.airDensitySlider.value() / 100),
                                                float(self.massSlider.value() / 100))
            
            self.rangeLabel.setText("Range: " + str(round(analytics[0], 5)) + " m")
            self.apogeeLabel.setText("Apogee: (" + str(round(analytics[1], 2)) + " m, " + str(round(analytics[2], 2)) + " m)")
            self.flightTimeLabel.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")
            self.rangeLabel_4.setText("Range: " + str(round(analytics[4], 5)) + " m")
            self.apogeeLabel_2.setText("Apogee: (" + str(round(analytics[5], 2)) + " m, " + str(round(analytics[6], 2)) + " m)")
            self.flightTimeLabel_2.setText("Time of Flight: " + str(round(analytics[7], 5)) + " s")
            self.airResFactorLabel.setText("Air Resistance Factor:\n" + str(round(analytics[8], 5)))

        except Exception as error: # invalid input
            # print(error)
            self.plot(chals.challenge9Path, [1, 1, 1, 0, 1, 1, 1, 1, 1])

    def plot(self, function, data):
        try:
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

# Challenge 9 info
class Chal9InfoWindow(QMainWindow, challenge9InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal9Window = Chal9Window()
        self.chal9Window.show()
        self.close()


# Extension
class ExtWindow(QMainWindow, extensionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # hiding line edits
        self.text_mode_on = False
        self.textModeCheckBox.toggled.connect(self.text_mode)
        self.launchSpeedLineEdit.setVisible(False)
        self.orbitTimeLineEdit.setVisible(False)
        self.orbitRadiusLineEdit.setVisible(False)
        self.massLineEdit.setVisible(False)
        self.planetRadiusLineEdit.setVisible(False)
        self.timeStepLineEdit.setVisible(False)
        self.maxSimLengthLineEdit.setVisible(False)

        # set up sliders
        self.launchSpeedSlider.setRange(0, 30000)
        self.launchSpeedSlider.setValue(15000)
        self.launchSpeedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.launchSpeedSlider.valueChanged.connect(self.generateGraph)
        self.updateSpeedLabel(15000)   

        self.orbitTimeSlider.setRange(0, 2000)
        self.orbitTimeSlider.setValue(500)
        self.orbitTimeSlider.valueChanged.connect(self.updateOrbitTimeLabel)
        self.orbitTimeSlider.valueChanged.connect(self.generateGraph)
        self.updateOrbitTimeLabel(500)

        self.orbitRadiusSlider.setRange(0, 100000)
        self.orbitRadiusSlider.setValue(20000)
        self.orbitRadiusSlider.valueChanged.connect(self.updateOrbitRadiusLabel)
        self.orbitRadiusSlider.valueChanged.connect(self.generateGraph)
        self.updateOrbitRadiusLabel(20000)

        self.massSlider.setRange(1, 100000)
        self.massSlider.setValue(7000)
        self.massSlider.valueChanged.connect(self.updateMassLabel)
        self.massSlider.valueChanged.connect(self.generateGraph)
        self.updateMassLabel(7000)

        self.planetRadiusSlider.setRange(1, 100000)
        self.planetRadiusSlider.setValue(6371)
        self.planetRadiusSlider.valueChanged.connect(self.updatePlanetRadiusLabel)
        self.planetRadiusSlider.valueChanged.connect(self.generateGraph)
        self.updatePlanetRadiusLabel(5000)

        self.timeStepSlider.setRange(100, 1000)
        self.timeStepSlider.setValue(150)
        self.timeStepSlider.valueChanged.connect(self.updateTimeStepLabel)
        self.timeStepSlider.valueChanged.connect(self.generateGraph)
        self.updateTimeStepLabel(150)

        self.maxSimLengthSlider.setRange(10000, 100000)
        self.maxSimLengthSlider.setValue(80000)
        self.maxSimLengthSlider.valueChanged.connect(self.updateSimulationTimeLabel)
        self.maxSimLengthSlider.valueChanged.connect(self.generateGraph)
        self.updateSimulationTimeLabel(80000)

        # link lineedit labels to sliders
        self.launchSpeedLineEdit.textChanged.connect(self.updateSpeedLabel)
        self.launchSpeedLineEdit.textChanged.connect(self.generateGraph)
        self.orbitTimeLineEdit.textChanged.connect(self.updateOrbitTimeLabel)
        self.orbitTimeLineEdit.textChanged.connect(self.generateGraph)
        self.orbitRadiusLineEdit.textChanged.connect(self.updateOrbitRadiusLabel)
        self.orbitRadiusLineEdit.textChanged.connect(self.generateGraph)
        self.massLineEdit.textChanged.connect(self.updateMassLabel)
        self.massLineEdit.textChanged.connect(self.generateGraph)
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)
        self.timeStepLineEdit.textChanged.connect(self.generateGraph)
        self.maxSimLengthLineEdit.textChanged.connect(self.updateSimulationTimeLabel)
        self.maxSimLengthLineEdit.textChanged.connect(self.generateGraph)

        # set earth buttons
        self.setEarthMassButton.clicked.connect(self.setEarthMass)
        self.setEarthRadiusButton.clicked.connect(self.setEarthPlanetRadius)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.extInfoWindow = ExtInfoWindow()
        self.extInfoWindow.show()
        self.close()
        
    def updateSpeedLabel(self, value):
        try:
            self.launchSpeedSlider.setValue(int(value))
            self.launchSpeedSliderLabel.setText(str(value) + " kmh⁻¹")
        except: # invalid input
            self.launchSpeedSlider.setValue(0)
            self.launchSpeedSliderLabel.setText("Invalid input from text input mode")

        self.launchSpeedLineEdit.setText(str(value))

    def updateOrbitTimeLabel(self, value):
        try:
            self.orbitTimeSlider.setValue(int(value))
            self.orbitTimeSliderLabel.setText(str(value) + " mins")
        except: # invalid input
            self.orbitTimeSlider.setValue(0)
            self.orbitTimeSliderLabel.setText("Invalid input from text input mode")

        self.orbitTimeLineEdit.setText(str(value))

    def updateOrbitRadiusLabel(self, value):
        try:
            self.orbitRadiusSlider.setValue(int(value))
            self.orbitRadiusSliderLabel.setText(str(value) + " km")
        except: # invalid input
            self.orbitRadiusSlider.setValue(0)
            self.orbitRadiusSliderLabel.setText("Invalid input from text input mode")

        self.orbitRadiusLineEdit.setText(str(value))

    def updateMassLabel(self, value):
        try:
            self.massSlider.setValue(int(value))
            self.massSliderLabel.setText(str(value) + " × 10²¹ /kg")
        except: # invalid input
            self.massSlider.setValue(0)
            self.massSliderLabel.setText("Invalid input from text input mode")

        self.massLineEdit.setText(str(value))

    def setEarthMass(self):
        self.updateMassLabel(5972)

    def updatePlanetRadiusLabel(self, value):
        try:
            self.planetRadiusSlider.setValue(int(value))
            self.planetRadiusSliderLabel.setText(str(value) + " /km")
        except: # invalid input
            self.planetRadiusSlider.setValue(0)
            self.planetRadiusSliderLabel.setText("Invalid input from text input mode")

        self.planetRadiusLineEdit.setText(str(value))

    def setEarthPlanetRadius(self):
        self.updatePlanetRadiusLabel(6371)


    def updateTimeStepLabel(self, value):
        try:
            self.timeStepSlider.setValue(int(value))
            self.timeStepSliderLabel.setText(str(value) + " s")
        except: # invalid input
            self.timeStepSlider.setValue(0)
            self.timeStepSliderLabel.setText("Invalid input from text input mode")

        self.timeStepLineEdit.setText(str(value))

    def updateSimulationTimeLabel(self, value):
        try:
            self.maxSimLengthSlider.setValue(int(value))
            self.maxSimLengthSliderLabel.setText(str(value) + " s")
        except: # invalid input
            self.maxSimLengthSlider.setValue(0)
            self.maxSimLengthSliderLabel.setText("Invalid input from text input mode")

        self.maxSimLengthLineEdit.setText(str(value))

    def text_mode(self, checked):
        self.text_mode_on = checked
        self.launchSpeedSlider.setVisible(not checked)
        self.orbitTimeSlider.setVisible(not checked)
        self.orbitRadiusSlider.setVisible(not checked)
        self.massSlider.setVisible(not checked)
        self.planetRadiusSlider.setVisible(not checked)
        self.timeStepSlider.setVisible(not checked)
        self.maxSimLengthSlider.setVisible(not checked)
        self.launchSpeedSliderLabel.setVisible(not checked)
        self.orbitTimeSliderLabel.setVisible(not checked)
        self.orbitRadiusSliderLabel.setVisible(not checked)
        self.massSliderLabel.setVisible(not checked)
        self.planetRadiusSliderLabel.setVisible(not checked)
        self.timeStepSliderLabel.setVisible(not checked)
        self.maxSimLengthSliderLabel.setVisible(not checked)
        self.launchSpeedLineEdit.setVisible(checked)
        self.orbitTimeLineEdit.setVisible(checked)
        self.orbitRadiusLineEdit.setVisible(checked)
        self.massLineEdit.setVisible(checked)
        self.planetRadiusLineEdit.setVisible(checked)
        self.timeStepLineEdit.setVisible(checked)
        self.maxSimLengthLineEdit.setVisible(checked)

    def generateGraph(self):
        try:
            if self.text_mode_on:
                self.plot(chals.extensionPath, [float(self.launchSpeedLineEdit.text()),
                                            float(self.orbitTimeLineEdit.text()),
                                            float(self.orbitRadiusLineEdit.text()),
                                            float(self.massLineEdit.text()),
                                            float(self.planetRadiusLineEdit.text()),
                                            float(self.timeStepLineEdit.text()),
                                            float(self.maxSimLengthLineEdit.text())])
                analytics = chals.extensionPath(None,
                                            float(self.launchSpeedLineEdit.text()),
                                            float(self.orbitTimeLineEdit.text()),
                                            float(self.orbitRadiusLineEdit.text()),
                                            float(self.massLineEdit.text()),
                                            float(self.planetRadiusLineEdit.text()),
                                            float(self.timeStepLineEdit.text()),
                                            float(self.maxSimLengthLineEdit.text()))
            else:
                self.plot(chals.extensionPath, [float(self.launchSpeedSlider.value()),
                                            float(self.orbitTimeSlider.value()),
                                            float(self.orbitRadiusSlider.value()),
                                            float(self.massSlider.value()),
                                            float(self.planetRadiusSlider.value()),
                                            float(self.timeStepSlider.value()),
                                            float(self.maxSimLengthSlider.value())])  
                analytics = chals.extensionPath(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.orbitTimeSlider.value()),
                                            float(self.orbitRadiusSlider.value()),
                                            float(self.massSlider.value()),
                                            float(self.planetRadiusSlider.value()),
                                            float(self.timeStepSlider.value()),
                                            float(self.maxSimLengthSlider.value()))
            if analytics[0]:
                self.simEndCauseLabel.setText("Simulation End Cause: Satellite Collided with Earth (Time: " + str(round(analytics[1], 5)) + "s)")
            else:
                self.simEndCauseLabel.setText("Simulation End Cause: Exceeded Max Simulation Length")

        except Exception as error: # invalid input
            # print(error)
            # self.plot(chals.extensionPath, [1, 1, 1, 1, 0, 0])
            pass

    def plot(self, function, data):
        try:
            self.graphLayout.removeWidget(self.canvas)
            self.graphLayout.update()
        except:
            pass

        self.fig = Figure(figsize = (5, 5), 
                        dpi = 100) 
        function(self.fig, *data)
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.graphLayout.addWidget(self.canvas)
        self.canvas.draw()

# Extension info
class ExtInfoWindow(QMainWindow, extensionInfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)
        self.codeButton.clicked.connect(self.showCode)

    def back(self):
        self.extWindow = ExtWindow()
        self.extWindow.show()
        self.close()

    def showCode(self):
        self.extCodeInfoWindow = ExtCodeInfoWindow()
        self.extCodeInfoWindow.show()
        self.close()

# Extension code info
class ExtCodeInfoWindow(QMainWindow, extensionCodeInfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 768)
        self.move(0, 0)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.extInfoWindow = ExtInfoWindow()
        self.extInfoWindow.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("BPhO Computational Challenge 2024")
    window.show()
    sys.exit(app.exec_())
