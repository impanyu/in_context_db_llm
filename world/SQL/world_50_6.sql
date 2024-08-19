-- MySQL dump 10.13  Distrib 8.0.19, for osx10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: world
-- ------------------------------------------------------
-- Server version	8.0.19-debug

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @old_autocommit=@@autocommit;

--
-- Current Database: `world`
--

/*!40000 DROP DATABASE IF EXISTS `world`*/;

CREATE DATABASE `world` DEFAULT CHARACTER SET utf8mb4;

USE `world`;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` char(35) NOT NULL DEFAULT '',
  `CountryCode` char(3) NOT NULL DEFAULT '',
  `District` char(20) NOT NULL DEFAULT '',
  `Population` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `CountryCode` (`CountryCode`),
  CONSTRAINT `city_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--
-- ORDER BY:  `ID`

set autocommit=0;
INSERT INTO `city` VALUES (1,'Kabul','AFG','Kabol',1780000);
INSERT INTO `city` VALUES (2,'Qandahar','AFG','Qandahar',237500);
INSERT INTO `city` VALUES (3,'Herat','AFG','Herat',186800);
INSERT INTO `city` VALUES (4,'Mazar-e-Sharif','AFG','Balkh',127800);
INSERT INTO `city` VALUES (33,'Willemstad','ANT','Curaçao',2345);
INSERT INTO `city` VALUES (34,'Tirana','ALB','Tirana',270000);



INSERT INTO `city` VALUES (82,'Salta','ARG','Salta',367550);
INSERT INTO `city` VALUES (83,'Moreno','ARG','Buenos Aires',356993);
INSERT INTO `city` VALUES (84,'Santa Fé','ARG','Santa Fé',353063);
INSERT INTO `city` VALUES (85,'Avellaneda','ARG','Buenos Aires',353046);
INSERT INTO `city` VALUES (86,'Tres de Febrero','ARG','Buenos Aires',352311);
INSERT INTO `city` VALUES (87,'Morón','ARG','Buenos Aires',349246);

INSERT INTO `city` VALUES (90,'Tigre','ARG','Buenos Aires',296226);



DELETE FROM `city` WHERE `ID` = 3;
DELETE FROM `city` WHERE `CountryCode` = 'ARG' and `Population` < 300000;













commit;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `Code` char(3) NOT NULL DEFAULT '',
  `Name` char(52) NOT NULL DEFAULT '',
  `Continent` enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
  `Region` char(26) NOT NULL DEFAULT '',
  `SurfaceArea` decimal(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` smallint DEFAULT NULL,
  `Population` int NOT NULL DEFAULT '0',
  `LifeExpectancy` decimal(3,1) DEFAULT NULL,
  `GNP` decimal(10,2) DEFAULT NULL,
  `GNPOld` decimal(10,2) DEFAULT NULL,
  `LocalName` char(45) NOT NULL DEFAULT '',
  `GovernmentForm` char(45) NOT NULL DEFAULT '',
  `HeadOfState` char(60) DEFAULT NULL,
  `Capital` int DEFAULT NULL,
  `Code2` char(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--
-- ORDER BY:  `Code`

set autocommit=0;
INSERT INTO `country` VALUES ('ABW','Aruba','North America','Caribbean',193.00,NULL,103000,78.4,828.00,793.00,'Aruba','Nonmetropolitan Territory of The Netherlands','Beatrix',129,'AW');
INSERT INTO `country` VALUES ('AFG','Afghanistan','Asia','Southern and Central Asia',652090.00,1919,22720000,45.9,5976.00,NULL,'Afganistan/Afqanestan','Islamic Emirate','Mohammad Omar',1,'AF');
INSERT INTO `country` VALUES ('AGO','Angola','Africa','Central Africa',1246700.00,1975,12878000,38.3,6648.00,7984.00,'Angola','Republic','José Eduardo dos Santos',56,'AO');
INSERT INTO `country` VALUES ('AIA','Anguilla','North America','Caribbean',96.00,NULL,8000,76.1,63.20,NULL,'Anguilla','Dependent Territory of the UK','Elisabeth II',62,'AI');
INSERT INTO `country` VALUES ('ALB','Albania','Europe','Southern Europe',28748.00,1912,3401200,71.6,3205.00,2500.00,'Shqipëria','Republic','Rexhep Mejdani',34,'AL');
INSERT INTO `country` VALUES ('AND','Andorra','Europe','Southern Europe',468.00,1278,78000,83.5,1630.00,NULL,'Andorra','Parliamentary Coprincipality','',55,'AD');
INSERT INTO `country` VALUES ('ANT','Netherlands Antilles','North America','Caribbean',800.00,NULL,217000,74.7,1941.00,NULL,'Nederlandse Antillen','Nonmetropolitan Territory of The Netherlands','Beatrix',33,'AN');
INSERT INTO `country` VALUES ('ARE','United Arab Emirates','Asia','Middle East',83600.00,1971,2441000,74.1,37966.00,36846.00,'Al-Imarat al-´Arabiya al-Muttahida','Emirate Federation','Zayid bin Sultan al-Nahayan',65,'AE');
INSERT INTO `country` VALUES ('ARG','Argentina','South America','South America',2780400.00,1816,37032000,75.1,340238.00,323310.00,'Argentina','Federal Republic','Fernando de la Rúa',69,'AR');
INSERT INTO `country` VALUES ('ARM','Armenia','Asia','Middle East',29800.00,1991,3520000,66.4,1813.00,1627.00,'Hajastan','Republic','Robert Kotšarjan',126,'AM');
INSERT INTO `country` VALUES ('ASM','American Samoa','Oceania','Polynesia',199.00,NULL,68000,75.1,334.00,NULL,'Amerika Samoa','US Territory','George W. Bush',54,'AS');
INSERT INTO `country` VALUES ('ATA','Antarctica','Antarctica','Antarctica',13120000.00,NULL,0,NULL,0.00,NULL,'–','Co-administrated','',NULL,'AQ');
INSERT INTO `country` VALUES ('ATF','French Southern territories','Antarctica','Antarctica',7780.00,NULL,0,NULL,0.00,NULL,'Terres australes françaises','Nonmetropolitan Territory of France','Jacques Chirac',NULL,'TF');
INSERT INTO `country` VALUES ('ATG','Antigua and Barbuda','North America','Caribbean',442.00,1981,68000,70.5,612.00,584.00,'Antigua and Barbuda','Constitutional Monarchy','Elisabeth II',63,'AG');
INSERT INTO `country` VALUES ('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation','Elisabeth II',135,'AU');
INSERT INTO `country` VALUES ('AUT','Austria','Europe','Western Europe',83859.00,1918,8091800,77.7,211860.00,206025.00,'Österreich','Federal Republic','Thomas Klestil',1523,'AT');
INSERT INTO `country` VALUES ('AZE','Azerbaijan','Asia','Middle East',86600.00,1991,7734000,62.9,4127.00,4100.00,'Azərbaycan','Republic','İlham Əliyev',144,'AZ');
INSERT INTO `country` VALUES ('BDI','Burundi','Africa','Eastern Africa',27834.00,1962,6695000,46.2,903.00,982.00,'Burundi/Uburundi','Republic','Pierre Buyoya',552,'BI');
INSERT INTO `country` VALUES ('BEL','Belgium','Europe','Western Europe',30518.00,1830,10239000,77.8,249704.00,243948.00,'België/Belgique','Constitutional Monarchy, Federation','Albert II',179,'BE');
INSERT INTO `country` VALUES ('BEN','Benin','Africa','Western Africa',112622.00,1960,6097000,50.2,2357.00,2141.00,'Bénin','Republic','Mathieu Kérékou',187,'BJ');
INSERT INTO `country` VALUES ('BFA','Burkina Faso','Africa','Western Africa',274000.00,1960,11937000,46.7,2425.00,2201.00,'Burkina Faso','Republic','Blaise Compaoré',549,'BF');
INSERT INTO `country` VALUES ('BGD','Bangladesh','Asia','Southern and Central Asia',143998.00,1971,129155000,60.2,32852.00,31966.00,'Bangladesh','Republic','Shahabuddin Ahmad',150,'BD');
INSERT INTO `country` VALUES ('BGR','Bulgaria','Europe','Eastern Europe',110994.00,1908,8190900,70.9,12178.00,10169.00,'Balgarija','Republic','Petar Stojanov',539,'BG');
INSERT INTO `country` VALUES ('BHR','Bahrain','Asia','Middle East',694.00,1971,617000,73.0,6366.00,6097.00,'Al-Bahrayn','Monarchy (Emirate)','Hamad ibn Isa al-Khalifa',149,'BH');
INSERT INTO `country` VALUES ('BHS','Bahamas','North America','Caribbean',13878.00,1973,307000,71.1,3527.00,3347.00,'The Bahamas','Constitutional Monarchy','Elisabeth II',148,'BS');
INSERT INTO `country` VALUES ('BIH','Bosnia and Herzegovina','Europe','Southern Europe',51197.00,1992,3972000,71.5,2841.00,NULL,'Bosna i Hercegovina','Federal Republic','Ante Jelavic',201,'BA');
INSERT INTO `country` VALUES ('BLR','Belarus','Europe','Eastern Europe',207600.00,1991,10236000,68.0,13714.00,NULL,'Belarus','Republic','Aljaksandr Lukašenka',3520,'BY');
INSERT INTO `country` VALUES ('BLZ','Belize','North America','Central America',22696.00,1981,241000,70.9,630.00,616.00,'Belize','Constitutional Monarchy','Elisabeth II',185,'BZ');
INSERT INTO `country` VALUES ('BMU','Bermuda','North America','North America',53.00,NULL,65000,76.9,2328.00,2190.00,'Bermuda','Dependent Territory of the UK','Elisabeth II',191,'BM');
INSERT INTO `country` VALUES ('BOL','Bolivia','South America','South America',1098581.00,1825,8329000,63.7,8571.00,7967.00,'Bolivia','Republic','Hugo Bánzer Suárez',194,'BO');
INSERT INTO `country` VALUES ('BRA','Brazil','South America','South America',8547403.00,1822,170115000,62.9,776739.00,804108.00,'Brasil','Federal Republic','Fernando Henrique Cardoso',211,'BR');
INSERT INTO `country` VALUES ('BRB','Barbados','North America','Caribbean',430.00,1966,270000,73.0,2223.00,2186.00,'Barbados','Constitutional Monarchy','Elisabeth II',174,'BB');
INSERT INTO `country` VALUES ('BRN','Brunei','Asia','Southeast Asia',5765.00,1984,328000,73.6,11705.00,12460.00,'Brunei Darussalam','Monarchy (Sultanate)','Haji Hassan al-Bolkiah',538,'BN');
INSERT INTO `country` VALUES ('BTN','Bhutan','Asia','Southern and Central Asia',47000.00,1910,2124000,52.4,372.00,383.00,'Druk-Yul','Monarchy','Jigme Singye Wangchuk',192,'BT');
INSERT INTO `country` VALUES ('BVT','Bouvet Island','Antarctica','Antarctica',59.00,NULL,0,NULL,0.00,NULL,'Bouvetøya','Dependent Territory of Norway','Harald V',NULL,'BV');
INSERT INTO `country` VALUES ('BWA','Botswana','Africa','Southern Africa',581730.00,1966,1622000,39.3,4834.00,4935.00,'Botswana','Republic','Festus G. Mogae',204,'BW');
INSERT INTO `country` VALUES ('CAF','Central African Republic','Africa','Central Africa',622984.00,1960,3615000,44.0,1054.00,993.00,'Centrafrique/Bê-Afrîka','Republic','Ange-Félix Patassé',1889,'CF');
INSERT INTO `country` VALUES ('CAN','Canada','North America','North America',9970610.00,1867,31147000,79.4,598862.00,625626.00,'Canada','Constitutional Monarchy, Federation','Elisabeth II',1822,'CA');
INSERT INTO `country` VALUES ('CCK','Cocos (Keeling) Islands','Oceania','Australia and New Zealand',14.00,NULL,600,NULL,0.00,NULL,'Cocos (Keeling) Islands','Territory of Australia','Elisabeth II',2317,'CC');
INSERT INTO `country` VALUES ('CHE','Switzerland','Europe','Western Europe',41284.00,1499,7160400,79.6,264478.00,256092.00,'Schweiz/Suisse/Svizzera/Svizra','Federation','Adolf Ogi',3248,'CH');
INSERT INTO `country` VALUES ('CHL','Chile','South America','South America',756626.00,1810,15211000,75.7,72949.00,75780.00,'Chile','Republic','Ricardo Lagos Escobar',554,'CL');
INSERT INTO `country` VALUES ('CHN','China','Asia','Eastern Asia',9572900.00,-1523,1277558000,71.4,982268.00,917719.00,'Zhongquo','People\'sRepublic','Jiang Zemin',1891,'CN');
INSERT INTO `country` VALUES ('CIV','Côte d’Ivoire','Africa','Western Africa',322463.00,1960,14786000,45.2,11345.00,10285.00,'Côte d’Ivoire','Republic','Laurent Gbagbo',2814,'CI');

DELETE FROM `country` WHERE `Code` = 'DOM';
DELETE FROM `country` WHERE `Code` = 'DJI';




INSERT INTO `country` VALUES ('USA','United States','North America','North America',9363520.00,1776,278357000,77.1,8510700.00,8110900.00,'United States','Federal Republic','George W. Bush',3813,'US');
INSERT INTO `country` VALUES ('JPN','Japan','Asia','Eastern Asia',377829.00,-660,126714000,80.7,3787042.00,4192638.00,'Nihon/Nippon','Constitutional Monarchy','Akihito',1532,'JP');






commit;

--
-- Table structure for table `countrylanguage`
--

DROP TABLE IF EXISTS `countrylanguage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countrylanguage` (
  `CountryCode` char(3) NOT NULL DEFAULT '',
  `Language` char(30) NOT NULL DEFAULT '',
  `IsOfficial` enum('T','F') NOT NULL DEFAULT 'F',
  `Percentage` decimal(4,1) NOT NULL DEFAULT '0.0',
  PRIMARY KEY (`CountryCode`,`Language`),
  KEY `CountryCode` (`CountryCode`),
  CONSTRAINT `countryLanguage_ibfk_1` FOREIGN KEY (`CountryCode`) REFERENCES `country` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countrylanguage`
--
-- ORDER BY:  `CountryCode`,`Language`

set autocommit=0;










INSERT INTO `countrylanguage` VALUES ('CAN','Punjabi','F',0.7);
INSERT INTO `countrylanguage` VALUES ('CAN','Spanish','F',0.7);
INSERT INTO `countrylanguage` VALUES ('CAN','Ukrainian','F',0.6);
INSERT INTO `countrylanguage` VALUES ('CCK','English','T',0.0);
INSERT INTO `countrylanguage` VALUES ('CCK','Malay','F',0.0);
INSERT INTO `countrylanguage` VALUES ('CHE','French','T',19.2);
INSERT INTO `countrylanguage` VALUES ('CHE','German','T',63.6);
INSERT INTO `countrylanguage` VALUES ('CHE','Italian','T',7.7);
INSERT INTO `countrylanguage` VALUES ('CHE','Romansh','T',0.6);
INSERT INTO `countrylanguage` VALUES ('CHL','Aimará','F',0.5);
INSERT INTO `countrylanguage` VALUES ('CHL','Araucan','F',9.6);
INSERT INTO `countrylanguage` VALUES ('CHL','Rapa nui','F',0.2);
INSERT INTO `countrylanguage` VALUES ('CHL','Spanish','T',89.7);
INSERT INTO `countrylanguage` VALUES ('CHN','Chinese','T',92.0);
INSERT INTO `countrylanguage` VALUES ('CHN','Dong','F',0.2);
INSERT INTO `countrylanguage` VALUES ('CHN','Hui','F',0.8);
INSERT INTO `countrylanguage` VALUES ('CHN','Mantšu','F',0.9);
INSERT INTO `countrylanguage` VALUES ('CHN','Miao','F',0.7);
INSERT INTO `countrylanguage` VALUES ('CHN','Mongolian','F',0.4);



UPDATE `countrylanguage` SET `Percentage` = 91.8 WHERE `CountryCode` = 'CHN' AND `Language` = 'Chinese';
DELETE FROM `countrylanguage` WHERE `CountryCode` = 'CAN' AND `Language` = 'Italian';



commit;

--
-- Dumping events for database 'world'
--

--
-- Dumping routines for database 'world'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
SET autocommit=@old_autocommit;

-- Dump completed on 2020-01-22  9:56:18



/*
Example for few shots:
create a table named 'Custumers' with columns CustomerID	CustomerName	ContactName	Address	City	PostalCode	Country

1. create table Customers (
CustomerID int NOT NULL AUTO_INCREMENT, 
CustomerName varchar(255) NOT NULL, 
ContactName varchar(255) NOT NULL, 
Address varchar(255) NOT NULL, 
City varchar(255) NOT NULL, 
PostalCode varchar(255) NOT NULL, 
Country varchar(255) NOT NULL,
primary key (CustomerID)
);

-- create a table named 'Orders' with columns OrderID	CustomerID	OrderDate	
2. create table Orders (
OrderID int NOT NULL AUTO_INCREMENT,
CustomerID int NOT NULL,
OrderDate date NOT NULL,
primary key (OrderID)
constraint fk_customer  foreign key (CustomerID) references customers(CustomerID)
);

--create a table named 'OrderDetails' with columns OrderDetailID	OrderID	ProductID	Quantity
3. create table OrderDetails (
OrderDetailID int NOT NULL AUTO_INCREMENT,
OrderID int NOT NULL,
ProductID int NOT NULL,
Quantity int NOT NULL,
primary key (OrderDetailID),
constraint fk_order foreign key (OrderID) references Orders(OrderID),
constraint fk_product foreign key (ProductID) references Products(ProductID)
);


-- create a table named 'products' with columns ProductID	ProductName	Unit Price
4. create table Products (
ProductID int NOT NULL AUTO_INCREMENT,
ProductName varchar(255) NOT NULL,
Unit varchar(255) NOT NULL,
Price decimal(10,2) NOT NULL,
primary key (ProductID)
);

-- insert a customer with CustomerID = 1, CustomerName = 'Alfreds Futterkiste', ContactName = 'Maria Anders', Address = 'Obere Str. 57', City = 'Berlin', PostalCode = '12209', Country = 'Germany' into the Customers table
-- insert a customer with CustomerID = 2, CustomerName = 'Ana Trujillo Emparedados y helados', ContactName = 'Ana Trujillo', Address = 'Avda. de la Constitución 2222', City = 'México D.F.', PostalCode = '05021', Country = 'Mexico' into the Customers table
-- insert a customer with CustomerID = 3, CustomerName = 'Antonio Moreno Taquería', ContactName = 'Antonio Moreno', Address = 'Mataderos 2312', City = 'México D.F.', PostalCode = '05023', Country = 'Mexico' into the Customers table
-- insert a customer with CustomerID = 4, CustomerName = 'Around the Horn', ContactName = 'Thomas Hardy', Address = '120 Hanover Sq.', City = 'London', PostalCode = 'WA1 1DP', Country = 'UK' into the Customers table


5. insert into Customers values (1, 'Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany');
6. insert into Customers values (2, 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitución 2222', 'México D.F.', '05021', 'Mexico');
7. insert into Customers values (3, 'Antonio Moreno Taquería', 'Antonio Moreno', 'Mataderos 2312', 'México D.F.', '05023', 'Mexico');
8. insert into Customers values (4, 'Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 'WA1 1DP', 'UK');

-- insert an order with OrderID = 10308, CustomerID = 2, OrderDate = '9/18/1996' into the Orders table
-- insert an order with OrderID = 10365, CustomerID = 3, OrderDate = '11/27/1996' into the Orders table

9. insert into Orders values (10308, 2, '9/18/1996');
10. insert into Orders values (10365, 3, '11/27/1996');

11. delete from Customers where CustomerID = 4;
12. update Orders set OrderDate = '9/19/1996' where OrderID = 10308;

-- insert an order detail with OrderDetailID = 162, OrderID = 10308, ProductID = 69, Quantity = 1 into the OrderDetails table
-- insert an order detail with OrderDetailID = 163, OrderID = 10308, ProductID = 70, Quantity = 5 into the OrderDetails table
-- insert an order detail with OrderDetailID = 314, OrderID = 10365, ProductID = 11, Quantity = 24 into the OrderDetails table

13.  insert into OrderDetails values (162, 10308, 69, 1);
14. insert into OrderDetails values (163, 10308, 70, 5);
15. insert into OrderDetails values (314, 10365, 11, 24);

-- insert a product with ProductID = 11, ProductName = 'Queso Cabrales', Unit = '1 kg pkg.', Price = 21 into the Products table
-- insert a product with ProductID = 69, ProductName = 'Gudbrandsdalsost', Unit = '10 kg pkg.', Price = 36 into the Products table
-- insert a product with ProductID = 70, ProductName = 'Outback Lager', Unit = '24 - 355 ml bottles', Price = 15 into the Products table

16. insert into Products values  (11, 'Queso Cabrales', '1 kg pkg.', 21);
17. insert into Products values  (69, 'Gudbrandsdalsost', '10 kg pkg.', 36);
18. insert into Products values  (70, 'Outback Lager', '24 - 355 ml bottles', 15);
19. insert into Products values  (1, 'Chais', '10 boxes x 20 bags', 18);

20. delete from Products where ProductID = 1;

-- For COT:
To answer the queries, you need to execute the above SQL step by step, and figure out the current data in the database.

-- For Few Shots COT:
After executing SQL command 1, an empty Customers table will be created, with columns CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country, and CustomerID as primary key,
After executing SQL command 2, an empty Orders table will be created, with columns OrderID, CustomerID, OrderDate, and OrderID as primary key, and CustomerID as foreign key referencing Customers table,
After executing SQL command 3, an empty OrderDetails table will be created, with columns OrderDetailID, OrderID, ProductID, Quantity, and OrderDetailID as primary key, and OrderID and ProductID as foreign key referencing Orders and Products table respectively,
After executing SQL command 4, an empty Products table will be created, with columns ProductID, ProductName, Unit, Price, and ProductID as primary key,

After executing SQL command 5, the Customers table will contain custermer with CustomerID = 1,
After executing SQL command 6, the Customers table will contain custermer with CustomerID = 2,
After executing SQL command 7, the Customers table will contain custermer with CustomerID = 3,
After executing SQL command 8, the Customers table will contain custermer with CustomerID = 4,
After executing SQL command 9, the Orders table will contain order with OrderID = 10308,
After executing SQL command 10, the Orders table will contain order with OrderID = 10365,
After executing SQL command 11, the Customers table will not contain custermer with CustomerID = 4, and only contain custermer with CustomerID = 1, 2, 3,
After executing SQL command 12, the order with OrderID = 10308 will have OrderDate = '9/19/1996',
After executing SQL command 13, the OrderDetails table will contain order detail with OrderDetailID = 162,
After executing SQL command 14, the OrderDetails table will contain order detail with OrderDetailID = 163,
After executing SQL command 15, the OrderDetails table will contain order detail with OrderDetailID = 314,
After executing SQL command 16, the Products table will contain product with ProductID = 11,
After executing SQL command 17, the Products table will contain product with ProductID = 69,
After executing SQL command 18, the Products table will contain product with ProductID = 70,
After executing SQL command 19, the Products table will contain product with ProductID = 1,
After executing SQL command 20, the Products table will not contain product with ProductID = 1, and only contain product with ProductID = 11, 69, 70.

Now if the user send query:
select CustomerID from Customers Join Orders on Customers.CustomerID = Orders.CustomerID Join OrderDetails on Orders.OrderID = OrderDetails.OrderID Join Products on OrderDetails.ProductID = Products.ProductID where Products.ID = 11;
then the query result is 3.

If the user send query:
select Count(*) from Products where Price > 20;
then the query result is 2.

If the user send query:
select OrderDate from Orders where OrderID = 10308;
then the query result is 9/19/1996.

If the user send query:
insert into Customers values (4, 'Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 'WA1 1DP', 'UK');
then the query will be successfully executed.

If the user send query:
insert into Orders values (10249, 4, '7/5/1996');
then the query will fail, with foreign key constraint violation.

If the user send query:
insert into Products values  (11, 'Queso Cabrales', '1 kg pkg.', 21);
then the query will fail, with primary key constraint violation.

If the user send query:
delete from Customers where CustomerID = 1;
then the query will be successfully executed.

If the user send query:
delete from Orders where OrderID = 10308;
then the query will fail, with foreign key constraint violation.

If the user send query:
update OrderDetails set Quantity = 2 where OrderDetailID = 162;
then the query will be successfully executed.

If the user send query:
update OrderDetails set ProductID = 1 where OrderDetailID = 162;
then the query will fail, with foreign key constraint violation.

*/

/*
Now pretend you are a relational database which has executed the above SQL script. 
Next you will receive a SQL query from the user.
You need to execute the query. 

The SQL query is as follows:
*/


-- select
-- 1. return the names of all countries
-- no filtering.
SELECT Name FROM country
-- 2. return the ID of all the cities in China with population greater than 350000. 
-- Double filtering. Range filtering.
SELECT ID FROM city WHERE CountryCode = 'CHN' AND Population > 350000
-- 3. return the names of all the countries with population greater than 100000000. 
-- Single filtering. Range filtering.
SELECT Name FROM country WHERE Population > 100000000
-- 4. return the languages with percentage greater than 50.0. 
-- Single filtering. Range filtering.
SELECT DISTINCT Language FROM countrylanguage WHERE Percentage > 50.0
-- 5. return the population of the city with ID = 50
-- Single filtering. 
SELECT Population FROM city WHERE ID = 50
-- 6. return the population of Japan
-- Single filtering. 
SELECT Population FROM country WHERE Code = 'JPN'
-- 7. return the names of all the countries in Asia with population greater than 50000000 and life expectancy greater than 60.0
-- triple filtering. Range filtering.
SELECT Name FROM country WHERE Continent = 'Asia' AND Population > 50000000 AND LifeExpectancy > 60.0

-- 8. return the names of all the cities with countrycode = 'CHN', ID in between 50 and 100, population greater than 100000 and less than 500000 
-- triple filtering. Range filtering.
SELECT Name FROM city WHERE CountryCode = 'CHN' AND ID BETWEEN 50 AND 100 AND Population > 100000 AND Population < 500000




-- 9. return the ID for all the cities in countries with population greater than 100000000
-- single filtering. Range filtering. Join.
SELECT city.ID FROM city JOIN country ON city.CountryCode = country.Code WHERE country.Population > 100000000

-- 10. return all the languages with percentage greater than 50.0 in asia
-- single filtering. Range filtering. join.
SELECT DISTINCT countrylanguage.Language FROM countrylanguage JOIN country ON countrylanguage.CountryCode = country.Code WHERE country.Continent = 'Asia' AND countrylanguage.Percentage > 50.0

-- 11. return all the cities in countries in Asia
-- single filtering. Join.
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code WHERE country.Continent = 'Asia'

-- 12. return all the cities with life expectancy greater than 80
-- single filtering. Range filtering. Join.
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code WHERE country.LifeExpectancy > 80.0

-- 13. return the distinct languages in countries in Asia
-- single filtering. Join.
SELECT DISTINCT countrylanguage.Language FROM countrylanguage JOIN country ON countrylanguage.CountryCode = country.Code WHERE country.Continent = 'Asia'

-- 14. return all the cities and the languages spoken in the countries in Asia with population greater than 100000000
-- double filtering. Range filtering. Triple Join.
SELECT city.Name, countrylanguage.Language FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Asia' AND country.Population > 100000000

-- 15. eturn all the cities in countries which English is spoken with percentage greater than 50.0
-- double filtering. Range filtering. Triple Join.
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = 'English' AND countrylanguage.Percentage > 50.0

-- 16. return all the cities in countries with life expectancy greater than 60 and which speak English with percentage greater than 10.0
-- triple filtering. Range filtering. Triple Join.
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE  country.LifeExpectancy > 60.0 AND countrylanguage.Language = 'English' AND countrylanguage.Percentage > 10.0



-- 17. return the number of cities in China
-- single filtering. count.
SELECT COUNT(ID) FROM city WHERE CountryCode = 'CHN'

-- 18. return the number of countries in Asia with population greater than 50000000
-- double filtering. count. range filtering.
SELECT COUNT(Code) FROM country WHERE Continent = 'Asia' AND Population > 50000000

-- 19. return the number of cities with population between 100000 and 500000 with countrycode = 'DZA'
-- double filtering. Range filtering. count.
SELECT COUNT(ID) FROM city WHERE CountryCode = 'DZA' AND Population BETWEEN 100000 AND 500000



-- 20. return the number of distinct languages
-- no filtering. count.
SELECT COUNT(DISTINCT Language) FROM countrylanguage

-- 21. return the number of cities in Algeria
-- single filtering. count. join.
SELECT COUNT(city.ID) FROM city JOIN country ON city.CountryCode = country.Code WHERE country.Name = 'Algeria'


-- 22. return the total number of countries
-- no filtering. count.
SELECT COUNT(Code) FROM country



-- 23. return the names of city in China sorted by population
-- single filtering. ranking.
SELECT Name FROM city WHERE CountryCode = 'CHN' ORDER BY Population

-- 24. return the names of countries in Asia sorted by surface area
-- single filtering. ranking.
SELECT Name FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea

-- 25. return the names of countries which speak English sorted by percentage
-- single filtering. ranking. join.
SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = 'English' ORDER BY countrylanguage.Percentage

-- 26. return the names of countries in Europe with GNP greater than 500000 sorted by population
-- double filtering. Range filtering. ranking.
SELECT Name FROM country WHERE Continent = 'Europe' AND GNP > 500000 ORDER BY Population


-- Insert

-- 27. insert a new city with ID = 188, Name = 'Djougou', CountryCode = 'BEN', Population = 134099
-- primary key violation. insert.
INSERT INTO city VALUES (188, 'Djougou', 'BEN', 134099)

-- 28. insert a new  city with ID = 1, Name = 'Kabul', CountryCode = 'AFG', Population = 1780000
-- primary key violation. insert.
INSERT INTO city VALUES (1, 'Kabul', 'AFG', 1780000)

-- 29. insert a new city with ID = 2, Name = 'Qandahar', CountryCode = 'AFF', Population = 237500
-- foreign key violation. insert.
INSERT INTO city VALUES (2, 'Qandahar', 'AFF', 237500)

-- 30. insert a language = English in coutnrycode = 'CCC' with percentage = 1.0 and isofficial = 'F'
-- foreign key violation. insert.
INSERT INTO countrylanguage VALUES ('CCC', 'English', 'F', 1.0)


-- 31. insert a new city with ID = 1532, Name = 'Tokyo', CountryCode = 'JPN', Population = 7980230
-- insert.
INSERT INTO city VALUES (1532, 'Tokyo', 'JPN', 7980230)

-- 32. insert a new city with ID = 3795, Name = 'Chicago', CountryCode = 'USA', Population = 2896016
-- insert.
INSERT INTO city VALUES (3795, 'Chicago', 'USA', 2896016)

-- 33. insert a new country with Code = 'THA', Name = 'Thailand', Continent = 'Asia', Region = 'Southeast Asia', SurfaceArea = 513115.00, Population = 61399000, LifeExpectancy = 68.6, GNP = 116416.00
-- insert.
INSERT INTO country VALUES ('THA', 'Thailand', 'Asia', 'Southeast Asia', 513115.00, 61399000, 68.6, 116416.00)

-- 34. insert a language = English in coutnrycode = 'CHN' with percentage = 1.0 and isofficial = 'F'
-- insert.
INSERT INTO countrylanguage VALUES ('CHN', 'English', 'F', 1.0)


-- 3. Delete
-- 35. delete the country with code = 'ARG'
-- foreign key violation. single filtering.
DELETE FROM country WHERE Code = 'ARG'

-- 36. delete all the countries in Asia with population greater than 5000000
-- double filtering. Range filtering. foreign key violation.
DELETE FROM country WHERE Continent = 'Asia' AND Population > 5000000

-- 37. delete all the countries with GNP greater than 300000 and less than 1000000
-- single filtering. Range filtering. foreign key violation.
DELETE FROM country WHERE GNP > 300000 AND GNP < 1000000

-- 38. delete all the countries with life expectancy larger than 60
-- single filtering. Range filtering. foreign key violation.
DELETE FROM country WHERE LifeExpectancy > 60.0

-- 39. delete all the languages in Europe
-- single filtering. foreign key violation. Join.
DELETE FROM countrylanguage JOIN country ON countrylanguage.CountryCode = country.Code WHERE country.Continent = 'Europe'


-- 40. delete the city with ID = 3795
-- single filtering. delete.
DELETE FROM city WHERE ID = 3795

-- 41. delete the city with ID = 1
-- single filtering. delete.
DELETE FROM city WHERE ID = 1

-- 42. delete the country with code = 'JPN'
-- single filtering.
DELETE FROM country WHERE Code = 'JPN'

-- 43. delete all the cities in China with population greater than 300000
-- single filtering. Range filtering. delete.
DELETE FROM city WHERE CountryCode = 'CHN' AND Population > 300000

-- 44. delete all the languages with percentage greater than 50.0
-- single filtering. Range filtering. delete.
DELETE FROM countrylanguage WHERE Percentage > 50.0


-- Update

-- 45. update the code of country with name = "China" to 'CHI'
-- foreign key violation. single filtering. update
UPDATE country SET Code = 'CHI' WHERE Name = 'China'

-- 46. update the code of country with name = "Argentina" to 'AAA'
-- foreign key violation. single filtering. update
UPDATE country SET Code = 'AAA' WHERE Name = 'Argentina'

-- 47. update the code of country with population = 126724000 to 'JPA'
-- foreign key violation. single filtering. update
UPDATE country SET Code = 'JPA' WHERE Population = 126724000


-- 48. update the population of the city with ID = 50 to 100120
-- single filtering. update.
UPDATE city SET Population = 100120 WHERE ID = 50

-- 49. update the life expectancy of the country with code = 'CHN' to 80.0
-- single filtering. update.
UPDATE country SET LifeExpectancy = 80.0 WHERE Code = 'CHN'

-- 50. update the percentage of language = Chinese in countrycode = 'CHN' to 93
-- double filtering. update.
UPDATE countrylanguage SET Percentage = 93 WHERE CountryCode = 'CHN' AND Language = 'Chinese'


-- 51. update all the cities in China with population greater than 300000, increate the population by 10%
-- double filtering. Range filtering. update. join
UPDATE city join country ON city.CountryCode = country.Code SET city.Population = city.Population * 1.1 WHERE country.Name = 'China' AND city.Population > 300000



