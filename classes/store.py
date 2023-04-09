from classes.customer import Customer
from classes.inventory import Inventory
import csv
import os

csv_customer_path = os.path.abspath("data/customers.csv")
csv_inventory_path = os.path.abspath("data/inventory.csv")
empty_list = []

class Store: #The store class imports from customer and inventory classes and builds all the relevant methods for running the Blockbuster store menu
  
  def __init__(self, name):
    self.name = name
    self.customers = Customer.load_customer_data()
    self.inventory = Inventory.load_inventory_data()

  def list_customers(self): #Calls the load_customer_data method from Customer class   
    return self.customers
  
  def list_inventory(self): #Calls the load_inventory_data method from Inventory class
    return self.inventory

  def find_customer(self, id): #Searches customer database to see if there is a record
    counter = 0
    for customer in self.customers:
      if customer.id == id:
        counter += 1
        return f"Customer: {customer.first_name} {customer.last_name}\nMovie(s) Currently Rented: {customer.current_video_rentals.replace('/', ', ')}"
    if counter == 0:
        return "There was no customer found with that id. Please enter a different id number or type 'exit' to go back to main menu."
  
  def add_new_customer(self, customer_info): #Takes in new customer info thru runner and uses add_customer_to_csv method below
    new_customer = Customer(**customer_info)
    self.customers.append(new_customer)
    self.add_customer_to_csv(customer_info)
    return '\nNew customer successfully added.'

  def add_customer_to_csv(self, customer_dictionary): #Adds new customer directly to CSV
    with open(csv_customer_path, 'a') as csv_file:
      field_names = ['id', 'account_type', 'first_name', 'last_name', 'current_video_rentals']
      csv_writer = csv.DictWriter(csv_file, fieldnames = field_names, delimiter = ',')
      csv_writer.writerow(customer_dictionary)
  
  def add_to_customer_rentals(self, id, title): #Adds to customer's rental list
    for customer in self.customers:
      if customer.id == id:
        customer_inventory = customer.current_video_rentals.split('/')
        customer_inventory.append(title)
        customer_inventory = '/'.join(customer_inventory)
        print(f"{customer.first_name} {customer.last_name} rented {title}")

  def remove_from_inventory(self, title): #Removes movie from store's inventory
    for item in self.inventory:
      if item.title == title:
        item.copies_available = str(int(item.copies_available) - 1)
        return item

  def remove_from_customer_rentals(self, title, id): #Removes returned movie from customer's rental list
    for customer in self.customers:
      if customer.id == id:
        customer_inventory = customer.current_video_rentals.split('/')
        print(customer_inventory)
        customer_inventory.remove(title)    
        customer_inventory = '/'.join(customer_inventory)
        print(customer_inventory)
        print(f"{customer.first_name} {customer.last_name} returned {title}")

  def add_to_inventory(self, title): #Adds returned movie back to store's inventory
    for item in self.inventory:
      if item.title == title:
        item.copies_available = str(int(item.copies_available) + 1)
        print(f'{item.title} was added back to Sierra Video inventory.')

  def rent_movie(self, title, id):
    #Method checks to see if 1) requested movie is available for rent 2) customer's rental account has room for more movies and 3) if customer's account has any ratings restrictions
    #Only when all three criteria are met does rent_movie call for the respective remove and add methods listed above

    item_counter = 0
    for item in self.inventory:
      if item.title == title and int(item.copies_available) > 0:
        item_counter += 1
        movie_rating = item.rating
    if item_counter == 0 or item.copies_available == 0:
        print("The requested movie is not available at our store.")

    for customer in self.customers:
      if customer.id == id:
        movies_rented = len(list(filter(None, customer.current_video_rentals.split('/')))) #Takes the string of movies for customer and converts to list length for total movie count
        if customer.account_type == 'sx' and movies_rented == 0:
          self.remove_from_inventory(title)
          self.add_to_customer_rentals(id, title)
        if customer.account_type == 'px' and movies_rented < 3:
          self.remove_from_inventory(title)
          self.add_to_customer_rentals(id, title)
        if customer.account_type == 'sf' and movies_rented == 0:
          if movie_rating != 'R': #Family account ('standard family') cannot rent R movie
            self.remove_from_inventory(title)
            self.add_to_customer_rentals(id, title)
          else:
            print("You have a family account. You cannot rent R-rated movies.")
        if customer.account_type == 'pf' and movies_rented < 3:
          if movie_rating != 'R': #Family account ('premium family') cannot rent R movie
            self.remove_from_inventory(title)
            self.add_to_customer_rentals(id, title)
          else:
            print("You have a family account. You cannot rent R-rated movies.")
    else:
      print("You have reached your rental limit. If you don't have a premium account, consider upgrading.\nOtherwise, please return a movie before attempting to rent a different one.")


  def return_movie(self, title, id): #Method to return movie that calls above remove/add methods to adjust inventories
    self.remove_from_customer_rentals(title, id)
    self.add_to_inventory(title)