#This is a Password Generator.

#Import function
import random
loop = 1
#code start
while True:
    many=int(input("How many password do you want to be generated? "))
    lenght=int(input("How long password you want? "))
    password = ""
    pas = ""
    for x in range(0, many):
        for b in range(0, lenght):
            rad = random.randint(0, 4)
            if (rad == 1) :
                pas = random.choice('abcdefghijklmnopqrstuvwxyz')
            elif (rad == 2) :
                pas = random.choice('%&#=+')
            elif (rad == 3) :
                pas = random.choice('1234567890')
            elif (rad == 4) :
                pas = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

            password = password + pas
        print (password)
        password = ""
    close=input("Do you want to generatet more password? Y/n ")

    if close != "Y" :
            break
