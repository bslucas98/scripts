#!/bin/bash 

## This script is usefull to extract specific sequences from a fasta file. Targeted sequence headers must be written in a \
## separate file (ex.: yourheaders.fa) with one header by line and can include the ">", although it's not required.
## Before running the script, be sure to set the path to your input headers file (line 7) and reference fasta (line 15)

FILES=yourheaders.fa

for f in $FILES
do
	echo "***Processing $f file***"
	headers=$(cat $f)
	for i in $headers
	do
		grep -A 1 "$i" path/to/reference.fa >> $f.filtered
		echo "$i done"
	done
done
