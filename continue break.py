i = 10
while(True):
    if i<20:
        i=i+2
        continue  #skip current iteration
    elif i==20:
        print(i)
        i=i+2
    else:
        break #exit loop
        
