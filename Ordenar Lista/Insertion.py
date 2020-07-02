import random

def insertion(ulist):
    n = len(ulist)
    for i in range(1,n):
        currentVal = ulist[i]
        j = i - 1
        while j >= 0 and ulist[j] > currentVal:
            ulist[j+1] = ulist[j]
            j = j - 1
        ulist[j+1] = currentVal
    return ulist

print("Lista Desordenada")

unordered = list(range(10))
random.shuffle(unordered)
print(unordered)

ordered=insertion(unordered)
print(ordered)