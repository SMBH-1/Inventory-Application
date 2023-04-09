from classes.store import Store

store = Store('Sierra Video') #Store class initialized

while True:
  user_input = input("""
  ==  Welcome to Sierra Video!  ==
  =  The Last Blockbuster Store  =
  
  1. View store video inventory
  2. View store customers
  3. View customer rented videos
  4. Add new customer
  5. Rent video
  6. Return video
  7. Exit
  ```
  """)

  match user_input:
    case "1": #Calls current inventory from store class
      current_inventory = store.list_inventory()
      for item in current_inventory:
        print(item)
    
    case "2": #Calls current customer list from store class
      customer_list = store.list_customers()
      for customer in customer_list:
        print(customer)

    case "3": #Finds customer in system through store class
      while True:
        relayed_id = input("Please enter a customer id: ")
        customer = store.find_customer(relayed_id)
        print(customer)
        if relayed_id == 'exit':
          break

    case "4": #Adds new customer using methods from store class
      customer_info = {}
      customer_list = store.list_customers()
      customer_info['id'] = len(customer_list)+1
      customer_info['account_type'] = input("Enter the type of account:\n'sx' (standard)\n'px' (premium)\n'sf' (standard family)\n'pf' (premium family)\n")
      customer_info['first_name'] = input("Enter new account holder's first name: ")
      customer_info['last_name'] = input("Enter new account holder's last name: ")
      customer_info['current_video_rentals'] = ''
      print(store.add_new_customer(customer_info))
      
    case "5": #Rents video by calling store class method
      movie_to_rent = input("Enter the name of movie to rent: ")
      entered_id = input("Enter the id of customer to rent: ")
      
      store.rent_movie(movie_to_rent, entered_id)

    case "6": #Returns video by calling store class method
      movie_to_return = input("Enter the name of movie to return: ")
      entered_id = input("Enter the id of customer returning movie: ")
      
      store.return_movie(movie_to_return, entered_id)

    case "7":
      exit()