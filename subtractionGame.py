# calculates the minimum excluded (non-negative) integer of a given set
def mex(s):
	s.sort()
	s1 = []
	for x in s:
		if x not in s1:
			s1.append(x)
	for i in range(len(s1)):
		if i != s1[i]:
			return i
	else:
		return i+1

# shows SG values for a subtraction game with subtraction set s upto element number n
def subtractionGame(s,n):
	sg = [0]*n
	for i in range(1,n):
		if min(s) <= i:
			s1 = [sg[i-x] if x <= i else 1000 for x in s]
			sg[i] = mex(s1)
		else:
			sg[i] = 0
	return sg

# generates a geometric sequence upto n terms with starting value a and ratio r
def geoSeq(a,r,n):
	return [a*(r**i) for i in range(n)]

# generates a fibonacci sequence upto n terms
def genFib(n):
	d = [1,1] + [0]*(n-2)
	for i in range(2,n):
		d[i] = d[i-1] + d[i-2]
	return d

# calculates z-array for period detection
def prefix(s):
    n = len(s)
    prefix = [-1]*n
    l,r = 0,0
    for i in range(1,n):
        if i > r:
            l,r = i,i
            while r < n and s[r-l] == s[r]:
                r += 1
            prefix[i] = r-l
            r -= 1
        else:
            k = i - l
            if prefix[k] < r - i + 1:
                prefix[i] = prefix[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                prefix[i] = r - l
                r -= 1
    return prefix

# calculates period length given SG-values
def period(l):
    l = l[::-1]
    pref = prefix(l)
    for i in range(1,len(pref)):
        pref[i] -= pref[i] % i
    # print(pref)
    best,end = 1,1
    for i in range(1,len(l)):
        z = pref[i]
        curend = i + pref[i]
        if pref[i] == 0:
          continue
        if z % i == 0 and i != curend and curend >= end:
          best = i
          end = curend
    for i in range(1,len(l)):
        if best % i == 0 and i + pref[i] == end:
            if pref[i] == 0:
                continue
            return i
    return best

# calculates pre-period length given SG-values and period length
def preperiod(sg, p):
    for i in range(len(sg)-p):
        if sg[i:i+p] == sg[i+p:i+2*p] == sg[i+2*p:i+3*p]:
            return i
    else:
        return -1

def solve(sg):
    p = period(sg)
    n0 = preperiod(sg, p)
    return [p, n0]

# print(calcPeriod(subtractionGame(geoSeq(1,3,10), 10)))
