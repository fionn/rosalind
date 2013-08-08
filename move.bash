#!/bin/bash

# A script for quickly moving Rosalind files after download.

cd ~/Downloads/

if [ -f rosalind_*.txt ]
then
	echo -n "Moving "
	ls -1b rosalind_*.txt | tr "\n" " "
	echo -e "to ~/code/rosalind/data/"
	mv ./rosalind_*.txt ~/code/rosalind/data/
else
	echo "No Rosalind data found"
fi
cd - 1>/dev/null

