import sys
#inputs
#remember to add python script names to input
mentors_file= sys.argv[1]
mentee_file= sys.argv[2]
outfile=sys.argv[3]
#opening files
m= open(mentors_file, 'r')
f= open(mentee_file,'r')
w= open(outfile,'w+')
line=f.readline()
#opening storage places
mentors={}
matched={}
leftovers = []
ustu=[]
#Creating Mentor information
for alines in m:
  if 'alias' in alines:
    continue
  mspline=alines.split()
  mentors[mspline[0]]=[mspline[1],mspline[2]]
#This is setting up the names of mentors with mentee list
for i in mentors:
  matched[mentors[i][0]]=[]
#This is creating the menee names
for line in f:
  fsplit = line.split()
  fn=fsplit[0]
  ln=fsplit[1]
  mentee_name=fn + ' '+ ln
  #Starting loop to check if mentor has space, matched, leftovers and if not working
  mentor_match = False
  for i in range(2,6):
    if mentor_match == False:
      mentor_name=mentors[fsplit[i]][0]
      if 'ustu' in line:
        ustu.append(mentee_name)
        mentor_match = True
      elif len(matched[mentor_name]) < int(mentors[fsplit[i]][1]):
        matched.setdefault(mentor_name, []).append(mentee_name)
        mentor_match = True
  if mentor_match == False:
        leftovers.append(mentee_name)
#Closing files 
f.close()
m.close()
#Wrting outfile with matches
header='USTU,'
w.write(header)
for a in ustu:
    w.write(str(a)+',')
unpaired='\nUnpaired,'
w.write(unpaired)
for b in leftovers:
    w.write(str(b)+',')
mentor='\nMatches\n'
w.write(mentor)
mach=''
for c in matched:
  w.write(str(c)+',')
  for d in matched[c]:
    mach=str(d)
    w.write(mach+',')
  newline='\n'
  w.write(newline)
w.close()
