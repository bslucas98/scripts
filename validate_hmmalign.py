#!/bin/env python
## run hmmalign.sh script to generate alignments
## This script is usefull to validate hmmer alignments. It generates a file containing the alignment percentage for each sequence. 

import os

os.chdir("/Users/lucasb/Documents/kinome_hevea/kinome_identification/hmmer_output/hmmalign_out")
all_folders = os.listdir(".")

for folder in all_folders:
    if not folder.startswith("."):  #remove .DS_Store hidden file
        os.chdir("/Users/lucasb/Documents/kinome_hevea/kinome_identification/hmmer_output/hmmalign_out")
        folder_name = folder
        os.chdir(folder)
        all_files = os.listdir(".")
        out_name = "/Users/lucasb/Documents/kinome_hevea/kinome_identification/hmmer_output/validation_"+folder_name+".txt" 
        output = open(out_name, "w") 
        for arquivo in all_files:
            with open(arquivo, "r") as f:
                fasta = f.read().splitlines()
                contador = 0
                ref_count = 0
                protein_tag = "none"
                for element in fasta:
                    if element.startswith("XP_"):
                        element2 = element.split()
                        protein_tag = element2[0]
                        for amino in element2[1]:
                            if amino.isupper():
                                contador += 1
                    elif element.startswith("#=GC RF"):
                        element3 = element.split()
                        for base in element3[2]:
                            if base == "x":
                                ref_count += 1
            output.write(str(protein_tag) + "\t" + str(contador/ref_count) + "\n")
        output.close()
