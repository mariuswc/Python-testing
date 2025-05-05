
menu = ["Add", "Remove", "Show", "Quit"]
grocerylist = []


def shoppinglist_menu(): 
        while True:
            userinput = input(f"Enter what you want from the {menu} ").capitalize()
            if userinput == "Quit":
                print("The shopping list has closed")
                break
            elif userinput == "Add":
                adding_menu()
            elif userinput == "Remove":
                remove_menu()
            elif userinput == "Show":
                show_list()
                shoppinglist_menu()
            else:
                print("Please enter a valid option")
    

def adding_menu():
    while True:
        what_to_add = input("What do you want to add? Press Q to go back to the main menu ").upper().strip()
        if what_to_add == "Q":
            return
        elif what_to_add in grocerylist:
            print("The item already exist")
        else:
            grocerylist.append(what_to_add)
            print(f"the list now contains: {grocerylist}")
    

def remove_menu():
    if grocerylist:
        while True:
            what_to_remove = input(f"What do you want to remove from the shoppinglist: {grocerylist} ").upper().strip()
            if what_to_remove not in grocerylist:
                print(f"the item you are trying to remove: {what_to_remove} does not exist in the list")            
            else:
                grocerylist.remove(what_to_remove)
                print(f"You removed {what_to_remove} from the grocerylist")
                if not grocerylist:
                    print("The list is empty")
                    adding_menu()
                remove_more = input("Do you wish to remove more items, press Y to continue or press N to QUIT and go back to main menu ").upper()
                if remove_more == "N":
                    shoppinglist_menu()
                
                else:
                    continue
    else:
        print("You need to add something to your shoppinglist before removing items")
        adding_menu()


def show_list():
  for x, item in enumerate(grocerylist, 1):
     print(f"{x}:{item}")



def main():
    shoppinglist_menu()
main()




# neste oppgave:
# Save/load the list from a file (with open(), readlines(), etc.)

#Add a feature to clear the whole list

#Add timestamps to items or mark them as "bought"

#Sort the list alphabetically
