#Assessment Task 1: Input Product Details with Required Data Types
#Assessment Task 2: Output with Formatting
# Taking Blink-it real time application

# Task 1: Collect the product details 

#1.Product ID 
product_id = int(input("Enter Product ID: "))

#2.Product Name 
product_name = input("Enter Product Name: ")

#3.Price
price = float(input("Enter Product price (₹): "))

#4. Categories
categories_input = input("Enter Categories (comma separated):  ")
categories = categories_input.split(",") #List 

#5. Stock Details
available_stock = int(input("Enter available stock: "))
sold_items = int(input("Enter sold items: "))
stock_details = (available_stock, sold_items) #tuple

#6. Discount Percentage 
discount = float(input("Enter Discount Percentage: "))

#7. Product Features 
features_input = input("Enter Product Features (comma separated): ")
product_features = set(features_input.split(',')) # set 

# 8. Supplier details 
supplier_name = input("Enter Supplier name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "name" : supplier_name,
    "contact" : supplier_contact,
    "location" : supplier_location

} # dict 

# Task 2: Display Using Formatting

print("\n--- Product Details ---")

# Comma Separation (sep=)
print("Product ID",product_id,"Product Name",product_name,sep = ",")

# Percentage Formatting
print("Price: ₹%.2f" % price)
print("Discount: %.1f%%" % discount)

# f-string 
print(f"Categories: {categories}")
print(f"Stock - Available: {stock_details[0]}, Sold: {stock_details[1]}")
print(f"Product Features: {product_features}")
print(f"Supplier: {supplier_details['name']} | Contact: {supplier_details['contact']} | Location: {supplier_details['location']}")

#.format() method 
print("Final Price after disount: ₹{:.2f}".format(price * (1 - discount/100)))