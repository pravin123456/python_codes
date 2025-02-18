li=[0,-1,-1,3,4,2]
i=0
j=len(li)-1
while i < j:
    if li[i]>li[i+1]:
        li[i],li[i+1]=li[i+1],li[i]
        i=-1
    i+=1
print("In Jenkins result will be printed:",li)
