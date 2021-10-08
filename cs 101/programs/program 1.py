#Jacob Frank, session 0002, Program #1

#getting the values of all the ingredients for each recipe set
recipe_cookies = {'butter':2.5, 'sugar':2, 'eggs':2, 'flour':8}
recipe_cake = {'butter':0.5, 'sugar':1, 'eggs':2, 'flour':1.5}
recipe_donuts = {'butter':0.25, 'sugar':0.5, 'eggs':3, 'flour':5}

print('Welcome to TOGO Bakery\n')
#asking for how many of each thing they are wanting to make
num_cookies = int(input('How many dozen cookies? => '))
num_cakes = int(input('\nHow many cakes? => '))
num_donuts = int(input('\nHow many dozen donuts? => '))
print()
#getting all the calculations done beforehand for readability
cups_butter = (recipe_cookies['butter'] * num_cookies) + (recipe_cake['butter'] * num_cakes) + (recipe_donuts['butter'] * num_donuts)
cups_sugar = (recipe_cookies['sugar'] * num_cookies) + (recipe_cake['sugar'] * num_cakes) + (recipe_donuts['sugar'] * num_donuts)
cups_eggs = (recipe_cookies['eggs'] * num_cookies) + (recipe_cake['eggs'] * num_cakes) + (recipe_donuts['eggs'] * num_donuts)
cups_flour = (recipe_cookies['flour'] * num_cookies) + (recipe_cake['flour'] * num_cakes) + (recipe_donuts['flour'] * num_donuts)

#printing the recipe
print('\nYou will need to order')
print('{:.1f} cups of butter'.format(cups_butter))
print('{:.1f} cups of sugar'.format(cups_sugar))
print('%d eggs'%cups_eggs)
print('{:.1f} cups of flour'.format(cups_flour))
