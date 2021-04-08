import sys
import numpy as np
import pandas as pd

#the file names and outfi name
clinical = sys.argv[1]
gene_expression = sys.argv[2]
outfi = sys.argv[3]

#opening clincial and gene expression data
clincial_data = pd.read_csv(clinical, sep = '\t')
gene_expression_data = pd.read_csv(gene_expression, sep = "\t")

#subsetting clincial data
is_primary = clincial_data["sample_type"]== "Primary Tumor" #checking for value in sample_type column
pt = clincial_data[is_primary] # contatins subset of clincial with only primary_tumor

#creating list of sample IDs from clincal data
only_primary_columns = list(pt["sampleID"])
only_primary_columns.insert(0,"sample")

#subsetting
primary_gene_expression = gene_expression_data[gene_expression_data.columns.intersection(only_primary_columns)]

#Normalizing data and printing out to csv
normalized_df = primary_gene_expression.apply(lambda x: x - primary_gene_expression.mean(axis = 1))
normalized_df.to_csv(outfi, sep='\t', mode='a')
