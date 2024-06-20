@echo off
echo This script will replicate 'dir' -- that contains a bunch of random folders and files -- to a new directory called 'dir_new' every 3 seconds.
echo A redundancy.log file will be created in the current directory with all the modifications.
echo.

python ..\src\main.py dir dir_new 3 seconds .
