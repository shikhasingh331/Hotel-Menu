#Define the menu of restaurant
menu={
    "pizza" : 40,
    "pasta" : 50,
    "Burger" : 60,
    "momose" : 70,
    "coffe" : 80
}

#Greet
print("Welcome to Python Resturant")
print("pizza: Rs40\n Pasta: Rs50\n Burger: Rs60\n momose: Rs70\n coffe: Rs80")

order_total = 0
# 80 + 70 = 150


item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu : 
    order_total += menu[item_1] #0+50
    print("your item {item_1} has been added to your order")
    
else :
    print("ordered item {item_1} is not available yet!")
    
another_order = input("do you want to add anoter item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item =")
    if item_2 in menu :
        order_total += menu[item_2]
        print("Item {item_2} has been added to order")
        
    else :
        print("ordered item {item_2} is not available!")
        
print(f"The total amount of item to pay is {order_total}")


    
