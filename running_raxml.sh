#!/bin/bash
## ogaden
SOD1_ogaden_outfi_name=../../Data/fasta/SOD1_ogaden_no_bt.fasta
PRLH_ogaden_outfi_name=../../Data/fasta/PRLH_ogaden_no_bt.fasta
BTA22_ogaden_outfi_name=../../Data/fasta/BTA22_ogaden_no_bt.fasta

## ndama
SOD1_ndama_outfi_name=../../Data/fasta/SOD1_ndama_no_bt.fasta
PRLH_ndama_outfi_name=../../Data/fasta/PRLH_ndama_no_bt.fasta
BTA22_ndama_outfi_name=../../Data/fasta/BTA22_ndama_no_bt.fasta


raxmlHPC -m GTRGAMMA -p 2 -n ogaden_PRLH -s ${PRLH_ogaden_outfi_name}
raxmlHPC -m GTRGAMMA -p 2 -#100 -b 2 -n ogaden_PRLH_boot -s ${PRLH_ogaden_outfi_name}
raxmlHPC -m GTRGAMMA -f b -t RAxML_bestTree.ogaden_PRLH -z RAxML_bootstrap.ogaden_PRLH_boot -n boot_bipartions_ogaden_PRLH

raxmlHPC -m GTRGAMMA -p 2 -n ogaden_SOD1 -s ${SOD1_ogaden_outfi_name}
raxmlHPC -m GTRGAMMA -p 2 -#100 -b 2 -n ogaden_SOD1_boot -s ${SOD1_ogaden_outfi_name}
raxmlHPC -m GTRGAMMA -f b -t RAxML_bestTree.ogaden_SOD1 -z RAxML_bootstrap.ogaden_SOD1_boot -n boot_bipartions_ogaden_SOD1

raxmlHPC -m GTRGAMMA -p 2 -n ogaden_BTA22_ref -s ${BTA22_ogaden_outfi_name}
raxmlHPC -m GTRGAMMA -p 2 -#100 -b 2 -n ogaden_BTA22_boot -s ${BTA22_ogaden_outfi_name}
raxmlHPC -m GTRGAMMA -f b -t RAxML_bestTree.ogaden_BTA22_ref -z RAxML_bootstrap.ogaden_BTA22_boot -n boot_bipartions_ogaden_BTA22


raxmlHPC -m GTRGAMMA -p 2 -n ndama_PRLH -s ${PRLH_ndama_outfi_name}
raxmlHPC -m GTRGAMMA -p 2 -#100 -b 2 -n ndama_PRLH_boot -s ${PRLH_ndama_outfi_name}
raxmlHPC -m GTRGAMMA -f b -t RAxML_bestTree.ndama_PRLH -z RAxML_bootstrap.ndama_PRLH_boot -n boot_bipartions_ndama_PRLH

raxmlHPC -m GTRGAMMA -p 2 -n ndama_SOD1 -s ${SOD1_ndama_outfi_name}
raxmlHPC -m GTRGAMMA -p 2 -#100 -b 2 -n ndama_SOD1_boot -s ${SOD1_ndama_outfi_name}
raxmlHPC -m GTRGAMMA -f b -t RAxML_bestTree.ndama_SOD1 -z RAxML_bootstrap.ndama_SOD1_boot -n boot_bipartions_ndama_SOD1

raxmlHPC -m GTRGAMMA -p 2 -n ndama_BTA22_ref -s ${BTA22_ndama_outfi_name}
raxmlHPC -m GTRGAMMA -p 2 -#100 -b 2 -n ndama_BTA22_boot -s ${BTA22_ndama_outfi_name}
raxmlHPC -m GTRGAMMA -f b -t RAxML_bestTree.ndama_BTA22_ref -z RAxML_bootstrap.ndama_BTA22_boot -n boot_bipartions_ndama_BTA22

