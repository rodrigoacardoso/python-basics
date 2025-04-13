list = []

while True:
    print ("\n1. Add an item")
    print("2. Remove an item")
    print("3. View list")
    print("4. Quit")

    option = input("Select an option: ")

    if option == "1":
        item = input("Add an item: ")
        list.append(item)
    elif option == "2":
       r_item = input("Remove an item: ") 
       if  r_item in list:
           list.remove(r_item) 
       else:
           print("Item not found")
    elif option == "3":
        print("Shopping list: ", list) 
    elif option == "4":
        break          
    else:
        print("Invalid option")          

    
       

           



