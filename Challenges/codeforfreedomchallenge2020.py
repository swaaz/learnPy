#CodeForFreedom Challenge 20/04/2020

#Write a program to print a list of strings in the predefined order, with the following modifications:
#If the string’s length is equal to its printed position, convert string to UPPERCASE
#	- Else convert the string to lowercase
#	- Except if the string’s position is unchanged from its original position
#	- Input will be a number N, then a list of N non-repeating numbers defining the required position of the string, and finally the list of N non-repeating strings. Output will be a list of N strings at the required location, with the required changes.

#- Input:
#5
#5
#4
#3
#1
#2
#Dog
#Goat
#Cat
#Horse
#Elephant

#- Output:
#horse
#elephant
#Cat
#GOAT
#dog

#global declaration

input_string_position = []
input_string = []
output_string = []
number = 0

#function to compare    
def compute():
    global output_string
    for x in range(number):
        a=(input_string_position[x]-1)
        if input_string_position[x] == len(input_string[x]) and x == a:
            output_string[a]=input_string[x]
        elif input_string_position[x] == len(input_string[x]):
            output_string[a]=input_string[x].upper()
        else:
            output_string[a]=input_string[x].lower()
            
#main function            
def main():
    global number
    number=int(input())
    for x in range(number):
        y=int(input())
        input_string_position.append(y)
    for x in range(number):
        y=input()
        input_string.append(y)
        #output_string.append(y)
    compute()
    for x in output_string:
        print(x)
#invoking main function        
main()