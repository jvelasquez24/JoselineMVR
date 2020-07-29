import sys
import numpy as np
import pandas as pd

#the file names and outfi name
clinical = sys.argv[1]
gene_expression = sys.argv[2]
# outfi = sys.argv[3]

#opening clincial and gene expression data
df = pd.read_csv(clinical, sep = '\t')
df2 = pd.read_csv(gene_expression, sep = "\t")

#subsetting clincial data
is_primary = df["sample_type"]== "Primary Tumor" #checking for value in sample_type column
pt = df[is_primary] # contatins subset of clincial with only primary_tumor

#creating list of sample IDs from clincal data
only_primary_columns = list(pt["sampleID"])
# only_primary_columns.insert(0,"sample")
#subsetting
primary_gene_expression = df2[df2.columns.intersection(only_primary_columns)]
# av= primary_gene_expression.mean(axis = 1)
# print(primary_gene_expression)
# primary_gene_expression.to_csv(outfi, sep='\t', mode='a')
# primary_gene_expression["mean"] = av.values
print(primary_gene_expression.head())

#normalized_df = (primary_gene_expression - primary_gene_expression.mean(axis = 1))
#print(normalized_df.head())
# print(av.head())
#print(primary_gene_expression - primary_gene_expression.mean(axis = 1))
normalized_df = primary_gene_expression.apply(lambda x: x - primary_gene_expression.mean(axis = 1))
print(normalized_df.head())
