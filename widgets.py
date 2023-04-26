import tkinter as tk
# note ttk provies more visually appealing widgets and is an extension of tkinter
# from tkinter import ttk
import ttkbootstrap as ttk # installed bootstrap for more visuals

def convert():
    """Logic for distance conversion"""
    print(entry_int.get()) # test, grabs number show in console
    mile_input = entry_int.get()
    km_output = mile_input * 1.61 # 1 mile is 1.61 km
    # Set the value of the output string variable to the result, rounded to 2 decimal places
    output_string.set("{:.2f} km".format(km_output))

# window... note the Tk() consructor method called on tk(tinkter)
# because bootstrap installed we can add a theme and more with the new ttkbootstrap
# window = tk.Tk()
window = ttk.Window(themename = "journal")
window.title("Miles to Kilometers Converter")
# size window
window.geometry("600x450")

# title ... note the 'master' parameter... it indicates the parent is 'window'
# and that this label will be a child of the 'window object'
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 24 bold")
#note pack() method just like adding children to layout
#NOTE pack method places widgets below each other
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
#note entry AND button will be child of input frame. Input frame is packaged with those
#two widgets and then sent to the window where the window is the parent of input frame
entry_int = tk.IntVar() #declaring variable to be of type int
entry = ttk.Entry(master = input_frame, textvariable = entry_int) # values stored in variable entryInt
button = ttk.Button(master = input_frame, text = 'Convert', command = convert) # note we add eventlistner function with command also note you only want to pass NOT - call convert()
#note you must pack the children of entry and button into the Frame
entry.pack(side = 'left', padx = 10) # adding styles
button.pack(side = 'left')

#once everything packaged pack it all up
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar() #stores string
output_label = ttk.Label(
    master = window,
    text = 'Output: ',
    font = "Calibri 24 ",
    textvariable = output_string) # eventlister overides the text above
output_label.pack(pady = 5)

#run Main loop
window.mainloop()
