import os
from time import sleep

def ips(start, end):
	import socket, struct
	start = struct.unpack('>I', socket.inet_aton(start))[0]
	end = struct.unpack('>I', socket.inet_aton(end))[0]
	return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

iplist = []
g = open('iprangelist.txt', 'r')

for line in g:
	start1= str(line.strip().split('-')[0].strip())
	end1= str(line.strip().split('-')[1].strip())
	try:
		#print "Hello"
		#print ips(start1,end1)
		iplist.extend(ips(start1,end1))
		iplist.append(end1)
		#print iplist
		#sleep(200)
	except Exception, err:
		print '1 %s '% err

g.close()

print "Total IP converted %s "% len(iplist)
f = open('IPrange2list_output.txt', 'w')
for item in iplist:
	f.write("%s\n" % item)
f.close() # close the file