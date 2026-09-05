# ===== INVENTORY MANAGEMENT SYSTEM =====

# 1. Add Product
# 2. View All Products
# 3. Search Product
# 4. Add Stock
# 5. Remove Stock
# 6. Update Product
# 7. Delete Product
# 8. Check Low Stock
# 9. Exit

print('===== INVENTORY MANAGEMENT SYSTEM =====')
print('1. Add Product')
print('2. View All Products')
print('3. Search Product')
print('4. Add Stock')
print('5. Remove Stock')
print('6. Update Product')
print('7. Delete Product')
print('8. Check Low Stock')
print('9. Exit')

import random
inventory_data={}
while True:
    option =input("Enter Option (Add product, View, Search ,Add stock, Remove stock, Update , Delete ,Check low stock, Exit) :").strip().lower()
    if option == "add product":
        prod_name=input("Enter Product name :").lower()
        category=input("Enter Category of Product :").lower()
        price=float(input("Enter price of Product :"))
        Quantity=float(input("Enter Product Quantity :"))
        Supplier=input("Enter Supplier Company name:").lower()
        product_id=random.randint(10000, 19999)
        print(f"This prodect ID numbers :{product_id}")

        inventory_data[product_id]={
            'Product_Name':prod_name,
            'Product_category':category,
            "Product_price":price,
            "Product_quantity":Quantity,
            "Product_Supplier":Supplier,
        }


        with open("inventory_view.text",'a') as file:
            file.write(f'{product_id} {5 * ' '} {prod_name} {10 * ' '} {category} {10 * ' '} {price} {10 * ' '} {Quantity}\n')

    elif option == 'view':
            print(inventory_data)
    elif option == 'search':
        print("Search by:")
        print('1. Product ID')
        print('2. Product Name')
        print("3. Category")

        choices=input("Enter Choices (1,2,3) :")
        if choices == '1':
            input_id=int(input("Enter Product ID to search :"))
            if input_id in inventory_data:
                print(inventory_data[input_id])
            else:
                print("Product ID not Found Try again!")
        elif choices == '2':
            Name=input("Enter Product name to find :").lower()
            for product_id,product in inventory_data.items():
                if product['Product_Name'] == Name :
                    print(f"Product name: {Name}")
                    print(f'Product category :{product['Product_category']}')
                    print(f'Product price :{product['Product_price']}')
                    print(f'Product quantity :{product['Product_quantity']}')
                    print(f"Product Id :{product_id}")
                else:
                    pass
        elif choices == '3':
            Cate=input("Enter Product Category to find :")
            for product_id,product in inventory_data.items():
                if product['Product_category'] == Cate :
                    print(f"Product name: {product['Product_Name']}")
                    print(f'Product category :{product['Product_category']}')
                    print(f'Product price :{product['Product_price']}')
                    print(f'Product quantity :{product['Product_quantity']}')
                    print(f"Product Id :{product_id}")
        else:
            print("Enter only numbers")
            continue
    elif option == 'add stock':
        ask=int(input("Enter Product Id Numbers:"))
        if ask in inventory_data:
            print("Product Found")
            stock=int(input("Enter Quantity to add :"))
            inventory_data[ask]['Product_quantity'] =inventory_data[ask]['Product_quantity'] + stock
            print(F"Curent product qunatity :{inventory_data[ask]['Product_quantity']}")
            print("Stock add succesfull")
        else:
            print("Product Id Numbers not found try again!")
    elif option == 'remove stock':
        ask=int(input("Enter Product Id Numbers:"))
        if ask in inventory_data:
            print("Product Found")
            remove=int(input("Enter  Quantity to remove :"))
            if inventory_data[ask]['Product_quantity'] >= remove:
                inventory_data[ask]['Product_quantity'] = inventory_data[ask]['Product_quantity'] - remove
                print(F"Curent product qunatity :{inventory_data[ask]['Product_quantity']}")
                print("Stock remove succesfull")
            else:
                print('Not enough stock')
                print(f"Available quantity:{inventory_data[ask]['Product_quantity']}")
                continue
        else:
            print("Product Id Numbers not found try again!")

    elif option == 'update':
        ask=int(input("Enter Product Id Numbers:"))
        if ask in inventory_data:
            print("Product Found")
            try:
                prod_name=input("Enter Product name to update:").lower()
                category=input("Enter Category of Product to update:").lower()
                price=float(input("Enter price of Product to update:"))
                Quantity =inventory_data[ask]['Product_quantity']
                Supplier=input("Enter Supplier Company name:").lower()
                product_id=ask
            except ValueError:
                inventory_data[product_id]={
                    'Product_Name':prod_name,
                    'Product_category':category,
                    "Product_price":price,
                    "Product_quantity":Quantity,
                    "Product_Supplier":Supplier,
                }

                with open("inventory_view.text",'a') as file:
                    file.write(f'{product_id} {6 * ' '} {prod_name} {8 * ' '} {category} {8 * ' '} {price} {9 * ' '} {Quantity}\n')
                print('Inventory Update succesfull')
        else:
            print("Product Id Numbers not found try again!")

    elif option == 'delete':
        ask=int(input("Enter Product Id Numbers:"))
        if ask in inventory_data:
            print("Product Found")
            say =str(input("Are you sure you want to delete this product? YES/NO :")).lower()
            if say == "yes":
                if inventory_data[ask]['Product_quantity'] == 0:
                    del inventory_data[ask]
                    print("Product delete Succesfull")
                else:
                    print("You can not delete a product if it still has stock.")
                    print(f'Quantity :{inventory_data[ask]['Product_quantity']}')
            else:
                print("Deletion cancelled")
        else:
            print("Product Id Numbers not found try again!")

    elif option == 'check low stock':
        low_stock_limit =int(input("Enter low-stock limit eg(10):"))
        for product_id,product in inventory_data.items():
            if product['Product_quantity'] <= low_stock_limit:
                print("low-stock product")
                print(product['Product_Name'],product['Product_quantity'])
            else:
                print("No Low-Stock product found")
                break

    elif option == 'exit':
        break
    else:
        print("Invaild option try again!")
        continue