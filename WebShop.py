categories = [["CatID","CatName","CatDescription"],[1,"gameconsoles","gaming"],[2,"keyboards","typing"]]
products = [["Pid","Pname","Price","CategoryId"],[1,"nintendo",50,1],[2,"logitech",10,2],[3,"ps4console",60,1]]
customers = [["CustId","CustEmail","CustPhonenumber","Address","Location","Country"],
             [1,"xxx@gmail.com","110","lucky street","Budapest","Hungary"],
             [2,"YYY@gmail.com","210","unlucky street","Shaanxi","China"],
             [3,"ZZZ@gmail.com","310","unlucky street","Shaanxi","China"]]
orders = [["orderID","Pid","Quantity","TotalPrice","CustomerId","Status"]]
orderID = 0
productID =0
customerID =0
categoryID = 0

#print menu funciton
def printOpt():
    print("---Welcome to the webshop admin page")
    print("|Type 1 to insert a new category\n"+
          "|Type 2 to insert a new Product\n"+
          "|Type 3 to insert a new Customer\n"+
          "|Type 4 to place a new order\n"+
          "|Type 5 to print all the data\n"+
          "|Type 6 to print the menu\n"+
          "|Type 7 to enter a product ID and get the total sales based on that\n"
          "|Tyoe 8 to get the total sales based on category \n"
          "|Type 9 to get the total sales based on the price range\n"
          "|Type 10 to get the total sales based on the location\n"
          "|Type 11 to quit"
          )

#print the stored data function
def printData(categories,products,customers,orders):
    print("--------Category--------")
    for cat in categories:
        new_cat=[str(i) for i in cat]
        for c in new_cat:
            print(c.center(8),end="  ")
        print()

    print()
    print("--------Products--------")
    for prod in products:
        new_prod=[str(i) for i in prod]
        for p in new_prod:
            print(p.center(8),end="  ")
        print()
    print()
    print("--------Customers--------")
    for cust in customers:
        new_cust = [str(j) for j in cust]
        for u in new_cust:
            print(u.center(8),end="  ")
        print()
    for ord in orders:
        new_ord = [str(k) for k in ord]
        for o in new_ord:
            print(o.center(10),end="    ")
        print()
    print()

#insert the category function
def insertCat(categories,CatId):
    CatName = input("Please enter a CatName")
    CatDesc = input("Please enter a Cat Description")
    categories.append([CatId,CatName,CatDesc])
    print("category inserted")

#insert the product funciton
def insertProd(products,categories,productID):
    valid = False
    categoryID = input("Please Type a valid category ID ")

    for cat in categories:
#        print(cat[0])
 #       print(type(cat[0]))
        if cat[0] == categoryID:
            valid=True
    if not valid:
        print("category ID not found, insertion failed")
    else:
        categoryID = int(categoryID)
        pname = input("Please enter a Product name")
        price = int(input("Please enter a Price"))
        products.append([productID,pname,price,categoryID])
        print("Product inserted")

#insert customer function
def insertCustomer(customers,customerID):
    custEmail = input("Please enter a customer Email")
    custPhone = input("please enter a customer Phone numer")
    custAddress = input("Please enter a customer address")
    custLocation = input("Please enter a customer location")
    custCountry = input("please enter a customer country")
    customers.append([customerID,custEmail,custPhone,custAddress,custLocation,custCountry])

#place orders function
def placeOrder(customers,products,orders,orderID):
    for prod in products:
        new_prod=[str(i) for i in prod]
        for p in new_prod:
            print(p.center(8),end="  ")
        print()
    print("products above")
    cus_valid = False
    prod_valid = False
    price = 0
    customerId = int(input("please enter the ID of the customer you want to place order for"))
    for cus in customers:
#        print(cus[0])
 #       print(type(cus[0]))
        if customerId == cus[0]:
            cus_valid = True
#    print(cus_valid)
    if not cus_valid:
        print("you have entered a invalid Customer ID, insertion failed")
    if cus_valid:
        productId = int(input("please enter the ID of the product you want to order"))
        for prod in products:
            if productId == prod[0]:
                prod_valid = True
                price = prod[2]
    #print(price)
    if not prod_valid and prod_valid:
        print("you have entered aN invalid Product ID, insertion failed")
    if  cus_valid and prod_valid:
        quantity = int(input("please enter the quantity or the products you would like to order for this customer"))
        TotalPrices = quantity * price
        status = "Preparing"
        orders.append([orderID,productId,quantity,TotalPrices,customerId,status])
        print("ordered successful")

#the function which help to get total sales based on the product ID
def getTotalSalesProd(orders,products):
    print("----products---")
    for prod in products:
        new_prod=[str(i) for i in prod]
        for p in new_prod:
            print(p.center(8),end="  ")
        print()
    print("all products above")
    productID = int(input("Please enter a valid Product ID"))
    total = 0
    quantity = 0
    valid = False
    for order in orders:
        if(productID==order[1]):
                total += order[3]
                quantity += order[2]
    print(quantity," pieces of Product ID: ",productID, " has been sold worth-- ",total)

#This function returns the corresponding category based on the given product ID
def getCategory(productID,products):
    for prod in products:
        if productID ==prod[0]:
            return  prod[3]

#This fucntion print the total sales based on the Categories
def getTotalSalesCat(products,orders,categories):
    for cat in categories:
        new_cat=[str(i) for i in cat]
        for c in new_cat:
            print(c.center(8),end="  ")
        print()
    print("all categories above")
    categoryID = int(input("Please enter a valid Category ID"))

    print("--------Catogry ID:",categoryID,"-------")
    for prod in products:
        quantity = 0
        total = 0
        valid = False
        for order in orders:
            if categoryID == getCategory(order[1],products) and prod[0] == order[1]:
                total += order[3]
                quantity += order[2]
                valid = True
        if valid:
            print("The total prices for Product ID ", prod[0] ," is ",total," , total quantity sold is",quantity)

#this fucntion sort the total sales amount for each product in whether ascending or descending order
def getTotalSalesPrice(products,orders):
    temp = int(input("In which order you would like to sort the Products sales, type 1 for higher to lower, type 0 for lower to higher"))
    dic = {}
    for prod in products:
        sum = 0
        for order in orders:
            if order[0]=="orderID":
                continue
            if(order[1]==prod[0]):
                sum += order[3]
        dic[prod[0]] = sum
    del dic["Pid"]
    if temp==1:
        new_dic=sorted(dic.items(), key=lambda x: x[1], reverse=True)
    elif temp==0:
        new_dic=sorted(dic.items(), key=lambda x: x[1])
    for key,value in new_dic:
        print("Product ID:",key,"Total Proce",value)

#returns a list contains all the stored locations
def getLocationList(customers):
    location = []
    for cust in customers:
        if cust[4] not in location:
            location.append(cust[4])
    return location

#returns the customer location based on the given Customer ID
def getLocation(customers,customerID)        :
    for cust in customers:
        if customerID == cust[0]:
            return cust[4]

#print the total sales of different locations
def getTotalSalesLoca(customers,orders):
    location = getLocationList(customers)
    for loc in location:
        sum=0
        valid = False
        for ord in orders:
            if ord[0]=="orderID":
                continue
            if getLocation(customers,ord[4]) == loc:
                sum += ord[3]
                valid = True
        if valid:
            print("The total price products sold for location",loc,"is :",sum)

#main code
printOpt()
while True:
    option = input("Hi there, Please enter a option, enter 6 to print the menu again")
    if option == "1":
        categoryID =  len(categories)
        insertCat(categories,categoryID)
    elif option == "2":
        productID = len(products)
        insertProd(products,categories,productID)
    elif option == "3":
        customerID = len(customers)
        insertCustomer(customers,customerID)
    elif option == "4":
        orderID = len(orders)
        placeOrder(customers,products,orders,orderID)
    elif option == "5":
        printData(categories,products,customers,orders)
    elif option == "6":
        printOpt()
    elif option == "7":
        getTotalSalesProd(orders,products)
    elif option == "8":
        getTotalSalesCat(products,orders,categories)
    elif option == "9":
        getTotalSalesPrice(products,orders)
    elif option == "10":
        getTotalSalesLoca(customers,orders)
    elif option == "11":
        break
    else:
        print("not a valid input")