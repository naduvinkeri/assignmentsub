# sys module to take command line arguments for input file and output file
# math for infinity
import sys
from math import inf

# open input file in read 
f=open(sys.argv[1],"r")
# dictionary goodies 
goodies={}

# generate dictionary out of file
for i,x in enumerate(f):
	if i==0:
		numberOfEmployees = int(x.split()[-1])
	elif i<4:
		continue
	else:
		g,p = x.split(': ')
		goodies[g]=int(p)

# close file
f.close()
#print(goodies)

# sort dictionary as part of algorithm
sorted_l = sorted(goodies, key=goodies.get)

# declare minimum value for comparison
minval=float(inf)

# starting index of answer
si=0

# find minimum value difference
for j in range(si,len(goodies)-numberOfEmployees):
	te = goodies[sorted_l[j+numberOfEmployees-1]]-goodies[sorted_l[j]]
	#print(te)
	if te<minval:
		minval=te
		si=j

# open file in write mode
wf = open(sys.argv[2],"a")
wf.write("The goodies selected for distribution are:\n\n")

# write values along with goodies
for j in range(numberOfEmployees):
	wf.write(str(sorted_l[si+j])+": "+str(goodies[sorted_l[si+j]]))
	wf.write("\n")

# write final value to file and close
wf.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(minval))
wf.close()

#print("final ",minval)
