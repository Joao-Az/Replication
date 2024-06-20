#!/usr/bin/env python
"""
@file:          redundancy.py
@description:   Imports base_functions.py and creates a replica of the source
                directory to a destination directory.
@author:        João Azevedo
@date:          17/06/2024
@parameters:
    - source directory;
    - destination directory;
    - log path
    - buffer value
@returns: 
    - a replica of the source directory in the requested destination
    - a log file
    - messages in standard output
"""
import os
from base_functions import message, log_write, log_init, compare_hashes, copy_file

def replication(source_directory, destination_directory, log_file, buffer):
    """
    Creates a copy of the source file to the destination directory or modifies an existing file. 
    Creates a directory folder in destination if it doesn't exists already.
    

    Args:
        source_directory:   The relative or full path of source directory
        source_directory:   The relative or full path of destination directory.
        log_file:           The relative or full path of file.
        buffer:             A buffer size.
    """

    obj_list = os.listdir(source_directory)

    for obj_name in obj_list:
        # Create a path object type of the parsed object
        src_obj_path = os.path.join(source_directory, obj_name)
        dst_obj_path = os.path.join(destination_directory, obj_name)
        
        # If the relative path of the folder does not exist in the destination folder, then create it, 
        # and if we are dealing with a file copy it over.
        if os.path.exists(dst_obj_path) == False:
            if os.path.isfile(src_obj_path) == True:
                copy_file(src_obj_path, dst_obj_path, buffer)
                line = message("created",dst_obj_path)
                log_write(log_file, line)
                print(line)
            elif os.path.isdir(src_obj_path) == True:
                os.mkdir(dst_obj_path)
                replication(src_obj_path, dst_obj_path, log_file, buffer)
                
        # If the relative path does exist then 
        elif os.path.exists(dst_obj_path) == True:
            if os.path.isfile(src_obj_path) == True:
                if compare_hashes(src_obj_path, dst_obj_path, buffer) == True:
                    pass
                elif compare_hashes(src_obj_path, dst_obj_path, buffer) == False:
                    copy_file(src_obj_path, dst_obj_path, buffer)
                    line = message("copied",dst_obj_path)
                    log_write(log_file, line)
                    print(line)
            elif os.path.isdir(src_obj_path) == True:
                    replication(src_obj_path, dst_obj_path, log_file, buffer)

def removal(source_directory, destination_directory, log_file, buffer):
    """
    Delete recursively files or directories in the destination that aren't present in source.
    Keyword: destination.

    Args:
        source_directory:   The relative or full path of source directory.
        source_directory:   The relative or full path ofdestination directory.
        log_file:           The relative or full path of file.
        buffer:             A buffer size.
    """
    # Fetch log file
    obj_list = os.listdir(destination_directory)

    for obj_name in obj_list:

        src_obj_path = os.path.join(source_directory, obj_name)
        dst_obj_path = os.path.join(destination_directory, obj_name)

        # The destination object should be removed if it is an empty  the destination object we are analysing doesn't exist in source then it should be removed. 
        # If the object is a file or an empty folder then it can be removed  now.
        # However if the object is a non-empty folder then we need to call the function once again.
        # For each removal, a line will be written in the log file.
        if os.path.exists(src_obj_path) == False:
            if os.path.isfile(dst_obj_path) == True:
                os.remove(dst_obj_path)
                line = message("removed",dst_obj_path)
                log_write(log_file, line)
                print(line)
            elif os.path.isdir(dst_obj_path) == True:
                if len(os.listdir(dst_obj_path)) == 0:
                    os.rmdir(dst_obj_path)
                    print(line)
                elif len(os.listdir(dst_obj_path)) != 0:
                    removal(src_obj_path,dst_obj_path, log_file, buffer)

        # If the folder object isn't empty then call removal() once more.
        elif os.path.exists(src_obj_path) == True:
            if os.path.isfile(dst_obj_path) == True:
                pass
            elif os.path.isdir(dst_obj_path) == True:
                if len(os.listdir(dst_obj_path)) == 0:
                    pass
                elif len(os.listdir(dst_obj_path)) != 0:
                    removal(src_obj_path, dst_obj_path, log_file, buffer)


def redundancy_function(src_path, dst_path, log_file, buffer):
    
    # Take care of conflicting paths
    common_path = os.path.commonpath([src_path, dst_path])
    if (dst_path==src_path) or (common_path == src_path):
        dst_path = str(input("Conflicting paths... \n    \
                             Please write a different destination directory path. \n    \
                             The destination should be outside the source path. \n    \
                             And if it shares the same parent directory as source, it should have different name. \n\
                             Destination directory: "))
    else: 
        pass

    log_init(log_file)

    if os.path.exists(dst_path) == True:
        replication(src_path,dst_path,log_file,buffer)
        removal(src_path,dst_path,log_file,buffer)   

    elif os.path.exists(dst_path) == False:
        os.mkdir(dst_path)
        replication(src_path,dst_path,log_file,buffer)

    log_write(log_file, "\n")















