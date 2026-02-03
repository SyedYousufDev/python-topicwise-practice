s = set() 
s.add(20) 
s.add(20.0000000) 
s.add('20') # length of s after these operations? 
#Length will be 2 because 20 and 20.0 is same in value

print(len(s))