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

#merge and remove extra columns
tm_not_zero_signalp = tm_not_zero.merge(signalp, how='left', on = 'ID')
tm_not_zero_signalp.columns = ['ID','TM','SP_prediction']
tzs_cleaned = tm_not_zero_signalp.drop(columns=['TM'])
#divide tzs_cleaned into two seperate files based on SP prediction
tm_nsg = tzs_cleaned[tzs_cleaned['SP_prediction'] == 'NO_SP']
tm_psg = tzs_cleaned[tzs_cleaned['SP_prediction'] == 'SP']

#merge with pfam and output
Osa_nsg_pfam_parser = tm_nsg.merge(pfam, how='inner', left_on = 'ID', right_on='seq id')

Osa_nsg_pfam_parser = Osa_nsg_pfam_parser.drop(columns=['ID', 'SP_prediction'])
Osa_nsg_pfam_parser.columns = ['seq_id','alignment_start','alignment_end','envelope_start',
                               'envelope_end','hmm_acc','hmm_name','type','hmm_start','hmm_end',
                               'hmm_length','bit_score','E-value','significance','clan']
Osa_nsg_pfam_parser.to_csv('Osa_nsg_pfam_parser.csv', index=False)

Osa_psg_pfam_parser = tm_psg.merge(pfam, how='inner', left_on = 'ID', right_on='seq id')
Osa_psg_pfam_parser = Osa_psg_pfam_parser.drop(columns=['ID', 'SP_prediction'])
Osa_psg_pfam_parser.columns = ['seq_id','alignment_start','alignment_end','envelope_start',
                               'envelope_end','hmm_acc','hmm_name','type','hmm_start','hmm_end',
                               'hmm_length','bit_score','E-value','significance','clan']
Osa_psg_pfam_parser.to_csv('Osa_psg_pfam_parser.csv', index=False)

#output a file that has SignalP, TM and pfam information
pfam_tm = pfam.merge(tm, how='outer', left_on = 'seq id', right_on= 'ID')
pfam_tm_signalp = pfam_tm.merge(signalp, how='outer', left_on = 'seq id', right_on = 'ID')
drop_columns = ['alignment start','alignment end','envelope start','envelope end','hmm acc',
                'type','hmm start','hmm end','hmm length','bit score','E-value','significance','clan']
pfam_tm_signalp_cleaned = pfam_tm_signalp.drop(columns=drop_columns)
pfam_tm_signalp_cleaned.columns = ['pfam_ID','hmm_name','TM_ID', 'TM', 'SP_ID', 'SP_prediction']
pfam_tm_signalp_cleaned.to_csv('pfam_tm_signalp_combined.csv', index=False)
