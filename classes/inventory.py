import csv
import os

class Inventory (): #Inventory class to keep track of store's current movie inventory
  def __init__(self, **kwargs):
    self.id = kwargs['id']
    self.title = kwargs['title']
    self.rating = kwargs['rating']
    self.release_year = kwargs['release_year']
    self.copies_available = kwargs['copies_available']

  def __str__(self):
    return f"Movie: {self.title.title()}\nCopies Available: {self.copies_available}\n"

  @classmethod
  def load_inventory_data(cls): #Class method to load inventory data in store class methods
    current_inventory = []
    path = os.path.abspath("data/inventory.csv")
    with open(path, 'r') as csv_file:
      file_reader = csv.DictReader(csv_file)
      for row in file_reader:
        current_inventory.append(Inventory(**dict(row)))
      return current_inventory