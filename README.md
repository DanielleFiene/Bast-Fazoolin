# Bast-Fazoolin
Restaurant Management System

Overview
This project is a restaurant management system implemented in Python. It defines a simple framework for managing restaurant menus, franchises, and businesses. The system allows for creating different types of menus, associating them with franchises, and managing multiple franchises under a single business.

Classes
Menu
Represents a menu at a restaurant. Each menu has:

name: The name of the menu (e.g., "brunch", "dinner").
items: A dictionary where keys are item names and values are their prices.
start_time: The start time when the menu becomes available (in 12-hour format).
end_time: The end time when the menu is no longer available (in 12-hour format).
Methods
__repr__(): Returns a string describing the menu's availability.
calculate_bill(purchased_items): Calculates the total bill for a list of purchased items.
Franchise
Represents a franchise of a restaurant business. Each franchise has:

address: The address of the franchise.
menus: A list of Menu objects available at the franchise.
Methods
__repr__(): Returns a string with the address of the franchise.
available_menus(time): Returns a list of menus available at a given time.
Business
Represents a business that can have multiple franchises. Each business has:

name: The name of the business.
franchises: A list of Franchise objects associated with the business.
Methods
__repr__(): Returns a string with the business name and the list of franchises.
