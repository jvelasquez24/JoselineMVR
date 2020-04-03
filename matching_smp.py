#! /usr/bin/env python
#joseline m velasquez-reyes
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--student_file')
    parser.add_argument('--alias_file')
    parser.add_argument('--outfile')

def matching_process():
    mentors={}
    matched={}
    leftovers = []
    ustu=[]
    #opening files
    m= open(mentor_file, 'r')
    f= open(mentee_file,'r')
    w= open(outfile,'w')
    line=f.readline()
#Creating Mentor information
    for alines in m:
      if 'alias' in alines:
        continue
      mspline=alines.split(',')
      mentors[mspline[0]]=[mspline[1],mspline[2]]
    #This is setting up the names of mentors with mentee list
    for i in mentors:
      matched[mentors[i][0]]=[]
    #This is creating the mentee names
    for line in f:
      fsplit = line.split(',')
      fn=fsplit[1]
      ln=fsplit[2]
      mentee_name=fn + ' '+ ln
      #Starting loop to check if mentor has space, matched, leftovers and if not working
      mentor_match = False
      for i in range(4,8):
        if mentor_match == False:
          mentor_name=mentors[fsplit[i]][0]
          if 'day' in line:
            ustu.append(mentee_name)
            mentor_match = True
          elif len(matched[mentor_name]) < int(mentors[fsplit[i]][1]):
            matched.setdefault(mentor_name, []).append(mentee_name)
            mentor_match = True
      if mentor_match == False:
        if len(matched[mentor_name]) < int(mentors[fsplit[i]][1]):
            matched.setdefault(mentor_name, []).append(mentee_name)
            mentor_match = True
        else:
            if mentee_name in leftovers:
                print(mentee_name + ' already in leftovers ')
            elif mentee_name not in leftovers:
                leftovers.append(mentee_name)
    val_list = list(mentors.values())
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
      for e in val_list:
        if e[0] == c:
          empty_slots = int(e[1]) - len(matched[e[0]])
          w.write(str(empty_slots)+' slots left,')
      newline='\n'
      w.write(newline)
#Closing files
    f.close()
    m.close()
    w.close()
#if you have any questions contact joselinev534@gmail.com

def main():
    args = parse_args()
    matching_process(args.alias_file,args.student_file,args.outfile)
