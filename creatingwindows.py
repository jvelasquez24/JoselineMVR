#creating windows 
import sys 
#inputs 
infile = sys.argv[1]
outfile = sys.argv[2]
window_size = sys.argv[3]
#Getting header & data
lines_per_file = int(window_size)
smallfile = None
header=''
with open(infile) as bigfile:
    for lineno, line in enumerate(bigfile):
    	if line.startswith('#'):
    		header=line
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = str(outfile)+'{}.vcf'.format(lineno)
            smallfile = open(small_filename, "w")
            smallfile.write(header)
    	if '#' in line:
    		continue 
        smallfile.write(line)
    if smallfile:
        smallfile.close()