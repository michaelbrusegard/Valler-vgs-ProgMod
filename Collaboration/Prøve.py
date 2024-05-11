mineTall = [9]

print(len(mineTall))
def summenAvTre(mineTall):
    if len(mineTall) == 3:
        return mineTall[0] + mineTall[1] + mineTall[2]
    elif len(mineTall) == 2:
        return mineTall[0] + mineTall[1]
    else:
        return mineTall[0]

print(summenAvTre(mineTall))




def noe(iskrem):
    return [iskrem[0], iskrem[len(iskrem)-1]]

print(noe([[1,2], [False, "nod"]]))