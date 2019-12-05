# select & copy files between folders based on .txt file list
# v0

import os
import sys
import shutil

def move_files(origin_folder, destination_folder, file_list_path):

    open_file_list_path = open(file_list_path)  
    
    for item in open_file_list_path.readlines():
        filename = item.replace('\n', '')
        #filelist preprocessing specific for each case
        filename = item.split('\t')[0]
        filename = filename.split('/')[2]
        
        origin_path = os.path.join(origin_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.copyfile(origin_path, destination_path)
        print(filename)
    open_file_list_path.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: copy_files_txt.py [origin_folder] [destination_folder] [file list path]')
        exit()
    
    origin_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    file_list_path = sys.argv[3]
    
    move_files(origin_folder, destination_folder, file_list_path)
