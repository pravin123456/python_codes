class MyString:
    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        temp=list(string)
        i = 0
        j = len(string) -1
        while i < j:
            temp[i], temp[j] = temp [j], temp[i]
            i +=1
            j -=1
        stdout= ''.join(temp)
        print (stdout)
    def another_str(string):
        reversed = string[::-1]
        print(reversed)

#def main():
 #   c1 = Mystring()
 #   c1.reverse_string("Hello")
 #   c1.another_str("Python")

#class Inherited(MyString):
#      def __init__(self):
#          pass
#d1 = Inherited ()
#d1.another_str()


class rever:
    def __init__(self,str):
        self.str=str

    def reverse(self):
        temp = list(str)
        i = 0
        j = len(str)-1
        while i <j:
            temp[i], temp[j] = temp[j], temp[i]
            i += 1
            j -= 1
        print(''.join(temp))
    def ddff(self):
        string = "aabbccab"
        i = 0
        j = len(string)
        st = ""
        while i < j:
            count = 1
            while (i < j - 1 and (string[i] == string[i + 1])):
                count += 1
                i += 1
            i += 1
            st+=(string[i-1] + self.str(count) if count >1 else string[i-1])
        # print(string[i-1]+str(count) if (count >1) else string[i-1])
       # print(st)



string = "aabbccab"
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
print(string[i-1]+str(count) if (count >1) else string[i-1])
print(st)


str="ddffkjij"
c=rever(str)
print(c.reverse())
c.ddff()

#def



