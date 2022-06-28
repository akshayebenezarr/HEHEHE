ass = [10, 12, -5]
stac=[]


def calc(a1,i):
    print(i)
    print("a1", a1)
    aba1=abs(a1)
    abi=abs(i)
    if aba1>abi:
        print("a1", a1)
        stac.append(a1)
    else:
        stac.append(i)
        print("i",i)


for i in ass:
    print(i)
    if i > 0:
        stac.append(i)
    elif i < 0:
        if stac:
            a1 = stac.pop()
            if a1<0:
                stac.append(a1)
                stac.append(i)
            else:
                calc(a1,i)

print(stac)