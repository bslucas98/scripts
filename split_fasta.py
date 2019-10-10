#!/bin/env python
## Before running this script, create a folder called split_fastas to store the output files
## PS.: Header names must not have whitespaces

#open file:
with open("/set/path/to/input.fasta", "r") as f:
    input = f.read().splitlines()

#split sequences:
for i in range(len(input)):
    if input[i][0] == ">":
        filename = "/Path/to/split_fastas/"+input[i]+".fa"
        fileout = open(filename, "w")
        fileout.write(input[i]+"\n"+input[i+1]+"\n")
        fileout.close()
f.close()

