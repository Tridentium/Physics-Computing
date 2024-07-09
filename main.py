import Testing as chals
from tkinter import ttk
from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

main_font = ("Modern", 16)
main_bold_font = ("Modern", 16, "bold")
main_font_heading = ("Modern", 36, "bold")
main_font_subheading = ("Modern", 28, "bold")
main_font_subsubheading = ("Modern", 22, "bold")

root = Tk()
root.title("BPhO Computational Challenge 2024")
root.state('zoomed')
root.configure(bg="#009dba")

def display_challenges():
    plot_button_1 = Button(master = chal1_frame,  
                     command = lambda: plot(chals.chal1ProjPath, [20, 45, 9.81, 2, 0.02]), 
                     height = 1,  
                     width = 12, 
                     text = "Challenge 1",
                     font=main_font)
    plot_button_1.pack(side=tk.LEFT)

    plot_button_2 = Button(master = chal2_frame,  
                        command = lambda: plot(chals.chal2ProjPath, [10, 42, 9.81, 1, 0.02]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 2") 
    plot_button_2.config(font=main_font)
    plot_button_2.pack(side=tk.LEFT)

    plot_button_3 = Button(master = chal3_frame,  
                        command = lambda: plot(chals.chal3ProjPath, [150, 9.81, 0, 0.01, 1000, 300]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 3")
    plot_button_3.config(font=main_font)
    plot_button_3.pack(side=tk.LEFT)

    plot_button_4 = Button(master = chal4_frame,  
                        command = lambda: plot(chals.chal4ProjPath, [10, 2, 9.81, 60]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 4") 
    plot_button_4.config(font=main_font)
    plot_button_4.pack(side=tk.LEFT)

    plot_button_5 = Button(master = chal5_frame,  
                        command = lambda: plot(chals.chal5ProjPath, [1.3063*115, 9.81, 0, 1000, 300]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 5") 
    plot_button_5.config(font=main_font)
    plot_button_5.pack(side=tk.LEFT)

    plot_button_6 = Button(master = chal6_frame,  
                        command = lambda: plot(chals.chal6ProjPath, [10, 2, 9.81, 60]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 6") 
    plot_button_6.config(font=main_font)
    plot_button_6.pack(side=tk.LEFT)

    plot_button_7 = Button(master = chal7_frame,  
                        command = lambda: plot(chals.chal7ProjPath, [10, 10]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 7") 
    plot_button_7.config(font=main_font)
    plot_button_7.pack(side=tk.LEFT)

    plot_button_8 = Button(master = chal8_frame,  
                        command = lambda: plot(chals.chal8ProjPath, [5, 0.7, 45, 10, 9.81, 6, 0.02]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 8") 
    plot_button_8.config(font=main_font)
    plot_button_8.pack(side=tk.LEFT)

    plot_button_9 = Button(master = chal9_frame,  
                        command = lambda: plot(chals.chal9ProjPath, [30, 20, 2, 9.81, 0.3, 0.007854, 1, 0.1, 0.01]), 
                        height = 1,  
                        width = 12,
                        text = "Challenge 9") 
    plot_button_9.config(font=main_font)
    plot_button_9.pack(side=tk.LEFT)    


def hide_menu():
    base_frame.pack_forget()
    menu_frame_blank.pack_forget()
    menu_frame_challenges.pack_forget()
    menu_frame_information.pack_forget()
    chal1_frame.pack_forget()
    chal2_frame.pack_forget()
    chal3_frame.pack_forget()
    chal4_frame.pack_forget()
    chal5_frame.pack_forget()
    chal6_frame.pack_forget()
    chal7_frame.pack_forget()
    chal8_frame.pack_forget()
    chal9_frame.pack_forget()


def show_menu():
    global base_frame
    base_frame = ttk.Frame(root)
    base_frame.pack(side=tk.TOP)

    global menu_frame_blank
    menu_frame_blank = ttk.Frame(root)
    menu_frame_blank.pack(side=tk.TOP)

    global menu_frame_challenges
    menu_frame_challenges = ttk.Frame(root)
    menu_frame_challenges.pack(side=tk.TOP)

    global menu_frame_information
    menu_frame_information = ttk.Frame(root)
    menu_frame_information.pack(side=tk.TOP)

    global chal1_frame
    chal1_frame = ttk.Frame(root)
    chal1_frame.pack(side=tk.TOP)

    global chal2_frame
    chal2_frame = ttk.Frame(root)
    chal2_frame.pack(side=tk.TOP)

    global chal3_frame
    chal3_frame = ttk.Frame(root)
    chal3_frame.pack(side=tk.TOP)

    global chal4_frame
    chal4_frame = ttk.Frame(root)
    chal4_frame.pack(side=tk.TOP)

    global chal5_frame
    chal5_frame = ttk.Frame(root)
    chal5_frame.pack(side=tk.TOP)

    global chal6_frame
    chal6_frame = ttk.Frame(root)
    chal6_frame.pack(side=tk.TOP)

    global chal7_frame
    chal7_frame = ttk.Frame(root)
    chal7_frame.pack(side=tk.TOP)

    global chal8_frame
    chal8_frame = ttk.Frame(root)
    chal8_frame.pack(side=tk.TOP)

    global chal9_frame
    chal9_frame = ttk.Frame(root)
    chal9_frame.pack(side=tk.TOP)

    menu_heading = ttk.Label(base_frame, text = "MODELLING PROJECTILES")
    menu_heading.config(font=main_font_heading)
    menu_heading.pack()
    menu_subheading = ttk.Label(base_frame, text = "BPhO Computational Challenge 2024")
    menu_subheading.config(font=main_font_subheading)
    menu_subheading.pack()

    challenges_button = Button(master=menu_frame_challenges,
                            command = lambda: display_challenges(),
                            height = 1,
                            width = 12,
                            text = "Challenges",
                            font = main_font_subsubheading)
    challenges_button.pack(side=tk.TOP)



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

    # hide menu buttons
    hide_menu()

    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 

    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                    root) 
    toolbar.update() 

    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()


if __name__ == "__main__":
    show_menu()
    root.mainloop()
