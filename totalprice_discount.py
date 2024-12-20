cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500, 'Charger': 1000, 'Pendrive': 900}
def totalPrice():
    if len(cart_items) == 0:
        print("The cart is empty!!")
        return
    total = sum(cart_items.values())
    if total >= 20000 and total <= 50000:
        total *= 0.9
        print("Total Price after 10% discount: ", total)
    elif total > 50000:
        total -= (total * 0.15)
        print("Total Price after 15% discount: ", total)
    else:
        print("Total Price: ", total)
totalPrice()