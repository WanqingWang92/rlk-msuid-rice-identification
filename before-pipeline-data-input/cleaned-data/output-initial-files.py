#print current dir and change into new working dir

import pandas as pd
import os

path = os.getcwd()
print(path)
new_path = path + '/before-pipeline-data-input/cleaned-data'
print(new_path)
os.chdir(new_path)

#import cleaned data
pfam = pd.read_csv('pfam_cleaned.csv')
signalp = pd.read_csv('signalp_cleaned.csv')
tm = pd.read_csv('tm_cleaned.csv')

#select tm rows where TM != 0
tm_not_zero = tm[tm['TM'] != 0]
#concat and remove extra columns
tm_not_zero_signalp = pd.concat([tm_not_zero, signalp], axis=1, join='inner')
tm_not_zero_signalp.columns = ['ID','TM','ID copy', 'SP prediction']
tzs_cleaned = tm_not_zero_signalp.drop(columns=['TM', 'ID copy'])
#divide tzs_cleaned into two seperate files based on SP prediction
tm_nsg = tzs_cleaned[tzs_cleaned['SP prediction'] == 'NO_SP']
tm_psg = tzs_cleaned[tzs_cleaned['SP prediction'] == 'SP']
#concat with pfam and output
Osa_nsg_pfam_parser = pd.concat([tm_nsg,pfam], axis=1, join='inner')
Osa_nsg_pfam_parser = Osa_nsg_pfam_parser.drop(columns=['ID', 'SP prediction'])
Osa_nsg_pfam_parser.columns = ['seq_id','alignment_start','alignment_end','envelope_start',
                               'envelope_end','hmm_acc','hmm_name','type','hmm_start','hmm_end',
                               'hmm_length','bit_score','E-value','significance','clan']
Osa_nsg_pfam_parser.to_csv('Osa_nsg_pfam_parser.csv', index=False)

Osa_psg_pfam_parser = pd.concat([tm_psg,pfam], axis=1, join='inner')
Osa_psg_pfam_parser = Osa_psg_pfam_parser.drop(columns=['ID', 'SP prediction'])
Osa_psg_pfam_parser.columns = ['seq_id','alignment_start','alignment_end','envelope_start',
                               'envelope_end','hmm_acc','hmm_name','type','hmm_start','hmm_end',
                               'hmm_length','bit_score','E-value','significance','clan']
Osa_psg_pfam_parser.to_csv('Osa_psg_pfam_parser.csv', index=False)