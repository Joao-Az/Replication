#!/usr/bin/env python
"""
@file:          base_functions.py
@description:   Creates base functions to be applied in redundancy.py.
@author:        João Azevedo
@date:          18/06/2024
@parameters:    None
@returns:       None
"""
from datetime import datetime
import hashlib

# Get date and time at run time
now = datetime.now()
current_dt      = str(now.strftime("%d/%m/%Y %H:%M:%S"))

def message(arg, obj):
    """
    Returns a string with a personalized message.

    Args:
        arg:    Is type of event ("created", "copied" or "removed").
        obj:    The object path in which the event ocurred.
    """
    if arg == "created":
        return f" "*4 + "📄File Created: ".ljust(16) + obj
    elif arg == "copied":
        return f" "*4 + "📃File Copied: ".ljust(16) + obj
    elif arg == "removed":
        return f" "*4 + "🗑️File Removed: ".ljust(16) + obj

def log_write(log_file, line):
    """
    Creates a log file (if it doesn't exist) and write event messages.

    Args:
        log_file:   The log file full path.
        line:       The string to be written.
    """
    with open(log_file, 'a', encoding='utf-8') as file:
        file.write(line + "\n")

def log_init(log_file):
    """
    Initializes a log transaction.

    Args:
        log_file:   The log file full path.
    """
    with open(log_file,"a") as log:
        log.write(" REPLICATION LOG ".center(36, "#") + "\n")
        log.write(str(current_dt.center(36,"_")) + "\n")

def hashfile(file, buffer):
    """
    Calculates file hash value and returns it.

    Args:
        file:   A file to be hashed.
        buffer: A buffer size.
    """
    # Initializing the sha256() encryption method
    sha256 = hashlib.sha256()
  
    # Generating the hash
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer)

            if not data:
                break
            
            sha256.update(data)

    return sha256.hexdigest()

def compare_hashes(src_file, dst_file, buffer):
    """
    Returns a bool based on the equality of hashes.

    Args:
        src_file: The source file path.
        dst_file: The destination file path.
        buffer: A buffer size.
    """
    return hashfile(src_file,buffer) == hashfile(dst_file,buffer)

def copy_file(source_path, destination_path, buffer):
    """
    Copies a file from source_path to destination_path.

    Args:
        source_path: The path to the source file.
        destination_path: The path to the destination file.
    """
    with open(source_path, 'rb') as src_file:
        with open(destination_path, 'wb') as dst_file:
            while True:
                chunk = src_file.read(buffer)
                if len(chunk) == 0:
                    break
                dst_file.write(chunk)
















