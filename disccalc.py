
disc = 0
ar = [8,4,6,2,3]
discar = []
s = len(ar)

def disccalc(ind):
    disc=ar[ind]
    for j in range(ind+1, s):
        if ar[ind] >= ar[j] :
            print(ar[ind],ar[j])
            disc = ar[ind] - ar[j]
            break


        #if a[ind] < a[j] :
            #disc=ar[ind]

    return disc

for i in range(0, s):

    discar.append(disccalc(i))
print(discar)
