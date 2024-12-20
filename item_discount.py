cart_items = {'Laptop': 51000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
def totalPrice():
    if len(cart_items) == 0:
        print("The cart is empty!")
        return
    total = 0
    for item, price in cart_items.items():
        if price > 50000: 
            price *= 0.85
        elif 20000 <= price <= 50000:  
            price *= 0.90
        total += price
    print("Total Price:", total)
totalPrice()