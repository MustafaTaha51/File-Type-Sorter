from sort_functions import *
from customtkinter import *
from tkinter import filedialog

# Function for switching between light and dark mode
def switch_mode():
    # Get button state
    switchState = state.get()

    # Switch mode based on current button state
    if switchState:
        btnSort.configure(bg_color=grey)
        switch.configure(bg_color=grey, text_color="white")
        label.configure(fg_color=grey, text_color="white")
        dropdown.configure(bg_color=grey, fg_color=grey, text_color="white")
        app._set_appearance_mode("dark")
    else:
        btnSort.configure(bg_color=kindaWhite)
        switch.configure(bg_color=kindaWhite, text_color="black")
        label.configure(fg_color=kindaWhite, text_color="black")
        dropdown.configure(bg_color=kindaWhite, fg_color=kindaWhite, text_color="black")
        app._set_appearance_mode("light")


# Function that prompts user to input a path and then runs sorting function
def prompt_and_sort():
    # Obtain file path from user
    selectedPath = filedialog.askdirectory()

    # Check if user gave input or cancelled
    if not selectedPath:
        print("Path was not selected")
    else:
        print(f"Selected path: {selectedPath}")

        # Sort files at path
        sort_files(selectedPath)


# Initialising GUI with 300x400 dimensions and variables for dark mode switch
app = CTk()
app.geometry("300x400")
app.resizable(width=False, height=False)
state = IntVar()

# Hexadecimal values for grey and light background
grey = "#282424"
kindaWhite = "#f0ecec"

# Creating and placing elements
btnSort = CTkButton(master=app, text="Sort", corner_radius=32, border_width=2, command=prompt_and_sort)
label = CTkLabel(master=app, text="Click To Sort Files", font=("Arial", 20),)
switch = CTkSwitch(master=app, text="Dark Mode", variable=state, command=switch_mode)
dropdown = CTkComboBox(master=app, values=["File Type", "Date of Creation"], dropdown_fg_color=kindaWhite)

label.place(relx=0.5, rely=0.4, anchor="center")
dropdown.place(relx=0.5, rely=0.5, anchor="center")
btnSort.place(relx=0.5, rely=0.6, anchor="center")
switch.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()