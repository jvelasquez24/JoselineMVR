#creating windows 
import sys 
import math
#inputs 
infile = sys.argv[1]
window_size = int(sys.argv[2])
name = infile.split(".")[0]
#Settinng position markers 
start_pos = 0
end_pos = start_pos + window_size
header = " "
#opening vcf & header 
inputvcf = open(infile,"r")
for line in inputvcf:
	if line.startswith("#CHROM"):
		header = line
inputvcf.close() 

#creating windows 
inputvcf = open(infile,"r")
ofi = open(name + "_{}.vcf".format(start_pos), 'w')
ofi.write(header)

for basecall in inputvcf:
	if basecall.startswith("#"):
			continue 
	pos = int(basecall.split('\t')[1])
	if start_pos < pos < end_pos:
		ofi.write(basecall)
	elif pos >= end_pos:
		ofi.close()
		start_pos = math.floor(pos / window_size) * window_size
		print("{} is geater than {}".format(pos, end_pos))
		end_pos = start_pos + window_size
		file_name = name + "_{}.vcf".format(start_pos)
		print("starting a new file named {}, for bases {} to {}".format(file_name, start_pos, end_pos))
		ofi = open(file_name, 'w')
		ofi.write(header)
		end_pos = start_pos + window_size
		ofi.write(basecall)