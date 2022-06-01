import glob
import os
path = os.getcwd()
print(path)
new_path = path + '/before-pipeline-data-input'
print(new_path)
os.chdir(new_path)

TM_files = glob.glob(new_path+"/**/*.gff3", recursive = True)
print(TM_files)
with open('TM_results.txt','w') as outfile:
    for names in TM_files:
        with open(names) as infile:
            outfile.write(infile.read())
        outfile.write("//")