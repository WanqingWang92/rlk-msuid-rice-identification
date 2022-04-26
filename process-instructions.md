# Identification of RLK and RLP in rice

---

Receptor like kinases (RLKs) and receptor like proteins (RLPs) are the plasma membrane binding proteins which includes immunity related proteins detecting PAMPs[^fn1], MAMPs[^fn2], and DAMPs[^fn3].

Prof. Yoji Kawano in IPSR is working on rice immune system with molecular biological approaches. Now he is interested in listing up the RLKs and RLPs in rice, _Oryza sativa_. Well known rice annotation data labeled with MSU gene ID (starting with "LOC_Os") do not have any previous publication listing up those genes. Thus, he asked me to help his project to list up them with following the way demonstrated in [Restrepo-Montoya et al., 2020](https://doi.org/10.1186/s12864-020-06844-z). 

[^fn1]: pathogen associated molecular patterns
[^fn2]: microbe associated molecular patterns
[^fn3]: damage associated molecular patterns

---

## Set up data analysis environment

Date this task done: Nov. 18, 2021

### Required tools
This project follows the way shown in [Restrepo-Montoya et al., 2020](https://doi.org/10.1186/s12864-020-06844-z).

- SignalP 4.0
- TMHMM2
- PfamScan with HMMER3.1b1
- Tool reposited in https://github.com/drestmont/plant_rlk_rlp/

### Setting up
1. Download docker image for signalP
    ~~I first created a virtual environment named "rlk" using anaconda 
    for this project.~~
    I installed docker and pulled the image named streptomyces/signalp. 
    
    This image contains signalp of version 5 and 6.
    To run the container with the image, execute the follwing code.
    docker run --rm -it -v ${PWD}:/home/work streptomyces/signalp
    
    
    
1. Downloading TMHMM2
    TMHMM are the tools lisenced by DTU Health Tech  an can be 
    downloaded from their web page. Need to register 
    user information to download them. Anyway, I could get executable 
    binaries of those tools. 
    
    
    
1. Installing PfamScan and HMMER3.1b1
    Manual installation of HMMER3 was failed with unknown error (just I 
    could not understand what the error message meant). Thus, 
    I made virtual environment named "pfamscan" and installed PfamScan 
    and HMMER via conda. The version of them were 1.6 and 3.3.2 for 
    PfamScan and HMMER, respectively.  
    
    `conda install -c bioconda pfam_scan`
    
    
    
1. Get clone of the script in github
    I just cloned files from https://github.com/drestmont/plant_rlk_rlp/
    which contains the tool I need.

### Run tools
1. signalP
- enter to the docker container
```{bash}
docker run --rm -it -v ${PWD}:/home/work streptomyces/signalp
```
The current directory specified as ${PWD} should contains a FASTA file to analyze via signalp.

- execute signalp

```{bash}
mkdir signalp_out

signalp6 --fastafile pep/all.pep --organism eukarya --output_dir signalp_out \
--format txt
```



2. TMHMM2
    Executable binary file does not work. Thus, I split multi-FASTA into 
    batches to be accepted by the TMHMM2 web tool. I submited 7 bathces
    each of which has 10,000 entries to the web tool in total and got the results.

  


3. PfamScan
Download Pfam-A.hmm.gz and Pfam-A.hmm.dat.gz from the Pfam web page and unziped them.
The current release is version 34.0.
Then, run the following to make valid database.
```{bash}
hmmpress Pfam-A.hmm
```

Execute pfam_scan.pl as following.
```{bash}
pfam_scan.pl -fasta pep/all.pep -dir tools/pfamdb -outfile pfam_out/pfam34_A_out
```



4. plant_rlk_rlp

---

## Note

- Nov. 18

  I've set up the pipeline, except for TMHMM2 which downloaded executable file does not respond. I went through the pipeline with the rice MSU genes and summarized data in a spread sheet to share with Prof. Kawano.

  
