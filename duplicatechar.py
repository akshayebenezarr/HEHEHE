s = "cbacdcbc"
s=[-1]
temp=[]



for c in s:
    ind=s.index(c)+1

    if c< li[-1]:
        print("char",c)
        print("last in list",li[-1])
        if c in s[ind:]:
             li.pop()
             print(li)
             li.append(c)
             print(li, "\n")

    else:
        li.append(c)
        print("appended", c)



print (li)