#---------- SNAKE WATER GUN GAME ----------------------

'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.choice ([1,-1,0])
youstr =  (input("Enter your choice: "))
youDict = {"s" :1, "w": -1, "g": 0}
reverseDict={1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f'computer chose {reverseDict[computer]}')
print(f'you chose {reverseDict[you]}')

if(computer == you):
    print("It's a tie!")

elif(computer ==-1 and you == 1):
    print("you win!")
elif(computer ==-1 and you == 0):
    print("you lose!")
elif(computer ==1 and you == -1):
    print("you lose!")
elif(computer ==1 and you == 0):
    print("you win!")
elif(computer ==0 and you == 1):
    print("you lose!")
elif(computer ==0 and you == -1):
    print("you win!")
else:
    print("something went wrong")


    print(" "*5+ "GAME OVER")
