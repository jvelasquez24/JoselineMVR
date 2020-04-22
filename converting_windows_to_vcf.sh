#!/bin/bash
#python script location
py_script=/home/joseline/Desktop/cattle/actualproject/Code/SummerGenomics/VCFtoFASTA.py
py_script2=/home/joseline/Desktop/cattle/actualproject/Code/JoselineMVR/fasta2nexus.py
metafi=/home/joseline/Desktop/cattle/actualproject/spring_2020/vcfs/meta_og_nd.csv
window_size=50000

for f in *.vcf; do
	ofi=$(echo `basename $f` | cut -d '.' -f1)
	opath=".fasta"
	python2 ${py_script} $f $ofi$opath $metafi
done

for d in *.fasta; do
	ofi2=$(echo `basename $d` | cut -d '.' -f1)
	opath2=".nex"
	python2 $py_script2 $d $ofi2$opath2
done

mv *.vcf vcf/
mv *.fasta fasta/
mv *.nex nexus/
