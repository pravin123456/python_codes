def findMinDiff(arr, n):
    # Initialize difference as infinite
    diff = 10 ** 20
    l=[]
    # Find the min diff by comparing difference
    # of all possible pairs in given array
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
                #l.append((arr[i],arr[j]))
    l.append([arr[i],arr[j]])
                # Return min diff
    return l
li=[1,2,5,7,8,9]
findMinDiff(li,len(li))
