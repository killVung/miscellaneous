import re

#Spliting with style

s = "b ab\naab 123"
#print(s)
#Tokenlize the String seperated by ab, just like the one with space
a = re.split("ab",s) 
assert a == ['b ', '\na', ' 123']

a = re.split("ba" ,s)
assert a == [s] #Give out the token of original s, due to non detection

a = re.split("^b", s) 
assert a == ['',' ab\naab 123'] #Steal the String that started with given letter

a = re.split("^a",s)
assert a == [s] #Since it isn't started with a, therefore return the original string

#Something cool started here

s = "b ab\naab 123"
r = (re.compile("^a",re.M)).split(s) #Recompile the line in multiple lines, so ^a can detect the a after \na = r.split(s)
assert r == ["b ab\n","ab 123"]

r = (re.compile("b$",re.M)).split(s) #Recompile into multiple lines, tokenlize String end with b
assert r == ["b a","\naab 123"]

r = re.split(".",s) #This is not tokenlize by ., but rather all of the characters
assert r == ['','','','','\n','','','','','','','']

r = re.split("\d",s) #Split it as long as it's digit, represented in escaped sequence form
assert r == ["b ab\naab ","","",""]

r = re.split("\D",s) #Basically anything with capitalize, mean the opposite, including escape seq
assert r == ['','','','','','','','','','123']


r = re.split("\w",s) #alphanumeric

#assert r == ['',' ','','\n','','','',' ','','','']

r = re.split("\W",s) # non alphanumeric
assert r == ['b','ab','aab','123']

#Shit starts here
s = "b ab\naab 123"
m = re.search("(a*)b([^a]*)(a*)b", s) 
#Search zero a or more, stop by b
#Search everything or more but a, stop by the third query
#Search zero a or more, stop by b
assert m.group(0) == "b ab"

m = re.search("(a+)b([^a]*)(a+)b", s) 
#Search 



#assert m.group(0) == ""





