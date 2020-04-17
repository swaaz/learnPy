# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

#function to compute
def compute(a,b,c):
    if c == "+" :
        print(a,c,b,"=",add(a,b))
    elif c == "-" :
        print(a,c,b,"=",sub(a,b))
    elif c == "*" :
        print(a,c,b,"=",mul(a,b))
    elif c == "/" :
        div(a,b)
    else:
        print("Invalid!!")
#function to add
def add(a,b):
    return (a+b)
#function to subtract
def sub(a,b):
    return(a-b)
#function to multiply
def mul(a,b):
    return(a*b)
#function to divide
def div(a,b):
    try:
        #divide
        print(a,"/",b,"=",format((a/b),".2f"))
    except:
        #if therr is an error while dividing
        print("Cannot be divided!!!")

a=int(input("Enter the operand "))
c=input("Enter the operator (+,-,*,/) ")
b=int(input("Enter the operand "))
compute(a,b,c)