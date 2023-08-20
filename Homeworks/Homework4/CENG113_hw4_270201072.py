### Student ID --> 270201072

### Recursively defined remove_task function!!
def remove_task(task_list, element):
    for sub_list in task_list:
        if type(sub_list) == list:
            if element in sub_list:
                if (remove_task(sub_list, element) == 1):
                    task_list.pop(task_list.index(sub_list))
        else:
            return 1


### Recursively defined print_remaining_task function!!
def print_remaining_tasks(task_list):
    if len(task_list) > 0:
        if task_list[0][0] == 'Task1':
            print(
                f"|  {task_list[0][0]}        | {task_list[0][1]} km         | {task_list[0][2]} km   |{task_list[0][3]}          |")
            print_remaining_tasks(task_list[1:])
        else:
            # print(f"|  {task_list[0][0]}        | {task_list[0][1]} km         | {task_list[0][2]} km   |{task_list[0][3]}       |")
            if task_list[0][0] == 'Task3':
                print(
                    f"|  {task_list[0][0]}        | {task_list[0][1]} km        | {task_list[0][2]} km   |{task_list[0][3]}          |")
                print_remaining_tasks(task_list[1:])
            else:
                # print(f"|  {task_list[0][0]}        | {task_list[0][1]} km         | {task_list[0][2]} km   |{task_list[0][3]}       |")
                # print_remaining_tasks(task_list[1:])
                if task_list[0][0] == 'Task4':
                    print(
                        f"|  {task_list[0][0]}        | {task_list[0][1]} km       | {task_list[0][2]} km   |{task_list[0][3]}          |")
                    print_remaining_tasks(task_list[1:])
                else:
                    if task_list[0][0] == 'Task5':
                        print(
                            f"|  {task_list[0][0]}        | {task_list[0][1]} km        | {task_list[0][2]} km   |{task_list[0][3]}          |")

                    else:
                        print(
                            f"|  {task_list[0][0]}        | {task_list[0][1]} km         | {task_list[0][2]} km   |{task_list[0][3]}         |")
                        print_remaining_tasks(task_list[1:])
    else:
        return


def Game_over():
    global m
    m = -1

### Game over variable m is used to finish game in any failure!!
m = 0
### Reading tasklist.txt!!
infile = open("taskList.txt", 'r')
a = infile.readlines()
task_list = []
nested_task_list = []
### removing \n symbols from list comes from readlines() method!!
for i in a:
    if '\n' in i:
        i = i[:-1]
        task_list.append(i)
    else:
        task_list.append(i)
### joining list and splitting it to obtain each element one by one!!
sep = ','
task_list = sep.join(task_list)

task_list = task_list.split(',')
### adding each task as a list and we obtain nested_task_list!!
count = 0
First_time = True
while count < len(task_list):
    if First_time == True:
        nested_task_list.append(task_list[:count + 4])
        count += 4
        First_time = False
    else:
        nested_task_list.append(task_list[count:count + 4])
        count += 4

### HP's of hero and pegasus ,their speed and lose of HP for each hour of the journey!!
hero_HP, pegasus_HP, hero_speed, pegasus_speed, hero_HP_lose, pegasus_HP_lose = 3000, 550, 20, 50, 10, 15
hour_passed, returning_hour, total_hour_passed = 0, 0, 0
#### Introduction to game part!!
print("Welcome to Hero's 5 labors!")

### While loop for main game!!
while len(nested_task_list) > 0 and m != -1:
    print('Remaining HP for Hero:', hero_HP)
    print('Remaining HP for Pegasus:', pegasus_HP, '\n')
    print('Here are the tasks left that hero needs to complete:')
    ####  the table of the game!!
    print('--------------------------------------------------------')
    print('| TaskName      | ByFootDistance | ByPegasus | HPNeeded |')
    print('--------------------------------------------------------')
    print_remaining_tasks(nested_task_list)
    print('--------------------------------------------------------')

    task_control_list = []
    x = input("Where should Hero go next?")
    x = x.lower()
    ### Validating the task location
    for i in nested_task_list:
        task_control_list.append(i[0])
    ### making all task names lowercase  because user inputs are case insensitive!!
    for i in range(len(task_control_list)):
        task_control_list[i] = task_control_list[i].lower()
    ### changing the nested_task_lists first element to lowercase not to cause wrong interpretation!!
    n = -1
    while n == -1:
        if x not in task_control_list:
            print('Invalid input')
            x = input("Where should Hero go next?")
            x = x.lower()
        else:
            break

    if m != -1:
        y = 'foot'
        n = -1
        ### Starting a while loop with seeding method and checking necessary conditions to go to selected location!!
        while n == -1:
            y = input('How do you want to travel?(Foot/Pegasus)')
            y = y.lower()
            for i in nested_task_list:
                if y == 'foot' and ( 'T' + x[1:] == i[0] and i[1] == '-1'):
                    ### Checking whether we can go to Task by foot by looking up to nested_task_lists 's First index if Foot is given as an input!!
                    print('You cannot go there by foot.')
            if y != 'foot' and y != 'pegasus':
                print('Invalid input')  ## Checking invalid inputs!!
            elif (y == 'pegasus' or y == 'foot'):
                if y == 'pegasus':
                    for i in nested_task_list:
                        if 'T' + x[1:] == i[0] and (pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                            print('Pegasus does not have enough HP.')
                            ### Conditions for Game over!!
                            for i in nested_task_list:
                                if ('T' + x[1:] == i[0]) and (i[1] != '-1') and (
                                        pegasus_HP - (int(i[2]) // pegasus_speed) * (
                                pegasus_HP_lose) < 0) and hero_HP - (
                                        int(i[1]) // hero_speed) * (hero_HP_lose) < 0:
                                    print('GAME OVER')
                                    Game_over()
                                    n = -2
                                if 'T' + x[1:] == i[0] and i[1] == '-1' and (
                                        pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                                    print('GAME OVER')
                                    Game_over()
                                    n = -2
                        else:
                            for i in nested_task_list:
                                if  'T' + x[1:] == i[0] and (pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) >= 0):
                                    n = -2  ### Finishing the loop by changing the value of seed which was n = -1 initially
                else:
                    for i in nested_task_list:
                        if y == 'foot' and ('T' + x[1:] == i[0] and i[1] != '-1'):
                            if hero_HP - (int(i[1]) // hero_speed) * (hero_HP_lose) >= 0:
                                n = -2  ### Finishing the loop by changing the value of seed which was n = -1 initially
                            else:
                                print('Hero does not have enough HP.')
                                ### Conditions for Game over!!
                                for i in nested_task_list:
                                    if ('T' + x[1:] == i[0]) and (i[1] != '-1') and (
                                            pegasus_HP - (int(i[2]) // pegasus_speed) * (
                                    pegasus_HP_lose) < 0) and hero_HP - (
                                            int(i[1]) // hero_speed) * (hero_HP_lose) < 0:
                                        print('GAME OVER')
                                        Game_over()
                                        n = -2
                                    if 'T' + x[1:] == i[0] and i[1] == '-1' and (
                                            pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                                        print('GAME OVER')
                                        Game_over()
                                        n = -2

        ###  Calculating The passed Time below for pegasus(if we chosed to go with pegasus)!!
        if y == 'pegasus':
            for i in nested_task_list:
                if 'T' + x[1:] == i[0]:
                    hour_passed = int(i[2]) // pegasus_speed
                    pegasus_HP = pegasus_HP - (hour_passed * pegasus_HP_lose)
                    total_hour_passed += hour_passed
                    break

        ### Calculating the passed time below for hero(if we chosed to go by foot)!!
        if y == 'foot':
            for i in nested_task_list:
                if 'T' + x[1:] == i[0]:
                    hour_passed = int(i[1]) // hero_speed
                    hero_HP = hero_HP - (hour_passed * hero_HP_lose)
                    total_hour_passed += hour_passed
                    break

        for i in nested_task_list:
            if 'T' + x[1:] == i[0]:
                hero_HP = hero_HP - int(i[3])

                ### Checking whether game will over due to Heros HP!!
        for i in nested_task_list:
            if 'T' + x[1:] == i[0] and hero_HP >= int(i[3]) and m != -1:
                print('Hero defeated the monster.')
            if 'T' + x[1:] == i[0] and hero_HP < int(i[3]):
                print('GAME OVER')
                Game_over()

        if m!= -1:
            if len(nested_task_list) == 5:
                print('Time passed:', hour_passed, 'hour\n')
            else:
                print('Time passed:', total_hour_passed, 'hour\n')

                ### After killing the monster if hero and pegasus can't go back to home due to HP !!
            for i in nested_task_list:
                if ('T' + x[1:] == i[0]) and (i[1] != '-1') and (pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0) and hero_HP - (int(i[1]) // hero_speed) * (hero_HP_lose) < 0:
                    print('GAME OVER')
                    Game_over()
                if 'T' + x[1:] == i[0] and i[1] == '-1' and (pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                    print('GAME OVER')
                    Game_over()
            if m != -1:
                print('Remaining HP for Hero:', hero_HP)
                print('Remaining HP for Pegasus:', pegasus_HP, '\n')
                ### Going back to Home part!!
                m = 'foot'
                u = -1
                while u == -1:
                    m = input('How do you want to go home?(Foot/Pegasus)')
                    m = m.lower()
                    for i in nested_task_list:
                        if m == 'foot' and ('T' + x[1:] == i[0] and i[1] == '-1'):
                            print('You cannot go there by foot.')
                    if m != 'foot' and m != 'pegasus':
                        print('Invalid input')
                    elif (m == 'pegasus' or m == 'foot'):
                        if m == 'pegasus':
                            for i in nested_task_list:
                                if 'T' + x[1:] == i[0] and (pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                                    print('Pegasus does not have enough HP.')
                                    ### Conditions for Game over!!
                                    for i in nested_task_list:
                                        if ('T' + x[1:] == i[0]) and (i[1] != '-1') and (
                                                pegasus_HP - (int(i[2]) // pegasus_speed) * (
                                        pegasus_HP_lose) < 0) and hero_HP - (
                                                int(i[1]) // hero_speed) * (hero_HP_lose) < 0:
                                            print('GAME OVER')
                                            Game_over()
                                            u = -2
                                        if 'T' + x[1:] == i[0] and i[1] == '-1' and (
                                                pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                                            print('GAME OVER')
                                            Game_over()
                                            u = -2
                                else:
                                    for i in nested_task_list:
                                        if 'T' + x[1:] == i[0] and (
                                                pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) >= 0):
                                            u = -2  ### Finishing the loop by changing the value of seed which was n = -1 initially

                        else:
                            for i in nested_task_list:
                                if m == 'foot' and ('T' + x[1:] == i[0] and i[1] != '-1'):
                                    if hero_HP - (int(i[1]) // hero_speed) * (hero_HP_lose) >= 0:
                                        u = -2
                                    else:
                                        print('Hero does not have enough HP.')
                                        ### Conditions for Game over!!
                                        for i in nested_task_list:
                                            if ('T' + x[1:] == i[0]) and (i[1] != '-1') and (
                                                    pegasus_HP - (int(i[2]) // pegasus_speed) * (
                                            pegasus_HP_lose) < 0) and hero_HP - (
                                                    int(i[1]) // hero_speed) * (hero_HP_lose) < 0:
                                                print('GAME OVER')
                                                Game_over()
                                                u = -2
                                            if 'T' + x[1:] == i[0] and i[1] == '-1' and (
                                                    pegasus_HP - (int(i[2]) // pegasus_speed) * (pegasus_HP_lose) < 0):
                                                print('GAME OVER')
                                                Game_over()
                                                u = -2

                ### Checking whether we can go back to home!!
                if m == 'pegasus':
                    for i in nested_task_list:
                        if 'T' + x[1:] == i[0]:
                            returning_hour = int(i[2]) // pegasus_speed
                            pegasus_HP = pegasus_HP - (returning_hour * pegasus_HP_lose)
                            hour_passed = returning_hour + hour_passed
                            total_hour_passed += returning_hour
                            break

                if m == 'foot':
                    for i in nested_task_list:
                        if 'T' + x[1:] == i[0]:
                            returning_hour = int(i[1]) // hero_speed
                            hero_HP = hero_HP - (returning_hour * hero_HP_lose)
                            hour_passed = returning_hour + hour_passed
                            total_hour_passed += returning_hour
                            break
                ### Calculating the total hour when we arrived the home!!
                print('Hero arrived home.')
                if len(nested_task_list) == 5:
                    print('Time passed:', hour_passed, 'hour', '\n')
                else:
                    print('Time passed:', total_hour_passed, 'hour', '\n')
                x = 'T' + x[1:]
                remove_task(nested_task_list, x)

if len(nested_task_list) == 0:
    print('Congratulations,you have completed the task.')
    name = input('What is your name:')
    print('Hall Of Fame')
    f = open('HallofFame.txt', 'a')
    ### Writing the finish time and name of player!!
    f.write(name + ',' + str(total_hour_passed) + ',')
    f.close()
    f = open('HallofFame.txt', 'r')
    ### Reading name of players and Scores from the file!!
    a = f.readline()
    a = a.split(',')
    if '' in a:
        a.remove('')

    score_list = []
    succeeded_users_list = []
    ### Putting the succeeded users scores to the score_list to determine the order in the Hall of Fame!!
    count = 1
    while count <= len(a):
        score_list.append(a[count])
        count += 2

    ### Putting the best three players to list succeeded_users_list to determine the order in the Hall of Fame!!
    count = 0
    while count <= len(a) - 2:
        succeeded_users_list.append(a[count])
        count += 2
    ### Sorting the score list in a descending order!!
    score_list.sort(reverse=True)

    sorted_user_list = []
    count = 0
    for i in a:
        if score_list[0] == i:
            sorted_user_list.append(a[a.index(i) - 1])
            del a[a.index(i) - 1]
            del a[a.index(i)]

            break

    for i in a:
        if score_list[1] == i:
            sorted_user_list.append(a[a.index(i) - 1])
            del a[a.index(i) - 1]
            del a[a.index(i)]
            break
    for i in a:
        if score_list[2] == i:
            sorted_user_list.append(a[a.index(i) - 1])
            break

    ### Printing the Hall Of Fame!!
    if len(sorted_user_list) == 1: ### if there is only one succeeded user!!
        print('------------------------------------')
        print('| Name               | Finish Time  |')
        print('------------------------------------')
        print(f"| {sorted_user_list[0]}              | {score_list[0]}          |")
        print('------------------------------------')

    elif len(sorted_user_list) == 2: ### if there are two succeeded users!!
        print('------------------------------------')
        print('| Name               | Finish Time  |')
        print('------------------------------------')
        print(f"| {sorted_user_list[0]}              | {score_list[0]}          |")
        print('------------------------------------')
        print(f"| {sorted_user_list[1]}           | {score_list[1]}          |")
        print('------------------------------------')

    elif len(sorted_user_list) == 3: ### Best three succeeded user!!
        print('------------------------------------')
        print('| Name               | Finish Time  |')
        print('------------------------------------')
        print(f"| {sorted_user_list[0]}              | {score_list[0]}          |")
        print('------------------------------------')
        print(f"| {sorted_user_list[1]}           | {score_list[1]}          |")
        print('------------------------------------')
        print(f"| {sorted_user_list[2]}              | {score_list[2]}          |")
        print('------------------------------------')



















