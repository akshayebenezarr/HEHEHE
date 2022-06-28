import math
q=[5, 6, 9, 0, 2, 3, 4]

lo = 0
hi = len(q)-1
mid =0


def find(lo,hi):

    a = True
    i=0
    while i<=len(q):
        mid = math.floor((lo + hi) / 2)
        i=i+1
        print(q[lo])
        print(q[mid])

        print(q[hi])
        if q[mid]==6:
            return mid


        elif q[mid ] >q[lo]:

            lo= mid

        else :
            hi= mid
a=find(lo,hi)
print("No of rotations=",a)