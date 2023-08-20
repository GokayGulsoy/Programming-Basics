menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit"

data_user = "users.txt"
infile = open(data_user,'r')
list_total = []
a = infile.readlines()
count = 0
while count < len(a):
    if "\n" in a[count]:
        a[count] = a[count][:-1]
        count += 1
    else:
        count +=1
list1 = []
count = 0
while count < len(a):
    b = a[count].split(';')
    list1.append(b)
    count += 1
list_menu = ["1","2","3","4","5"]
special_symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "{", "}", "[",
                       "]", "|", "/", ":", ";", "<", ".", "?", ","]

number_list = ['0','1','2','3','4','5','6','7','8','9']
alphabetic_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

loggin_list = []


def main_menu_caller():
    print(menu_text)
    y = input("")
    if y not in list_menu:
        print("Invalid option\n")
        a = -1
        while a < 0:
            print(menu_text)
            y = input("")
            if y in list_menu:
                break
            else:
                print("Invalid option\n")
                #if x == 5:
                 #   break

    return y


def username_loggin():################## for x == 1
    m = input("Please enter username:\n")

    count = 0
    while count < len(list1):
        if m == list1[count][0]:
            if m not in loggin_list:
                loggin_list.append(m)
                break
            else:
                break

        else:
            count += 1


    return m

def user_name_password_correctness():######### for x == 1

    global m

    m = username_loggin()
    empty_string_cleaner()
    n = input("Please enter password:\n")
    count = 0

    while count < len(list1):
        if m == list1[count][0] and n == list1[count][1]:
            print("Logged in\n")
            break
        else:
            count += 1
            if count == len(list1)-1 and n != list1[count][1]:
                print("Wrong password or username\n")
                k = -1

    return n


def username_validity():
    global p
    global l
    l = -3
    p = input("Please enter username:\n")

    if p != '':
        if not any(char.isupper() for char in p):
            counter = 0
            while counter < len(p):
                if p[counter] in special_symbol_list:
                    print("Username not valid\n")
                    l = -4
                    break
                else:
                    counter += 1
                    if counter == len(p) - 1 and p[counter] not in special_symbol_list:
                        counter = len(p)
                        count = 0

                        while count < len(list1):
                            if p == list1[count][0]:
                                print("Username not valid\n")
                                l = -4
                                break
                            else:
                                count += 1
                                if count == len(list1)-1 and p not in list1[count][0]:
                                    list1.append([p])
                                    break

        else:
            print("Username not valid\n")
            l = -4



    else:
        print("Username not valid\n")
        l = -4


def password_validity():
    u = input("Please enter password:\n")
    if 4 <= len(u) and len(u) <= 8:
                counter = 0
                while counter < len(u):
                    if u[counter] in number_list:
                        count = 0
                        while count < len(u):
                            if u[count] in alphabetic_letters:
                                count = len(u)
                                if p == list1[len(list1)-1][0]:
                                    list1[len(list1) - 1].insert(1, u)
                                    list1[len(list1)- 1].insert(2,'')
                                    counter = len(u)
                                else:
                                    options()
                            else:
                                count += 1
                                if count == len(u)-1 and u[count] not in alphabetic_letters:
                                    print("Password not valid\n")
                                    counter = len(u)

                    else:
                        counter += 1
                        if counter == len(u) - 1 and u[counter] not in number_list:
                            print("Password not valid\n")

    else:
        print("Password not valid\n")

def Save_and_exit():
    count = 0
    sep = ";"
    while count < len(list1):
        list1[count] = sep.join(list1[count])
        count += 1

    f = open("users.txt","w")
    for i in list1:
        f.write(i+'\n')
    f.close()

def empty_string_cleaner():
    counter = 0
    while counter < len(list1):
        if list1[counter] == ['']:
            del list1[counter]
        else:
            counter += 1

def wrong_created_user_name_cleaner():
    counter = 0
    while counter < len(list1):
        if len(list1[counter]) == 1:
            del list1[counter]
        else:
            counter += 1


def add():
    if x != 5:
        c = input("Please enter the name of your new friend:\n")
        counter = 0
        while counter < len(list1):
            if c == list1[counter][0]:
                count = 0
                while count < len(list1):
                    if list1[count][0] == m:
                        if list1[count][2] == "":
                            list1[count][2] = c
                            counter = len(list1)
                            break
                        else:
                            list1[count][2] = list1[count][2] + ',' + c
                            counter = len(list1)
                            break
                    else:
                        count += 1
                        if x == 5:
                            break


            else:
                counter += 1
                if counter == len(list1) - 1 and c != list1[counter][0]:
                    print("Friend not found\n")
                    if x == 5:
                        break

def show():
    if x != 5:
        counter = 0
        while counter < len(list1):
            if list1[counter][0] == m:
                print(list1[counter][2])
                break
            else:
                counter += 1
                if x == 5:
                    break


def options():
    global k
    k = -1
    while k == -1:
        global x
        x = main_menu_caller()

        if x == "1":
            user_name_password_correctness()
            k = -1

        if x == "2":
            username_validity()
            if l == -4:
                k = -1
            else:
                password_validity()
                empty_string_cleaner()
                wrong_created_user_name_cleaner()
                k = -1

        if x == "3":
            count = 0
            while count < len(list1):
                if list1[count][0] in loggin_list:
                    add()
                    k = -1
                    break
                else:
                    count += 1
                    if count == len(list1) - 1 and list1[count][0] not in loggin_list:
                        print("You need to log in first\n")
                        k = -1

        if x == "4":

            count = 0
            while count < len(list1):
                if list1[count][0] in loggin_list:
                    show()
                    k = -1
                    break

                else:
                    count += 1
                    if count == len(list1) - 1 and list1[count][0] not in loggin_list:
                        print("You need to log in first\n")

        if x == "5":
            Save_and_exit()
            x = 5
            break

options()
