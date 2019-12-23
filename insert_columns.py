# Inserts an empty "column name" and the corresponding "column name-tag" at position pos

import sys
import pandas as pd
import numpy as np

def insert_columns(origin_path, column_name, column_position):
    destination_path = origin_path + '_new'
    column_tag_name = column_name + '-tag'
    df = pd.read_csv(origin_path)
    df.insert(column_position, column = column_tag_name, value = np.NaN)
    df.insert(column_position + 1, column = column_name, value = np.NaN)
    df.to_csv(destination_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: insert_columns.py [origin_path] [column_name] [column_position]')
        exit()
    
    origin_path = sys.argv[1]
    column_name = sys.argv[2]
    column_position = sys.argv[3]
    
    insert_columns(origin_path, column_name, column_position)