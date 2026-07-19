tasks = []
import time
while True:
    print('  To-Do list Menu  ')
    print('1.Add new task.')
    print('2.Want to see all tasks.')
    print('3.Delete a task.')
    print('4.Exit')
    
    choice = input('Choose your choice (1,2,3,4)\n:')
    
    if choice == '1':
        task = input('Give name of task you want to add :-')
        tasks.append(task)
        print('Task is added on list!')
        time.sleep(2)
    elif choice == '2':
        print('---Your Tasks ---')
        if len(tasks) == 0:
            print('List is fully empty.')
            time.sleep(2)
        else:
            for index, t in enumerate(tasks, start=1):
                print(f'{index}.{t}')
                time.sleep(2)       
    elif choice == '3':
        if len(tasks) == 0:
            print('There is no tasks to delete.')
        else:
            task_no = int(input('Which task would you want to delete?\n:'))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"'{removed}' deleted!")
            else:
                print('Wrong task number!')
        time.sleep(2)      
    elif choice  == '4':
        print('Programme is closing.Bye!')
        break
    else:
        print('Wrong choice!\nPlese only chosse from 1,2,3 or 4.')
            

            
            
            
            
            
            
            
            
            
            
            
            
                          