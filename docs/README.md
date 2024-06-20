# Table of Contents
- [Table of Contents](#table-of-contents)
- [Project](#project)
    - [Description](#problem-description)
    - [Requirements](#requirements)
        - [Syncronization](#synchronization)
        - [Methods](#methods)
        - [Solution Delivery](#solution-delivery)
- [Deliverables](#deliverables)
- [Dependencies](#dependencies)
- [Tree](#tree)
- [How To Run](#how-to-run)
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

### Solution Delivery
- The solution ought to be presented in the form of a link to the public GitHub repositor.

# Deliverables
- redundancy.py generates a replica and initializes a log file.
- main.py schedules a task to run redundancy.py based on user command prompt input and generates a redundancy.log, as well as outputing it in the terminal.
- requirements.txt containing host system requirements such as Python version and libraries. 
- A README.md containg preliminary information.
- A test folder with random folders and random files, including ones heavier than 64KB.
- runme.sh and runme.bat to test the code.
- Business use case presentation. 

# Dependencies
- The dependencies (or rather dependency) are already integrated within the virtual environment, however, one can refer to them through the requirements.txt;
- The python version used throughout this project was Python 3.12.4.

# Tree
```
Test_Task
├───docs
│       README.md
│       Redundancy.odp
│       requirements.txt
│
├───src
│   │   base_functions.py
│   │   main.py
│   │   redundancy.py
│   │
│   └───__pycache__
│
└───tests
    │   README.txt.txt
    │   redundancy.log
    │   runme.bat
    │   runme.sh
    │
    └───dir
```

# How To Run
- To deploy a replication job, one needs to headover to the command prompt or termainal, (ideally) activate the virtual environment and run 
``python .\main.py <source_directory> <destination_directory> <time_step> <time_unit> <log_path>``
- If folder names have spaces in them, the user is required to enter the path in quotes. Otherwise, the program will assume each section divided by a space as being a positional argument. 
- Here, time_step is an integer and time_unit is either the "seconds", "minutes", "hours", "days" or "weeks".

# Footnotes 
- There are many reasons why one would want to copy over a directory, such as versioning, disaster recovery and testing, however there're two edge cases:
    - One where the user can state that it wants a replication of that source directory tree in the same parent directory;
    - Another where the user tries to replicate the destination folder within the source directory;
The current program deals with these by warning the user to input a new destination path.
- The buffer size should be adequate to the operations. If its too big then we encounter an increase in memory usage without any gains in terms of performance. If its too small then we may encounter errors due to having the same hash outputs for instance. Optimal sizes range between 8 to 64 KB. It is hard-coded to be 65536 bytes. For instance, if we are dealing with files that are 10KB, as many as they be, having a buffer of 45KB is suboptimal. 
- As requested in the task document only events ("created", "copied" and "removed") related to files are logged and outputted in the command prompt.  
- Infrastructure-wise, it is assumed that the job is on an 24/7 powered-on computer or server.

# Future Work
- Higher level of scheduling detail. 



