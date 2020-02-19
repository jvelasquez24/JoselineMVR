#!/bin/bash
#python script location 
py_script=/home/jvelasquez2408/Desktop/actualproject_harddrive/spring_2020/Code/SummerGenomics/VCFtoFASTA.py
py_script2=/home/jvelasquez2408/Desktop/actualproject_harddrive/spring_2020/Code/fasta2nexus.py
for f in ../*.vcf; do
	ofi=$(echo `basename $f` | cut -d '.' -f1)
	opath=".fasta"
	python2 ${py_script} $f $ofi$opath
done 

for d in *.fasta; do 
	ofi2=$(echo `basename $d` | cut -d '.' -f1)
	opath2=".nex"
	python2 $py_script2 $d $ofi2$opath2
done 
