task =[]


def show_task():

    if len(task) == 0:
        print("no task add")

    else:

        print("\n------ your task ------")

        for i, t in enumerate(task, 1):

            print(f"{i}.{t}")



def add_task():

    add = input("enter the task \n")
    task.append(add)

    print(f"{add} is added")



def remove_task():

    show_task()

    remove = int(input("enter the task.no which you want to remove  :  "))

    task.pop(remove-1)

    print("after the task remove ",task)



while True:

    print("\n----- your task -----")

    print("1.show task")

    print("2.add task")

    print("3.remove task")

    print("4.quit")


    choise = input("choise (1-4): ")

    if choise == "1":
        show_task()
    elif choise == "2":
        add_task()
    elif choise == "3":
        remove_task()
    elif choise == "4":
        print("allah hafiz")
        break
    else:
        print("you choise invalied option ")