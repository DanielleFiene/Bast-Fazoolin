# Define the Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
        self.representative_string = f'{self.name} menu is available from {self.start_time} to {self.end_time}'

    def __repr__(self):
        return self.representative_string
    
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
            else:
                print(f"Warning: {item} is not on the menu.")
        return total

# Define the Franchise class
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f'Franchise located at: {self.address}'
    
    def available_menus(self, time):
        def time_to_int(t):
            parts = t.split()
            if len(parts) == 2:
                hour, period = parts
                hour, minute = map(int, hour.split(':'))
                if period == 'pm' and hour != 12:
                    hour += 12
                if period == 'am' and hour == 12:
                    hour = 0
                return hour * 100 + minute
            return 0

        time_int = time_to_int(time)
        available_menus = []

        for menu in self.menus:
            start_time_int = time_to_int(menu.start_time)
            end_time_int = time_to_int(menu.end_time)
            if start_time_int <= time_int <= end_time_int:
                available_menus.append(menu)

        return available_menus

# Define the Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return f'Business name: {self.name}, Franchises: {self.franchises}'

# Create instances of Menu for each menu type
brunch = Menu(
    name="brunch",
    items={'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},
    start_time="11am",
    end_time="4pm"
)

early_bird = Menu(
    name="early bird",
    items={'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushrooms ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00},
    start_time="3pm",
    end_time="6pm"
)

dinner = Menu(
    name="dinner",
    items={'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom raviolo (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00},
    start_time="5pm",
    end_time="11pm"
)

kids = Menu(
    name="kids",
    items={'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},
    start_time="11am",
    end_time="9pm"
)

# Create the arepas_menu instance
arepas_menu = Menu(
    name="Arepas",
    items={
        'arepa pabellon': 7.00,
        'pernil arepa': 8.50,
        'guayanes arepa': 8.00,
        'jamon arepa': 7.50
    },
    start_time="10am",
    end_time="8pm"
)

# Create Franchise instances with addresses and all menus
flagship_store = Franchise(
    address="1232 West End Road",
    menus=[brunch, early_bird, dinner, kids]
)

new_installment = Franchise(
    address="12 East Mulberry Street",
    menus=[brunch, early_bird, dinner, kids]
)

# Create the arepas_place Franchise instance
arepas_place = Franchise(
    address="189 Fitzgerald Avenue",
    menus=[arepas_menu]
)

# Create the Business instances
basta_fazoolin = Business(
    name="Basta Fazoolin' with my Heart",
    franchises=[flagship_store, new_installment]
)

take_a_arepa = Business(
    name="Take a' Arepa",
    franchises=[arepas_place]
)

# Print the Business objects to verify
print(basta_fazoolin)
print(take_a_arepa)

# Test the available_menus method
print("Menus available at 3pm at flagship store:")
for menu in flagship_store.available_menus("3pm"):
    print(menu)

print("\nMenus available at 5pm at new installment:")
for menu in new_installment.available_menus("5pm"):
    print(menu)
