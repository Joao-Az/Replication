#!/usr/bin/env python
"""
@file:          main.py
@description:   Imports redundancy.py, calls its functions to be run
                and generates scheduled task based on user input. 
@author:        João Azevedo
@date:          19/06/2024
@parameters:    None
@returns:       CRON job deployment that replicates a source file directory. 
"""

import __main__
import sys
import datetime
import redundancy as r
import schedule
import time

src_path        = str(sys.argv[1])
dst_path        = str(sys.argv[2])
time_step       = int(sys.argv[3])
time_unit       = str(sys.argv[4])
log_path        = str(sys.argv[5])
buffer          = 65536 #64 KB in Bytes

# Create log file path
log_name        = "redundancy"
log_file = f"{log_path}/{log_name}.log"

def task(src, dst, log, buf):
    now             = datetime.datetime.now()
    current_dt      = str(now.strftime("%d/%m/%Y %H:%M:%S"))
    print(" REPLICATION LOG ".center(36, "#") + "\n")
    print(str(current_dt.center(36,"_")) + "\n")
    r.redundancy_function(src, dst, log, buf)
    
def main():
    
    time_unit_map = {
        'seconds': schedule.every(time_step).seconds,
        'minutes': schedule.every(time_step).minutes,
        'hours': schedule.every(time_step).hours,
        'days': schedule.every(time_step).days,
        'weeks': schedule.every(time_step).weeks
    }
    
    if time_unit.lower() in time_unit_map:
        time_unit_map[time_unit].do(task, src_path, dst_path, log_file, buffer)
    else:
        raise ValueError("Please enter either 'seconds', 'minutes', 'hours', 'days', 'weeks'")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down scheduled task ...")
        sys.exit(0)
    
if __name__ == "__main__":
    main()