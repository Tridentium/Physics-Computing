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
    base_frame.pack_forget()
    menu_frame_blank.pack_forget()
    menu_frame_challenges.pack_forget()
    menu_frame_information.pack_forget()

    global challenges_heading_frame
    challenges_heading_frame = ttk.Frame(root)
    challenges_heading_frame.pack(side=tk.TOP)

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

    global back_to_menu_frame
    back_to_menu_frame = ttk.Frame(root)
    back_to_menu_frame.pack(side=tk.TOP)


    challenges_heading = ttk.Label(challenges_heading_frame, text = "Projectiles Challenges")
    challenges_heading.config(font=main_font_subheading)
    challenges_heading.pack(side=tk.LEFT)

    plot_button_1 = Button(master = chal1_frame,  
                     command = lambda: [plot(chals.chal1ProjPath, [20, 45, 9.81, 2, 0.02]), chal1_user_inputs()], 
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

    back_to_menu_button = Button(master = back_to_menu_frame,  
                        command = lambda: [hide_challenges_menu(),
                                           show_main_menu()], 
                        height = 1,  
                        width = 24,
                        text = "Back to Main Menu") 
    back_to_menu_button.config(font=main_font)
    back_to_menu_button.pack(side=tk.LEFT)


def hide_challenges_menu():
    challenges_heading_frame.pack_forget()
    chal1_frame.pack_forget()
    chal2_frame.pack_forget()
    chal3_frame.pack_forget()
    chal4_frame.pack_forget()
    chal5_frame.pack_forget()
    chal6_frame.pack_forget()
    chal7_frame.pack_forget()
    chal8_frame.pack_forget()
    chal9_frame.pack_forget()
    back_to_menu_frame.pack_forget()


def show_main_menu():
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

    menu_heading = ttk.Label(base_frame,
                             text="MODELLING PROJECTILES",
                             font=main_font_heading)
    menu_heading.pack()
    menu_subheading = ttk.Label(base_frame,
                                text="BPhO Computational Challenge 2024",
                                font=main_font_subheading)
    menu_subheading.pack()

    challenges_button = Button(master=menu_frame_challenges,
                            command = lambda: display_challenges(),
                            height = 1,
                            width = 12,
                            text = "Challenges",
                            font = main_font_subsubheading)
    challenges_button.pack(side=tk.TOP)



def plot(function, data):
    # frames
    global graph_frame
    graph_frame = ttk.Frame(root)
    graph_frame.pack(side=tk.TOP)

    global entry_frame
    entry_frame = ttk.Frame(root)
    entry_frame.pack(side=tk.TOP)

    back_frame = ttk.Frame(root)
    back_frame.pack(side=tk.TOP)

    # figure
    global fig
    fig = Figure(figsize = (5, 5), 
                    dpi = 100) 

    plot1 = fig.add_subplot(111)
    # list of squares 
    
    function(plot1, *data)

    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    global canvas
    canvas = FigureCanvasTkAgg(fig, 
                                master = graph_frame)   
    canvas.draw() 

    # hide menu buttons
    hide_challenges_menu()

    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar 
    # toolbar = NavigationToolbar2Tk(canvas, 
    #                                 root) 
    # toolbar.update() 

    # placing the toolbar on the Tkinter window 
    # canvas.get_tk_widget().pack()

    back_to_challenges_button = Button(master = back_frame,  
                        command = lambda: [graph_frame.pack_forget(),
                                           entry_frame.pack_forget(),
                                           back_frame.pack_forget(),
                                           display_challenges()], 
                        height = 1,  
                        width = 24,
                        text = "Back to Challenges") 
    back_to_challenges_button.config(font=main_font)
    back_to_challenges_button.pack(side=tk.LEFT)


def update_plot(projPath, data):
    global canvas
    for graph in graph_frame.winfo_children():
        fig.clear()
        graph.destroy()
    plot1 = fig.add_subplot(111)
    projPath(plot1, *data)
    canvas = FigureCanvasTkAgg(fig, 
                                master = graph_frame)   
    canvas.draw() 
    canvas.get_tk_widget().pack()


def chal1_user_inputs():
    speed_frame = ttk.Frame(entry_frame)
    speed_frame.pack(side=tk.TOP)
    angle_frame = ttk.Frame(entry_frame)
    angle_frame.pack(side=tk.TOP)
    g_frame = ttk.Frame(entry_frame)
    g_frame.pack(side=tk.TOP)
    height_frame = ttk.Frame(entry_frame)
    height_frame.pack(side=tk.TOP)
    time_step_frame = ttk.Frame(entry_frame)
    time_step_frame.pack(side=tk.TOP)

    speed_label = tk.Label(speed_frame,
                           text="Launch Speed /ms^-1: ",
                           font=main_font)
    speed_label.pack(side=tk.LEFT)
    angle_label = tk.Label(angle_frame,
                           text="Launch Angle /deg: ",
                           font=main_font)
    angle_label.pack(side=tk.LEFT)
    g_label = tk.Label(g_frame,
                       text="g /ms^-2: ",
                       font=main_font)
    g_label.pack(side=tk.LEFT)
    height_label = tk.Label(height_frame,
                            text="Launch Height /m): ",
                            font=main_font)
    height_label.pack(side=tk.LEFT)
    time_step_label = tk.Label(time_step_frame,
                               text="Time Step /s: ",
                               font=main_font)
    time_step_label.pack(side=tk.LEFT)

    launch_speed = tk.DoubleVar()
    launch_angle = tk.DoubleVar()
    g = tk.DoubleVar()
    launch_height = tk.DoubleVar()
    time_step = tk.DoubleVar()

    launch_speed.set(20.0)
    launch_angle.set(45.0)
    g.set(9.81)
    launch_height.set(2.0)
    time_step.set(0.02)

    launch_speed_entry = tk.Entry(speed_frame,
                            font=main_font,
                            textvariable=launch_speed)
    launch_speed_entry.pack(side=tk.LEFT)
    launch_angle_entry = tk.Entry(angle_frame,
                            font=main_font,
                            textvariable=launch_angle)
    launch_angle_entry.pack(side=tk.LEFT)
    g_entry = tk.Entry(g_frame,
                 font=main_font,
                 textvariable=g)
    g_entry.pack(side=tk.LEFT)
    launch_height_entry = tk.Entry(height_frame,
                             font=main_font,
                             textvariable=launch_height)
    launch_height_entry.pack(side=tk.LEFT)
    time_step_entry = tk.Entry(time_step_frame,
                         font=main_font,
                         textvariable=time_step)
    time_step_entry.pack(side=tk.LEFT)

    plot_chal1 = Button(master = entry_frame,  
                     command = lambda: [update_plot(chals.chal1ProjPath, [launch_speed.get(),
                                                                   launch_angle.get(),
                                                                   g.get(),
                                                                   launch_height.get(),
                                                                   time_step.get()])],
                     height = 1,  
                     width = 12, 
                     text = "Update Plot",
                     font=main_font)
    plot_chal1.pack()


if __name__ == "__main__":
    show_main_menu()
    root.mainloop()
