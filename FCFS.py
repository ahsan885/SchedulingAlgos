#!/usr/bin/python
a=[]
t=0
total=raw_input("Enter total number of processes:")

for i in xrange(int(total)):
	a.append([])
	a[i].append(raw_input("Enter Name of process:"))
	a[i].append(int(raw_input("Arrival Time:")))
	a[i].append(int(raw_input("burst time:")))
	t=t+a[i][2]

a.sort(key= lambda a:a[1])
print 'PName\tA. Time\tB.Time'

for i in xrange(int(total)):
	print a[i][0] ,'\t',a[i][1],'\t',a[i][2]

print "Total Time : ",t
