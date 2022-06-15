#print current dir and change into new working dir
import pandas as pd
import os
import re
path = os.getcwd()
print(path)
new_path = path + '/before-pipeline-data-input'
print(new_path)
os.chdir(new_path)
import re
#1. import pfam result
pfam = pd.read_csv('pfam_A_out.txt',header=None,sep='\s+', comment='#')
pfam.columns = ['seq id','alignment start','alignment end','envelope start','envelope end','hmm acc','hmm name','type',
                'hmm start','hmm end','hmm length','bit score','E-value','significance','clan']
print(len(pfam))
pfam_cleaned =pfam[pfam['seq id'].str.contains('Chr') == False]
print(len(pfam_cleaned))
pfam_cleaned.to_csv('pfam_cleaned.csv', index=False)



#2. import signalP result
signalp = pd.read_csv('prediction_results.txt', usecols= [0,1],sep='\s+', header=None, comment='#')
signalp.columns = ['ID','SP prediction']
#substring ID column
for i in range(0, len(signalp)):
    signalp.iloc[i].ID = signalp.iloc[i].ID[:17]
#remove non nuclear gene
print(len(signalp))
signalp = signalp[signalp['ID'].str.contains('Chr') == False]
print(len(signalp))
#remove - then add back LOC_
signalp['ID'] = signalp["ID"].str.replace("_$","")
print(signalp.head())
signalp.to_csv('signalp_cleaned.csv', index=False)


#3. read TM file as string
pattern = re.compile(".*Number of predicted TMRs.*")
tm_cleaned = []
with open ('TM_results.txt', 'rt') as myfile:
    for line in myfile:
      if pattern.search(line) != None:
          tm_cleaned.append(line)
tm_cleaned = pd.DataFrame(tm_cleaned)
#duplicate column, string subset
tm_cleaned.columns=['ID']
tm_cleaned['TM'] = tm_cleaned['ID']
#substring ID column
tm_cleaned['ID'] = tm_cleaned["ID"].str.replace("# ","")
tm_cleaned['ID'] = tm_cleaned["ID"].str.replace(" Number of predicted TMRs","")
tm_cleaned['ID'] = tm_cleaned["ID"].str.replace("\n","")
tm_cleaned['ID'] = tm_cleaned["ID"].str.replace(r": \d*",r"",regex = True)

tm_cleaned['TM'] = tm_cleaned["TM"].str.replace(r"^#.*TMRs: ",r"",regex = True)
tm_cleaned['TM'] = tm_cleaned["TM"].str.replace("\n","")
tm_cleaned = tm_cleaned[tm_cleaned['ID'].str.contains('Chr') == False]
print(len(tm_cleaned))
tm_cleaned.to_csv('tm_cleaned.csv', index=False)