#!/bin/bash

echo -e "This script will replicate 'dir' to a new directory called 'dir_new' every 3 seconds.\n"
echo -e "A redundancy.log file will be created in the current directory with all the modifications.\n"

python ../src/main.py dir dir_new 3 seconds .