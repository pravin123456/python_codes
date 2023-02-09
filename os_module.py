import os
l='file1.txt'
d='file3.txt'
rd=open(l,'rb+')
print(rd.read())
ld=os.system('cp -rp "%s" "%s"'%(l,d))
ld1=open(d,'rb+')
print(ld1.readlines())

