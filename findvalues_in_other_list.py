l1 = [1,3,0]
l3 = [1,2,3,2,3,3,3,1]
d={}
#d1 = {l1[i]:l1[i]+1 for i in range(len(l1)) if l1[i] in l3}
#print(d1)

for i in l1:
    for j in l3:
        if i ==j:
            if i in d:
                d[i]=d[i]+1
            else:

                d[i]=1
print(d)

