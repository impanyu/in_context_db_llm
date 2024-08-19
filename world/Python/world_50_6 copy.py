from databases import Database
# an imaginary database module, which contains a simplified class Database
# the interface of the class Database is listed as follows:
# class Database:
#     def __init__(self, name=""): create a database named "name"
#     def create_table(self, table_name="", columns={}, primary_key=(),foreign_key={}): create a table named "table_name" with columns and primary key
#     def insert(self, table_name="", data={}): insert data into table
#     def delete(self, table_name="", condition={}, join_by=[]): delete data which satisfy condition from table
#     def update(self, table_name="", data={}, condition={},join_by=[]): update data which satisfy condition in table
#     def select(self, table_names=[], columns=[], condition={}, join_by=[], order_by=[],distinct=False): return data from tables which satisfy condition and join. join_by is a list of tuples, each tuple contains the pair of columns to join

INF = float('inf')

# create a database named "world", containing three tables: "country", "city", "countrylanguage" and their corresponding metadata
db = Database("world")
db.create_table("country",
                {"GNP": {"type": "float", "default": 0},
                "Code": {"type": "string", "default": ""}, 
                "Name": {"type": "string", "default": ""}, 
                "Region": {"type": "string", "default": ""}, 
                "Continent": {"type": "string", "default": ""}, 
                "Population": {"type": "int", "default": 0}, 
                "SurfaceArea": {"type": "float", "default": 0}, 
                "LifeExpectancy": {"type": "float", "default": 0}}, 
                ("Code"))
db.create_table("city",
                {"ID": {"type": "int", "default": 0,"auto_increment": True}, 
                "Name": {"type": "string", "default": ""}, 
                "CountryCode": {"type": "string", "default": ""}, 
                "Population": {"type": "int", "default": 0}}, 
                ("ID"),
                {"CountryCode": "country.Code"})
db.create_table("countrylanguage",
                {"CountryCode": {"type": "string", "default": ""}, 
                "Language": {"type": "string", "default": ""}, 
                "IsOfficial": {"type": "string", "default": ""}, 
                "Percentage": {"type": "float", "default": 0}}, 
                ("CountryCode", "Language"),
                {"CountryCode": "country.Code"})

db.insert("country",{"GNP": 828.00, "Code": "ABW", "Name": "Aruba", "Region": "Caribbean", "Continent": "North America", "Population": 103000, "SurfaceArea": 193.00, "LifeExpectancy": 78.4})
db.insert("country",{"GNP": 5976.00, "Code": "AFG", "Name": "Afghanistan", "Region": "Southern and Central Asia", "Continent": "Asia", "Population": 22720000, "SurfaceArea": 652090.00, "LifeExpectancy": 45.9})
db.insert("country",{"GNP": 6648.00, "Code": "AGO", "Name": "Angola", "Region": "Central Africa", "Continent": "Africa", "Population": 12878000, "SurfaceArea": 1246700.00, "LifeExpectancy": 38.3})
db.insert("country",{"GNP": 63.20, "Code": "AIA", "Name": "Anguilla", "Region": "Caribbean", "Continent": "North America", "Population": 8000, "SurfaceArea": 96.00, "LifeExpectancy": 76.1})
db.insert("country",{"GNP": 3205.00, "Code": "ALB", "Name": "Albania", "Region": "Southern Europe", "Continent": "Europe", "Population": 3401200, "SurfaceArea": 28748.00, "LifeExpectancy": 71.6})
db.insert("country",{"GNP": 1630.00, "Code": "AND", "Name": "Andorra", "Region": "Southern Europe", "Continent": "Europe", "Population": 78000, "SurfaceArea": 468.00, "LifeExpectancy": 83.5})
db.insert("country",{"GNP": 1941.00, "Code": "ANT", "Name": "Netherlands Antilles", "Region": "Caribbean", "Continent": "North America", "Population": 217000, "SurfaceArea": 800.00, "LifeExpectancy": 74.7})
db.insert("country",{"GNP": 37966.00, "Code": "ARE", "Name": "United Arab Emirates", "Region": "Middle East", "Continent": "Asia", "Population": 2441000, "SurfaceArea": 83600.00, "LifeExpectancy": 74.1})
db.insert("country",{"GNP": 340238.00, "Code": "ARG", "Name": "Argentina", "Region": "South America", "Continent": "South America", "Population": 37032000, "SurfaceArea": 2780400.00, "LifeExpectancy": 75.1})
db.insert("country",{"GNP": 1813.00, "Code": "ARM", "Name": "Armenia", "Region": "Middle East", "Continent": "Asia", "Population": 3520000, "SurfaceArea": 29800.00, "LifeExpectancy": 66.4})
db.insert("country",{"GNP": 334.00, "Code": "ASM", "Name": "American Samoa", "Region": "Polynesia", "Continent": "Oceania", "Population": 68000, "SurfaceArea": 199.00, "LifeExpectancy": 75.1})
db.insert("country",{"GNP": 0.00, "Code": "ATA", "Name": "Antarctica", "Region": "Antarctica", "Continent": "Antarctica", "Population": 0, "SurfaceArea": 13120000.00, "LifeExpectancy": null})
db.insert("country",{"GNP": 0.00, "Code": "ATF", "Name": "French Southern territories", "Region": "Antarctica", "Continent": "Antarctica", "Population": 0, "SurfaceArea": 7780.00, "LifeExpectancy": null})
db.insert("country",{"GNP": 612.00, "Code": "ATG", "Name": "Antigua and Barbuda", "Region": "Caribbean", "Continent": "North America", "Population": 68000, "SurfaceArea": 442.00, "LifeExpectancy": 70.5})
db.insert("country",{"GNP": 351182.00, "Code": "AUS", "Name": "Australia", "Region": "Australia and New Zealand", "Continent": "Oceania", "Population": 18886000, "SurfaceArea": 7741220.00, "LifeExpectancy": 79.8})
db.insert("country",{"GNP": 211860.00, "Code": "AUT", "Name": "Austria", "Region": "Western Europe", "Continent": "Europe", "Population": 8091800, "SurfaceArea": 83859.00, "LifeExpectancy": 77.7})
db.insert("country",{"GNP": 4127.00, "Code": "AZE", "Name": "Azerbaijan", "Region": "Middle East", "Continent": "Asia", "Population": 7734000, "SurfaceArea": 86600.00, "LifeExpectancy": 62.9})
db.insert("country",{"GNP": 903.00, "Code": "BDI", "Name": "Burundi", "Region": "Eastern Africa", "Continent": "Africa", "Population": 6695000, "SurfaceArea": 27834.00, "LifeExpectancy": 46.2})
db.insert("country",{"GNP": 249704.00, "Code": "BEL", "Name": "Belgium", "Region": "Western Europe", "Continent": "Europe", "Population": 10239000, "SurfaceArea": 30518.00, "LifeExpectancy": 77.8})
db.insert("country",{"GNP": 2357.00, "Code": "BEN", "Name": "Benin", "Region": "Western Africa", "Continent": "Africa", "Population": 6097000, "SurfaceArea": 112622.00, "LifeExpectancy": 50.2})
db.insert("country",{"GNP": 2425.00, "Code": "BFA", "Name": "Burkina Faso", "Region": "Western Africa", "Continent": "Africa", "Population": 11937000, "SurfaceArea": 274000.00, "LifeExpectancy": 46.7})
db.insert("country",{"GNP": 32852.00, "Code": "BGD", "Name": "Bangladesh", "Region": "Southern and Central Asia", "Continent": "Asia", "Population": 129155000, "SurfaceArea": 143998.00, "LifeExpectancy": 60.2})
db.insert("country",{"GNP": 12178.00, "Code": "BGR", "Name": "Bulgaria", "Region": "Eastern Europe", "Continent": "Europe", "Population": 8190900, "SurfaceArea": 110994.00, "LifeExpectancy": 70.9})
db.insert("country",{"GNP": 6366.00, "Code": "BHR", "Name": "Bahrain", "Region": "Middle East", "Continent": "Asia", "Population": 617000, "SurfaceArea": 694.00, "LifeExpectancy": 73.0})
db.insert("country",{"GNP": 3527.00, "Code": "BHS", "Name": "Bahamas", "Region": "Caribbean", "Continent": "North America", "Population": 307000, "SurfaceArea": 13878.00, "LifeExpectancy": 71.1})
db.insert("country",{"GNP": 2841.00, "Code": "BIH", "Name": "Bosnia and Herzegovina", "Region": "Southern Europe", "Continent": "Europe", "Population": 3972000, "SurfaceArea": 51197.00, "LifeExpectancy": 71.5})
db.insert("country",{"GNP": 13714.00, "Code": "BLR", "Name": "Belarus", "Region": "Eastern Europe", "Continent": "Europe", "Population": 10236000, "SurfaceArea": 207600.00, "LifeExpectancy": 68.0})
db.insert("country",{"GNP": 630.00, "Code": "BLZ", "Name": "Belize", "Region": "Central America", "Continent": "North America", "Population": 241000, "SurfaceArea": 22696.00, "LifeExpectancy": 70.9})
db.insert("country",{"GNP": 2328.00, "Code": "BMU", "Name": "Bermuda", "Region": "North America", "Continent": "North America", "Population": 65000, "SurfaceArea": 53.00, "LifeExpectancy": 76.9})
db.insert("country",{"GNP": 8571.00, "Code": "BOL", "Name": "Bolivia", "Region": "South America", "Continent": "South America", "Population": 8329000, "SurfaceArea": 1098581.00, "LifeExpectancy": 63.7})
db.insert("country",{"GNP": 776739.00, "Code": "BRA", "Name": "Brazil", "Region": "South America", "Continent": "South America", "Population": 170115000, "SurfaceArea": 8547403.00, "LifeExpectancy": 62.9})
db.insert("country",{"GNP": 2223.00, "Code": "BRB", "Name": "Barbados", "Region": "Caribbean", "Continent": "North America", "Population": 270000, "SurfaceArea": 430.00, "LifeExpectancy": 73.0})
db.insert("country",{"GNP": 11705.00, "Code": "BRN", "Name": "Brunei", "Region": "Southeast Asia", "Continent": "Asia", "Population": 328000, "SurfaceArea": 5765.00, "LifeExpectancy": 73.6})
db.insert("country",{"GNP": 372.00, "Code": "BTN", "Name": "Bhutan", "Region": "Southern and Central Asia", "Continent": "Asia", "Population": 2124000, "SurfaceArea": 47000.00, "LifeExpectancy": 52.4})
db.insert("country",{"GNP": 0.00, "Code": "BVT", "Name": "Bouvet Island", "Region": "Antarctica", "Continent": "Antarctica", "Population": 0, "SurfaceArea": 59.00, "LifeExpectancy": null})
db.insert("country",{"GNP": 4834.00, "Code": "BWA", "Name": "Botswana", "Region": "Southern Africa", "Continent": "Africa", "Population": 1622000, "SurfaceArea": 581730.00, "LifeExpectancy": 39.3})
db.insert("country",{"GNP": 1054.00, "Code": "CAF", "Name": "Central African Republic", "Region": "Central Africa", "Continent": "Africa", "Population": 3615000, "SurfaceArea": 622984.00, "LifeExpectancy": 44.0})
db.insert("country",{"GNP": 598862.00, "Code": "CAN", "Name": "Canada", "Region": "North America", "Continent": "North America", "Population": 31147000, "SurfaceArea": 9970610.00, "LifeExpectancy": 79.4})
db.insert("country",{"GNP": 0.00, "Code": "CCK", "Name": "Cocos (Keeling) Islands", "Region": "Australia and New Zealand", "Continent": "Oceania", "Population": 600, "SurfaceArea": 14.00, "LifeExpectancy": null})
db.insert("country",{"GNP": 264478.00, "Code": "CHE", "Name": "Switzerland", "Region": "Western Europe", "Continent": "Europe", "Population": 7160400, "SurfaceArea": 41284.00, "LifeExpectancy": 79.6})
db.insert("country",{"GNP": 72949.00, "Code": "CHL", "Name": "Chile", "Region": "South America", "Continent": "South America", "Population": 15211000, "SurfaceArea": 756626.00, "LifeExpectancy": 75.7})
db.insert("country",{"GNP": 982268.00, "Code": "CHN", "Name": "China", "Region": "Eastern Asia", "Continent": "Asia", "Population": 1277558000, "SurfaceArea": 9572900.00, "LifeExpectancy": 71.4})
db.insert("country",{"GNP": 11345.00, "Code": "CIV", "Name": "Côte d’Ivoire", "Region": "Western Africa", "Continent": "Africa", "Population": 14786000, "SurfaceArea": 322463.00, "LifeExpectancy": 45.2})


db.delete("country",{"Code":"DOM"})
db.delete("country",{"Code":"DJI"})




db.insert("country",{"GNP": 3787042.00, "Code": "JPN", "Name": "Japan", "Region": "Eastern Asia", "Continent": "Asia", "Population": 126714000, "SurfaceArea": 377829.00, "LifeExpectancy": 80.7})
db.insert("country",{"GNP": 8510700.00, "Code": "USA", "Name": "United States", "Region": "North America", "Continent": "North America", "Population": 278357000, "SurfaceArea": 9363520.00, "LifeExpectancy": 77.1})





db.insert("city",{"ID": 1, "Name": "Kabul", "Population": 1780000, "CountryCode": "AFG"})
db.insert("city",{"ID": 2, "Name": "Qandahar", "Population": 237500, "CountryCode": "AFG"})
db.insert("city",{"ID": 3, "Name": "Herat", "Population": 186800, "CountryCode": "AFG"})
db.insert("city",{"ID": 4, "Name": "Mazar-e-Sharif", "Population": 127800, "CountryCode": "AFG"})
db.insert("city",{"ID": 33, "Name": "Willemstad", "Population": 2345, "CountryCode": "ANT"})
db.insert("city",{"ID": 34, "Name": "Tirana", "Population": 270000, "CountryCode": "ALB"})


db.insert("city",{"ID": 82, "Name": "Salta", "Population": 367550, "CountryCode": "ARG"})
db.insert("city",{"ID": 83, "Name": "Moreno", "Population": 356993, "CountryCode": "ARG"})
db.insert("city",{"ID": 84, "Name": "Santa Fé", "Population": 353063, "CountryCode": "ARG"})
db.insert("city",{"ID": 85, "Name": "Avellaneda", "Population": 353046, "CountryCode": "ARG"})
db.insert("city",{"ID": 86, "Name": "Tres de Febrero", "Population": 352311, "CountryCode": "ARG"})
db.insert("city",{"ID": 87, "Name": "Morón", "Population": 349246, "CountryCode": "ARG"})

db.insert("city",{"ID": 90, "Name": "Tigre", "Population": 296226, "CountryCode": "ARG"})



db.delete("city",{"ID": 3})
db.delete("city",{"CountryCode":'ARG', "Population":[0, 300000]})



















db.insert("countrylanguage",{"Language": "Punjabi", "IsOfficial": "F", "Percentage": 0.7, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Spanish", "IsOfficial": "F", "Percentage": 0.7, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Ukrainian", "IsOfficial": "F", "Percentage": 0.6, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "T", "Percentage": 0.0, "CountryCode": "CCK"})
db.insert("countrylanguage",{"Language": "Malay", "IsOfficial": "F", "Percentage": 0.0, "CountryCode": "CCK"})
db.insert("countrylanguage",{"Language": "French", "IsOfficial": "T", "Percentage": 19.2, "CountryCode": "CHE"})
db.insert("countrylanguage",{"Language": "German", "IsOfficial": "T", "Percentage": 63.6, "CountryCode": "CHE"})
db.insert("countrylanguage",{"Language": "Italian", "IsOfficial": "T", "Percentage": 7.7, "CountryCode": "CHE"})
db.insert("countrylanguage",{"Language": "Romansh", "IsOfficial": "T", "Percentage": 0.6, "CountryCode": "CHE"})
db.insert("countrylanguage",{"Language": "Aimará", "IsOfficial": "F", "Percentage": 0.5, "CountryCode": "CHL"})
db.insert("countrylanguage",{"Language": "Araucan", "IsOfficial": "F", "Percentage": 9.6, "CountryCode": "CHL"})
db.insert("countrylanguage",{"Language": "Rapa nui", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "CHL"})
db.insert("countrylanguage",{"Language": "Spanish", "IsOfficial": "T", "Percentage": 89.7, "CountryCode": "CHL"})
db.insert("countrylanguage",{"Language": "Chinese", "IsOfficial": "T", "Percentage": 92.0, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Dong", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Hui", "IsOfficial": "F", "Percentage": 0.8, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Mantšu", "IsOfficial": "F", "Percentage": 0.9, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Miao", "IsOfficial": "F", "Percentage": 0.7, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Mongolian", "IsOfficial": "F", "Percentage": 0.4, "CountryCode": "CHN"})



db.update("countrylanguage", {"Percentage": 91.8}, {"CountryCode":'CHN', "Language":'Chinese'})
db.delete("countrylanguage", {"CountryCode":'CAN', "Language":'Italian'})
    



# Example for few shots:
# 1. example_db = Database("example")
# 2. example_db.create_table("Customers", {"CustomerID": {"type": "int", "default": 0, "auto_increment": True}, "CustomerName": {"type": "varchar(255)", "default": ""}, "ContactName": {"type": "varchar(255)", "default": ""}, "Address": {"type": "varchar(255)", "default": ""}, "City": {"type": "varchar(255)", "default": ""}, "PostalCode": {"type": "varchar(255)", "default": ""}, "Country": {"type": "varchar(255)", "default": ""}}, ("CustomerID"))
# 3. example_db.create_table("Orders", {"OrderID": {"type": "int", "default": 0, "auto_increment": True}, "CustomerID": {"type": "int", "default": 0}, "OrderDate": {"type": "date", "default": ""}}, ("OrderID"), {"CustomerID": "Customers.CustomerID"})
# 4. example_db.create_table("OrderDetails", {"OrderDetailID": {"type": "int", "default": 0, "auto_increment": True}, "OrderID": {"type": "int", "default": 0}, "ProductID": {"type": "int", "default": 0}, "Quantity": {"type": "int", "default": 0}}, ("OrderDetailID"), {"OrderID": "Orders.OrderID", "ProductID": "Products.ProductID"})
# 5. example_db.create_table("Products", {"ProductID": {"type": "int", "default": 0, "auto_increment": True}, "ProductName": {"type": "varchar(255)", "default": ""}, "Unit": {"type": "varchar(255)", "default": ""}, "Price": {"type": "decimal(10,2)", "default": 0.0}}, ("ProductID"))

# 6. example_db.insert("Customers",{"CustomerID": 1, "CustomerName": "Alfreds Futterkiste", "ContactName": "Maria Anders", "Address": "Obere Str. 57", "City": "Berlin", "PostalCode": "12209", "Country": "Germany"})
# 7. example_db.insert("Customers",{"CustomerID": 2, "CustomerName": "Ana Trujillo Emparedados y helados", "ContactName": "Ana Trujillo", "Address": "Avda. de la Constitución 2222", "City": "México D.F.", "PostalCode": "05021", "Country": "Mexico"})
# 8. example_db.insert("Customers",{"CustomerID": 3, "CustomerName": "Antonio Moreno Taquería", "ContactName": "Antonio Moreno", "Address": "Mataderos 2312", "City": "México D.F.", "PostalCode": "05023", "Country": "Mexico"})
# 9. example_db.insert("Customers",{"CustomerID": 4, "CustomerName": "Around the Horn", "ContactName": "Thomas Hardy", "Address": "120 Hanover Sq.", "City": "London", "PostalCode": "WA1 1DP", "Country": "UK"})

# 10. example_db.insert("Orders",{"OrderID": 10308, "CustomerID": 2, "OrderDate": "1996-09-18"})
# 11. example_db.insert("Orders",{"OrderID": 10365, "CustomerID": 3, "OrderDate": "1996-11-27"})

# 12. db.delete("Customers",{"CustomerID": 4})
# 13. db.update("Orders",{"OrderDate": "1996-09-19"}, {"OrderID": 10308})

# 14. example_db.insert("OrderDetails",{"OrderDetailID": 162, "OrderID": 10308, "ProductID": 69, "Quantity": 1})
# 15. example_db.insert("OrderDetails",{"OrderDetailID": 163, "OrderID": 10308, "ProductID": 70, "Quantity": 5})
# 16. example_db.insert("OrderDetails",{"OrderDetailID": 314, "OrderID": 10365, "ProductID": 11, "Quantity": 24})

# 17. example_db.insert("Products",{"ProductID": 11, "ProductName": "Queso Cabrales", "Unit": "1 kg pkg.", "Price": 21})
# 18. example_db.insert("Products",{"ProductID": 69, "ProductName": "Gudbrandsdalsost", "Unit": "10 kg pkg.", "Price": 36})
# 19. example_db.insert("Products",{"ProductID": 70, "ProductName": "Outback Lager", "Unit": "24 - 355 ml bottles", "Price": 15})
# 20. example_db.insert("Products",{"ProductID": 1, "ProductName": "Chais", "Unit": "10 boxes x 20 bags", "Price": 18})

# 21. db.delete("Products",{"ProductID": 1})


# For COT:
# To answer the queries, you need to execute the above python command step by step, and figure out the current data in the database.

# For Few Shots COT:
# After executing python command 1, a new database named example will be created.
# After executing python command 2, the Customers table will be created with columns CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country, and CustomerID as primary key.
# After executing python command 3, the Orders table will be created with columns OrderID, CustomerID, OrderDate, and OrderID as primary key, and CustomerID as foreign key referencing Customers.CustomerID.
# After executing python command 4, the OrderDetails table will be created with columns OrderDetailID, OrderID, ProductID, Quantity, and OrderDetailID as primary key, and OrderID and ProductID as foreign key referencing Orders.OrderID and Products.ProductID.
# After executing python command 5, the Products table will be created with columns ProductID, ProductName, Unit, Price, and ProductID as primary key.

# After executing python command 6, the Customers table will contain custermer with CustomerID = 1,
# After executing python command 7, the Customers table will contain custermer with CustomerID = 2,
# After executing python command 8, the Customers table will contain custermer with CustomerID = 3,
# After executing python command 9, the Customers table will contain custermer with CustomerID = 4,
# After executing python command 10, the Orders table will contain order with OrderID = 10308,
# After executing python command 11, the Orders table will contain order with OrderID = 10365,
# After executing python command 12, the Customers table will not contain custermer with CustomerID = 4, and only contain custermer with CustomerID = 1, 2, 3,
# After executing python command 13, the order with OrderID = 10308 will have OrderDate = '9/19/1996',
# After executing python command 14, the OrderDetails table will contain order detail with OrderDetailID = 162,
# After executing python command 15, the OrderDetails table will contain order detail with OrderDetailID = 163,
# After executing python command 16, the OrderDetails table will contain order detail with OrderDetailID = 314,
# After executing python command 17, the Products table will contain product with ProductID = 11,
# After executing python command 18, the Products table will contain product with ProductID = 69,
# After executing python command 19, the Products table will contain product with ProductID = 70,
# After executing python command 20, the Products table will contain product with ProductID = 1,
# After executing python command 21, the Products table will not contain product with ProductID = 1, and only contain product with ProductID = 11, 69, 70.

# Now if the user send query:
# db.select(["CustomerID"], ["Customers"], {"ProductID":11}, [("Customers.CustomerID","Orders.CustomerID"),("Orders.OrderID","OrderDetails.OrderID"),("OrderDetails.ProductID","Products.ProductID")])
# then the query result is 3.

# If the user send query:
# len(db.select(["ProductID"], ["Products"], {"Price":[20,INF]}))
# then the query result is 2.

# If the user send query:
# db.select(["OrderDate"], ["Orders"], {"OrderID":10308})
# then the query result is 9/19/1996.

# If the user send query:
# db.insert("Customers",{"CustomerID": 4, "CustomerName": "Around the Horn", "ContactName": "Thomas Hardy", "Address": "120 Hanover Sq.", "City": "London", "PostalCode": "WA1 1DP", "Country": "UK"})
# then the query will be successfully executed.

# If the user send query:
# db.insert("Orders",{"OrderID": 10249, "CustomerID": 4, "OrderDate": "7/5/1996"})
# then the query will fail, with foreign key constraint violation.

# If the user send query:
# db.insert("Products",{"ProductID": 11, "ProductName": "Queso Cabrales", "Unit": "1 kg pkg.", "Price": 21})
# then the query will fail, with primary key constraint violation.

# If the user send query:
# db.delete("Customers",{"CustomerID": 1})
# then the query will be successfully executed.

# If the user send query:
# db.delete("Orders",{"OrderID": 10308})
# then the query will fail, with foreign key constraint violation.

# If the user send query:
# db.update("OrderDetails",{"Quantity": 2}, {"OrderDetailID": 162})
# then the query will be successfully executed.

# If the user send query:
# db.update("OrderDetails",{"ProductID": 1}, {"OrderDetailID": 162})
# then the query will fail, with foreign key constraint violation.


# Now pretend you are a python interpreter which has already executed the above python code.
# Next you will receive a query from the user, which is also written in python code. 
# You need to execute the query and reply to the user with the standard output of query.
# The query is as follows:


# select
# 1. return the names of all countries
# no filtering.
db.select(["Name"], ["country"])
# 2. return the ID of all the cities in China with population greater than 350000. 
# Double filtering. Range filtering.
db.select(["ID"], ["city"], {"CountryCode":'CHN', "Population":[350000, INF]})
# 3. return the names of all the countries with population greater than 100000000. 
# Single filtering. Range filtering.
db.select(["Name"], ["country"], {"Population":[100000000,INF]})
# 4. return the languages with percentage greater than 50.0. 
# Single filtering. Range filtering.
db.select(["Language"], ["countrylanguage"], {"Percentage":[50.0,100.0]},distinct=True)
# 5. return the population of the city with ID = 50
# Single filtering. Exact filtering.
db.select(["Population"], ["city"], {"ID":50})
# 6. return the population of japan
# Single filtering. 
db.select(["Population"], ["country"], {"Code":'JPN'})
# 7. return the names of all the countries in Asia with population greater than 50000000 and life expectancy greater than 60.0
# triple filtering. Range filtering.
db.select(["Name"], ["country"], {"Continent":'Asia', "Population":[50000000,INF], "LifeExpectancy":[60.0,INF]})
# 8. return the names of all the cities with countrycode = 'CHN', ID in between 50 and 100, population greater than 100000 and less than 500000 
# triple filtering. Range filtering.
db.select(["Name"], ["city"], {"CountryCode":'CHN', "ID":[50,100], "Population":[100000,500000]})

# 9. return the ID for all the cities in countries with population greater than 100000000
# single filtering. Range filtering. Join.
db.select(["city.ID"], ["city", "country"], {"country.Population":[100000000,INF]}, [("city.CountryCode","country.Code")])
# 10. return all the languages with percentage greater than 50.0 in Asia 
# double filtering. Range filtering. join.
db.select(["countrylanguage.Language"], ["countrylanguage", "country"], {"country.Continent":'Asia', "countrylanguage.Percentage":[50.0,100.0]}, [("countrylanguage.CountryCode","country.Code")], distinct=True)

# 11. return all the cities in countries in Asia
# single filtering. Join.
db.select(["city.Name"], ["city", "country"], {"country.Continent":'Asia'}, [("city.CountryCode","country.Code")])
# 12. return all the cities with life expectancy greater than 80
# single filtering. Range filtering. Join.
db.select(["city.Name"], ["city", "country"], {"country.LifeExpectancy":[80.0,INF]}, [("city.CountryCode","country.Code")])
# 13. return the distinct languages in countries in Asia
# single filtering. Join.
db.select(["countrylanguage.Language"], ["countrylanguage", "country"], {"country.Continent":'Asia'}, [("countrylanguage.CountryCode","country.Code")],distinct=True) 

# 14. return all the cities and the languages spoken in the countries in Asia with population greater than 100000000
# double filtering. Range filtering. Triple Join.
db.select(["city.Name","countrylanguage.Language"], ["city", "country", "countrylanguage"], {"country.Continent":'Asia', "country.Population":[100000000,INF]}, [("city.CountryCode","country.Code"),("countrylanguage.CountryCode","country.Code")])
# 15. return all the cities in countries which English is spoken with percentage greater than 50.0
# double filtering. Range filtering. Triple Join.
db.select(["city.Name"], ["city", "country", "countrylanguage"], {"countrylanguage.Language":'English', "countrylanguage.Percentage":[50.0,100.0]}, [("city.CountryCode","country.Code"),("countrylanguage.CountryCode","country.Code")])
# 16. return all the cities in countries with life expectancy greater than 60 and which speak English with percentage greater than 10.0
# triple filtering. Range filtering. Triple Join.
db.select(["city.Name"], ["city", "country", "countrylanguage"], { "country.LifeExpectancy":[60.0,INF], "countrylanguage.Language":'English', "countrylanguage.Percentage":[10.0,100.0]}, [("city.CountryCode","country.Code"),("countrylanguage.CountryCode","country.Code")])



# 17. return the number of cities in China
# single filtering. count.
len(db.select(["ID"], ["city"], {"CountryCode":'CHN'}))
# 18. return the number of countries in Asia with population greater than 50000000
# double filtering. count. range filtering.
len(db.select(["Code"], ["country"], {"Continent":'Asia', "Population":[50000000,INF]}))
# 19. return the number of cities with population between 100000 and 500000 with countrycode = 'DZA'
# double filtering. Range filtering. count.
len(db.select(["ID"], ["city"], {"CountryCode":'DZA', "Population":[100000,500000]}))


# 20. return the number of distinct languages
# no filtering. count.
len(db.select(["Language"], ["countrylanguage"],distinct=True))
# 21. return the number of cities in Algeria
# single filtering. count. join. 
len(db.select(["ID"], ["city","country"], {"country.Name":'Algeria'}, [("city.CountryCode","country.Code")]))
# 22. return the total number of countries
# no filtering. count.
len(db.select(["Code"], ["country"]))


# 23. return the names of city in China sorted by population
# single filtering. ranking.
db.select(["Name"], ["city"], {"CountryCode":'CHN'}, order_by=["Population"])
# 24. return the names of countries in Asia sorted by surface area
# single filtering. ranking.
db.select(["Name"], ["country"], {"Continent":'Asia'}, order_by=["SurfaceArea"])
# 25. return the names of countries which speak English sorted by percentage
# single filtering. ranking. join.
db.select(["country.Name"], ["countrylanguage", "country"], {"countrylanguage.Language":'English'}, [("countrylanguage.CountryCode","country.Code")], order_by=["countrylanguage.Percentage"])
# 26. return the names of countries in Europe with GNP greater than 500000 sorted by population
# double filtering. Range filtering. ranking.
db.select(["Name"], ["country"], {"Continent":'Europe', "GNP":[500000,INF]}, order_by=["Population"])


# Insert
# 27. insert a new city with ID = 188, Name = 'Djougou', CountryCode = 'BEN', Population = 134099
# primary key violation. insert.
db.insert("city",{"ID": 188, "Name": "Djougou", "Population": 134099, "CountryCode": "BEN"})

# 28. insert a new  city with ID = 1, Name = 'Kabul', CountryCode = 'AFG', Population = 1780000
# primary key violation. insert.
db.insert("city",{"ID": 1, "Name": "Kabul", "Population": 1780000, "CountryCode": "AFG"})

# 29. insert a new city with ID = 2, Name = 'Qandahar', CountryCode = 'AFF', Population = 237500
# foreign key violation. insert.
db.insert("city",{"ID": 2, "Name": "Qandahar", "Population": 237500, "CountryCode": "AFF"})

# 30. insert a language = English in coutnrycode = 'CCC' with percentage = 1.0 and isofficial = 'F'
# foreign key violation. insert.
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "F", "Percentage": 1.0, "CountryCode": "CCC"})


# 31. insert a new city with ID = 1532, Name = 'Tokyo', CountryCode = 'JPN', Population = 7980230
# insert.
db.insert("city",{"ID": 1532, "Name": "Tokyo", "Population": 7980230, "CountryCode": "JPN"})
# 32. insert a new city with ID = 3795, Name = 'Chicago', CountryCode = 'USA', Population = 2896016
# insert.
db.insert("city",{"ID": 3795, "Name": "Chicago", "Population": 2896016, "CountryCode": "USA"})
# 33. insert a new country with Code = 'THA', Name = 'Thailand', Continent = 'Asia', Region = 'Southeast Asia', SurfaceArea = 513115.00, Population = 61399000, LifeExpectancy = 68.6, GNP = 116416.00
# insert.
db.insert("country",{"Code": 'THA', "Name": 'Thailand', "Continent": 'Asia', "Region": 'Southeast Asia', "SurfaceArea": 513115.00,  "Population": 61399000, "LifeExpectancy": 68.6, "GNP": 116416.00})
# 34. insert a language = English in coutnrycode = 'CHN' with percentage = 1.0 and isofficial = 'F'
# insert.
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "F", "Percentage": 1.0, "CountryCode": "CHN"})

# Delete
# 35. delete the country with code = 'ARG'
# foreign key violation. single filtering.
db.delete("country",{"Code":'ARG'})
# 36. delete all the countries in Asia with population greater than 5000000
# double filtering. Range filtering. foreign key violation.
db.delete("country",{"Continent":'Asia', "Population":[5000000,INF]})
# 37. delete all the countries with GNP greater than 300000 and less than 1000000
# single filtering. Range filtering. foreign key violation.
db.delete("country",{"GNP":[300000,1000000]})
# 38. delete all the countries with life expectancy larger than 60
# single filtering. Range filtering. foreign key violation.
db.delete("country",{"LifeExpectancy":[60.0,INF]})
# 39. delete all the languages for countries in Europe
# single filtering. foreign key violation. join.
db.delete("countrylanguage",{"country.Continent":'Europe'},[("countrylanguage.CountryCode","country.Code")])


# 40. delete the city with ID = 3795
# single filtering. delete.
db.delete("city",{"ID":3795})
# 41. delete the city with ID = 1
# single filtering. delete.
db.delete("city",{"ID":1})
# 42. delete the country with code = 'JPN'
# single filtering.
db.delete("country",{"Code":'JPN'})
# 43. delete all the cities in China with population greater than 300000
# single filtering. Range filtering. delete.
db.delete("city",{"CountryCode":'CHN', "Population":[300000,INF]})
# 44. delete all the languages with percentage greater than 50.0
# single filtering. Range filtering. delete.
db.delete("countrylanguage",{"Percentage":[50.0,100.0]})


# Update


# 45. update the code of country with name = "China" to 'CHI'
# foreign key violation. single filtering. update
db.update("country",{"Code": 'CHI'}, {"Name":'China'})
# 46. update the code of country with name = "Argentina" to 'AAA'
# foreign key violation. single filtering. update
db.update("country",{"Code": 'AAA'}, {"Name":'Argentina'})
# 47. update the code of country with population = 126724000 to 'JPA'
# foreign key violation. single filtering. update
db.update("country",{"Code": 'JPA'}, {"Population":126724000})


# 48. update the population of the city with ID = 50 to 100120
# single filtering. update.
db.update("city",{"Population": 100120}, {"ID":50})
# 49. update the life expectancy of the country with code = 'CHN' to 80.0
# single filtering. update.
db.update("country",{"LifeExpectancy": 80.0}, {"Code":'CHN'})
# 50. update the percentage of language = Chinese in countrycode = 'CHN' to 93
# double filtering. update.
db.update("countrylanguage",{ "Percentage": 93.0}, {"Language":'Chinese', "CountryCode":'CHN'})

# 51. update all the cities in China with population greater than 300000, increate the population by 10%
# double filtering. Range filtering. update. join
db.update("city",{"Population": "VALUE(city.Population)*1.1"}, {"country.Name": 'China', "city.Population":[300000,INF]}, [("city.CountryCode","country.Code")])






