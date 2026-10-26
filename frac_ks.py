val = [100, 60, 120]
wt = [20, 10, 30]
C = 50

def swap(arr, i):
    arr[i],arr[i+1] = arr[i+1], arr[i]

vw = []
for i in range(0,len(val)):
    vw.append(val[i]/wt[i])
swapped=1
while swapped:
    for i in range(0, len(val)-1):
        swapped=0
        if vw[i]<vw[i+1]:
            swapped=1
            swap(vw, i)
            swap(val, i)
            swap(wt, i)

def frac_ks(val, wt, C, remC):
    cur_prof=0
    for i in range(0, len(wt)):
        if wt[i]<=remC:
            cur_prof += val[i]
            remC -= wt[i]
        else:
            cur_prof += (remC/wt[i])*val[i]
            break
    return cur_prof

print(frac_ks(val, wt, C, C))
