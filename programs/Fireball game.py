import random
import datetime
def checker(machinelist, usrlist):
#here each ticket is being checked with the lotto result
#In case of fireball, each ticket is being checked with the fireball combinations also
    for i in range(3):
        if usrlist[i] == machinelist:
            return True
    else:
        return False
#fire ball function
def fireball():
    fireball_result = [[] for i in range(3)]
    fireball_number = random.sample(range(0,10),1)
    fireball_number = fireball_number[0]
    for i in range(3):
        temp = list(lottolist)
        temp[i] = fireball_number
        fireball_result[i] = list(temp)
        result = checker(temp,tickets)
        temp = []
        if result is True:
            print("Yay you won $150 as part of the fireball win")
            print("your tickets are {}".format(tickets))
            print("The lotto result is {}".format(lottolist))
            print("The fireball number is {}".format(fireball_number))
            print("The fireball result is {}".format(fireball_result[i]))
            break
    else:
        print("nice try, better luck next time")
        print("your tickets are {}".format(tickets))
        print("The lotto result is {}".format(lottolist))
        print("The fireball number is {}".format(fireball_number))
        print("The fireball result is {}".format(fireball_result))


# This is the pick 3 lottery result for the weak
lottolist = sorted(random.sample(range(0,10),3))
#user gets three picks which means user get 3 tickets against the lottory result.
#initializing that ticket array. This is a list of list
tickets = [[] for i in range(3)]
print("Welsome to pick 3!!! You have three chances which means 3 tickets")
#This is used to just print the ticket number in print statement
ticketnumber = 1
#we are giving user three chance here which is similar to user getting 3 tickets
for i in range(0,3):
    print("Enter your ticket {} which is 3 number in range 0 to 9".format(ticketnumber))
    for j in range(0,3):
        try:
            number = int(input())
            #error handling
        except (ValueError, RuntimeError, TypeError, NameError):
            print("oops enter a numbers in range 0 to 9")
            number = int(input())
            if number not in range(0,10):
                print("oops enter a numbers in range 0 to 9")
                number = int(input())
        tickets[i].append(number)
    ticketnumber += 1
print("Do you want to play it with fireball or not\n If you want to play fireball please enter 1 \n If you want to play pick 3 lotto without fireball please enter 0")
userinput = int(input())
#error handling
if userinput not in range(0,2):
    print("Enter valid input 0 or 1")
    userinput = int(input())
if userinput == 1:
    fireball()
#checking the tickets against the lottary list without fireball option
elif userinput == 0:
    result = checker(lottolist, tickets)
    if result is True:
        print("Yay!! you won $100")
        print("your tickets are {} \n pick 3 lotto result is {}".format(tickets,lottolist))
    else:
        print("nice try, better luck next time")
        print("your tickets are {} \n pick 3 lotto result is {}".format(tickets,lottolist))

