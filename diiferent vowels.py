A=input("enter your word:")
vowels=['a','e','i','o','u']
list1=[]
for i in A:
    if (i in vowels and i not in list1):
        list1.append(i)
print("vowels present in given word:",list1)
