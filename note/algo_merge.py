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
		lft = a[:mid] #What if this actually created a new array and put all the numbers in?
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
merge2(array,[],0,len(array)-1,invCount)


'''
The truth of merge sort in action, 
is that you have two arrows which locate the indices of the array you are going to split,
and then you move them as the way to merge
'''

'''
Array for science 
[6,1,7,2,5]
'''
def merge2(a,tmp,invCount,left,right,invCount):
	if left < right:
		int center = (left + right) // 2
		merge2(a,tmp,left,center)
		merge2(a,tmp,center + 1,right)
		merge_both(a,tmp,left,center + 1, right)

def merge_both(a,tmp,left,right, rightEnd):
	i = 0 #For left part 
	j = 0 #For right part
	k = 0 #For tmp array

	while i < len(left) and j < len(right):
		if a[left] < a[right]:
			tmp[k] = a[left]
			i += 1
		else:
			tmp[k] = a[right]
			j += 1
		k += 1

		while i < len(left):
			tmp[k] = a[i]
			i += 1
			k += 1
		while j < len(right):
			tmp[k] = a[j]
			j += 1
			k += 1
	print(a)