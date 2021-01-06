task=[]
while True:
    print("********My To Do App *******")
    print("1.Add Task")
    print("2.View All Tasks")
    print("0.Exit")
    Choose_Option=int(input("enter your option:"))
    if Choose_Option==1:
        Taskname=input("enter your task:")
        task.append(Taskname)
        print("Task Added")
    elif Choose_Option==2:
        print(task)
    elif Choose_Option==0:
        print("Bye")
    else:
        print("Invalid  Choose_Option ")

