import Testing as chals
from tkinter import ttk
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 


root = Tk()

frame = ttk.Frame(root, padding = 20)

def plot(function, data):
    fig = Figure(figsize = (5, 5), 
                    dpi = 100) 


    plot1 = fig.add_subplot(111)
    # list of squares 
    
    function(plot1, *data)

    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                                master = root)   
    canvas.draw() 

    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 

    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                    root) 
    toolbar.update() 

    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()

ttk.Label(frame, text = "Graphs")
plot_button = Button(master = root,  
                     command = lambda: plot(chals.chal1ProjPath, [20, 45, 9.81, 2, 0.02]), 
                     height = 2,  
                     width = 10, 
                     text = "Graph1") 
plot_button.pack()
plot_button1 = Button(master = root,  
                     command = lambda: plot(chals.chal2ProjPath, [10, 42, 9.81, 1, 0.02]), 
                     height = 2,  
                     width = 10, 
                     text = "Graph2") 
plot_button1.pack()


root.mainloop()
