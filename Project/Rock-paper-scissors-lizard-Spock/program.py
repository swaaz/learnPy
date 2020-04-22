#importing 
import sys
import random
#function which convert name to number
def name_to_number(name):
   
    if name.lower() == "rock":
        return 0
    elif name.lower() == "spock":
        return 1
    elif name.lower() == "paper":
        return 2
    elif name.lower() == "lizard":
        return 3
    elif name.lower() == "scissors":
        return 4
#function which converts number to name
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number ==4:
        return "scissors"
#function to check the values and print the result
def check(player_choice): 
    print ()
    print ("Player chooses : ",player_choice)
    Player_number = name_to_number(player_choice)
    Comp_number=random.randrange(0,5)
    Comp_name = number_to_name(Comp_number)
    print ("Computer Chooses",Comp_name)
    x=(Player_number - Comp_number) % 5 #logic to compute winner
    if x==0:
        print ("-----Tie!------")
    elif x==1 or x==2:
        print ("------Computer wins!------")
    elif x==3 or x==4:
        print ("------Player wins!------")

#main function
def main():
    while(True):
        print()
        x=int(input("Rock-paper-scissors-lizard-Spock\n------------Options------------\n1 ==> Play <==\n2 ==> Stop <==\nEnter the choice : "))
        if x == 1:
            print()
            y=input("Enter the choice :\nRock or Spock or Paper or Lizard or Scissors : \n")
            check(y)
        else:
            print()
            print("------Game End!!!------")
            sys.exit()
#function call          
main()

