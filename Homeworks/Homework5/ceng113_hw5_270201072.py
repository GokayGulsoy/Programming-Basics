import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand
        self.stack = stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2],
                           ['b',2],['b',3],['b',3],['b',4],
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:
            self.update_count_deck(card)
        self.hand = [['!',-1],['!',-1],['!',-1]]


    def get_tip(self, tip):
        self_hand = [['!', -1], ['!', -1], ['!', -1]]
        ### This code block checks all the possible tips and gives the best tip to computer!!
        if len(tip) == 5:
            if tip[4] == "w" or tip[4] == "b":
                for i in tip:
                    if i == "1":
                        self.hand[0][0] = tip[4]
                    if i == "2":
                        self.hand[1][0] = tip[4]
                    if i == "3":
                        self.hand[2][0] = tip[4]
        counter = 0
        if len(tip) == 5:
            if tip[4] == "1" or tip[4] == "2" or tip[4] == "3" or tip[4] == "4":
                for i in tip:
                    if i == "1" and counter < 4:
                        self.hand[0][1] = int(tip[4])
                        counter += 2
                    if i == "2" and counter < 4:
                        self.hand[1][1] = int(tip[4])
                        counter += 2
                    if i == "3" and counter < 4:
                        self.hand[2][1] = int(tip[4])
                        counter += 2

        if len(tip) == 7:
            if tip[6] == "w" or tip[6] == "b":
                for i in tip:
                    if i == "1":
                        self.hand[0][0] = tip[6]
                    if i == "2":
                        self.hand[1][0] = tip[6]
                    if i == "3":
                        self.hand[2][0] = tip[6]
        counter = 0
        if len(tip) == 7:
            if tip[6] == "1" or tip[6] == "2" or tip[6] == "3" or tip[6] == "4":
                for i in tip:
                    if i == "1" and counter < 6:
                        self.hand[0][1] = int(tip[6])
                        counter += 2
                    if i == "2" and counter < 6:
                        self.hand[1][1] = int(tip[6])
                        counter += 2
                    if i == "3" and counter < 6:
                        self.hand[2][1] = int(tip[6])
                        counter += 2
        if len(tip) == 3:
            if tip[2] == "w" or tip[2] == "b":
                for i in tip:
                    if i == "1":
                        self.hand[0][0] = tip[2]
                    if i == "2":
                        self.hand[1][0] = tip[2]
                    if i == "3":
                        self.hand[2][0] = tip[2]
        if len(tip) == 3:
            if tip[2] == "1" or tip[2] == "2" or tip[2] == "3" or tip[2] == "4":
                for i in tip:
                    if i == "1":
                        self.hand[0][1] = int(tip[2])
                        break
                    if i == "2":
                        self.hand[1][1] = int(tip[2])
                        break
                    if i == "3":
                        self.hand[2][1] = int(tip[2])
                        break

    # Updating the coun_deck for bot!!
    def update_count_deck(self,card):
        if isinstance(card,list):
           self.count_deck.remove(card)
        if isinstance(card,int):
            self.count_deck.remove(self.count_deck[card])

        # Removing the card from count_deck which is located in the players hand!!
    def update_hand(self,num):
        #num = a
        comp_hand.pop(num)
        self.hand.pop(num)
        self.hand.append(['!',-1])
        if len(self.count_deck) != 0:
            b = random.randint(0, len(self.count_deck) - 1)
            comp_hand.append(self.count_deck[b])
            deck.pop(b)
            self.count_deck.pop(b)

    def give_tip(self):
        u = 0
        k = 0
        # my decision-making algorithm first checks the best tip for colors if it is the best
        # case it gives the tip ,otherwise it checks the values and gives the best tip accordingly!!
        while True:
            if play_hand[0][0] == play_hand[1][0] and play_hand[0][0] == play_hand[2][0] and len(play_hand) == 3:
                u = -1
                if [1,2,3,play_hand[0][0]] not in tip_control:
                    tip_control.append([1,2,3,play_hand[0][0]])
                    print(f"1,2,3,{play_hand[0][0]}")
                    break
            if play_hand[0][1] == play_hand[1][1] and play_hand[0][1] == play_hand[2][1] and u != -1 and len(play_hand) == 3:
                if [1,2,3,play_hand[0][1]] not in tip_control:
                    tip_control.append( [1,2,3,play_hand[0][1]])
                    print(f"1,2,3,{play_hand[0][1]}")
                    break
            if play_hand[0][0] == play_hand[1][0] and play_hand[0][0] != play_hand[2][0] and len(play_hand) > 1:
                k = -1
                if [1,2,play_hand[0][0]] not in tip_control:
                     tip_control.append([1,2,play_hand[0][0]])
                     print(f"1,2,{play_hand[0][0]}")
                     break
            if play_hand[0][0] == play_hand[2][0] and play_hand[0][0] != play_hand[1][0] and len(play_hand) > 1:
                k = -1
                if [1, 3, play_hand[0][0]] not in tip_control:
                     tip_control.append([1, 3, play_hand[0][0]])
                     print(f"1,3,{play_hand[0][0]}")
                     break
            if play_hand[2][0] == play_hand[1][0] and play_hand[2][0] != play_hand[0][0] and len(play_hand) > 1:
                k = -1
                if [2, 3, play_hand[2][0]] not in tip_control:
                     tip_control.append([2, 3, play_hand[2][0]])
                     print(f"2,3,{play_hand[2][0]}")
                     break
                ### decision-making  according to values!!
            if play_hand[0][1] == play_hand[1][1] and play_hand[0][1] != play_hand[2][1] and u != -1 and k != -1 and len(play_hand) > 1:
                if [1, 2, play_hand[0][1]] not in tip_control:
                     tip_control.append([1, 2, play_hand[0][1]])
                     print(f"1,2,{play_hand[0][1]}")
                     break
            if play_hand[0][1] == play_hand[2][1] and play_hand[0][1] != play_hand[1][1] and u != -1 and k != -1 and len(play_hand) > 1:
                if [1, 3, play_hand[0][1]] not in tip_control:
                     tip_control.append([1, 3, play_hand[0][1]])
                     print(f"1,3,{play_hand[0][1]}")
                     break
            if play_hand[2][1] == play_hand[1][1] and play_hand[2][1] != play_hand[0][1] and u != -1 and k != -1 and len(play_hand) > 1:
                if [2, 3, play_hand[2][1]] not in tip_control:
                     tip_control.append([2, 3, play_hand[0][1]])
                     print(f"2,3,{play_hand[2][1]}")
                     break


    # Bot tries to stack the known card here!!
    def pick_stack(self):
        # I create some variables for checking conditions!!
        global q
        global x
        stack_capacity = 0
        q = 0
        x = 0
        k = 1
        while k <= 3:
            if ['b', k] not in stack[0] and ['b', k] in self.hand:
                if k == 1:
                    x = self.hand.index(['b', k])
                    stack[0].append(self.hand[x])
                    stack_capacity += 1
                    print('Location of the card is:', x + 1)
                    q += 1
                    break

                if k != 1 and ['b', k - 1] in stack[0]:
                    if ['b', k] not in stack[0] and ['b', k] in self.hand and stack_capacity == 0:
                        x = self.hand.index(['b', k])
                        stack[0].append(self.hand[x])
                        stack_capacity += 1
                        print('Location of the card is:', x + 1)
                        q += 1
                        break

            k += 1

        k = 1
        while k <= 4:
            if ['w', k] not in stack[1] and ['w', k] in self.hand and stack_capacity == 0:
                if k == 1:
                    q = 0
                    x = self.hand.index(['w', k])
                    stack[1].append(self.hand[x])
                    stack_capacity += 1
                    print('Location of the card is:', x+1)
                    q += 1
                    break

                if k != 1 and ['w', k - 1] in stack[1]:
                    if ['w', k] not in stack[1] and ['w', k] in self.hand and stack_capacity == 0:
                        q = 0
                        x = self.hand.index(['w', k])
                        stack[1].append(self.hand[x])
                        stack_capacity += 1
                        q += 1
                        break

            k += 1
    # Bot tries to discard if card can not be stacked !!
    def pick_discard(self):
        # this variables are used to check necessary conditions in this function!!
        stack_control = 0
        pop_count = 0
        s = -5
        r = -5
        z = -5
        j = -5
        k = 0
        if len(self.hand) == 3:
            while k <= 2:
                if (self.hand[k] in stack[0]) or (self.hand[k] in stack[1]):
                    m = self.hand.index(self.hand[k])
                    trash.append(self.hand[k])
                    for i in comp_hand:
                        if i == trash[len(trash) - 1]:
                            comp_hand.remove(trash[len(trash) - 1])
                            self.hand.remove(self.hand[k])
                    stack_control += 1
                    pop_count += 1
                    break

                k += 1

        if len(self.hand) == 2:
            k = 0
            while k <= 1:
                if (self.hand[k] in stack[0]) or (self.hand[k] in stack[1]):
                    m = self.hand.index(self.hand[k])
                    trash.append(self.hand[k])
                    for i in comp_hand:
                        if i == trash[len(trash) - 1]:
                            comp_hand.remove(trash[len(trash) - 1])
                            self.hand.remove(self.hand[k])
                    stack_control += 1
                    pop_count += 1
                    break


                k += 1

        elif len(self.hand) == 1:
            k = 0
            if (self.hand[k] in stack[0]) or (self.hand[k] in stack[1]):
                m = self.hand.index(self.hand[k])
                trash.append(self.hand[k])
                for i in comp_hand:
                    if i == trash[len(trash) - 1]:
                        comp_hand.remove(trash[len(trash) - 1])
                        self.hand.remove(self.hand[k])
                stack_control += 1
                pop_count += 1



        for i in self.hand:
            for i in self.hand:
                if i == ['!', -1] and stack_control == 0:
                    stack_control += 1
                    m = self.hand.index(i)
                    trash.append(comp_hand[m])
                    self.hand.remove(self.hand[m])
                    pop_count += 1

                    for i in self.hand:
                        if i[0] != "!":
                            r = self.hand.index(i)
                            z = 0
                            z += 1
                            break
                    if z != 1:
                        r = 0
                    for i in self.hand:
                        if i[1] != -1:
                            s = self.hand.index(i)
                            j = 0
                            j += 1
                            break
                    if j != 1:
                        s = 0

                    for i in comp_hand:
                        if comp_hand.count(i) == 2 and pop_count == 0:
                            comp_hand.remove(i)
                            self.hand.remove(self.hand[m])
                            pop_count += 1
                            break

                    for i in comp_hand:
                        if i[0] != self.hand[r][0] and i[1] != self.hand[s][1] and s != 0 and r != 0 and pop_count == 0:
                            pop_count += 1
                            comp_hand.remove(i)
                            self.hand.remove(self.hand[m])
                            break

                    if s == 0 and z == 0 and pop_count == 0:
                        pop_count += 1
                        comp_hand.remove(comp_hand[0])
                    if pop_count == 0:
                        pop_count += 1
                        comp_hand.remove(comp_hand[m])
                        self.hand.remove(self.hand[m])
                    stack_control += 1
                    break

        for i in self.hand:
            if (i[0] != "!" and i[1] == -1) and stack_control == 0:
                stack_control += 1
                m = self.hand.index(i)
                trash.append(comp_hand[m])


                w = 0
                for i in comp_hand:
                    if i[0] == self.hand[m][0] and pop_count == 0:
                        if w == 0:
                            pop_count += 1
                            comp_hand.remove(i)
                            self.hand.remove(self.hand[m])
                            w += 1
                            break

                if pop_count == 0:
                    pop_count += 1
                    comp_hand.remove(comp_hand[m])
                    self.hand.remove(self.hand[m])
                k = 10
                break



        for i in self.hand:
            if (i[0] == '!' and i[1] != -1) and stack_control == 0:
                stack_control += 1
                m = self.hand.index(i)
                trash.append(comp_hand[m])


                for i in comp_hand:
                   if i[1] == self.hand[m][1]:
                     pop_count += 1
                     comp_hand.remove(i)
                     self.hand.remove(self.hand[m])
                     break

                   if pop_count == 0:
                       pop_count += 1
                       comp_hand.remove(comp_hand[m])
                       self.hand.remove(self.hand[m])
                break
     # Drawing a new card from deck!!
        if len(self.count_deck) != 0:
            l = random.randint(0, len(self.count_deck) - 1)
            self.hand.append(['!', -1])
            comp_hand.append(self.count_deck[l])
            deck.remove(self.count_deck[l])
            self.count_deck.remove(self.count_deck[l])
            re_sorted_trash = []



# Shuffling the deck !!
def shuffle(deck):
    deck_new = []
    counted_a = []
    while len(deck_new) <= len(deck):
        a = random.randint(0, 15)  # this generates a random integer which we will use in the index of deck!!
        if a not in counted_a:
            deck_new.append(deck[a])
            counted_a.append(a)
            if len(counted_a) == 16:
                break
    deck = deck_new

def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")
# This part updates the players hand after stacking or discarding!!
def update_hand(hand,deck,num):
    if discarder == 1:
        # Discarding part!!
        hand.pop(num-1)
        if len(deck) > 0:
            l = random.randint(0, len(deck) - 1)
            hand.append(deck[l])
            bot.update_count_deck(l)
            deck.pop(l)

    if stacker == 1:
        # Stacking part!!
        hand.pop(num-1)
        if len(deck) > 0:
            l = random.randint(0, len(deck) - 1)
            hand.append(deck[l])
            bot.update_count_deck(l)
            deck.pop(l)
# This function checks whether player can stack the card or not!!
def try_stack(card,stack,trash,lives):
    global stacker
    #global g
    #g = 0
    stacker = 0
    stack_capacity = 0
    c = 0
    k = 1
    p = 0
    u = 0
    while k <= 4:
        if play_hand[card-1][0] == "b" and play_hand[card-1][1] == k and ['b',k] not in stack[0]:
            if k == 1:
                g = play_hand.index(['b', k])
                stack[0].append(play_hand[g])
                stack_capacity += 1
                stacker += 1
                update_hand(play_hand, deck, g+1)
                if len(play_hand) == 2:
                    k = -10
                if len(play_hand) == 1:
                    k = -10
                # printing the location of the card stacked !!
                print('Location of the card is:', g + 1)
                c += 1
                u = -1
                p += 1
                break


            if k != 1 and ['b', k - 1] in stack[0]:
                if ['b', k] not in stack[0] and ['b', k]  in play_hand and u != -1 and stack_capacity == 0:
                    g = play_hand.index(['b', k])
                    stack[0].append(play_hand[g])
                    stack_capacity += 1
                    stacker += 1
                    update_hand(play_hand, deck, g+1)
                    if len(play_hand) == 2:
                        k = -10
                    if len(play_hand) == 1:
                        k = -10
                    # printing the location of the card stacked !!
                    print('Location of the card is:', g + 1)
                    c += 1
                    p += 1
                    break

        k += 1

    if k != -10:
        z = 0
        k = 1
        p = 0
        u = 0
        while k <= 4:
            if play_hand[card - 1][0] == "w" and play_hand[card - 1][1] == k and ["w", k] not in stack[1] and stack_capacity == 0:
                if k == 1:
                    a = play_hand.index(['w', k])
                    stack[1].append(play_hand[a])
                    stack_capacity += 1
                    stacker += 1
                    update_hand(play_hand, deck, a + 1)
                    if len(play_hand) == 2:
                        k = -10
                    if len(play_hand) == 1:
                        k = -10
                    # printing the location of the card stacked !!
                    z += 1
                    u = -1
                    p += 1
                    print('Location of the card is:', a + 1)

                if k != 1 and ['w', k - 1] in stack[1] and k != -10:
                    if ['w', k] not in stack[1] and ['w', k] in play_hand and u != -1 and stack_capacity == 0:
                        a = play_hand.index(['w', k])
                        stack[1].append(play_hand[a])
                        stack_capacity += 1
                        stacker += 1
                        update_hand(play_hand, deck, a + 1)
                        if len(play_hand) == 2:
                            k = -10
                        if len(play_hand) == 1:
                            k = -10
                         # printing the location of the card stacked !!
                        print('Location of the card is:', a + 1)
                        z += 1
                        p += 1

            k += 1
        if len(play_hand) == 2:
            k = -10
        if len(play_hand) == 1:
            k = -10

        if c != 1 and z != 1:
            trash.append(play_hand[card - 1])
            re_sorted_trash = []
            k = 1
            while k <= 4:
                if ["w", k] in trash:
                    i = trash.index(["w", k])
                    re_sorted_trash.append(trash[i])
                    if stacker == 0:
                        stacker += 1
                    update_hand(play_hand, deck, card)
                    k += 1
                else:
                    k += 1
            k = 1
            while k <= 4:
                if ["b", k] in trash:
                    i = trash.index(["b", k])
                    re_sorted_trash.append(trash[i])
                    k += 1
                    if stacker == 0:
                        stacker += 1
                    update_hand(play_hand, deck, card)

                else:
                    k += 1

            trash = re_sorted_trash
            print("Warning:")
            return -3

# Player try to discard card in this function!!
def discard(card,trash,tips):
    global discarder
    discarder = 0
    tips += 1
    trash.append(play_hand[card-1])
    re_sorted_trash = []
    k = 1
    while k <= 4:
        if ["w", k] in trash:
            i = trash.index(["w", k])
            re_sorted_trash.append(trash[i])
            k += 1
        else:
            k += 1
    k = 1
    while k <= 4:
        if ["b", k] in trash:
            i = trash.index(["b", k])
            re_sorted_trash.append(trash[i])
            k += 1
        else:
            k += 1
    for i in trash:
        if i == ["b", -1] or ["w",-1]:
            re_sorted_trash.append(i)
    discarder += 1
    trash = re_sorted_trash
    print(f"tips:{tips}")
    return -6

print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
tips = 3
lives = 2
shuffle(deck)
q = 0
x = 0
# I randomly dealt three cards to player and computer!!
tip_control = []
comp_hand = []
counted_m = []
while len(comp_hand) < 3:
    m = random.randint(0,15)
    if m not in counted_m:
        comp_hand.append(deck[m])
        counted_m.append(m)

a,b,c =  deck[counted_m[0]],deck[counted_m[1]],deck[counted_m[2]]
com_hand_first = [a,b,c]
# Dealt cards are removed from the deck here!!
deck.remove(a)
deck.remove(b)
deck.remove(c)

play_hand = []
counted_n = []
while len(play_hand) < 3:
    n = random.randint(0,12)
    if n not in counted_n:
        play_hand.append(deck[n])
        counted_n.append(n)

a,b,c =  deck[counted_n[0]],deck[counted_n[1]],deck[counted_n[2]]
# Dealt cards are removed from the deck here!!
deck.remove(a)
deck.remove(b)
deck.remove(c)

bot = Gamebot(play_hand,stack)# Gamebot object is created.
# Updating the computers hand for first dealt cards!!
for i in com_hand_first:
    bot.update_count_deck(i)
turn = 0# 0 means player, 1 means computer. So for each game, the player starts.
while True:
    # stacker and discarder variables controls the stacking an discarding process!!
    discarder = 0
    stacker = 0
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:", comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                turn = 1
                print(play_hand)
                tip = input('give a good tip according to bots hand:')
                bot.get_tip(tip)
                tips -= 1
                print(f"tips:{tips}")


            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            # Player tries to stack card here!!
            turn = 1
            card = int(input('Please give the location of the card that you want to stack:'))
            a = try_stack(card,stack,trash,lives)
            if a == -3:
                lives -= 1
                print(f"Current number of lives:{lives}")

        elif inp == "d":
            # Player tries to stack card here!!
            turn = 1
            card = int(input('Please give the location of card to be discarded:'))
            print(play_hand)
            a = discard(card,trash,tips)
            if a == -6:
                tips += 1
            update_hand(play_hand,deck,card)

        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        if tips > 1  and len(play_hand)>0:
            # bot gives a tip in this part!!
            bot.give_tip()
            tips -= 1
            print(f"tips:{tips}")

        else:
            # Bot tries to stack the card it knows precisely, otherwise it discards it!!
            bot.pick_stack()
            if q == 1:
                bot.update_hand(x)
            else:
                bot.pick_discard()
                tips += 1

        turn = 0
    score = sum([len(d) for d in stack])
    if lives == 0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break
