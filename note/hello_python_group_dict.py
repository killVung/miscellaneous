def buildDict(**kwargs):	
	return { key : value for key,value in kwargs.items()} 

print(buildDict(two=3,three=4))