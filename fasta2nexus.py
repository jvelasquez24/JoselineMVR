#trying to print nexus for cow
import sys
#input
infile=sys.argv[1]
outfile=sys.argv[2]
ofi= open(outfile,'w')
fi=open(infile,'r')
#storage
dna={}
name=[]
seq=[]
#sorting fasta
for line in fi:
    if '>' in line:
        lplit=line.split()
        name.append(lplit[0].replace('>',''))
    elif 'A' or '?' in line:
        seqlit=line.split()
        seq.append(seqlit[0])
for i in range(0,len(name)):
    dna[name[i]]=[seq[i]]
#formating
if len(seq[0])==len(seq[1]):
    print("these first two are equal")
    ntax=str((len(dna)))
    nchar=str(len(seq[0]))
    newline='\n'
    header='#NEXUS\n'
    start_block='Begin DATA;\n'
    data_type='DATATYPE=DNA;'
    first_line='\tDimensions NTAX='+ntax+' NCHAR='+nchar+';\n'
    second_line='\tFormat MISSING=? GAP=-'+' '+data_type+'\n'
    matrix='\tMatrix'
    endblock='\t;\nEND;'
    #writing out nexus file
    ofi.write(header+newline+start_block+first_line+second_line+matrix+newline)
    for ii in dna:
        ofi.write(str(ii)+' ')
        ofi.write(str(dna[ii][0])+'\n')
    ofi.write(endblock)
    #Closing files
    ofi.close()
    fi.close()
else:
    print("ERROR: Sequences are not equal lengths")
