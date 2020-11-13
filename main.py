# Anthony Clark
# CS 30
# November 9th, 2020
# RPG Numerical Lists


# Print Numerical list
def printInvNumerical(inv, title):
    print(title)
    for i, item in enumerate(inv):
        print(f'{i + 1}: {item.title()}')


# initilize inventories
weapons = []
consumables = []

# add items
for item in ['sword', 'bow', 'dagger']:
    weapons.append(item)
for item in ['health potion', 'sandwich', 'magic scroll', 'water bottle']:
    consumables.append(item)

# Print inventories numerically
printInvNumerical(weapons, 'Weapons')
print()
printInvNumerical(consumables, 'Consumables')
