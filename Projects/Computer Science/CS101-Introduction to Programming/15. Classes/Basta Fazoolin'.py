# Making the Menus

# create a `Menu` class - Task 1
class Menu:
  # give `Menu` a constructor with five parameters - Task 2
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  # give Menu class a string representation method - Task 7
  def __repr__(self):
    return '{} menu available from {} to {}'.format(self.name, self.start_time, self.end_time)

  # calculate_bill method - Task 9
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

# create `Menu` object or instance of class `Menu` - Task 3
# Brunch Menu
brunch_items = {
'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu('brunch', brunch_items, 1100, 1600)

# Early bird Menu - Task 4
early_bird_items = {
'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('early_bird', early_bird_items, 1500, 1800)

# Dinner Menu - Task 5
dinner_items = {
'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('dinner', dinner_items, 1700, 2300)

# Kids Menu - Task 6
kids_items = {
'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('kids', kids_items, 1100, 2100)

# Call print(brunch) - Task 8
print(brunch_menu)
# calculate total price of purchase - Test Task 10
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

# calculate bill about early_bird purchase - Task 11
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Creating the Franchises

# create `Franchise` class _ Task 12
class Franchise:
  # constructor for `Franchise` class - Task 13
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  # gives `Franchise` a string representation - Task 15
  def __repr__(self):
    return self.address

  # give `Franchise` an available_menus() method - Task 16
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
    
# create first two franchise - Task 14 
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

# test available_menus() method - Task 17
print(flagship_store.available_menus(1200))

# test available_menus() method - Task 18
print(flagship_store.available_menus(1700))

# Creating Businesses!

# create `Business` class - Task 19
class Business:
  # constructor for `Business` class - Task 20
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# create first `Business` - Task 21
business_value = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# create `arepas_menu` - Task 22
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

# create first Arepa franchise
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)



