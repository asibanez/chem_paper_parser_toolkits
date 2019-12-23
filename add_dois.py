# Adds the DOIs to the cveids of the parsed paragraphs
# Inputs: paragraph list, DOI list, annotations

import sys
import pandas as pd

def add_dois(paragraph_list_path, doi_list_path, annotations_path):
    destination_path = annotations_path + '_with_DOIs'
    paragraph_df = pd.read_csv(paragraph_list_path)
    doi_df = pd.read_csv(doi_list_path, header = None)
    annotation_df = pd.read_csv(annotations_path, dtype = {'cveid' : str})
    
    for index, row in annotation_df.iterrows():
        text = row.description
        par_number = row.cveid
        match_index = paragraph_df.index[paragraph_df['description'] == text].tolist()
        if len(match_index) > 1: print('Error: more than one coindicences')
        doi = doi_df.iloc[match_index[0]][0]
        new_doi = doi + '-' + str(par_number)
        annotation_df.at[index,'cveid'] = new_doi         
    annotation_df.to_csv(destination_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: add_dois.py [paragraph_list_path] [doi_list_path] [annotations_path]')
        exit()
    
    paragraph_list_path = sys.argv[1]
    doi_list_path = sys.argv[2]
    annotations_path = sys.argv[3]
    
    add_dois(paragraph_list_path, doi_list_path, annotations_path)
