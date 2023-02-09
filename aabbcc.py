string = "aabbccabc"
i = 0
j = len(string)
st=""
while i < j:
    count = 1
    while (i<j-1 and (string[i] == string [i+1])):
        count+=1
        i+=1
    i+=1
    st+=(string[i-1]+str(count) if (count >1) else string[i-1])
#print(string[i-1]+str(count) if (count >1) else string[i-1])
print(st)
