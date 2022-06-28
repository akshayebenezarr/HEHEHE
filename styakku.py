st=[]

def push(val):
    if checkfull():
        print("Full")
    else:
        st.append(val)
        print(st)

def pop():
    if (len(st) ==0):
        print("List empty")
    else:
        st.pop()
        print(st)

def checkfull():
    if len(st)>max:
        return True
    else:
        return False
max=int(input("what is the max size"))


while True:
    ch = int(input("1.Push\n2.Pop\n3.Exit"))
    if ch==1:
        val=input("Enter value")
        push(val)
    elif ch==2:
        pop()
    elif ch==3:
        print("seri moodu")
        break
    else:
        print("Option thappu")
        break
