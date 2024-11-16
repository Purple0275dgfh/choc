#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sqlite3

def create_tables():
    conn = sqlite3.connect('chocolate_shop.db')
    cursor = conn.cursor()
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS Flavors (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,is_seasonal BOOLEAN NOT NULL,available_stock INTEGER NOT NULL
                    );''')
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS Ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,quantity INTEGER NOT NULL
                    );''')
    
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS Customer_Feedback (id INTEGER PRIMARY KEY AUTOINCREMENT,suggestion TEXT NOT NULL,allergy_concerns TEXT,
                        date TEXT NOT NULL);''')

    conn.commit()
    conn.close()


        
def add_flavor():
    conn = sqlite3.connect('chocolate_shop.db')
    cursor = conn.cursor()

    name = input("Enter the flavor name: ")
    is_seasonal = input("Is it seasonal (yes/no): ").lower() == 'yes'
    stock = int(input("Enter available stock: "))

    cursor.execute("INSERT INTO Flavors (name, is_seasonal, available_stock) VALUES (?, ?, ?)",(name, is_seasonal, stock))
    conn.commit()
    conn.close()

    print("Seasonal Flavor '{}' added with stock {}.".format(name, stock))


def manage_ingredient_inventory():
    conn = sqlite3.connect('chocolate_shop.db')
    cursor = conn.cursor()

    print("\n1. Add new ingredient")
    print("2. Update existing ingredient quantity")
    print("3. View ingredients")

    choice = input("Choose an option: ")

    if choice == '1':
        ingredient_name = input("Enter  name: ")
        ingredient_quantity = int(input("Enter  quantity: "))
        
        cursor.execute("INSERT INTO Ingredients (name, quantity) VALUES (?, ?)",(ingredient_name, ingredient_quantity))
        conn.commit()
        print("Ingredient '{}' added with quantity {}.".format(ingredient_name, ingredient_quantity))

    elif choice == '2':
        ingredient_name = input("Enter ingredient name to update: ")
        new_quantity = int(input("Enter the new quantity: "))
        
        cursor.execute("UPDATE Ingredients SET quantity = ? WHERE name = ?",
                       (new_quantity, ingredient_name))
        conn.commit()
        print("Ingredient '{}' updated to quantity {}.".format(ingredient_name, new_quantity))

    elif choice == '3':
        cursor.execute("SELECT * FROM Ingredients")
        ingredients = cursor.fetchall()
        
        if ingredients:
            for ingredient in ingredients:
                print("ID: {} | Name: {} | Quantity: {}".format(ingredient[0], ingredient[1], ingredient[2]))
        else:
            print("No ingredients found.")

    conn.close()


def add_customer_feedback():
    conn = sqlite3.connect('chocolate_shop.db')
    cursor = conn.cursor()

    suggestion = input("Enter your flavor suggestion: ")
    allergy = input("Any allergy? (none,blank): ")
    

    cursor.execute("INSERT INTO Customer_Feedback (suggestion, allergy) VALUES (?, ?, ?)",
                   (suggestion, allergy))
    conn.commit()
    conn.close()

    print(" Your suggestion '{}' has been submitted.".format(suggestion))


def view_customer_feedback():
    conn = sqlite3.connect('chocolate_shop.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Customer_Feedback")
    feedbacks = cursor.fetchall()

    if feedbacks:
        for feedback in feedbacks:
            print("ID: {} | Suggestion: {} | Allergy: {} ".format(feedback[0], feedback[1], feedback[2]))
    else:
        print("No feedback available.")

    conn.close()


def main():
    create_tables()  

    while True:
        print("\nChocolate Shop Management")
        
        print("1. View Seasonal Flavors")
        
        print("2. Add New Seasonal Flavor")
        
        print("3. Manage Ingredient Inventory")
        
        print("4. Add Customer Feedback")
        
        print("5. Exit")
        
        choice = input("Choose option: ")
        

        if choice == '1':
            conn = sqlite3.connect('chocolate_shop.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Flavors WHERE is_seasonal = 1")
            seasonal_flavors = cursor.fetchall()
            
            if seasonal_flavors:
                for flavor in seasonal_flavors:
                    print("{}. {} - Stock: {}".format(flavor[0], flavor[1], flavor[3]))
            else:
                print("No seasonal.")
            conn.close()

        elif choice == '2':
            add_flavor()

        elif choice == '3':
            manage_ingredient_inventory()

        elif choice == '4':
            print("\n1. View ")
            print("2. Add ")
            
            feedback_choice = input("Choose an option: ")
            if feedback_choice == '1':
                view_customer_feedback()
                
            elif feedback_choice == '2':
                add_customer_feedback()

        elif choice == '5':
            print("THank YOu")
            break
            

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




