item = input("What would you like to buy: ")
quantity = int(input("How many of them you wanna buy: "))
price = float(input("What is the price of the item: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your Total is ${total:.2f}.")