# Builds on top of Chem Parser v12 FINAL
#   Takes only one paragraph per paper 
#   Processes a batch of papers
# v1 -> Processes paragraphs instead of sentences to increase speed
# v2 -> Takes only one random paragraph per paper
# v3 -> Skips empty paragrapahs
# v4 -> Generates DOI file --- DRAFT
# v5 -> Based on ChemDataExtractor tokenizer
#       Includes random seed set to 0
# v6 -> Adds DOI to id
# v7 -> Adds maximum paragraph size filtering

from chemdataextractor.nlp.tokenize import ChemWordTokenizer
import chemdataextractor as cde
import pandas as pd
import random
import tqdm
import sys
import os
cwt = ChemWordTokenizer()

def read_file_list(file_list_path):
    open_file = open(file_list_path, 'r')
    file_list = []
    DOI_list = []
    for item in open_file.readlines():
        # Customize for each case
        file_name = item.replace('\n', '').split('\t')[0].split('/')[2]
        DOI = item.replace('\n', '').split('\t')[1]
        file_list.append(file_name)
        DOI_list.append(DOI)
    return(file_list, DOI_list)  

def clean_paragraph(paragraph):
    par_clean = paragraph.text.replace('\n',' ')
    par_clean = par_clean.replace('/',' / ')
    par_clean = par_clean.replace('‑','-')
    par_clean = par_clean.replace('- ','-')
    return(par_clean)

def select_paragraph(output_df):
    length = len(output_df)
    position = random.randint(0,max(0, length-1))
    chosen_paragraph = output_df.iloc[position]
    return(chosen_paragraph)

def parse_one_paper(file_path, DOI):
    #Initialization of variables
    target_keywords = ['abstract','scheme','schemes','table','tables','entry','entries','report','synthesis'
                       'synthesized','gave','gives','cathalized','yield','yields','obtained']
    headers = ['table','scheme','figure']
    stopwords = ['and', 'with', 'or', 'of']
    par_min_len = 25
    par_max_len = 300
    cems_min_len = 2
    id = 0
    output_df = pd.DataFrame(columns = ['cveid','description','spans'])
    
    #Open file
    file = open(file_path,'rb')
    doc = cde.Document.from_file(file)
    
    # Create cems list
    cems = doc.cems
    cems_list = []
    for item in cems:
        name = item.text
        if name.lower not in stopwords and len(name) >= cems_min_len:
            cems_list.append(name)
    cems_list = set(cems_list)
    cems_list = sorted(cems_list)    
    
    # Iterate through paragraphs in document
    n_par = len(doc.elements)
    i = 0
    while i < n_par:
        par_text = doc.elements[i].text
        if 'experimental section' in par_text.lower():
            break
        # Clean and tokenize sentences in paragraph
        par_tok = cwt.tokenize(par_text)
        if len(par_tok) > 0:
            par_tok_text = ' '.join(par_tok)
            par_tok_lower = [x.lower() for x in par_tok] 
            # Look for elegible paragraphs
            condition_1 = any(x in par_tok_lower for x in target_keywords)
            condition_2 = len(par_tok) >= par_min_len
            condition_3 = len(par_tok) <= par_max_len
            condition_4 = par_tok[0].lower() not in headers
            if (condition_1 and condition_2 and condition_3 and condition_4):        
                # Detect and position cems in sentences group
                spans = []
                for token_index, token in enumerate(par_tok):
                    for item in cems_list:
                        if item == token:
                            span_b = token_index
                            span_e = token_index + 1
                            spans.append(span_b)
                            spans.append(span_e)
                # Build dataframe
                spans_str = ', '.join(str(x) for x in spans)
                id_full = DOI + '-' + str(id)
                output_df = output_df.append({'cveid':id_full,'description':par_tok_text,'spans':spans_str},ignore_index = True)
                id += 1
        i += 1
    return(output_df)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: ChemParserBatch_v7.py [origin_folder] [destination_path] [file list path]')
        exit()

    origin_folder = sys.argv[1]
    destination_path = sys.argv[2]
    file_list_path = sys.argv[3]
    DOI_file_path = destination_path + '.doi'
        
    random.seed(0)
    open_output_file = open(destination_path, 'w+')
    open_DOI_file = open(DOI_file_path, 'w+')
    output_global_df = pd.DataFrame(columns = ['cveid','description','spans'])
    file_list, DOI_list = read_file_list(file_list_path)
    
    for file, DOI in tqdm.tqdm(zip(file_list, DOI_list)):
        print(file, DOI)
        file_path = os.path.join(origin_folder, file)
        output_df = parse_one_paper(file_path, DOI)
        #skips the case of non-identified paragraphs
        if len(output_df) > 0:
            chosen_paragraph = select_paragraph(output_df)
            output_global_df = output_global_df.append(chosen_paragraph)
            open_DOI_file.write(DOI+'\n')
        output_global_df.to_csv (destination_path, index = None, header=True)
    
    open_output_file.close()
    open_DOI_file.close()
