import sys
#inputs
mentors_file= sys.argv[1]
mentee_file= sys.argv[2]
#opening files
m= open(mentors_file, 'r')
f= open(mentee_file,'r')
line=f.readline()
#opening storage places 
mentee={}
mentors={}
matched={}
leftovers = []

for alines in m:
  if 'alias' in alines:
    continue
  mspline=alines.split()
  mentors[mspline[0]]=[mspline[1],mspline[2]]
# print(mentors)
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
  for i in range(2,6):
    mentor_name=mentors[fsplit[i]][0]
    if len(matched[mentor_name]) < int(mentors[fsplit[2]][1]):
     matched.setdefault(mentor_name, []).append(mentee_name)
     break
    elif mentee_name not in leftovers:
      leftovers.append(mentee_name)
      break
    else:
        print('im broken'+ mentee_name)