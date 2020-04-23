# creating dictionaries using class
class Sweetmenu(dict):
    def __init__(self):
        self = dict()
    def add_element(self,index,value):
        self[index] = value

#creating class object
sweet_menu=Sweetmenu()

n=int(input('Enter the no. of items you want to add in your menu'))
for i in range(0,n):
    sweet_menu.name=str(input('Enter the name of the sweet'))
    sweet_menu.price=int(input('Enter the price you want to desginate to the sweet'))
    print(str(sweet_menu.name)+' will cost you around '+str(sweet_menu.price)+' Dollars')
    sweet_menu.add_element(sweet_menu.name,sweet_menu.price)
print(sweet_menu)

selected_items = []    

count=0

"""
def select_item(menu):
    for i in range(len(menu)):
        select=input('Select the sweet of your choice from the menu')
        selected_items.append(select)
    return select

def Bill(selected_items, menu):
    for i in range(len(selected_items)):
       coun+=count+menu[i]
    print(coun)    
         
            
a=select_item(sweet_menu)
print('The selected item are: ',a)
b=Bill(selected_items,sweet_menu.menu)
print('The Bill of dollars',b)

"""