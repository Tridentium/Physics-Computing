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
        self.setGeometry(100, 100, 760, 650)
        
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
        self.setGeometry(100, 100, 760, 650)

        self.pushButton_4.clicked.connect(self.back) # "back"
        self.pushButton_2.clicked.connect(self.open_chal1) # "challenge 1"
        self.pushButton_3.clicked.connect(self.open_chal2) # "challenge 2"
        self.pushButton.clicked.connect(self.open_chal3) # "challenge 3"
        self.pushButton_5.clicked.connect(self.open_chal4) # "challenge 4"
        self.pushButton_6.clicked.connect(self.open_chal5) # "challenge 5"
        self.pushButton_7.clicked.connect(self.open_chal6) # "challenge 6"
        self.pushButton_8.clicked.connect(self.open_chal7) # "challenge 7"
        self.pushButton_9.clicked.connect(self.open_chal8) # "challenge 8"
        

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

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
                self.plot(chals.chal1ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.chal1ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
        except: # invalid input
            self.plot(chals.chal1ProjPath, [0, 0, 0, 0, 0])

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

# challenge 1 info
class Chal1InfoWindow(QMainWindow, challenge1InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal1Window = Chal1Window()
        self.chal1Window.show()
        self.close()


# challenge 2
class Chal2Window(QMainWindow, challenge2Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

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
                self.plot(chals.chal2ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.chal2ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
                
            analytics = chals.chal2ProjPath(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSlider.value()),
                                            float(self.launchHeightSlider.value()),
                                            float(self.timeStepSlider.value()))
            self.rangeLabel.setText("Range: " + str(round(analytics[0], 5)) + " m")
            self.apogeeLabel.setText("Apogee: (" + str(round(analytics[1], 5)) + " m, " + str(round(analytics[2], 5)) + " m)")
            self.flightTimeLabel.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")

        except Exception as error: # invalid input
            # print(error)
            self.plot(chals.chal2ProjPath, [0, 0, 0, 0, 0])

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

# challenge 2 info
class Chal2InfoWindow(QMainWindow, challenge2InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal2Window = Chal2Window()
        self.chal2Window.show()
        self.close()

        
# challenge 3
class Chal3Window(QMainWindow, challenge3Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

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
                self.plot(chals.chal3ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text()),
                                                float(self.XLineEdit.text()),
                                                float(self.YLineEdit.text())])
            else:
                self.plot(chals.chal3ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value()),
                                                float(self.XSlider.value()),
                                                float(self.YSlider.value())])
                
            analytics = chals.chal3ProjPath(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.gSlider.value()),
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
            self.plot(chals.chal2ProjPath, [0, 0, 0, 0, 0])

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

# challenge 3 info
class Chal3InfoWindow(QMainWindow, challenge3InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal3Window = Chal3Window()
        self.chal3Window.show()
        self.close()


class Chal4Window(QMainWindow, challenge4Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal2InfoWindow = Chal4InfoWindow()
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
                self.plot(chals.chal4ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.chal4ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
                
            analytics = chals.chal4ProjPath(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSlider.value()),
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
            self.plot(chals.chal4ProjPath, [1, 0, 1, 1, 1])

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

# challenge 4 info
class Chal4InfoWindow(QMainWindow, challenge4InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal4Window = Chal4Window()
        self.chal4Window.show()
        self.close()


# challenge 5
class Chal5Window(QMainWindow, challenge5Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

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
                self.plot(chals.chal5ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text()),
                                                float(self.XLineEdit.text()),
                                                float(self.YLineEdit.text())])
            else:
                self.plot(chals.chal5ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value()),
                                                float(self.XSlider.value()),
                                                float(self.YSlider.value())])

        except Exception as error: # invalid input
            self.plot(chals.chal5ProjPath, [1, 1, 1, 1, 1, 1])

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

# challenge 5 info
class Chal5InfoWindow(QMainWindow, challenge5InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal5Window = Chal5Window()
        self.chal5Window.show()
        self.close()


class Chal6Window(QMainWindow, challenge6Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

        # plot default graph
        self.generateGraph()

    def back(self):
        self.challengesWindow = ChallengesWindow()
        self.challengesWindow.show()
        self.close()

    def displayInfo(self):
        self.chal2InfoWindow = Chal4InfoWindow()
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
                self.plot(chals.chal6ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.chal6ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.timeStepSlider.value())])
                
            analytics = chals.chal6ProjPath(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSlider.value()),
                                            float(self.launchHeightSlider.value()),
                                            float(self.timeStepSlider.value()))
            
            self.rangeLabel.setText("Range: " + str(round(analytics[0], 5)) + " m")
            self.apogeeLabel.setText("Apogee: (" + str(round(analytics[1], 5)) + " m, " + str(round(analytics[2], 5)) + " m)")
            self.flightTimeLabel.setText("Time of Flight: " + str(round(analytics[3], 5)) + " s")
            self.rangeLabel_2.setText("Max Range: " + str(round(analytics[4], 5)) + " m")
            self.apogeeLabel_2.setText("Apogee: (" + str(round(analytics[5], 5)) + " m, " + str(round(analytics[6], 5)) + " m)")
            self.flightTimeLabel_2.setText("Time of Flight: " + str(round(analytics[7], 5)) + " s")
            self.distanceLabel.setText("Distance: " + str(round(analytics[8], 5)) + "m")
            self.distanceLabel_2.setText("MaxDistance: " + str(round(analytics[9], 5)) + "m")

        except Exception as error: # invalid input
            print(error)
            self.plot(chals.chal6ProjPath, [1, 0, 1, 1, 1])

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

# challenge 6 info
class Chal6InfoWindow(QMainWindow, challenge6InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal6Window = Chal6Window()
        self.chal6Window.show()
        self.close()


# challenge 7
class Chal7Window(QMainWindow, challenge7Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

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
                self.plotLeft(chals.chal7ProjPathLeft, [float(self.launchSpeedLineEdit.text()),
                                                    float(self.gLineEdit.text()),
                                                    float(self.timeStepLineEdit.text())])
                self.plotRight(chals.chal7ProjPathRight, [float(self.launchSpeedLineEdit.text()),
                                                    float(self.gLineEdit.text()),
                                                    float(self.timeStepLineEdit.text())])
            else:
                self.plotLeft(chals.chal7ProjPathLeft, [float(self.launchSpeedSlider.value()),
                                                    float(self.gSlider.value()),
                                                    float(self.timeStepSlider.value())])
                self.plotRight(chals.chal7ProjPathRight, [float(self.launchSpeedSlider.value()),
                                                    float(self.gSlider.value()),
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

# challenge 7 info
class Chal7InfoWindow(QMainWindow, challenge7InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal7Window = Chal7Window()
        self.chal7Window.show()
        self.close()


# challenge 8
class Chal8Window(QMainWindow, challenge8Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # back button
        self.backButton.clicked.connect(self.back)

        # info button
        self.infoButton.clicked.connect(self.displayInfo)

        # restitution coefficient changed by slider
        global RestitutionCoefficientChangedBySlider
        RestitutionCoefficientChangedBySlider = True

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
        self.maxBouncesSlider.setRange(0, 10)
        self.maxBouncesSlider.setValue(6)
        self.maxBouncesSlider.valueChanged.connect(self.updateMaxBouncesLabel)
        self.maxBouncesSlider.valueChanged.connect(self.generateGraph)
        self.updateMaxBouncesLabel(6)

        self.restitutionCoefficientSlider.setRange(0, 100)
        self.restitutionCoefficientSlider.setValue(70)
        self.restitutionCoefficientSlider.valueChanged.connect(self.changedRestitutionCoefficientSlider)
        self.restitutionCoefficientSlider.valueChanged.connect(self.generateGraph)
        self.updateRestitutionCoefficientLabel(70)

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
        self.timeStepLineEdit.textChanged.connect(self.updateTimeStepLabel)

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
    
    def updateMaxBouncesLabel(self, value):
        try:
            self.maxBouncesSlider.setValue(int(value))
            self.maxBouncesSliderLabel.setText(str(value))
        except: # invalid input
            self.maxBouncesSlider.setValue(0)
            self.maxBouncesSliderLabel.setText("Invalid input from text input mode")

        self.maxBouncesLineEdit.setText(str(value))

    def changedRestitutionCoefficientSlider(self, value):
        global RestitutionCoefficientChangedBySlider
        RestitutionCoefficientChangedBySlider = True
        self.updateRestitutionCoefficientLabel(value)
    
    def changedRestitutionCoefficientLineEdit(self, value):
        global RestitutionCoefficientChangedBySlider
        RestitutionCoefficientChangedBySlider = False
        self.updateRestitutionCoefficientLabel(value)

    def updateRestitutionCoefficientLabel(self, value):
        global RestitutionCoefficientChangedBySlider
        if RestitutionCoefficientChangedBySlider:
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
                self.plot(chals.chal8ProjPath, [float(self.launchSpeedLineEdit.text()),
                                                float(self.restitutionCoefficientLineEdit.text()),
                                                float(self.launchAngleLineEdit.text()),
                                                float(self.gLineEdit.text()),
                                                float(self.launchHeightLineEdit.text()),
                                                float(self.maxBouncesLineEdit.text()),
                                                float(self.timeStepLineEdit.text())])
            else:
                self.plot(chals.chal8ProjPath, [float(self.launchSpeedSlider.value()),
                                                float(self.restitutionCoefficientSlider.value() * 10),
                                                float(self.launchAngleSlider.value()),
                                                float(self.gSlider.value()),
                                                float(self.launchHeightSlider.value()),
                                                float(self.maxBouncesSlider.value()),
                                                float(self.timeStepSlider.value())])
            
            analytics = chals.chal8ProjPath(None,
                                            float(self.launchSpeedSlider.value()),
                                            float(self.restitutionCoefficientLineEdit.value()),
                                            float(self.launchAngleSlider.value()),
                                            float(self.gSlider.value()),
                                            float(self.launchHeightSlider.value()),
                                            float(self.maxBouncesSlider.value()),
                                            float(self.timeStepSlider.value()))
            
            self.flightTimeLabel.setText("Time of Flight for\nMax Number of\nBounces:\n\n" + str(round(analytics[1], 5)) + " s")

        except Exception as error: # invalid input
            # print(error)
            self.plot(chals.chal8ProjPath, [0, 1, 0, 1, 1, 0, 1])

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

# challenge 8 info
class Chal8InfoWindow(QMainWindow, challenge8InfoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.back)

    def back(self):
        self.chal8Window = Chal8Window()
        self.chal8Window.show()
        self.close()


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
