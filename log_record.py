#!/usr/bin/python3
import subprocess
import os
from datetime import datetime
from pathlib import Path
#==================

def log_record():
    
    now = datetime.now()
    timestr = now.strftime("%Y-%m%d-%H:%M:%S")

    #路徑
    folder = '/Users/wowbincom/Downloads/python_yaml/updates'
    log_file = open(Path('/')/folder/'log.txt','a+')
    err_file = open(Path('/')/folder/'err.txt','a+')
    #print(log_file)
    subprocess.run(['echo "Run Process Success >>> "{}'.format(timestr)],shell=True,stdout=log_file,stderr=err_file)
    #print(Path('/')/folder/'log.txt')
    print("Log record")

log_record()