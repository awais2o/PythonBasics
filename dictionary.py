#dictionary is nothing but key value pairs

d1={1:7,"bilal":3,3:"awais"}   # kind of list  in which we can allocate any data eg list, str, dictionary itself with help of key
#key:data key can be string or int
print(d1["bilal"]) #key is  a kind of index to aproach data

d1["qamar"]=59
print(d1)
#in dict if we use d1=d2 so there will be pointer connnection chsnge in 1 willl chsangee other so use funtion   copy()
d2=d1.copy()
print(d2)