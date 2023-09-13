#Dictionaries
my_dict= {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

d={'k1':'123','k2': '[1,2,3]', 'k3':{'insidekey':'100'}}
print(d['k2'])
print(d['k3'])
print(d['k3']['insidekey'])
d['k4']=500
print(d)
print(d.keys())
print(d.values())
print(d.items())
