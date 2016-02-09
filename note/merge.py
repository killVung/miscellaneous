def mergeIndex(a,b,c=[]):
	ccnt = 0
	acnt = 0
	bcnt = 0	
	invCount = 0
	while acnt < len(a) and bcnt < len(b):		
		if a[acnt] < b[bcnt]:
			c.append(a[acnt])
			acnt = acnt + 1
		else:
			invCount = invCount + (len(a) - acnt)			
			c.append(b[bcnt])			
			bcnt = bcnt + 1
		ccnt = ccnt + 1

	rest = a if acnt < len(a) else b	
	restcnt = acnt if acnt < len(a) else bcnt

	while restcnt < len(rest):
		c.append(rest[restcnt])
		restcnt = restcnt + 1	
	return invCount


def merge(a,invCount):		
	c = []	
	if len(a) > 1:		
		mid = len(a) // 2
		lft = a[:mid]
		rgh = a[mid:]	
		merge(lft,invCount)
		merge(rgh,invCount)
		invCount += mergeIndex(lft,rgh,c)	
	return c,invCount	

array = [1,3,5,2,4,6]
invCount = 0
array,invCount = merge(array,invCount)
print(array)
print(invCount)