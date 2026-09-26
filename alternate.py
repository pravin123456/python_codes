st="automation testing using python hello world"
st=st.split()
for i in range(len(st)):
    if i%2==0:
        print(st[i], end=" ")
    else:
        print(st[i][::-1], end=" ")
        

st3="automation testing using python hello world"   
st1={}
st2={w:1 if w not in st1 and not st1.update({w:1}) else st1[w]+1 for w in st3}

print(st2)
