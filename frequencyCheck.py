f = open('periodBlocks.txt','r')
l = f.readlines()
#print(l)
for x in range(0,len(l),2):
	k = l[x]
	t = 0
	for i in range(len(k)):
		if k[i] == ':':
			t = k[(i+2):-1]
	#print(t)
	pb = list(map(int,t.strip().split(' ')))
	f1,f2,f3 = 0,0,0
	for i in range(len(pb)-4):
		if pb[i:i+4] == [3,5,5,5]:
			f3 += 1
		elif pb[i:i+3] == [3,5,5] and pb[i+3] != 5:
			f2 += 1
		elif pb[i:i+2] == [3,5] and pb[i+2] != 5:
			f1 += 1
	print(f1,f2,f3)

