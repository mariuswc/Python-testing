from datetime import datetime
menu = ["Add", "Remove", "Show", "Quit","Clear"]
grocerylist = []

try:
            with open("handleliste.txt", "r") as file:
                for line in file:
                    grocerylist.append(line.strip())
except FileNotFoundError:
            grocerylist = []

def shoppinglist_menu(): 
        while True:
            userinput = input(f"Enter what you want from the list {menu}: ").upper().strip()
            if userinput == "QUIT":
                quitting()
                break
            elif userinput == "SHOW":
                show_list()
                shoppinglist_menu()
            elif userinput == "ADD":
                adding_menu()
            elif userinput == "REMOVE":
                remove_menu()
            elif userinput == "CLEAR":
                 clear_list()
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
            dt = datetime.now().strftime("%Y-%m-%d %H:%M")
            grocerylist.append(f"{what_to_add} - {dt}")
            grocerylist.sort()
            print(f"The list now contains {grocerylist} at {dt}" )
            saving_file()

def remove_menu():
    if grocerylist:
        while True:
            what_to_remove = input(f"What do you want to remove from the shoppinglist: {grocerylist} ").upper().strip()
            if what_to_remove not in grocerylist:
                print(f"the item you are trying to remove: {what_to_remove} does not exist in the list")            
            else:
                grocerylist.remove(what_to_remove)
                print(f"You removed {what_to_remove} from the grocerylist")
                saving_file()
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
    if not grocerylist:
        print("The list is empty")
    else:
        for x, item in enumerate(grocerylist, 1):
            print(f"{x}:{item}")

def clear_list():
    
    if not grocerylist:
        print("The list is already empty")
        return
            
    print("Current list:")
    for item in grocerylist:
        print(f"- {item}") 
            
    areyousure = input(f"Are you sure you want to clear the list? (Y or N): ").upper().strip()
    
    if areyousure == "Y":
        grocerylist.clear()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M") 
        print(f"The list has been cleared at {timestamp}")
        grocerylist.append(f"List cleared at {timestamp}")  
        saving_file()
            
    else:
        print("The list has not been cleared.")
 

def quitting():
    print("The session has quit")
    return

def saving_file():
    with open("handleliste.txt", "w") as file:
            for item in grocerylist:
                file.write(item + "\n")
        
                
def main():
        shoppinglist_menu()
        saving_file()
        

main()




# neste oppgave:
# Save/load the list from a file (with open(), readlines(), etc.) check!

#Add a feature to clear the whole list check!

#Add timestamps to items or mark them as "bought"check!

#Sort the list alphabetically check!
