# Table of Contents
- [Table of Contents](#table-of-contents)
- [Project](#project)
    - [Description](#problem-description)
    - [Requirements](#requirements)
        - [Syncronization](#synchronization)
        - [Methods](#methods)
        - [Presentation](#presentation)
- [Deliverables](#deliverables)
- [Dependencies](#dependencies)
- [Footnotes](#footnotes)

# Project
## Description
- Implement a program that synchronizes two folders: source and replica. 
- The program should maintain a full, identical copy of source folder at replica folder.
- Use either Python, C/C++ or C#.

## Requirements
### Synchronization 
- Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder; 
- Synchronization should be performed periodically: meaning it should be a CRON job;
- File creation/copying/removal operations should be logged to a file and to the console output; 
- Folder paths, synchronization interval and log file path should be provided using the command line arguments.

### Methods
- It is undesirable to use third-party libraries that implement folder synchronization.
- It is allowed (and recommended) to use external libraries implementing other well-known algorithms. 
    - For example, there is no point in implementing yet another function that calculates MD5 if you need it for the task – it is perfectly acceptable to use a third-party (or built-in) library.

### Presentation
- The solution ought to be presented in the form of a link to the public GitHub repositor.

# Deliverables
- redundancy.py generates a replica
- cron_job.py creates a cron job to run redundancy.py and generates a log file as well as outputing it in the terminal;
- A file documenting all the steps taken.
- A file containing host system requirements such as Python version and libraries. 
- A README.md containg preliminary information.
- Business use case document. 
- Budget document.

# Dependencies
- The dependencies are already integrated within the virtual environment, however, one can refer to them through the requirements.txt;
- The python version used throughout this project was Python 3.12.4;
- The libraries used are:
    - os

# Footnotes 
- There are many reasons why one would want to copy over a directory, such as versioning, disaster recovery and testing, however there's an edge ase where the user can state that it wants a copy of that same directory in the same path as the source. This is an edge case that the current program deals by warning the user and by asking for a confirmation (y/n). If the response is positive (y) then the copy of the source directory will assume the same name plus the suffix "_copy" (e.g. sourcedir_copy).
- The buffer size should be adequate to the operations. If its too big then we encounter an increase in memory usage without any gains in terms of performance. If its too small then we may encounter errors due to having the same hash outputs for instance. Optimal sizes range between 8 to 64 KB.
- The user is required to input full paths or relative paths to the path from which the program is being run. 
