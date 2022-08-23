categories = [["CatID", "CatName", "CatDescription"], [1, "gameconsoles", "gaming"], [2, "keyboards", "typing"]]
products = [["Pid", "Pname", "Price", "CategoryId"], [1, "nintendo", 50, 1], [2, "logitech", 10, 2],
            [3, "ps4console", 60, 1]]
customers = [["CustId", "CustEmail", "CustPhonenumber", "Address", "Location", "Country"],
             [1, "xxx@gmail.com", "110", "lucky street", "Budapest", "Hungary"],
             [2, "YYY@gmail.com", "210", "unlucky street", "Shaanxi", "China"],
             [3, "ZZZ@gmail.com", "310", "unlucky street", "Shaanxi", "China"]]
orders = [["orderID", "Pid", "Quantity", "TotalPrice", "CustomerId", "Status"]]
orderID = 0
productID = 0
customerID = 0
categoryID = 0


# print menu funciton
def printOpt():
    print("---Welcome to the webshop admin page")
    print("|Type 1 to insert a new record\n" +
          "|Type 2 to edit orders\n" +
          "|Type 3 to print all the data\n" +
          "|Type 4 to print the menu\n" +
          "|Type 5 to get the total sales\n" +
          "|Type 6 to delete items\n" +
          "|Type 7 to quit"
          )


# print the stored data function
def printData(categories, products, customers, orders):
    print("--------Category--------")
    for cat in categories:
        new_cat = [str(i) for i in cat]
        for c in new_cat:
            print(c.center(8), end="  ")
        print()

    print()
    print("--------Products--------")
    for prod in products:
        new_prod = [str(i) for i in prod]
        for p in new_prod:
            print(p.center(8), end="  ")
        print()
    print()
    print("--------Customers--------")
    for cust in customers:
        new_cust = [str(j) for j in cust]
        for u in new_cust:
            print(u.center(8), end="  ")
        print()
    print("-------Orders------")
    for ord in orders:
        new_ord = [str(k) for k in ord]
        for o in new_ord:
            print(o.center(10), end="    ")
        print()
    print()


# insert the category function
def insertCat(categories, CatId):
    CatName = input("Please enter a CatName")
    CatDesc = input("Please enter a Cat Description")
    categories.append([CatId, CatName, CatDesc])
    print("category inserted")


# insert the product funciton
def insertProd(products, categories, productID):
    valid = False
    categoryID_input = input("Please Type a valid category ID ")

    if not categoryID_input.isnumeric():
        print("not a valid input")
    else:
        for cat in categories:
            categoryID = int(categoryID_input)
            if cat[0] == categoryID:
                valid = True
        if not valid:
            print("category ID not found, insertion failed")
        else:
            categoryID = int(categoryID)
            pname = input("Please enter a Product name")
            price_input = input("Please enter a Price")
            if price_input.isnumeric():
                price = int(price_input)
                products.append([productID, pname, price, categoryID])
                print("Product inserted")
            else:
                print("not a valid price")


# insert customer function
def insertCustomer(customers, customerID):
    custEmail = input("Please enter a customer Email")
    custPhone = input("please enter a customer Phone numer")
    if custPhone.isnumeric() == False or len(custPhone) > 10:
        print("not a valid phone number")
    else:
        custAddress = input("Please enter a customer address")
        custLocation = input("Please enter a customer location")
        custCountry = input("please enter a customer country")
        customers.append([customerID, custEmail, custPhone, custAddress, custLocation, custCountry])


# remove element function
def removeEle(list, ID):
    found = False
    for l in list:
        if l[0] == ID:
            list.remove(l)
            found = True
    if found:
        print("successfully deleted")
    else:
        print("item not found")


# place orders function
def placeOrder(customers, products, orders, orderID):
    for prod in products:
        new_prod = [str(i) for i in prod]
        for p in new_prod:
            print(p.center(8), end="  ")
        print()
    print("products above")
    cus_valid = False
    prod_valid = False
    price = 0
    customerId_input = input("please enter the ID of the customer you want to place order for")
    if not customerId_input.isnumeric():
        print("the customer ID you entered is not valid, ID must be numeric")
    else:
        customerId = int(customerId_input)
        for cus in customers:
            #            print(cus[0])
            #           print(type(cus[0]))
            if customerId == cus[0]:
                cus_valid = True
        #    print(cus_valid)
        if not cus_valid:
            print("The customer ID you inserted not exist, insertion failed")
        if cus_valid:
            productId = int(input("please enter the ID of the product you want to order"))
            for prod in products:
                if productId == prod[0]:
                    prod_valid = True
                    price = prod[2]
        # print(price)
        if not prod_valid and prod_valid:
            print("you have entered aN invalid Product ID, insertion failed")
        if cus_valid and prod_valid:
            quantity = int(input("please enter the quantity or the products you would like to order for this customer"))
            TotalPrices = quantity * price
            status = "Preparing"
            orders.append([orderID, productId, quantity, TotalPrices, customerId, status])
            print("ordered successful")


# the function which help to get total sales based on the product ID
def getTotalSalesProd(orders, products):
    print("----products---")
    for prod in products:
        new_prod = [str(i) for i in prod]
        for p in new_prod:
            print(p.center(8), end="  ")
        print()
    print("all products above")

    input_productID = input("Please enter a valid Product ID")
    if not input_productID.isnumeric():
        print("invalid input,please enter a valid number")
    else:
        productID = int(input_productID)
        valid = False
        total = 0
        quantity = 0
        for order in orders:
            if productID == order[1]:
                total += order[3]
                quantity += order[2]
                valid = True
        if valid:
            print(quantity, " pieces of Product ID: ", productID, " has been sold worth-- ", total)
        else:
            print("the entered product ID not found")


# This function returns the corresponding category based on the given product ID
def getCategory(productID, products):
    for prod in products:
        if productID == prod[0]:
            return prod[3]


# This fucntion print the total sales based on the Categories
def getTotalSalesCat(products, orders, categories):
    for cat in categories:
        new_cat = [str(i) for i in cat]
        for c in new_cat:
            print(c.center(8), end="  ")
        print()
    print("all categories above")
    categoryID_input = input("Please enter a valid Category ID")
    if not categoryID_input.isnumeric():
        print("invalid input, the category ID must be a numeric number")
    else:
        categoryID = int(categoryID_input)
        for prod in products:
            quantity = 0
            total = 0
            valid = False
            for order in orders:
                if categoryID == getCategory(order[1], products) and prod[0] == order[1]:
                    total += order[3]
                    quantity += order[2]
                    valid = True
            if valid:
                print("The total price for Product ID ", prod[0], " is ", total, " , total quantity sold is", quantity)

# this fucntion sort the total sales amount for each product in whether ascending or descending order
def getTotalSalesPrice(products, orders):
    temp_input = input(
        "In which order you would like to sort the Products sales, type 1 for higher to lower, type 0 for lower to higher")
    if not temp_input.isnumeric():
        print("invalid input , please enter a valid number")
    else:
        temp = int(temp_input)
        dic = {}
        for prod in products:
            sum = 0
            for order in orders:
                if order[0] == "orderID":
                    continue
                if (order[1] == prod[0]):
                    sum += order[3]
            dic[prod[0]] = sum
        del dic["Pid"]
        if temp == 1:
            new_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            for key, value in new_dic:
                print("Product ID:", key, "Total Proce", value)
        elif temp == 0:
            new_dic = sorted(dic.items(), key=lambda x: x[1])
            for key, value in new_dic:
                print("Product ID:", key, "Total Proce", value)
        else:
            print("not a valid input")


# returns a list contains all the stored locations
def getLocationList(customers):
    location = []
    for cust in customers:
        if cust[4] not in location:
            location.append(cust[4])
    return location


# returns the customer location based on the given Customer ID
def getLocation(customers, customerID):
    for cust in customers:
        if customerID == cust[0]:
            return cust[4]


# print the total sales of different locations
def getTotalSalesLoca(customers, orders):
    location = getLocationList(customers)
    for loc in location:
        sum = 0
        valid = False
        for ord in orders:
            if ord[0] == "orderID":
                continue
            if getLocation(customers, ord[4]) == loc:
                sum += ord[3]
                valid = True
        if valid:
            print("The total price of products sold for location", loc, "is :", sum)


# change order status fuction
def changeOrderStatus(orders):
    orderID_input = input("Please enter a valid order ID you would like to change for")
    if orderID_input.isnumeric():
        found = False
        orderID = int(orderID_input)
        for order in orders:
            if order[0] == orderID:
                statue = input("please enter a number you would like to change for this order(1.shipping 2.delivered")
                if statue == "1":
                    order[5] = "shipping"
                    found = True
                elif statue == "2":
                    order[5] = "delivered"
                    found = True
                else:
                    print("not a valid input")
                    found = True
        if not found:
            print("ID not found")
    else:
        print("the ID you entered is not valid")


# main code
printOpt()
while True:
    option = input("Hi there, Please enter a option, enter 4 to print the menu again")
    if option == "1":
        print("--------New Data-----------")
        print("|Type 1 to insert a new category")
        print("|Type 2 to insert a new product")
        print("|Type 3 to insert a new customer")
        data_type = input("Please select the data type you would like to upload to the system\n")
        if data_type == "1":
            categoryID = len(categories)
            insertCat(categories, categoryID)
        elif data_type == "2":
            productID = len(products)
            insertProd(products, categories, productID)
        elif data_type == "3":
            customerID = len(customers)
            insertCustomer(customers, customerID)
        else:
            print("invalid input, failed to insert new data")
    elif option == "2":
        print("-----Orders-----")
        print("|Type 1 to place new orders")
        print("|Type 2 to change order status")
        orderOpt_input = input("Please Type you choice")
        if orderOpt_input.isnumeric():
            if orderOpt_input == "1":
                print("-------New Order Placement--------")
                orderID = len(orders)
                placeOrder(customers, products, orders, orderID)
            elif orderOpt_input == "2":
                print("--------Order Status Change-----")
                changeOrderStatus(orders)

        else:
            print("invalid input")

    elif option == "3":
        printData(categories, products, customers, orders)
    elif option == "4":
        print("-------Printing Menu---------")
        printOpt()
    elif option == "5":
        print("------Total Sales-----")
        print("|Type 1 to get the total sales based on the given product ID")
        print("|Type 2 to get the total sales based on the given Category ID")
        print("|Type 3 to get the sorted total sales for each product")
        print("|Type 4 to get the total sales based on the locations")
        sales_type = input("Please choose the types of the total sales that can be queried for you:")
        if sales_type == "1":
            getTotalSalesProd(orders, products)
        elif sales_type == "2":
            getTotalSalesCat(products, orders, categories)
        elif sales_type == "3":
            getTotalSalesPrice(products, orders)
        elif sales_type == "4":
            getTotalSalesLoca(customers, orders)
        else:
            print("invalid input, failed to query the total sales")
    elif option == "6":
        print("------Deletion-----")
        print("|Type 1 to delete the category record")
        print("|Type 2 to delete the product record")
        print("|Type 3 to delete the customer record")
        print("|Type 4 to delete the order record")
        deletion = input("Please enter a number to delete the record")
        if deletion == "1":
            categoryID_input = input("Please enter the category ID you would like to delete")
            if categoryID_input.isnumeric():
                categoryID = int(categoryID_input)
                removeEle(categories, categoryID)
                for prod in products:
                    if prod[3] == categoryID:
                        products.remove(prod)

            else:
                print("Please input a valid ID number")
        elif deletion == "2":
            productID_input = input("Please enter the product ID you would like to delete")
            if productID_input.isnumeric():
                productID = int(productID_input)
                removeEle(products, productID)

            else:
                print("Please input a valid ID number")
        elif deletion == "3":
            customerID_input = input("Please enter the customer ID you would like to delete")
            if customerID_input.isnumeric():
                customerID = int(customerID_input)
                removeEle(customers, customerID)
            else:
                print("Please input a valid ID number")
        elif deletion == "4":
            orderID_input = input("Please enter the order ID you would like to delete")
            if orderID_input.isnumeric():
                orderID = int(orderID_input)
                removeEle(orders, orderID)
            else:
                print("Please input a valid ID number")
        else:
            print("not a valid input")
    elif option == "7":
        break
    else:
        print("not a valid input")
