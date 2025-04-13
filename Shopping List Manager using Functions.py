def menu():
    print ("\n1. Add an item")
    print ("2. Remove an item")
    print ("3. View list")
    print ("4. Quit")


def add_item(list):
    item = input("Add an item: ")
    list.append(item)   

def remove_item(list):
    r_item = input("Remove an item: ") 
    if r_item in list:
        list.remove(r_item) 
    else:
        print("Item not found.")    

def view_list(list):
    print("Shopping list: ", list)

def shopping_list_manager():
    list = []

    while True:
        menu()

        option = input("Select an option: ")

        if option == "1":
            add_item(list)
        elif option == "2":
            remove_item(list)
        elif option == "3":
            view_list(list)
        elif option == "4":
            break   
        else:
            print("Invalid option.")     

shopping_list_manager()

