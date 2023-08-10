"""This script will generate a printout with the number of sequence reads per 
sample from a MiSeq download
Usage: python count_reads.py <fastq directory>
"""
import subprocess
import sys
import os
import re
import gzip

raw_output = subprocess.check_output('find {} -type f -name "*.fastq.gz" | grep -v Apple'.format(sys.argv[1]), shell = True)
pathlist = sorted(raw_output.rstrip().split('\n'))

if len(pathlist) % 2 == 0:
        for i in range(0, len(pathlist), 2):
            filename = os.path.basename(pathlist[i])
            sample = re.sub("_S[0-9]*_L[0-9]*.*","", os.path.basename(pathlist[i]))
            count = 0
            for line in gzip.open(pathlist[i]): count += 1
            print('\t'.join([str(sample), str(count / 4)]))
else: 
    print("check: uneven number of files")
