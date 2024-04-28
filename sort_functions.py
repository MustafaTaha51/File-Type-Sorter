import os
from shutil import move
from magic import Magic

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