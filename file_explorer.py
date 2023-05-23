from tkinter import *
from tkinter import filedialog


# Function for opening the file explorer window
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select your image",
                                          filetypes = (("png",
                                                        "*.png"),
                                                       ("jpg",
                                                        "*.jpg")))
    
    # Change label contents
    label_file_explorer.configure(text = "File opened: " + filename)
    button_exit.configure(text= "Validate file")
        
# Create root window
window = Tk()

# COnfigure window and buttons
window.title("File Explorer")
window.config(background = "white")
label_file_explorer = Label(window, text = "File Explorer", fg = "blue")
button_explore = Button(window, text = "Browse Files", command = browseFiles)
button_exit = Button(window, text = "Exit", command = window.destroy)

#Make the window sticky for every case
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight= 1)
window.grid_rowconfigure(2, weight= 1)
window.grid_columnconfigure(0, weight=1)

# Grid method is chosen for placing the widgets at respective positions
# in a table like structure by specifying rows and columns
default_button_grid = {"padx": 10, "pady": 10, "sticky": "nsew"}
label_file_explorer.grid(row=0, column=0, **default_button_grid)
button_explore.grid(row=1, column=0, **default_button_grid)
button_exit.grid(row=2, column=0, **default_button_grid)
  
# Let the window wait for any events
window.mainloop()

# Create global variable to set in browseFiles function
filename = ""
print("File path : " + filename)