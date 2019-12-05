# Slices a text file and saves it to namefile.sliced.txt
# v2 -> adds number of sliced lines to filename

import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: text_slice.py [origin path] [first line] [last line] \n\t Ouput = origin path + .sliced')
        exit()

    origin_path = sys.argv[1]
    first_line = int(sys.argv[2])
    last_line = int(sys.argv[3])
    destination_path = origin_path + '.sliced_' + str(first_line) + '-' + str(last_line) 

    open_origin_file = open(origin_path, 'r')
    open_destination_file = open(destination_path, 'w+')
    
    for i, item in enumerate(open_origin_file.readlines()):
        if i >= first_line and i <= last_line:
            open_destination_file.write(item)

    open_origin_file.close()
    open_destination_file.close()
