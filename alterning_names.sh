#!/bin/bash

#Vcf to fasta
#Change tip names

vcf_to_fasta_python_script=VCFtoFASTA.py
meta_file=../../Data/meta_og_nd.csv

##Ogaden
ogaden_SOD1_outfi=../../Data/vcf/ogaden_SOD1.vcf
ogaden_PRLH_outfi=../../Data/vcf/ogaden_PRLH.vcf
ogaden_BTA22_outfi=../../Data/vcf/ogaden_BTA22.vcf

SOD1_ogaden_outfi_name=../../Data/fasta/SOD1_ogaden_no_bt.fasta
PRLH_ogaden_outfi_name=../../Data/fasta/PRLH_ogaden_no_bt.fasta
BTA22_ogaden_outfi_name=../../Data/fasta/BTA22_ogaden_no_bt.fasta

#SOD1
python2 ${vcf_to_fasta_python_script} ${ogaden_SOD1_outfi} ${SOD1_ogaden_outfi_name} ${meta_file}
#PRLH
python2 ${vcf_to_fasta_python_script} ${ogaden_PRLH_outfi} ${PRLH_ogaden_outfi_name} ${meta_file}
#BTA22
python2 ${vcf_to_fasta_python_script} ${ogaden_BTA22_outfi} ${BTA22_ogaden_outfi_name} ${meta_file}

##Ndama
ndama_SOD1_outfi=../../Data/vcf/ndama_SOD1.vcf
ndama_PRLH_outfi=../../Data/vcf/ndama_PRLH.vcf
ndama_BTA22_outfi=../../Data/vcf/ndama_BTA22.vcf

##Ndama
SOD1_ndama_outfi_name=../../Data/fasta/SOD1_ndama_no_bt.fasta
PRLH_ndama_outfi_name=../../Data/fasta/PRLH_ndama_no_bt.fasta
BTA22_ndama_outfi_name=../../Data/fasta/BTA22_ndama_no_bt.fasta
#SOD1
python2 ${vcf_to_fasta_python_script} ${ndama_SOD1_outfi} ${SOD1_ndama_outfi_name} ${meta_file}
#PRLH
python2 ${vcf_to_fasta_python_script} ${ndama_PRLH_outfi} ${PRLH_ndama_outfi_name} ${meta_file}
#BTA22
python2 ${vcf_to_fasta_python_script} ${ndama_BTA22_outfi} ${BTA22_ndama_outfi_name} ${meta_file}

