

def findm(*t,**kwargs):
    for k,v in kwargs.items():
        print(v)
    #l=[]
    for i in t:
        l.append(i)
    t=[]
    while l:
        max=l[0]
        for i in range(len(l)):
            if l[i] > max:
                max=l[i]
        t.append(max)
        l.remove(max)
    print(t)
l=[1,3,-4,5,2]
k={'1':2}


nums = [1, 2, 3, 4, 5, 6]
print([nums[i ^ 1] for i in range(len(nums))])
nums=[nums[i^1] for i in range(len(nums))]
print(nums)

def find(*args,**kwargs):
    sum=0
    for i in args:
        sum+=i
    print (sum)
    #for k,v in kwargs.items():
    print(kwargs["a"])
    for k,v in kwargs.items():
        print(k,v)
h={"a":2,"b":2}
find(1,2,3,4,**h)


def findsum(num,target):
	l=[]
	for i in range(len(num)):
		sum=0
		for j in range(i,len(num)):
			sum+=num[j]
			if sum==target:
				l.append(num[i:j+1])
	print(l)
num=[1,2,3,4]
target=3
findsum(num,target)



def findmaxcoun(str):
    l=len(str)
    res=str[0]
    count=0
    for i in range(l):
        ccount=1
        for j in range(i+1,l):
            if str[i] != str[j]:
                break
            ccount+=1
        if ccount>count:
            count=ccount
            res=str[i]
    print(res)
findmaxcoun("abccdddc")



def finmaxcoun(str):
    i=0
    j=len(str)
    l=len(str)
    res=str[0]
    count=0
    for i in range(j):
        ccount=1
        for j in range(i+1,l):
            if str[i]!=str[j]:
                break
            ccount+=1
        if ccount>count:
            count=ccount
            res=str[i]
    print("result is:",res)

str="aabbbbc"
finmaxcoun(str)

def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return (excl if excl > incl else incl)


# Driver program to test above function
arr = [5, 5, 10, 100, 10, 5]
print ("max sum is",find_max_sum(arr))


def maxSubArraySum(a, size):
    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far



my_list = [97, 98, 97, 1, 2, 100, 98, 99, 97, 98, 97];
    #sort list max to min
my_list.sort(reverse = True)
    # take largest number as starting point
last_item = my_list[0]
new_list = [last_item]
print(new_list)
    # loop through list for every item to assure that we dont stop too soon
#for i in range(len(my_list)):
for number in my_list:
            # compare the current number with the last number inserted to new_list
            # if its smaller we add it to the list and update the last item
    if number == last_item-1:
        new_list.append(number)
        last_item = number
print("ne",new_list)

my_list = [97, 98, 97, 1, 2, 100, 98, 99, 97, 98, 97];
# sort list max to min
my_list.sort(reverse=True)
#print(my_list)
# take largest number as starting point
last_item = my_list[0]
new_list = [last_item]
# loop through list for every item to assure that we dont stop too soon
for i in range(len(my_list)):
    for number in my_list:
        # compare the current number with the last number inserted to new_list
        # if its smaller we add it to the list and update the last item
        if number == last_item - 1:
            new_list.append(number)
            last_item = number
print(new_list)

import re
regex=r"([a-zA-Z]+)\ (\d+)"
regex1=r"()"
regex = r"([a-zA-Z]+)\ (\d+)"
regex=r"([a-zA-Z]+)\ (\d+)"
l=[1,2,3]

print (k in enumerate(l))

match = re.search(regex, "I was born on June 24")

if match != None:

    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index % s, % s" % (match.start(), match.end()))

    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: % s" % (match.group(0)))

    # So this will print "June"
    print("Month: % s" % (match.group(1)))

    # So this will print "24"
    print("Day: % s" % (match.group(2)))

else:
    print("The regex pattern does not match.")


def nextPermutation(arr):
    # find the length of the array
    n = len(arr)

    # start from the right most digit and find the first
    # digit that is smaller than the digit next to it.
    k = n - 2
    while k >= 0:
        if arr[k] < arr[k + 1]:
            break
        k -= 1

    # reverse the list if the digit that is smaller than the
    # digit next to it is not found.
    if k < 0:
        arr = arr[::-1]
    else:

        # find the first greatest element than arr[k] from the
        # end of the list
        for l in range(n - 1, k, -1):
            if arr[l] > arr[k]:
                break

        # swap the elements at arr[k] and arr[l
        arr[l], arr[k] = arr[k], arr[l]

        # reverse the list from k + 1 to the end to find the
        # most nearest greater number to the given input number
        arr[k + 1:] = reversed(arr[k + 1:])

    return arr


# Driver code
arr = [5, 3, 4, 9, 7, 6]






