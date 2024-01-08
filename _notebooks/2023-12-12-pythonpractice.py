# Programming: Creating a “store”
# Use knowledge of arrays, loops and variable storage to create a “store” with console inputs.
# Commands: Buy, sell, check inventory, quit, and program should print customets money left after every command


items = {"car" : 100,
         "phone" : 10, 
         "apple" : 1}

customerMoney = 1
customerInventory = {"apple" : 3,
                      "phone" : 1}


userInput = input("are you gonna buy or sell?: ")
while userInput != "quit":
    if userInput != "sell" and userInput != "buy" and userInput != "check inventory":
        print("choose either buy, sell, or check inventory")
        break
    if userInput == "buy":
        print(items)
        secondUserInput = input("what are you gonna buy?: ")
        if secondUserInput in items:
            if customerMoney - items[secondUserInput] >=0:
                customerInventory[secondUserInput] = customerInventory.get(secondUserInput, 0) +1
                customerMoney = customerMoney - items[secondUserInput]
                print(customerInventory)
                print(customerMoney)
                break
            else:
                print("your money: " + str(customerMoney) + ". with this money, you cant buy anything")
                break
    if userInput == "sell":
        
    

