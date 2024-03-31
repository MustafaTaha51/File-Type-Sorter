import os
from sys import argv
from magic import Magic
from shutil import move
from customtkinter import *
from tkinter import filedialog

selectedPath = None

app = CTk()
app.geometry("300x400")
state = IntVar()

# Function for switching between light and dark mode
def switch_mode():
    # Get button state
    switchState = state.get()

    # Switch mode based on current button state
    if switchState == 1:
        app._set_appearance_mode("dark")
    else:
        app._set_appearance_mode("light")


# Function that prompts user to input a path and then runs sorting function
def prompt_and_sort():
    # Obtain file path from user
    global filePath
    filePath = filedialog.askdirectory()

    # Check if user gave input or cancelled
    if not filePath:
        print("Path was not selected")
    else:
        print(f"Selected path: {filePath}")

        # Sort files at path
        sort_files(filePath)


# Function that obtains file type of file at a path
def get_file_type(filePath):
    # Create a magic.Magic() object
    m = Magic()

    # Determine file type
    fileType = m.from_file(filePath)
    return fileType.split()[0]  # Extract the first word (file type)


# Function that creates new directory if it doesn't already exist, and sorting files into them
def create_dir_move(downloadsDir, filePath, dirName, dirNames):
    if dirName:
        # Combine the parent directory path with the new directory name
        newDirPath = os.path.join(downloadsDir, dirName)
        
        # Check if the file is a regular file
        if os.path.isfile(filePath):
            # Check if the destination directory already exists
            if dirName not in dirNames and not os.path.exists(newDirPath):
                os.mkdir(newDirPath)  # Make new directory with file type as name
                dirNames.append(dirName)
            
            # Move the file from the source location to the destination location
            move(filePath, newDirPath)


# Sorts files at a path
def sort_files(selectedPath):
    # List for storing directory names
    dirNames = []

    # Define the path to the Downloads folder in Windows
    downloadsDir = selectedPath

    # List all files in the Downloads directory, catch exception if path doesn't exist
    try:
        filesInDownloads = os.listdir(downloadsDir)
    except FileNotFoundError:
        print("File path was not found")
        return

    # Determine the file types of each file
    for fileName in filesInDownloads:
        # Join filename with path
        filePath = os.path.join(downloadsDir, fileName)
    
        # If a directory is detected, ignore it, otherwise get_file_type
        try:
            fileType = get_file_type(filePath)
        except IsADirectoryError:
            fileType = None
        
        # Run create_dir_move
        create_dir_move(downloadsDir, filePath, fileType, dirNames)

    print("Sorted!")


btnSort = CTkButton(master=app, text="Sort", corner_radius=32, border_width=2, command=prompt_and_sort)
label = CTkLabel(master=app, text="Click To Sort Files", font=("Arial", 20),)
switch = CTkSwitch(master=app, text="Dark Mode", variable=state, command=switch_mode)

btnSort.place(relx=0.5, rely=0.5, anchor="center")
switch.place(relx=0.5, rely=0.6, anchor="center")
label.place(relx=0.5, rely=0.4, anchor="center")

app.mainloop()







