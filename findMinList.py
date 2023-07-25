list = [-1,2,3,4,-2,0]
#min = list[0]
#max = list[0]
newl = []
while list:
    min = list[0]
   # print(min)
    for i in range(len(list)):
        if list[i] < min:
           min = list[i]
	#   print(min)
    newl.append(min)
    list.remove(min)
#    if list[i] > max:
#       max = list [i]
#print ("Min and Max valu is", min,max)
print ("New List",newl)


