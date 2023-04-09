import csv
import os
class Customer(): #Customer class to keep track of store's customer database
  def __init__(self, **kwargs):
    self.id = kwargs['id']
    self.account_type = kwargs['account_type']
    self.first_name = kwargs['first_name']
    self.last_name = kwargs['last_name']
    self.current_video_rentals = kwargs['current_video_rentals']
    
  def __str__(self):
    return f"Customer ID: {self.id}, Name: {self.first_name} {self.last_name}"

  @classmethod
  def load_customer_data(cls): #Class method to load customer data in store class methods
    customer_list = []
    path = os.path.abspath("data/customers.csv")
    with open(path, 'r') as csv_file:
      file_reader = csv.DictReader(csv_file)
      for row in file_reader:
        customer_list.append(Customer(**dict(row)))
      return customer_list