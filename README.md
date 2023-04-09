# Inventory Application
Manages customer and inventory information using Python, Django, and PostgreSQL/CSV files



Application manages: 

1) Customer Data: 
    * customer's ID
    * customer's account type
    * customer's name
    * customer's current rentals

2) Store Inventory Data:
    * video ID
    * video title
    * video rating
    * video release year
    * number of copies per title
 
Application Menu: 
1. Viewing current store inventory (shows titles and copies available)

2. Viewing all customers (shows customer_id and name)

3. Viewing a customer's current rented videos (takes in customer ID and outputs current rented videos for that customer)

4. Adding a new customer

5. Renting a video out to a customer (input video title and customer ID; limited based on customer account type)

6. Returning a video from a customer (input video title and customer ID)

7. Exiting the application
