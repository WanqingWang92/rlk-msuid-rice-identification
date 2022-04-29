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

