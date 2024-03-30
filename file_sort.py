import os
from sys import argv
from magic import Magic
from shutil import move
from customtkinter import *

app = CTk()
app.geometry("300x400")

def switch_mode():
    switchState = state.get()
    if switchState == 1:
        app._set_appearance_mode("dark")
    else:
        app._set_appearance_mode("light")

btnSort = CTkButton(master=app, text="Sort", corner_radius=32, border_width=2)

label = CTkLabel(master=app, text="Click To Sort Files", font=("Arial", 20),)

state = IntVar()

switch = CTkSwitch(master=app, text="Dark Mode", variable=state, command=switch_mode)

btnSort.place(relx=0.5, rely=0.5, anchor="center")
switch.place(relx=0.5, rely=0.6, anchor="center")
label.place(relx=0.5, rely=0.4, anchor="center")

app.mainloop()

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


def main():
    # Check if command-line argument for file path was provided
    if len(argv) > 1:
        # List for storing directory names
        dirNames = []

        # Define the path to the Downloads folder in Windows
        downloadsDir = argv[1]

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
    else:
        # Alert user about command-line argument usage
        print("Usage: python3 script_name.py <file_path>")
        print("Please provide the required command-line argument.")


if __name__ == '__main__':
    main()
