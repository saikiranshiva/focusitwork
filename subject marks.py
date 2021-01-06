sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
sub6=int(input("Enter marks of the fifth subject: "))
list=[sub1,sub2,sub3,sub4,sub5,sub6]
print(list)
for i in list:
    print("marks:",i)
    
Total_Marks=(sub1+sub2+sub3+sub4+sub5+sub6)
print("Total marks of the student :",Total_Marks)
avg=(sub1+sub2+sub3+sub4+sub5+sub6)/6
print("Average marks of the student:",avg)