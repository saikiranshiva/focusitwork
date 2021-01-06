A=[1,3,5,6,3,5,6,2]
print("the original list is:", A)
res=[]
for i in A:
    if i not in res:
        res.append(i)

print("the list after removing duplicates:" , res )