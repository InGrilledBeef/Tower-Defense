#Author: Ingrid Qin
#Date: 11/27/2019
#Purpose: This is a program that allows users order pizza

#This function calculates the HST
def HST_calculator(total):
    tax = 0.13 * total
    print("The HST is $%.2f" %(tax))
    return tax

#This function sees if the user chooses to pick up or have their order delivered. If the user wishes for their pizza to be delivered, $3.50 is added to the total cost.
def deliver(delivery, total):
    if delivery == "Y" or delivery == "YES":
        total += 3.5
        if pizza_num >= 4:
            print("Your delivery gratuity is $3.50")
            print("The cost of your order is $%.2f" %(total))
        else:
            print("A delivery charge of $3.50 will be applied")
            print("So, the cost of your order is $%.2f" %(total))
    if delivery == "N" or delivery == "NO":
        print("You have chosen to pick-up your order")

    return total

#This function calculates the price after the 15% discount
def discount(total):
    print("You qualify for a 15% volume discount")
    total = total - (total * 0.15)
    print("So, the cost of your order is $%.2f" %(total))
    return total

#This function sees if the user wants to order another pizza
def again():
    #A while loop is used in case the user inputted an invalid input
    while True:
        print()
        another = input("Would you like to order another pizza? (Y/N) ")
        another = another.upper()
        if another == "N" or another == "NO":
            return False
        elif another == "Y" or another == "YES":
            return True
        else:
            print("Sorry, that is not a valid input. Please try again")

#This function returns the price for each pizza size
def size_choice(size):
    if size == "Small":
        return 6.95
    if size == "Medium":
        return 8.49
    if size == "Large":
        return 10.49
    if size == "X-Large":        
        return 13.49

#This function takes the size the user inputs and returns it as words that are easier to work with
def size_in_words(size):
    if size == "S" or size == "SMALL":
        return "Small"
    if size == "M" or size == "MEDIUM":
        return "Medium"
    if size == "L" or "LARGE":
        return "Large"
    if size == "XL" or "X-LARGE":
        return "X-Large"

#This function finds the price of the toppings for each size
def toppings_price(size):
    print()
    if size == "Small":
        print("Each topping is $1.35")
        return 1.35
    if size == "Medium":
        print("Each topping is $1.50")
        return 1.50
    if size == "Large":
        print("Each topping is $1.75")
        return 1.75
    if size == "X-Large":
        print("Each topping is $1.95")
        return 1.95

#This function deals with the custom pizzas
def custom_toppings(total_cost, pizza_size):
    #This contains the cost of the toppings
    toppings_cost = toppings_price(pizza_size)
    
    #The toppings are added into a list and then are printed out. After that, the user chooses the toppings.
    print()
    print("Here are your choices for toppings.\nType 11 when you are finished entering the toppings.")
    print()
    toppings_list = ["Olives", "Mushrooms", "Green Peppers", "Hot Peppers", "Onions", "Pineapple", "Anchovies", "Ham", "Sausage", "Pepperoni", "No (more) toppings please!"]
    #This variable is used so that the toppings will align with their assigned numbers.
    topping_num = 1
    for i in toppings_list:
        print(str(topping_num) + '.', i)
        topping_num += 1
    print()
    topping = int(input("Please choose a topping! "))

    #Counts number of toppings
    count = 0

    #The program will keep asking for toppings until the user inputs 11
    while topping != 11:
        #This while loop is used in case the user inputs an invalid input
        while topping < 1 or topping > 11:
            print("Sorry that is not a valid choice. Please try again")
            print()
            topping = int(input("Please choose a topping! "))
        if topping == 11:
            break
        total_cost += toppings_cost
        count += 1
        #Every time the user inputs a topping, the program prints out which topping they added, and the toppings menu again
        print("You have added", toppings_list[topping -1], "to your pizza.")
        print()
        print("Here are your choices for toppings.\nType 11 when you are finished entering the toppings.")
        topping_num = 1
        print()
        for i in toppings_list:
            print(str(topping_num) + '.', i)
            topping_num += 1
        print()
        topping = int(input("Please choose a topping! "))
    print()
    #This is the final print statement after all the toppings the user wants are added onto their pizza
    if count == 1:
        print("One", pizza_size, "pizza with", count, "topping is $%.2f" %(total_cost))
    else:
        print("One", pizza_size, "pizza with", count, "toppings is $%.2f" %(total_cost))
    return total_cost

#This is the function for the ready-made pizza
def ready_pizza(total_cost, pizza_size):
    print()
    #This is a list of ready-made pizzas. 
    ready_made_pizzas = ["Pepperoni", "Cheese", "Hawaiian", "Vegetarian", "Olive"]

    #This will change the total cost to the cost of the ready-made pizza according to the user's pizza size input 
    if pizza_size == "Small":
        print("The total cost of a Small ready-made pizza is $9.19")
        total_cost = 9.19
    if pizza_size == "Medium":
        print("The total cost of a Medium ready-made pizza is $10.99")
        total_cost = 10.99
    if pizza_size == "Large":
        print("The total cost of a Large ready-made pizza is $13.29")
        total_cost = 13.29
    if pizza_size == "X-Large":
        print("The total cost of a X-Large ready-made pizza is $16.69")
        total_cost = 16.69

    print()
    print("Here are your ready-made pizzas. You can only choose one pizza.")
    print()
    count = 1
    for i in ready_made_pizzas:
        print(str(count)+".", i)
        count += 1

    print()
    #This print statement is here because (almost) everyone loves olives and those who do no like olives are not qualified to be human.
    print("As a recommendation, Feeling Saucy's infamous pizza is the Olive Pizza, made purely of Olives.")

    print()
    pizza_choice = int(input("Please choose a pizza! (input a number) "))
    #This while loop is used in case the user inputs an invalid input
    while pizza_choice < 1 or pizza_choice > 5:
        print("Sorry that is not a valid choice. Please try again")
        print()
        pizza_choice = int(input("Please choose a pizza! (input a number) "))

    print()
    #This will be the final print statement after the user chooses their pizza
    if pizza_choice == 5:
        print("You have ordered an", ready_made_pizzas[pizza_choice - 1], "pizza")
    else:
        print("You have ordered a", ready_made_pizzas[pizza_choice - 1], "pizza")
    
    return total_cost

#This is the function for the pizza specials
def special_pizza(total_cost, pizza_size):
    print()
    #If special_order == False, that means the user no longer wishes to order the special
    special_order = special_or_not()
    if special_order != True:
        return total_cost
    #This will change the total cost to the cost of the special according to the user's pizza size input 
    if pizza_size == "Small":
        print("The total cost of a special for a Small pizza is $7.29")
        total_cost = 7.29
    if pizza_size == "Medium":
        print("The total cost of a special for a Medium pizza is $9.09")
        total_cost = 9.09
    if pizza_size == "Large":
        print("The total cost of a special for a Large pizza is $11.39")
        total_cost = 11.39
    if pizza_size == "X-Large":
        print("The total cost of a special for a X-Large pizza is $14.79")
        total_cost = 14.79
        
    return total_cost

#In this function, the special for each day prints and it asks the user if they still want to order the special
def special_or_not():
    day = input("What day is it today? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun) ")
    day = day.upper()
    while (day != "MON" and day != "TUES" and day != "WED" and day != "THURS" and day != "FRI" and day != "SAT" and day != "SUN" and
    day != "MONDAY" and day != "TUESDAY"and day != "WEDNESDAY" and day != "THURSDAY" and day != "FRIDAY" and day != "SATURDAY" and day != "SUNDAY"):
        print("Sorry that is not a valid day. Please try again")
        day = input("What day is it today? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun) ")
        day = day.upper()

    today_special = ""

    print()
    #These will print out the day's special according to the day the user inputs
    if day == "MON" or day == "MONDAY":
        print("Today's special is the Cauli Super Plant Pizza")
        print("It is made with Cauliflower Crust, topped with homestyle Tomato Sauce, Mozzarella Cheese, Plant-based Pepperoni and Plant-based Chorizo Crumble.")
        print("Toppings contain gluten")  
    elif day == "TUES" or day == "TUESDAY":
        print("Today's special is the Steak and Blue Cheese Pizza")
        print("It is made with Regular Dough, topped with Mozzarella Cheese, Garlic Spread, Fresh Mushrooms, and Steak Strips")
    elif day == "WED" or day == "WEDNESDAY":
        print("Today's special is the Sausage Mushroom Melt")
        print("Is is made with Regular Dough, topped with Creamy Garlic Sauce, Mozzarella Cheese, Italiano Blend Seasoning, Fresh Mushrooms, and Spicy Italian Sausage") 
    elif day == "THURS" or day == "THURSDAY":
        print("Today's special is the Greek Pizza")
        print("It is made with Regular Dough, topped with Mozzarella Cheese, Feta Cheese, Home Syle Italian Tomate Sauce, Kalamata Olives, Red Onions, and Spinach")
    elif day == "FRI" or day == "FRIDAY":
        print("Today's special is called the KinBon Lee Special")
        print("This is a sodium chloride based pizza, as it is made with fried sodium chloride dough, and topped with sodium chloride from the sea, and sodium chloride from rich minerals")
    elif day == "SAT" or day == "SATURDAY":
        print("Today's special is the Sriracha and Honey Pizza")
        print("It is made with Regular Dough, topped with a Habanero Cheese Base, Honey Garic Swirl, Sriracha Swirl, and Home Style Italian Tomato Sauce")
    elif day == "SUN" or day == "SUNDAY":
        print("Today's special is the Chipotle Chicken Pizza")
        print("It is made with Regular Dough, topped with Chipotle Chicken, Mozzarella Cheese, Chipotle Sauce, and Red Onions") 
    
    print()
    #This is asked in case the user changes their mind after seeing the special
    continue_or_not = input("Do you still want to order the special? (Y/N) ")
    continue_or_not = continue_or_not.upper()
    #This while loop is here just in case there is an invalid input
    while continue_or_not != "Y" and continue_or_not != "YES" and continue_or_not != "N" and continue_or_not != "NO":
        print()
        print("Sorry that is not a valid input. Please try again")
        print()
        continue_or_not = input("Do you stil want to order the special? (Y/N) ")
        continue_or_not = continue_or_not.upper()

    if continue_or_not == "Y" or "YES":
        return True
    return False

 
#This function deals with the order    
def order():
    #The size choice is the first input. The size and their corresponding prices are printed out, then the user can choose the size of pizza they desire.
    print()
    print("Here are the prices for our pizzas\nSmall - $6.95\nMedium - $8.49\nLarge - $10.49\nX-Large - $13.49")
    
    #This counter counts how many pizzas the user orders
    pizza_num = 0
    print()
    pizza_size = input("What size pizza would you like? (S/M/L/XL) ")
    pizza_size = pizza_size.upper()

    # Checks to see if the size the user entered is invalid and keeps asking
    # until they enter in a valid size before continuing on with the program
    while (pizza_size != "S" and pizza_size != "SMALL" and
           pizza_size != "M" and pizza_size != "MEDIUM" and
           pizza_size != "L" and pizza_size != "LARGE" and
           pizza_size != "XL" and pizza_size != "X-LARGE"):
        print("Sorry. That is not a valid size. Please try again.")
        print()
        pizza_size = input("What size pizza would you like? (S/M/L/XL) ")
        pizza_size = pizza_size.upper()

    #This will convert the size input into something more universally used in the code.
    pizza_size = size_in_words(pizza_size)

    #This is an accumulator that will total up the cost for the final bill        
    total_cost = size_choice(pizza_size)
    
    
    #This asks the user if they want a custom pizza, a ready made pizza, or the special
    while True:
        print()
        custom_ready_special = input("Do you want a custom made pizza, a ready-made pizza, or today's special? (custom/ready-made/special) ")
        custom_ready_special = custom_ready_special.upper()
        #This checks if the user inputted an invalid input and will keep checking until it isn't invalid
        while custom_ready_special != "CUSTOM" and custom_ready_special != "READY-MADE" and custom_ready_special != "SPECIAL":    
            print("Sorry that is not a valid input. Please try again")
            print()
            custom_ready_special = input("Do you want a custom made pizza, a ready-made pizza, or today's special? (custom/ready-made/special) ")
            custom_ready_special = custom_ready_special.upper()
        
        #Depending on what the user inputs (custom/ready-made/special), a specific function is called to meet the user's needs
        if custom_ready_special == "CUSTOM":
            total_cost == custom_toppings(total_cost, pizza_size)
            break
        elif custom_ready_special == "READY-MADE":
            total_cost = ready_pizza(total_cost, pizza_size)
            break
        elif custom_ready_special == "SPECIAL":
            temp = total_cost
            total_cost = special_pizza(total_cost, pizza_size) 
            #If temp == total_cost, that means the user changed their mind and did not order the special
            if temp != total_cost:
                break
            
    return total_cost


#Here is where the code "starts"
print("Welcome to Feeling Saucy Pizzeria!")
#This contains the total cost of the entire order
total_pizzaCost = 0
#This contains the number of pizzas the user orders
pizza_num = 0
another_order = True

#This runs until the user does not wish to order another pizza
while another_order:
    total_pizzaCost += order()
    pizza_num += 1
    another_order = again()
    
print()
#This asks the user if they want their pizza delivered
delivery = input("Is this for delivery? (Y/N) ")
delivery = delivery.upper()
while delivery != "Y" and delivery != "YES"  and delivery != "N" and delivery != "NO":
    print("Sorry that is not a valid input. Please try again")
    print()
    delivery = input("Is this for delivery? (Y/N) ")
    delivery = delivery.upper()
    
print()
#Everything else from here calculates and prints out the final bill
print("Here is your final bill")
if pizza_num == 1:
    print("Cost for", pizza_num, "pizza is $%.2f" %(total_pizzaCost))
else:
    print("Cost for", pizza_num, "pizzas is $%.2f" %(total_pizzaCost))

#This checks if the user is eligible for a 15% discount
if pizza_num >= 4:
    total_pizzaCost = discount(total_pizzaCost)
    
total_pizzaCost = deliver(delivery, total_pizzaCost)
total_pizzaCost += HST_calculator(total_pizzaCost)
#And this is the very final statement of the the entire bill and code
print("Your final total is $%.2f" %(total_pizzaCost))




