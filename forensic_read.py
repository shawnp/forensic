#!/usr/bin/env python3

with open("forensic_log") as f:
    content = f.read() # Read the whole file
    lines = content.split('|') # a list of all sentences
    for l in lines: # for each sentence
           print(l)
