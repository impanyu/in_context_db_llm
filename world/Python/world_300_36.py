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
db.insert("country",{"GNP": 9174.00, "Code": "CMR", "Name": "Cameroon", "Region": "Central Africa", "Continent": "Africa", "Population": 15085000, "SurfaceArea": 475442.00, "LifeExpectancy": 54.8})
db.insert("country",{"GNP": 6964.00, "Code": "COD", "Name": "Congo, The Democratic Republic of the", "Region": "Central Africa", "Continent": "Africa", "Population": 51654000, "SurfaceArea": 2344858.00, "LifeExpectancy": 48.8})
db.insert("country",{"GNP": 2108.00, "Code": "COG", "Name": "Congo", "Region": "Central Africa", "Continent": "Africa", "Population": 2943000, "SurfaceArea": 342000.00, "LifeExpectancy": 47.4})
db.insert("country",{"GNP": 100.00, "Code": "COK", "Name": "Cook Islands", "Region": "Polynesia", "Continent": "Oceania", "Population": 20000, "SurfaceArea": 236.00, "LifeExpectancy": 71.1})
db.insert("country",{"GNP": 102896.00, "Code": "COL", "Name": "Colombia", "Region": "South America", "Continent": "South America", "Population": 42321000, "SurfaceArea": 1138914.00, "LifeExpectancy": 70.3})


db.delete("country",{"Code":"DOM"})
db.delete("country",{"Code":"DJI"})

db.delete("country",{"Code":"CYM"})
db.delete("country",{"Code":"CUB"})


db.insert("country",{"GNP": 7137.00, "Code": "GHA", "Name": "Ghana", "Region": "Western Africa", "Continent": "Africa", "Population": 20212000, "SurfaceArea": 238533.00, "LifeExpectancy": 57.4})
db.insert("country",{"GNP": 258.00, "Code": "GIB", "Name": "Gibraltar", "Region": "Southern Europe", "Continent": "Europe", "Population": 25000, "SurfaceArea": 6.00, "LifeExpectancy": 79.0})
db.insert("country",{"GNP": 2352.00, "Code": "GIN", "Name": "Guinea", "Region": "Western Africa", "Continent": "Africa", "Population": 7430000, "SurfaceArea": 245857.00, "LifeExpectancy": 45.6})
db.insert("country",{"GNP": 3501.00, "Code": "GLP", "Name": "Guadeloupe", "Region": "Caribbean", "Continent": "North America", "Population": 456000, "SurfaceArea": 1705.00, "LifeExpectancy": 77.0})
db.insert("country",{"GNP": 320.00, "Code": "GMB", "Name": "Gambia", "Region": "Western Africa", "Continent": "Africa", "Population": 1305000, "SurfaceArea": 11295.00, "LifeExpectancy": 53.2})
db.insert("country",{"GNP": 293.00, "Code": "GNB", "Name": "Guinea-Bissau", "Region": "Western Africa", "Continent": "Africa", "Population": 1213000, "SurfaceArea": 36125.00, "LifeExpectancy": 49.0})
db.insert("country",{"GNP": 283.00, "Code": "GNQ", "Name": "Equatorial Guinea", "Region": "Central Africa", "Continent": "Africa", "Population": 453000, "SurfaceArea": 28051.00, "LifeExpectancy": 53.6})
db.insert("country",{"GNP": 120724.00, "Code": "GRC", "Name": "Greece", "Region": "Southern Europe", "Continent": "Europe", "Population": 10545700, "SurfaceArea": 131626.00, "LifeExpectancy": 78.4})
db.insert("country",{"GNP": 318.00, "Code": "GRD", "Name": "Grenada", "Region": "Caribbean", "Continent": "North America", "Population": 94000, "SurfaceArea": 344.00, "LifeExpectancy": 64.5})
db.insert("country",{"GNP": 0.00, "Code": "GRL", "Name": "Greenland", "Region": "North America", "Continent": "North America", "Population": 56000, "SurfaceArea": 2166090.00, "LifeExpectancy": 68.1})
db.insert("country",{"GNP": 19008.00, "Code": "GTM", "Name": "Guatemala", "Region": "Central America", "Continent": "North America", "Population": 11385000, "SurfaceArea": 108889.00, "LifeExpectancy": 66.2})
db.insert("country",{"GNP": 681.00, "Code": "GUF", "Name": "French Guiana", "Region": "South America", "Continent": "South America", "Population": 181000, "SurfaceArea": 90000.00, "LifeExpectancy": 76.1})
db.insert("country",{"GNP": 1197.00, "Code": "GUM", "Name": "Guam", "Region": "Micronesia", "Continent": "Oceania", "Population": 168000, "SurfaceArea": 549.00, "LifeExpectancy": 77.8})
db.insert("country",{"GNP": 722.00, "Code": "GUY", "Name": "Guyana", "Region": "South America", "Continent": "South America", "Population": 861000, "SurfaceArea": 214969.00, "LifeExpectancy": 64.0})
db.insert("country",{"GNP": 166448.00, "Code": "HKG", "Name": "Hong Kong", "Region": "Eastern Asia", "Continent": "Asia", "Population": 6782000, "SurfaceArea": 1075.00, "LifeExpectancy": 79.5})
db.insert("country",{"GNP": 0.00, "Code": "HMD", "Name": "Heard Island and McDonald Islands", "Region": "Antarctica", "Continent": "Antarctica", "Population": 0, "SurfaceArea": 359.00, "LifeExpectancy": null})
db.insert("country",{"GNP": 5333.00, "Code": "HND", "Name": "Honduras", "Region": "Central America", "Continent": "North America", "Population": 6485000, "SurfaceArea": 112088.00, "LifeExpectancy": 69.9})
db.insert("country",{"GNP": 20208.00, "Code": "HRV", "Name": "Croatia", "Region": "Southern Europe", "Continent": "Europe", "Population": 4473000, "SurfaceArea": 56538.00, "LifeExpectancy": 73.7})
db.insert("country",{"GNP": 3459.00, "Code": "HTI", "Name": "Haiti", "Region": "Caribbean", "Continent": "North America", "Population": 8222000, "SurfaceArea": 27750.00, "LifeExpectancy": 49.2})
db.insert("country",{"GNP": 48267.00, "Code": "HUN", "Name": "Hungary", "Region": "Eastern Europe", "Continent": "Europe", "Population": 10043200, "SurfaceArea": 93030.00, "LifeExpectancy": 71.4})
db.insert("country",{"GNP": 84982.00, "Code": "IDN", "Name": "Indonesia", "Region": "Southeast Asia", "Continent": "Asia", "Population": 212107000, "SurfaceArea": 1904569.00, "LifeExpectancy": 68.0})
db.insert("country",{"GNP": 447114.00, "Code": "IND", "Name": "India", "Region": "Southern and Central Asia", "Continent": "Asia", "Population": 1013662000, "SurfaceArea": 3287263.00, "LifeExpectancy": 62.5})
db.insert("country",{"GNP": 0.00, "Code": "IOT", "Name": "British Indian Ocean Territory", "Region": "Eastern Africa", "Continent": "Africa", "Population": 0, "SurfaceArea": 78.00, "LifeExpectancy": null})
db.insert("country",{"GNP": 75921.00, "Code": "IRL", "Name": "Ireland", "Region": "British Islands", "Continent": "Europe", "Population": 3775100, "SurfaceArea": 70273.00, "LifeExpectancy": 76.8})
db.insert("country",{"GNP": 195746.00, "Code": "IRN", "Name": "Iran", "Region": "Southern and Central Asia", "Continent": "Asia", "Population": 67702000, "SurfaceArea": 1648195.00, "LifeExpectancy": 69.7})
db.insert("country",{"GNP": 11500.00, "Code": "IRQ", "Name": "Iraq", "Region": "Middle East", "Continent": "Asia", "Population": 23115000, "SurfaceArea": 438317.00, "LifeExpectancy": 66.5})
db.insert("country",{"GNP": 8255.00, "Code": "ISL", "Name": "Iceland", "Region": "Nordic Countries", "Continent": "Europe", "Population": 279000, "SurfaceArea": 103000.00, "LifeExpectancy": 79.4})
db.insert("country",{"GNP": 97477.00, "Code": "ISR", "Name": "Israel", "Region": "Middle East", "Continent": "Asia", "Population": 6217000, "SurfaceArea": 21056.00, "LifeExpectancy": 78.6})
db.insert("country",{"GNP": 1161755.00, "Code": "ITA", "Name": "Italy", "Region": "Southern Europe", "Continent": "Europe", "Population": 57680000, "SurfaceArea": 301316.00, "LifeExpectancy": 79.0})
db.insert("country",{"GNP": 3787042.00, "Code": "JPN", "Name": "Japan", "Region": "Eastern Asia", "Continent": "Asia", "Population": 126714000, "SurfaceArea": 377829.00, "LifeExpectancy": 80.7})
db.insert("country",{"GNP": 42168.00, "Code": "UKR", "Name": "Ukraine", "Region": "Eastern Europe", "Continent": "Europe", "Population": 50456000, "SurfaceArea": 603700.00, "LifeExpectancy": 66.0})
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
db.insert("city",{"ID": 91, "Name": "Malvinas Argentinas", "Population": 290335, "CountryCode": "ARG"})
db.insert("city",{"ID": 92, "Name": "Vicente López", "Population": 288341, "CountryCode": "ARG"})
db.insert("city",{"ID": 93, "Name": "Berazategui", "Population": 276916, "CountryCode": "ARG"})
db.insert("city",{"ID": 94, "Name": "Corrientes", "Population": 258103, "CountryCode": "ARG"})
db.insert("city",{"ID": 95, "Name": "San Miguel", "Population": 248700, "CountryCode": "ARG"})
db.insert("city",{"ID": 96, "Name": "Bahía Blanca", "Population": 239810, "CountryCode": "ARG"})
db.insert("city",{"ID": 97, "Name": "Esteban Echeverría", "Population": 235760, "CountryCode": "ARG"})
db.insert("city",{"ID": 98, "Name": "Resistencia", "Population": 229212, "CountryCode": "ARG"})
db.insert("city",{"ID": 99, "Name": "José C. Paz", "Population": 221754, "CountryCode": "ARG"})
db.insert("city",{"ID": 100, "Name": "Paraná", "Population": 207041, "CountryCode": "ARG"})

db.delete("city",{"ID":90})
db.delete("city",{"ID":2})
db.delete("city",{"CountryCode":'ARG', "Population":[0, 200000]})
db.delete("city",{"Name":'Resistencia'})
db.update("city",{"Population":207000}, {"Name":'Paraná'})

db.delete("city",{"ID": 91})
db.delete("city",{"ID": 3})
db.delete("city",{"CountryCode":'ARG', "Population":[0, 300000]})
db.delete("city",{"Name":'Bahía Blanca'})
db.update("city",{"Population":237000}, {"Name":'José C. Paz'})



db.insert("city",{"ID": 128, "Name": "Vanadzor", "Population": 172700, "CountryCode": "ARM"})
db.insert("city",{"ID": 129, "Name": "Oranjestad", "Population": 29034, "CountryCode": "ABW"})
db.insert("city",{"ID": 130, "Name": "Sydney", "Population": 3276207, "CountryCode": "AUS"})
db.insert("city",{"ID": 131, "Name": "Melbourne", "Population": 2865329, "CountryCode": "AUS"})
db.insert("city",{"ID": 132, "Name": "Brisbane", "Population": 1291117, "CountryCode": "AUS"})
db.insert("city",{"ID": 133, "Name": "Perth", "Population": 1096829, "CountryCode": "AUS"})
db.insert("city",{"ID": 134, "Name": "Adelaide", "Population": 978100, "CountryCode": "AUS"})
db.insert("city",{"ID": 135, "Name": "Canberra", "Population": 322723, "CountryCode": "AUS"})
db.insert("city",{"ID": 136, "Name": "Gold Coast", "Population": 311932, "CountryCode": "AUS"})
db.insert("city",{"ID": 137, "Name": "Newcastle", "Population": 270324, "CountryCode": "AUS"})
db.insert("city",{"ID": 138, "Name": "Central Coast", "Population": 227657, "CountryCode": "AUS"})
db.insert("city",{"ID": 139, "Name": "Wollongong", "Population": 219761, "CountryCode": "AUS"})
db.insert("city",{"ID": 140, "Name": "Hobart", "Population": 126118, "CountryCode": "AUS"})
db.insert("city",{"ID": 141, "Name": "Geelong", "Population": 125382, "CountryCode": "AUS"})
db.insert("city",{"ID": 142, "Name": "Townsville", "Population": 109914, "CountryCode": "AUS"})
db.insert("city",{"ID": 143, "Name": "Cairns", "Population": 92273, "CountryCode": "AUS"})
db.insert("city",{"ID": 144, "Name": "Bakı", "Population": 1787800, "CountryCode": "AZE"})
db.insert("city",{"ID": 145, "Name": "Gəncə", "Population": 299300, "CountryCode": "AZE"})
db.insert("city",{"ID": 146, "Name": "Sumqayıt", "Population": 283000, "CountryCode": "AZE"})
db.insert("city",{"ID": 147, "Name": "Mingəçevir", "Population": 93900, "CountryCode": "AZE"})
db.insert("city",{"ID": 148, "Name": "Nassau", "Population": 172000, "CountryCode": "BHS"})
db.insert("city",{"ID": 149, "Name": "al-Manama", "Population": 148000, "CountryCode": "BHR"})
db.insert("city",{"ID": 150, "Name": "Dhaka", "Population": 3612850, "CountryCode": "BGD"})
db.insert("city",{"ID": 151, "Name": "Chittagong", "Population": 1392860, "CountryCode": "BGD"})
db.insert("city",{"ID": 152, "Name": "Khulna", "Population": 663340, "CountryCode": "BGD"})
db.insert("city",{"ID": 153, "Name": "Rajshahi", "Population": 294056, "CountryCode": "BGD"})
db.insert("city",{"ID": 154, "Name": "Narayanganj", "Population": 202134, "CountryCode": "BGD"})
db.insert("city",{"ID": 155, "Name": "Rangpur", "Population": 191398, "CountryCode": "BGD"})
db.insert("city",{"ID": 156, "Name": "Mymensingh", "Population": 188713, "CountryCode": "BGD"})
db.insert("city",{"ID": 157, "Name": "Barisal", "Population": 170232, "CountryCode": "BGD"})
db.insert("city",{"ID": 158, "Name": "Tungi", "Population": 168702, "CountryCode": "BGD"})
db.insert("city",{"ID": 159, "Name": "Jessore", "Population": 139710, "CountryCode": "BGD"})
db.insert("city",{"ID": 160, "Name": "Comilla", "Population": 135313, "CountryCode": "BGD"})
db.insert("city",{"ID": 161, "Name": "Nawabganj", "Population": 130577, "CountryCode": "BGD"})
db.insert("city",{"ID": 162, "Name": "Dinajpur", "Population": 127815, "CountryCode": "BGD"})
db.insert("city",{"ID": 163, "Name": "Bogra", "Population": 120170, "CountryCode": "BGD"})
db.insert("city",{"ID": 164, "Name": "Sylhet", "Population": 117396, "CountryCode": "BGD"})
db.insert("city",{"ID": 165, "Name": "Brahmanbaria", "Population": 109032, "CountryCode": "BGD"})
db.insert("city",{"ID": 166, "Name": "Tangail", "Population": 106004, "CountryCode": "BGD"})
db.insert("city",{"ID": 167, "Name": "Jamalpur", "Population": 103556, "CountryCode": "BGD"})
db.insert("city",{"ID": 168, "Name": "Pabna", "Population": 103277, "CountryCode": "BGD"})
db.insert("city",{"ID": 169, "Name": "Naogaon", "Population": 101266, "CountryCode": "BGD"})
db.insert("city",{"ID": 170, "Name": "Sirajganj", "Population": 99669, "CountryCode": "BGD"})
db.insert("city",{"ID": 171, "Name": "Narsinghdi", "Population": 98342, "CountryCode": "BGD"})
db.insert("city",{"ID": 172, "Name": "Saidpur", "Population": 96777, "CountryCode": "BGD"})
db.insert("city",{"ID": 173, "Name": "Gazipur", "Population": 96717, "CountryCode": "BGD"})
db.insert("city",{"ID": 174, "Name": "Bridgetown", "Population": 6070, "CountryCode": "BRB"})
db.insert("city",{"ID": 175, "Name": "Antwerpen", "Population": 446525, "CountryCode": "BEL"})
db.insert("city",{"ID": 176, "Name": "Gent", "Population": 224180, "CountryCode": "BEL"})
db.insert("city",{"ID": 177, "Name": "Charleroi", "Population": 200827, "CountryCode": "BEL"})
db.insert("city",{"ID": 178, "Name": "Liège", "Population": 185639, "CountryCode": "BEL"})
db.insert("city",{"ID": 179, "Name": "Bruxelles [Brussel]", "Population": 133859, "CountryCode": "BEL"})
db.insert("city",{"ID": 180, "Name": "Brugge", "Population": 116246, "CountryCode": "BEL"})
db.insert("city",{"ID": 181, "Name": "Schaerbeek", "Population": 105692, "CountryCode": "BEL"})


db.insert("city",{"ID": 1990, "Name": "Xianyang", "Population": 352125, "CountryCode": "CHN"})
db.insert("city",{"ID": 1991, "Name": "Tai´an", "Population": 350696, "CountryCode": "CHN"})
db.insert("city",{"ID": 1992, "Name": "Chifeng", "Population": 350077, "CountryCode": "CHN"})
db.insert("city",{"ID": 1993, "Name": "Shaoguan", "Population": 350043, "CountryCode": "CHN"})
db.insert("city",{"ID": 1994, "Name": "Nantong", "Population": 343341, "CountryCode": "CHN"})
db.insert("city",{"ID": 1995, "Name": "Leshan", "Population": 341128, "CountryCode": "CHN"})
db.insert("city",{"ID": 1996, "Name": "Baoji", "Population": 337765, "CountryCode": "CHN"})
db.insert("city",{"ID": 1997, "Name": "Linyi", "Population": 324720, "CountryCode": "CHN"})
db.insert("city",{"ID": 1998, "Name": "Tonghua", "Population": 324600, "CountryCode": "CHN"})
db.insert("city",{"ID": 1999, "Name": "Siping", "Population": 317223, "CountryCode": "CHN"})
db.insert("city",{"ID": 2000, "Name": "Changzhi", "Population": 317144, "CountryCode": "CHN"})
db.insert("city",{"ID": 2001, "Name": "Tengzhou", "Population": 315083, "CountryCode": "CHN"})
db.insert("city",{"ID": 2002, "Name": "Chaozhou", "Population": 313469, "CountryCode": "CHN"})
db.insert("city",{"ID": 2003, "Name": "Yangzhou", "Population": 312892, "CountryCode": "CHN"})
db.insert("city",{"ID": 2004, "Name": "Dongwan", "Population": 308669, "CountryCode": "CHN"})
db.insert("city",{"ID": 2005, "Name": "Ma´anshan", "Population": 305421, "CountryCode": "CHN"})
db.insert("city",{"ID": 2006, "Name": "Foshan", "Population": 303160, "CountryCode": "CHN"})
db.insert("city",{"ID": 2007, "Name": "Yueyang", "Population": 302800, "CountryCode": "CHN"})
db.insert("city",{"ID": 2008, "Name": "Xingtai", "Population": 302789, "CountryCode": "CHN"})
db.insert("city",{"ID": 2009, "Name": "Changde", "Population": 301276, "CountryCode": "CHN"})


db.delete("city",{"ID":3011})
db.delete("city",{"ID":2000})
db.delete("city",{"CountryCode":'CHN', "Population":[0, 310000]})
db.update("city",{"Population":1790000}, {"ID":1})
db.update("city",{"Population":127900}, {"Name":'Mazar-e-Sharif'})

db.delete("city",{"ID": 3012})
db.delete("city",{"ID": 2001})
db.delete("city",{"CountryCode":'USA', "Population":[0, 300000]})
db.update("city",{"Population":240000}, {"ID":2})
db.update("city",{"Population":310000}, {"Name":'Tampa'})

db.insert("countrylanguage",{"Language": "Dutch", "IsOfficial": "T", "Percentage": 5.3, "CountryCode": "ABW"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "F", "Percentage": 9.5, "CountryCode": "ABW"})
db.insert("countrylanguage",{"Language": "Papiamento", "IsOfficial": "F", "Percentage": 76.7, "CountryCode": "ABW"})
db.insert("countrylanguage",{"Language": "Spanish", "IsOfficial": "F", "Percentage": 7.4, "CountryCode": "ABW"})
db.insert("countrylanguage",{"Language": "Balochi", "IsOfficial": "F", "Percentage": 0.9, "CountryCode": "AFG"})

db.delete("countrylanguage",{"CountryCode":'AND'})
db.delete("countrylanguage", {"Language":'Mbundu'})
db.update("countrylanguage",{ "Percentage": 1.0}, {"Language":'English', "CountryCode":'AIA'})



db.delete("countrylanguage",{"CountryCode":'AGO'})
db.delete("countrylanguage", {"Language":'Luvale'})
db.update("countrylanguage",{ "Percentage": 2.0}, {"Language":'Turkmenian', "CountryCode":'AFG'})

db.insert("countrylanguage",{"Language": "Dutch", "IsOfficial": "T", "Percentage": 0.0, "CountryCode": "ANT"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "F", "Percentage": 7.8, "CountryCode": "ANT"})
db.insert("countrylanguage",{"Language": "Papiamento", "IsOfficial": "T", "Percentage": 86.2, "CountryCode": "ANT"})
db.insert("countrylanguage",{"Language": "Arabic", "IsOfficial": "T", "Percentage": 42.0, "CountryCode": "ARE"})
db.insert("countrylanguage",{"Language": "Hindi", "IsOfficial": "F", "Percentage": 0.0, "CountryCode": "ARE"})
db.insert("countrylanguage",{"Language": "Indian Languages", "IsOfficial": "F", "Percentage": 0.3, "CountryCode": "ARG"})
db.insert("countrylanguage",{"Language": "Italian", "IsOfficial": "F", "Percentage": 1.7, "CountryCode": "ARG"})
db.insert("countrylanguage",{"Language": "Spanish", "IsOfficial": "T", "Percentage": 96.8, "CountryCode": "ARG"})
db.insert("countrylanguage",{"Language": "Armenian", "IsOfficial": "T", "Percentage": 93.4, "CountryCode": "ARM"})
db.insert("countrylanguage",{"Language": "Azerbaijani", "IsOfficial": "F", "Percentage": 2.6, "CountryCode": "ARM"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "T", "Percentage": 3.1, "CountryCode": "ASM"})
db.insert("countrylanguage",{"Language": "Samoan", "IsOfficial": "T", "Percentage": 90.6, "CountryCode": "ASM"})
db.insert("countrylanguage",{"Language": "Tongan", "IsOfficial": "F", "Percentage": 3.1, "CountryCode": "ASM"})
db.insert("countrylanguage",{"Language": "Creole English", "IsOfficial": "F", "Percentage": 95.7, "CountryCode": "ATG"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "T", "Percentage": 0.0, "CountryCode": "ATG"})
db.insert("countrylanguage",{"Language": "Arabic", "IsOfficial": "F", "Percentage": 1.0, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "Canton Chinese", "IsOfficial": "F", "Percentage": 1.1, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "T", "Percentage": 81.2, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "German", "IsOfficial": "F", "Percentage": 0.6, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "Greek", "IsOfficial": "F", "Percentage": 1.6, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "Italian", "IsOfficial": "F", "Percentage": 2.2, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "Serbo-Croatian", "IsOfficial": "F", "Percentage": 0.6, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "Vietnamese", "IsOfficial": "F", "Percentage": 0.8, "CountryCode": "AUS"})
db.insert("countrylanguage",{"Language": "Czech", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "German", "IsOfficial": "T", "Percentage": 92.0, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Hungarian", "IsOfficial": "F", "Percentage": 0.4, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Polish", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Romanian", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Serbo-Croatian", "IsOfficial": "F", "Percentage": 2.2, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Slovene", "IsOfficial": "F", "Percentage": 0.4, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Turkish", "IsOfficial": "F", "Percentage": 1.5, "CountryCode": "AUT"})
db.insert("countrylanguage",{"Language": "Armenian", "IsOfficial": "F", "Percentage": 2.0, "CountryCode": "AZE"})
db.insert("countrylanguage",{"Language": "Azerbaijani", "IsOfficial": "T", "Percentage": 89.0, "CountryCode": "AZE"})
db.insert("countrylanguage",{"Language": "Lezgian", "IsOfficial": "F", "Percentage": 2.3, "CountryCode": "AZE"})
db.insert("countrylanguage",{"Language": "Russian", "IsOfficial": "F", "Percentage": 3.0, "CountryCode": "AZE"})
db.insert("countrylanguage",{"Language": "French", "IsOfficial": "T", "Percentage": 0.0, "CountryCode": "BDI"})
db.insert("countrylanguage",{"Language": "Kirundi", "IsOfficial": "T", "Percentage": 98.1, "CountryCode": "BDI"})
db.insert("countrylanguage",{"Language": "Swahili", "IsOfficial": "F", "Percentage": 0.0, "CountryCode": "BDI"})
db.insert("countrylanguage",{"Language": "Arabic", "IsOfficial": "F", "Percentage": 1.6, "CountryCode": "BEL"})
db.insert("countrylanguage",{"Language": "Dutch", "IsOfficial": "T", "Percentage": 59.2, "CountryCode": "BEL"})
db.insert("countrylanguage",{"Language": "French", "IsOfficial": "T", "Percentage": 32.6, "CountryCode": "BEL"})
db.insert("countrylanguage",{"Language": "German", "IsOfficial": "T", "Percentage": 1.0, "CountryCode": "BEL"})
db.insert("countrylanguage",{"Language": "Italian", "IsOfficial": "F", "Percentage": 2.4, "CountryCode": "BEL"})
db.insert("countrylanguage",{"Language": "Turkish", "IsOfficial": "F", "Percentage": 0.9, "CountryCode": "BEL"})
db.insert("countrylanguage",{"Language": "Adja", "IsOfficial": "F", "Percentage": 11.1, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Aizo", "IsOfficial": "F", "Percentage": 8.7, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Bariba", "IsOfficial": "F", "Percentage": 8.7, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Fon", "IsOfficial": "F", "Percentage": 39.8, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Ful", "IsOfficial": "F", "Percentage": 5.6, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Joruba", "IsOfficial": "F", "Percentage": 12.2, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Somba", "IsOfficial": "F", "Percentage": 6.7, "CountryCode": "BEN"})
db.insert("countrylanguage",{"Language": "Busansi", "IsOfficial": "F", "Percentage": 3.5, "CountryCode": "BFA"})
db.insert("countrylanguage",{"Language": "Dagara", "IsOfficial": "F", "Percentage": 3.1, "CountryCode": "BFA"})
db.insert("countrylanguage",{"Language": "Dyula", "IsOfficial": "F", "Percentage": 2.6, "CountryCode": "BFA"})
db.insert("countrylanguage",{"Language": "Ful", "IsOfficial": "F", "Percentage": 9.7, "CountryCode": "BFA"})
db.insert("countrylanguage",{"Language": "Gurma", "IsOfficial": "F", "Percentage": 5.7, "CountryCode": "BFA"})
db.insert("countrylanguage",{"Language": "Mossi", "IsOfficial": "F", "Percentage": 50.2, "CountryCode": "BFA"})
db.insert("countrylanguage",{"Language": "Bengali", "IsOfficial": "T", "Percentage": 97.7, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Chakma", "IsOfficial": "F", "Percentage": 0.4, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Garo", "IsOfficial": "F", "Percentage": 0.1, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Khasi", "IsOfficial": "F", "Percentage": 0.1, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Marma", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Santhali", "IsOfficial": "F", "Percentage": 0.1, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Tripuri", "IsOfficial": "F", "Percentage": 0.1, "CountryCode": "BGD"})
db.insert("countrylanguage",{"Language": "Bulgariana", "IsOfficial": "T", "Percentage": 83.2, "CountryCode": "BGR"})
db.insert("countrylanguage",{"Language": "Macedonian", "IsOfficial": "F", "Percentage": 2.6, "CountryCode": "BGR"})
db.insert("countrylanguage",{"Language": "Romani", "IsOfficial": "F", "Percentage": 3.7, "CountryCode": "BGR"})
db.insert("countrylanguage",{"Language": "Turkish", "IsOfficial": "F", "Percentage": 9.4, "CountryCode": "BGR"})
db.insert("countrylanguage",{"Language": "Arabic", "IsOfficial": "T", "Percentage": 67.7, "CountryCode": "BHR"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "F", "Percentage": 0.0, "CountryCode": "BHR"})



db.delete("countrylanguage", {"CountryCode":'BRA'})

db.delete("countrylanguage", {"CountryCode":'BLZ'})


db.insert("countrylanguage",{"Language": "Ndebele", "IsOfficial": "F", "Percentage": 1.3, "CountryCode": "BWA"})
db.insert("countrylanguage",{"Language": "San", "IsOfficial": "F", "Percentage": 3.5, "CountryCode": "BWA"})
db.insert("countrylanguage",{"Language": "Shona", "IsOfficial": "F", "Percentage": 12.3, "CountryCode": "BWA"})
db.insert("countrylanguage",{"Language": "Tswana", "IsOfficial": "F", "Percentage": 75.5, "CountryCode": "BWA"})
db.insert("countrylanguage",{"Language": "Banda", "IsOfficial": "F", "Percentage": 23.5, "CountryCode": "CAF"})
db.insert("countrylanguage",{"Language": "Gbaya", "IsOfficial": "F", "Percentage": 23.8, "CountryCode": "CAF"})
db.insert("countrylanguage",{"Language": "Mandjia", "IsOfficial": "F", "Percentage": 14.8, "CountryCode": "CAF"})
db.insert("countrylanguage",{"Language": "Mbum", "IsOfficial": "F", "Percentage": 6.4, "CountryCode": "CAF"})
db.insert("countrylanguage",{"Language": "Ngbaka", "IsOfficial": "F", "Percentage": 7.5, "CountryCode": "CAF"})
db.insert("countrylanguage",{"Language": "Sara", "IsOfficial": "F", "Percentage": 6.4, "CountryCode": "CAF"})
db.insert("countrylanguage",{"Language": "Chinese", "IsOfficial": "F", "Percentage": 2.5, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Dutch", "IsOfficial": "F", "Percentage": 0.5, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "English", "IsOfficial": "T", "Percentage": 60.4, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Eskimo Languages", "IsOfficial": "F", "Percentage": 0.1, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "French", "IsOfficial": "T", "Percentage": 23.4, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "German", "IsOfficial": "F", "Percentage": 1.6, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Italian", "IsOfficial": "F", "Percentage": 1.7, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Polish", "IsOfficial": "F", "Percentage": 0.7, "CountryCode": "CAN"})
db.insert("countrylanguage",{"Language": "Portuguese", "IsOfficial": "F", "Percentage": 0.7, "CountryCode": "CAN"})
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
db.insert("countrylanguage",{"Language": "Puyi", "IsOfficial": "F", "Percentage": 0.2, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Tibetan", "IsOfficial": "F", "Percentage": 0.4, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Tujia", "IsOfficial": "F", "Percentage": 0.5, "CountryCode": "CHN"})
db.insert("countrylanguage",{"Language": "Uighur", "IsOfficial": "F", "Percentage": 0.6, "CountryCode": "CHN"})


db.update("countrylanguage", {"Percentage": 91.8}, {"CountryCode":'CHN', "Language":'Chinese'})
db.delete("countrylanguage", {"CountryCode":'CAN', "Language":'Italian'})
    

db.update("countrylanguage", {"Percentage": 8.0}, {"CountryCode":'CHE', "Language":'Italian'})
db.delete("countrylanguage", {"CountryCode":'CAN', "Language":'Spanish'})




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






