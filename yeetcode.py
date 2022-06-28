uip=input("Enter the string of paranthesis to be checked")
length = len(uip)
dic={")":"(",
     "}":"{",
     "]":"["}
st=[]
lis=["(",
     ")",
     "[",
     "]",
     "{",
     "}",
     ]
w=True
def push (l):

    if len(st)>=1 and (dic[l]==(st[-1])):
        st.pop()
        print("after popin",st)

    else:
        st.append(l)
        print(st)

for l in uip:
    if l in lis:
        while w:
            top=l
            w=False
        push(l)
    else:
        print("invalis input")




