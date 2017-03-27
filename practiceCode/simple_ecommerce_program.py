cart = []
shopping_status = False
total = 0
products = {
    '101': {'name': 'Shirt', 'price': 500},
    '102': {'name': 'Jeans', 'price': 700},
    '103': {'name': 'Mobile', 'price': 800},
    '104': {'name': 'Gadget', 'price': 1000},
    '105': {'name': 'Shoes', 'price': 690},
    '106': {'name': 'Watch', 'price': 350},
    '107': {'name': 'Belt', 'price': 850},
    '108': {'name': 'Wallet', 'price': 570},
    '109': {'name': 'Trouser', 'price': 880},
    '110': {'name': 'Shorts', 'price': 420},
}

print("============================================Welcome to HarMaal Shopping Site=======================================")
print("We offers these items")
print("Code\t\t\tProduct Name\t\t\tPrice")

for key,value in products.items():
    print(key+'\t\t\t\t\t'+value['name']+'\t\t\t\t'+str(value['price']))

print("\nInstructions:\n1.Enter Code of an item which you want to buy")
print("2.When will you complete your shopping type bill to take your bill\n")

while shopping_status == False:
    item = input("\nEnter Code of an item which you want to buy?")
    if item == 'q':
        shopping_status = True
    elif item == 'bill':
        print("\nDear customer you bought these items:")
        for items in cart:
            print("%s Rs.%d "%(products[items]['name'], products[items]['price']))
            total = total + products[items]['price']
        print("Your total amount is %sRs."%total)
        shopping_status = True
    else:
        if item in products:
            cart.append(item)
        else:
            print("This product is not in our stock")
