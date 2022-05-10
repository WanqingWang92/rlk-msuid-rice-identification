# RLK project journal

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

