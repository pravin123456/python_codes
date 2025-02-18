
################# 01 ###############
s="Praavin@12hhhh3hjssjjsssii"
i=0
j=len(s)-1
kt=""
count=1
while i <j:
    if s[i]==s[i+1]:
        count+=1
    else:
        kt+=s[i] + str(count) if count >1 else s[i]
        count=1
    i+=1
kt+=s[i] + str(count) if count >1 else s[i]
print(kt)


################## 02 ###################
li=[2,1,2,3,4,3,2,1,2]
for i in range(len(li)):
    left=sum(li[:i])
    right=sum(li[i+1:])
    if left==right:
        print(li[i])

################# 03 ####################

k=18
prime=True
for i in range(2,k):
    if k%i==0:
        prime=False
if prime:
    print("Prime Number")
else:
    print("Not Prime")


################### 04 ####################
li=[]
for i in range(100,200):
    Prime=True
    num=i
    for j in range(2,num):
        if num%j==0:
            Prime=False
    if Prime:
        li.append(num)
print(li)

################### 05 ######################
k=123321
temp=k
rev=0
while temp!=0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if rev==k:
    print("Palindrome")
else:
    print("Not Palindrome")

################### 06 ########################
li1=[]
for i in range(100,200):
    num=i
    temp=num
    rev=0
    while temp !=0:
        dig= temp%10
        rev=rev*10+dig
        temp=temp//10
    if rev==num:
        li1.append(num)
print("All Prime Numbers",li1)

#################### 07 #######################

li2=[]
for i in range(100,200):
    num=i
    temp=num
    rev=0
    while temp !=0:
        dig= temp%10
        rev=rev+dig
        temp=temp//10
    if rev%2==0:
        li2.append(num)
print("All even sum Numbers",li2)

################### 08 ##########################

li3=[]
for i in range(100,500):
    num=i
    temp=num
    rev=0
    while temp !=0:
        dig= temp%10
        rev=rev+dig**3
        temp=temp//10
    if rev==num:
        li3.append(num)
print("All armstrong Numbers",li3)

#################### 09 ##########################

st2="{}[]"
def perm(st2):
    while True:
        if "{}" in st2:
            st2=st2.replace("{}","")
        if "[]" in st2:
            st2=st2.replace("[]","")
        else:
            return not st2
print(perm(st2))


##################### 10 #############################

st1="pravindevidaspatke"
st3={}
st4={w:1 if  w not in st3 and not st3.update({w:1}) else st3[w]+1 for w in st1}
print(st4)

st5={}
for i in st1:
    if i in st5:
        st5[i]=st5[i]+1
    else:
        st5[i]=1
print(st5)

##################### 11 ###############################

k=45

l=[0,2,44,46]
for i in range(len(l)):
    if l[i]>k:
        index=i
l=l[:index] + [k] + l[index:]

print(l)

##################### 12 ###############################

new_string = ""
string = "pythooonnnpooll"
count = 1
i=0
j=len(string)-1
count1=1
while i <j:
    if string[i]==string[i+1]:
        count1+=1
    else:
        new_string+=string[i]+ str(count1) if count1>1 else string[i]
        count1=1
    i+=1
new_string+=string[i]+ str(count1) if count1>1 else string[i]
print(new_string)

##################### 13 #######################

st1 = "Hi Pravin"
st1 = st1.split()
kt1 = ""
for i in st1:
    kt1 = kt1 + " " + i[:-1] + i[-1].upper() * 2
print("result is",kt1)

#################### 14 ########################

class A:
    __instance = None
    def __init__(self):
        if A.__instance !=None:
            raise Exception("Can not crate instance more than one")
        else:
            A.__instance=self
            self.name="Pravin"
            self.sirname="Patke"
            print(self.name,self.sirname)
a1=A()
#a2=A()

##################### 15 #########################

class B:
    def __init__(self):
        pass
    def whats(self):
        print("I am B")
class C:
    def __int__(self):
        pass

    def whats(self):
        print("I am C")
class D:
    @staticmethod
    def choice(ch1):
        if ch1=="B":
            return B()
        if ch1=="C":
            return C()
d1=D.choice("C")
d1.whats()

######################## 16 #######################

#with open('data1.txt', 'r') as rd:
 #   rd=rd.readlines()
#k1=rd[0].split()
#l1=rd[1].split()
#l2=rd[2].split()
#s1=zip(l1,l2)
#s2=zip(k1,s1)
#print(dict(s2))

######################## 17 #######################

import re
input = "ABCDCDCCDC .1.1 .1"
pattern=re.compile( r'(?=(CDC))')
li=pattern.findall(input)
l2=re.compile(r'(?=(CDC))')
print(l2.findall(input))

####################### 18 #######################

class C:
    def __init__(self):
        self.name=15
        self.__name1=20
        #self.str="Pravin"
class B(C):
    def __init__(self):
        #self.str=str
        super().__init__()
        print(self.name)
b1=B()

##################### 19 ########################

S = "code practice quiz   geeks"
def rev_w(S, start, end):
    while start<end:
        S[start],S[end]=S[end],S[start]
        start+=1
        end-=1
def rev_s(S):
    S=list(S)
    start,end=0,len(S)-1
    rev_w(S, start, end)
    start,end=0,0
    while end<len(S):
        if S[end]== " ":
            rev_w(S, start, end-1)
            start=end+1
        end=end+1
    rev_w(S, start, end-1)
    print(''.join(S))
rev_s(S)

######################## 20 ##################

def printsubsequence(input, output):
    if len(input)==0:
        print(output, end=" ")
        return
    printsubsequence(input[1:], input[0]+output)
    printsubsequence(input[1:], output)

input="abcd"
output=""
printsubsequence(input, output)

###################### 21 ####################

import csv, operator
data = csv.reader(open('s12.csv'), delimiter=',')
data1 = sorted(data, key=lambda kv:(int(kv[2]),kv[1],kv[0]))
print('After sorting:')
print(data1)
print(int(10))

###################### 22 #####################

import csv
fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
filename="1.csv"
with open(filename, 'w') as csvfile:
    wd=csv.writer(csvfile)
    wd.writerow(fields)
    wd.writerows(rows)
rd=csv.reader(open(filename))
print(next(rd))
for i in rd:
    print(i)

import json
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
rd=json.dumps(employee)
ld=json.loads(rd)
print(ld)

###################### 23 ####################

def outer(func):
    def inner(a,b):
        func(a,b)
    return inner

@outer
def sum(a,b):
    print(a+b)

sum(7,6)

###################### 24 ####################

lst = [1, 4, 5, 1, 3, 2, 1, -4]
lst1=[]
k=5
for i in range(len(lst)):
    sum_so_far=0
    for j in range(i, len(lst)):
        sum_so_far+=lst[j]
        if sum_so_far==k:
            lst1.append([lst[i:j+1]])
print(lst1)

l3=[]
while lst:
    num=lst.pop()
    diff=k-num
    if diff in lst:
        l3.append([diff,num])
print(l3)

######################## 25 #####################

list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
list1=sorted(list, key=lambda kv:(kv[1],kv[0]))
list2=sorted(list, key=lambda kv:(kv[0],kv[1]))
print(list1)
print(list2)

######################## 26 #######################

a=[1,1,2,3,4,5,2,1]
b=[1,2]
c=[i for i in b if i in a]
d={}
for i in b:
    for j in a:
        if i==j:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
print(d)

######################## 27 #########################

l=[i for i in range(100) if i%3==0]
print(l)

######################## 28 #########################

def myfunc():
    print("Mocked")
def func():
    print("Unmocked")
func=myfunc()

######################### 29 ########################

string="aabbcbbbcdfgg"
i=0
j=len(string)
kt2=""
while i <j:
    count=1
    while (i<j-1 and string[i]==string[i+1]):
        count+=1
        i+=1
    i+=1
    kt2+=string[i-1] + str(count) if count >1 else string[i-1]
print(kt2)

########################## 30 ########################

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
d={}
for k,v in files.items():
    d.setdefault(v,[]).append(k)
print(d)

########################## 31 #########################

for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
        if i==j:
            print(i*j, end=" ")
    print("\n")

########################## 32 ###########################

k=5
li4=[1,2,3,4,5]
li5=[]
for i in range(len(li4)-1):
    for j in range(i+1, len(li4)-1):
        if li4[i]+li4[j]==k:
            li5.append([li4[i],li4[j]])
print(li5)

########################## 33 ############################

li6=[1,6,3,5,2]

diff= 10**20
li7=[]
for i in range(len(li6)):
    for j in range(i+1,len(li6)):
        if abs(li6[i]-li6[j])<diff:
            diff=abs(li6[i]-li6[j])
            li7.append([li6[i],li6[j]])
print(li7[-1])

########################### 34 ############################

li8=[0,-1,-2,4,5,2]
i=0
j=len(li8)
while i < j-1:
    if li8[i]>li8[i+1]:
        li8[i],li8[i+1]=li8[i+1],li8[i]
        i=-1
    i+=1
print(li8)

########################## 35 ###############################

l11=["ll.c", "ll1.a", "kkkj.b", "hjdjh.d"]
l12=[i.split('.') for i in l11]
l13=sorted(l12, key=lambda kv:(kv[1],kv[0]))
l14=['.'.join(i) for i in l13]
print(l14)

########################## 37 ################################

for i in range(5,0,-1):
    for j in range(i,6):
        print(j, end=" ")
    print('\r')

######################### 38 ##################################

def args1(t, **d):
    for i in t:
        print(i, end=" ")
    for k,v in d.items():
        print(k,v)
l=[1,2,3,4]
d={"1":9, "2":9}
args1(l,**d)

nums = [1, 2, 3, 4, 5, 6]
l111=[nums[i^1] for i in range(len(nums))]
print(l111)

######################## 39 ##################################

s11="aaabbbbbddddddddddddddd"
i=0
j=len(s11)-1
res=s11[0]
ccount=1
for i in range(j):
    count=1
    for j in range(i+1,j):
        if s11[i]==s11[j]:
            count+=1
    if count>ccount:
        res=s11[i]
print(res)

###################### 40 ###################################

arr = [5, 5, 10, 100, 10, 5]
incl=0
excl=0
for i in arr:
    new_excl=excl if excl > incl else incl
    incl=excl+i
    excl=new_excl
print(excl if excl>incl else incl)

####################### 41 ###################################
a = [-2, -3, 4, -1, -2, 1, 5, -3]
max_so_far=0
max_ending_here=0
start=0
end=0
for i in range(len(a)):
    max_ending_here+=a[i]
    if max_so_far<max_ending_here:
        max_so_far=max_ending_here
        start=s
        end=i
    if max_ending_here<0:
        max_ending_here=0
        s=i+1
print(max_so_far, start, end)

###################### 42 ####################################

str1="Pravin"
r=''
for i in str1:
    if ord(i) in range(97,123):
        r+=chr(ord(i)-32)
    elif ord(i) in range(65,91):
        r+=chr(ord(i)+32)
print(r)

###################### 43 #####################################

li1=[-1,5,2,4,6]
for i in range(len(li1)):
    for j in range(i+1, len(li1)):
        if li1[i]>li1[j]:
            li1[i],li1[j]=li1[j],li1[i]
print(li1)

###################### 44 #####################################

my_list = [97, 98, 97, 1, 2, 100, 98, 99, 97, 98, 97]
my_list.sort(reverse=True)
last_item=my_list[0]
new_list=[my_list[0]]
for number in my_list:
    if number==last_item-1:
        new_list.append(number)
        last_item=number
print(new_list)

##################### 45 #######################################

def next_max(arr):
    n=len(arr)
    k=len(arr)-2
    while k>=0:
        if arr[k]<arr[k+1]:
            break
        k=k-1
    if k<0:
        arr=arr[::-1]
    else:
        for l in range(n-1,k,-1):
            if arr[l]>arr[k]:
                break
        arr[l],arr[k]=arr[k],arr[l]
        arr[k + 1:] = reversed(arr[k + 1:])
    return arr
arr = [5, 3, 4, 9, 7, 6]
print(next_max(arr))

#################### 46 #######################################

lii=[1,2,3,4,5,6]
li2=[(lii[i+1],lii[i]) for i in range(0,len(lii),2)]
print(li2)

fruits = ["apple", "bana", "cherry"]
x,y,z = fruits
print(x,y,z)

#################### 47 ########################################

def try_recursion(x):
    if x <=0:
        return 0
    else:
       result= x+try_recursion(x-1)
    return result
print(try_recursion(5))

def try_fact(y):
    if y==0 or y ==1:
        return 1
    else:
        res=try_fact(y-2)+try_fact(y-1)
    return res
print(try_fact(5))


#################### 48 ########################################

nlist=[(1,3),(2,3),(4,9),(7,0)]
li=[]
for i in nlist:
    for j in i:
        l.append(j)
print(l)

#################### 49 #######################################

di=[]
string = ['city1', 'class5', 'room2', 'city2']
substr = ['class', 'city']
for i in substr:
    for j in string:
        if i in j:
            di.append(i)

print(di)

#################### 50 #######################################

import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records1.csv"

with open(filename, 'w') as fd:
    wr=csv.writer(fd)
    wr.writerow(fields)
    wr.writerows(rows)
with open(filename,'r') as r:
    rd=csv.reader(r)
    print(next(rd))
    for i in rd:
        print(i)

import json
di1={'key': 8, 'key1':9}
jd=json.dumps(di1)
rd1=json.loads(jd)
print(rd1),

######################### 51 ####################################

li=[(1,2),(3,4),(5,6)]
print(*zip(*li))

nums = [1, 2, 3, 4, 5, 6]
print([nums[i^1] for i in range(len(nums))])

class A:
    @classmethod
    def hello(cls, name):
        cls.name=name
        print(cls.name)
a=A.hello("Pravin")

st1 = "a2b2c2a1b1c1"
kt1 = ""

for i in range(1,len(st1),2):
    kt1+=st1[i-1]*int(st1[i])
print(kt1)

############################ 52 ###################################

#Annagram
di2 = {}
l2 = []
l3 = ['cat', 'adg', 'dag', 'gad', 'tac']
for i in l3:
    key=''.join(sorted(i))
    if key in di2.keys():
        l2.append(di2[key].append(i))
    else:
        di2[key]=[i]
print(di2)


########################### 53 ####################################

def per(s1,i,l):
    re=[]
    if i==l:
        re.append(''.join(s1))
    else:
        for j in range(i,l):
            s1[i],s1[j]=s1[j],s1[i]
            per(s1,i+1,l)
            s1[i], s1[j] = s1[j], s1[i]
    print(re)

str = "lskdfddd"
#str=list(str)
#per(list(str),0,len(str))

######################### 54 #######################################

st = [1, 1, 2, 3, 4, 2, 4, 4, 2]
stack = []
for i in st:
    if not stack or stack[-1] !=i:
        stack.append(i)
    else:
        stack.pop()
print(stack)

######################### 55 #######################################

def add(x,y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
print(add(8,9))

dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3=dict1|dict2
print(dict3)

######################### 56 #######################################


def has4(x):
    while x!=0:
        if x%10==4:
            return True
        x=x//10
def check(n):
    li=[]
    for i in range(n):
        if has4(i):
            li.append(i)
    print(li)
check(100)

########################## 57 ####################################


import re
input = "ABCDCDCCDC .1.1 .1"
pattern=re.compile( r'(?=(CDC))')
li=pattern.findall(input)
l2=re.compile(r'(?=(CDC))')
print(l2.findall(input))


########################## 58 #####################################

s = '23511011501782351112179911801562340161171141148'
st6=s[::-1]
i=0
j=1
l=len(s)-1
cur=0
caps=range(97,123)
small=range(65,91)
space=32
ans=[]
while j<l:
    cur=int(st6[i:j])
    if cur in caps or cur in small or cur==space:
        ans.append(chr(cur))
        i=j
        j=i+1
    else:
        j+=1
print(''.join(ans))

########################### 59 ################################

li=[100, 180, 260, 310, 40, 535, 695]
i=0
j=len(li)
while i < j-1:
    while i<j-1 and li[i+1]<=li[i]:
        index=i
    if i==j-1:
        break
    buy=i
    i+=1
    while i<j-1 and li[i]>=li[i-1]:
        i+=1
    sell=i-1
print(buy,sell)


######################### 60 ###############################

st="2342"
k="2"
index=-1
j=len(st)
ans=""
for i in range(0,j-1):
    if (st[i]==k and (ord(st[i])-ord('0'))<(ord(st[i+1])-ord('0'))):
        index=i
        break
if index==-1:
    for i in range(j,-1,-1):
        if st[i]==k:
            index=i
            break
for i in range(j):
    if i !=index:
        ans=ans+st[i]
print(ans)

li=[100, 180, 260, 310, 40, 535, 695]
i=0
j=len(li)
while i<j-1:
    while i <j-1 and li[i+1]<=li[i]:
        i+=1
    if i ==j-1:
        break
    buy=i
    i+=1
    while i <j and li[i]>=li[i-1]:
        i+=1
    sell=i-1
    print(buy, sell)

def isIncreasing(li, n):
    for i in range(0, n - 1):
        if li[i + 1] <= li[i]:
            return False
    return True
def canBeIncreasing(li):
    n = len(li)
    for i in range(n):
        if isIncreasing(li[: i] + li[i + 1:], n - 1):
            return True
    return False
li = [1, 2, 1, 1]
















