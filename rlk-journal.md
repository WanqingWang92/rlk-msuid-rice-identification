# RLK project journal
SignalP version 6
DeepTMHMM 1.0.9
pfam_scan 1.6 HMMER 3.3.2
## 4/26/2022 
- environment: windows terminal
- git 
  - create a new repository
  - add .gitignore (selected python)
  - add license (GNU General Public License v3.0)
  - git clone (paste SSH code)

    (checked windows **optional feature** to see **Open SSH Server** is installed)
- docker
  - downloaded docker
  - docker pull command to pull image (**streptomyces/signalp**)

## 4/28/2022
- download all.pep from MSU website, pasted to current dir
  - run command at C:\Workshop\rlk-msuid-rice-identification
```{bash}
    docker run --rm -it -v ${PWD}:/home/work streptomyces/signalp
```
${PWD} is current dir on my side, /home/work is the dir on docker
```{bash}
mkdir signalp_out

signalp6 --fastafile ./all.pep --organism eukarya --output_dir signalp_out \
--format txt
```
## 5/10/2022
Understood the files in script folder produced by Dr. Furuta, 01 is to separate 
the pep file into 10000 each, because the web version of TMHMM 2.0 tool has a limit.
file 02 to 04 are files that export the result form signalp, TMHMM and pfam, in the 
end 05 combine and export the result into an excel file. 
- build a directory R-script for R script
- copy 01_separateFASTA.R into separate-pep.R
- readAAStringSet, AA stands for amino acid
- seq_along() creates a vector that contains a sequence of numbers from 1 
to the object’s length.
- build a directory separate-pep for out put result of separate-pep.R 
- generated batch_1:7.pep files

**The TMHMM-2.0 is outdated.** Deep TMHMM is used instead. This version
allows for more than 10000 per run. will use all.pep file.
- used anaconda to install pybiolib, it did not work out
- used pip install command from the website
- the command installed successfully, though biolib function cannot run

**Cannot get the terminal version working,** will use the website to run
- batch1 took too long on the website and it aborted after 1.5 hr
- batch7 finished, I compared the result from Dr. Furuta's, they are 
not completely the same

**tried using ubuntu on windows** and it worked.

## 5/11/2022
- The ubuntu run was terminated after ~1h. 
- try rerun using ubuntu on batch_1.pep to shorten the total time.
- also tried on the web version again, generally it is a bit slower than 
the terminal
- still exceed time limits, used R script to further divide to 13 batches.
- rerun ubuntu and website version
- the access is limited to sign in after one run, will sign in through the
website and finish running the rest on there. Everything seems to work, 
though the server gets busy around 15:00,cannot get project in.

## 5/12/2022
- finished running the rest of the batches on the DeepTMHMM website

## 5/17/2022
- tried to install pfam through conda, failed
- build a visual environment to solve the problem, could not activate the env
- changed into the ubuntu system through pycharm
- create new environment
- figure out the python interpreter for rlk-msuid-rice-identification project
```{bash}
    conda install -c bioconda pfam_scan
```
- this installed hmmer as well 

**according to perl/bioinfo thread, it is better to use hmmer 3 with cut off**
- unzip and index Pfam database
```{bash}
    gunzip Pfam-A.hmm.gz
    hmmpress Pfam-A.hmm
```
- generated 4 Pfam files as a result
```{bash}
  hmmscan --cpu 8 --notextw --cut_ga --domtblout hmmerout.txt Pfam-A.hmm all.pep
```

## 5/18/2022
- continue running the hmmscan

## 5/19/2022
- git push 

## 5/23/2022
- create pfamscan depository
- downloaded PfamScan.tar.gz
- gunzip PfamScan.tar.gz
- downloaded Pfam-A.hmm.dat.gz and Pfam-A.hmm.gz
- gunzip these two files, the original file will disappear
- using conda installed perl moose
- try the command 
```
pfam_scan.pl -fasta pep/all.pep -dir pfam -outfile output/pfam_A_out
```
- computer was left to run for the night, even though there is no message in the 
terminal, the output is the same as Dr Furuta's

## 5/30/2022
- combine-TM-data.py
- try to combine all the DeepTMHMM results into one file

## 5/31/2022
- combine-df.py
- imported pfam_A_out.txt, output pfam_cleaned.csv
- imported prediction_results.txt for signal p, output signalp_cleaned.csv
- imported TM_results.txt, output tm_cleaned.csv

## 6/1/2022
- import three cleaned data files, output two files for github pipline
- 
## 6/13/2022
- completed run1 for github script using ath data provided
- talked with Dr. Furuta, decided to use the other_d_rlk list in the github, while adding RLK, RLP 
domains experimentally validated in rice. No other domains from validated rice RLK or RLP that need
to be added.

## 6/15/2022
- I realised there is a problem when write out the two rice files, the concat method
used was not joining the data correctly
- also signal IP some isoform of the genes were short indexed, 
need to fix that as well.
- checked the TM results as well, eg LOC_Os03g05390.12 will only be recorded
as LOC_Os03g05390.1. Will update that result as well.
- in the end, both signalp and TM had the same number of output: 66153, 
pfam is more due to duplicated domains, it is 80455.
- I also output pfam_tm_signalp_combined csv file for future purpose
- re-run the script and the result looked reasonable

## 6/16/2022
- updated gene look up script to compare experimentally validated genes and predicted
genes. 
- the result looks promising. all the genes supposed to be predicted were there.
the rest of them missing a TM domain. 

## 6/17/2022
- during the process of organizing rlk and rlp list for sensei, I realized the rlk count
for generating the general rlk excel used rlp count for glectin_b/s/p. 
- created the heatmap depository and rlk_deg.py to obtain the rlk, rlp degs. 

## 6/21/2022
- corrected sp column of rlk list
- produced the rlk and rlp deg list
 