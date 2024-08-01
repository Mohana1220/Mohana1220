menu = {
    'Pasta': 50,
    'Pizza': 60,
    'Coffee': 70,
    'Idly': 40,
    'Dosa': 50,
    'Vada': 55
}
print('Welcome to the ML Restaurant!')
print(' Pasta:Rs 50\n Pizza:Rs 60\n Coffee:Rs 70\n Idly:Rs 40\n Dosa:Rs 50\n Vada:Rs 55')
ordered_items = 0
order = input('Would you like to order anything?  (Y/N)')
if order == 'Y':
    item_1 = input('Enter the name of your item')
    ordered_items += menu[item_1]
    print(f"your item {item_1} is added to your order")
else:
    print('Ordered item not in the menu')
another_order = input('Do you want add any other items? (Y/N)')
if another_order == 'Y':
    item_2 = input('Enter the name of your item')
    ordered_items += menu[item_2]
    print(f"your item {item_2} is added to your order")
else:
    print('Ordered item not in the menu')

print(f'Total ordered_items {ordered_items}')

