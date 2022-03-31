#!/usr/bin/python3
import os
import shutil
#import urllib.request
from datetime import datetime
import yaml
from hasher import sha1
from log_record import log_record
#from notifier import send_notification
#=================================
def move_files(filename):
    #時間
    now = datetime.now()
    timestr = now.strftime("%Y-%m-%d")
    #print(">>>>>>>>>>>>>"+timestr)
    #file_index ='_1'

    #路徑
    newfolder = '/Users/wowbincom/Downloads/python_yaml/updates'
    oldfolder = '/Users/wowbincom/Downloads/python_yaml'
    
    #檔名
    src_file = oldfolder+'/'+filename
    dst_file = newfolder+'/Last_waf_{}.yml'.format(now.strftime("%Y-%m-%d"))#+ file_index)
    #shutil.copy(filename, '/Users/wowbincom/Downloads/python_yaml/updates/')
    #os.rename(filename, '/Users/wowbincom/Downloads/python_yaml/updates/latest.yml'.format(now.strftime("%Y%d%m%H%M%S")))
    if not os.path.exists(newfolder):
        os.mkdir(newfolder)
    else:
        shutil.copyfile(src_file,dst_file)
        print(">>>>> Creat New File success")

def check_for_update(yaml_file):
    # get date and time as string
    now = datetime.now()
    #filename = '/Users/wowbincom/Downloads/python_yaml/demo_update.yml'#.format(now.strftime("%Y%d%m%H%M%S"))
    filename = yaml_file
    #move_files(filename)
    
    # download file
    #url = 'https://tonyteaches.tech/test.pdf'
    #urllib.request.urlretrieve(url, filename)
    
    # get hashes
    try:
        hash_latest = sha1('/Users/wowbincom/Downloads/python_yaml/updates/Last_waf_{}.yml'.format(now.strftime("%Y-%m-%d")))
        print(">>>>> hash success ")
    except:
        move_files(filename)
        print('First file saved')
        return
    hash_new = sha1(filename)
    
    # compare hashes
    if hash_latest != hash_new:
        print('Found update')
        move_files(filename)
        #send_notification(url)
    else:
        print('No update')
        #os.remove(filename)

#check_for_update()