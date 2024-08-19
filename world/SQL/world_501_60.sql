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

INSERT INTO `city` VALUES (37,'Constantine','DZA','Constantine',443727);
INSERT INTO `city` VALUES (38,'Annaba','DZA','Annaba',222518);
INSERT INTO `city` VALUES (39,'Batna','DZA','Batna',183377);
INSERT INTO `city` VALUES (40,'Sétif','DZA','Sétif',179055);
INSERT INTO `city` VALUES (41,'Sidi Bel Abbès','DZA','Sidi Bel Abbès',153106);

INSERT INTO `city` VALUES (44,'Blida (el-Boulaida)','DZA','Blida',127284);
INSERT INTO `city` VALUES (45,'Béjaïa','DZA','Béjaïa',117162);
INSERT INTO `city` VALUES (46,'Mostaganem','DZA','Mostaganem',115212);
INSERT INTO `city` VALUES (47,'Tébessa','DZA','Tébessa',112007);
INSERT INTO `city` VALUES (48,'Tlemcen (Tilimsen)','DZA','Tlemcen',110242);


DELETE FROM `city` WHERE `ID` = 10;
DELETE FROM `city` WHERE `ID` = 40;
DELETE FROM `city` WHERE `CountryCode` = 'ANT';
DELETE FROM `city` WHERE `CountryCode` = 'DZA' and `Population` < 150000;
Update `city` set `Population` = 100300 where `ID` = 50;
Update `city` set `Population` = 117200 where `Name` = 'Béjaïa';

DELETE FROM `city` WHERE `ID` = 11;
DELETE FROM `city` WHERE `ID` = 41;
DELETE FROM `city` WHERE `CountryCode` = 'ALB';
DELETE FROM `city` WHERE `CountryCode` = 'AFG' and `Population` > 200000;
Update `city` set `Population` = 610000 where `ID` = 36;
Update `city` set `Population` = 120000 where `Name` = 'Mostaganem';



INSERT INTO `city` VALUES (51,'Ech-Chleff (el-Asnam)','DZA','Chlef',96794);
INSERT INTO `city` VALUES (52,'Ghardaïa','DZA','Ghardaïa',89415);
INSERT INTO `city` VALUES (53,'Tafuna','ASM','Tutuila',5200);
INSERT INTO `city` VALUES (54,'Fagatogo','ASM','Tutuila',2323);
INSERT INTO `city` VALUES (55,'Andorra la Vella','AND','Andorra la Vella',21189);
INSERT INTO `city` VALUES (56,'Luanda','AGO','Luanda',2022000);
INSERT INTO `city` VALUES (57,'Huambo','AGO','Huambo',163100);
INSERT INTO `city` VALUES (58,'Lobito','AGO','Benguela',130000);

INSERT INTO `city` VALUES (60,'Namibe','AGO','Namibe',118200);
INSERT INTO `city` VALUES (61,'South Hill','AIA','–',961);
INSERT INTO `city` VALUES (62,'The Valley','AIA','–',595);
INSERT INTO `city` VALUES (63,'Saint John´s','ATG','St John',24000);
INSERT INTO `city` VALUES (64,'Dubai','ARE','Dubai',669181);

INSERT INTO `city` VALUES (82,'Salta','ARG','Salta',367550);
INSERT INTO `city` VALUES (83,'Moreno','ARG','Buenos Aires',356993);
INSERT INTO `city` VALUES (84,'Santa Fé','ARG','Santa Fé',353063);
INSERT INTO `city` VALUES (85,'Avellaneda','ARG','Buenos Aires',353046);
INSERT INTO `city` VALUES (86,'Tres de Febrero','ARG','Buenos Aires',352311);
INSERT INTO `city` VALUES (87,'Morón','ARG','Buenos Aires',349246);

INSERT INTO `city` VALUES (90,'Tigre','ARG','Buenos Aires',296226);
INSERT INTO `city` VALUES (91,'Malvinas Argentinas','ARG','Buenos Aires',290335);
INSERT INTO `city` VALUES (92,'Vicente López','ARG','Buenos Aires',288341);
INSERT INTO `city` VALUES (93,'Berazategui','ARG','Buenos Aires',276916);
INSERT INTO `city` VALUES (94,'Corrientes','ARG','Corrientes',258103);
INSERT INTO `city` VALUES (95,'San Miguel','ARG','Buenos Aires',248700);
INSERT INTO `city` VALUES (96,'Bahía Blanca','ARG','Buenos Aires',239810);
INSERT INTO `city` VALUES (97,'Esteban Echeverría','ARG','Buenos Aires',235760);
INSERT INTO `city` VALUES (98,'Resistencia','ARG','Chaco',229212);
INSERT INTO `city` VALUES (99,'José C. Paz','ARG','Buenos Aires',221754);
INSERT INTO `city` VALUES (100,'Paraná','ARG','Entre Rios',207041);

DELETE FROM `city` WHERE `ID` = 90;
DELETE FROM `city` WHERE `ID` = 2;
DELETE FROM `city` WHERE `CountryCode` = 'ARG' and `Population` < 200000;
DELETE FROM `city` WHERE `NAME` = 'Resistencia';
Update `city` set `Population` = 207000 where `Name` = 'Paraná';

DELETE FROM `city` WHERE `ID` = 91;
DELETE FROM `city` WHERE `ID` = 3;
DELETE FROM `city` WHERE `CountryCode` = 'ARG' and `Population` < 300000;
DELETE FROM `city` WHERE `NAME` = 'Bahía Blanca';
Update `city` set `Population` = 237000 where `Name` = 'José C. Paz';

INSERT INTO `city` VALUES (101,'Godoy Cruz','ARG','Mendoza',206998);
INSERT INTO `city` VALUES (102,'Posadas','ARG','Misiones',201273);
INSERT INTO `city` VALUES (103,'Guaymallén','ARG','Mendoza',200595);
INSERT INTO `city` VALUES (104,'Santiago del Estero','ARG','Santiago del Estero',189947);
INSERT INTO `city` VALUES (105,'San Salvador de Jujuy','ARG','Jujuy',178748);
INSERT INTO `city` VALUES (106,'Hurlingham','ARG','Buenos Aires',170028);
INSERT INTO `city` VALUES (107,'Neuquén','ARG','Neuquén',167296);
INSERT INTO `city` VALUES (108,'Ituzaingó','ARG','Buenos Aires',158197);
INSERT INTO `city` VALUES (109,'San Fernando','ARG','Buenos Aires',153036);
INSERT INTO `city` VALUES (110,'Formosa','ARG','Formosa',147636);
INSERT INTO `city` VALUES (111,'Las Heras','ARG','Mendoza',145823);
INSERT INTO `city` VALUES (112,'La Rioja','ARG','La Rioja',138117);
INSERT INTO `city` VALUES (113,'San Fernando del Valle de Cata','ARG','Catamarca',134935);
INSERT INTO `city` VALUES (114,'Río Cuarto','ARG','Córdoba',134355);
INSERT INTO `city` VALUES (115,'Comodoro Rivadavia','ARG','Chubut',124104);
INSERT INTO `city` VALUES (116,'Mendoza','ARG','Mendoza',123027);
INSERT INTO `city` VALUES (117,'San Nicolás de los Arroyos','ARG','Buenos Aires',119302);
INSERT INTO `city` VALUES (118,'San Juan','ARG','San Juan',119152);
INSERT INTO `city` VALUES (119,'Escobar','ARG','Buenos Aires',116675);
INSERT INTO `city` VALUES (120,'Concordia','ARG','Entre Rios',116485);
INSERT INTO `city` VALUES (121,'Pilar','ARG','Buenos Aires',113428);
INSERT INTO `city` VALUES (122,'San Luis','ARG','San Luis',110136);
INSERT INTO `city` VALUES (123,'Ezeiza','ARG','Buenos Aires',99578);
INSERT INTO `city` VALUES (124,'San Rafael','ARG','Mendoza',94651);
INSERT INTO `city` VALUES (125,'Tandil','ARG','Buenos Aires',91101);
INSERT INTO `city` VALUES (126,'Yerevan','ARM','Yerevan',1248700);
INSERT INTO `city` VALUES (127,'Gjumri','ARM','Širak',211700);
INSERT INTO `city` VALUES (128,'Vanadzor','ARM','Lori',172700);
INSERT INTO `city` VALUES (129,'Oranjestad','ABW','–',29034);
INSERT INTO `city` VALUES (130,'Sydney','AUS','New South Wales',3276207);
INSERT INTO `city` VALUES (131,'Melbourne','AUS','Victoria',2865329);
INSERT INTO `city` VALUES (132,'Brisbane','AUS','Queensland',1291117);
INSERT INTO `city` VALUES (133,'Perth','AUS','West Australia',1096829);
INSERT INTO `city` VALUES (134,'Adelaide','AUS','South Australia',978100);
INSERT INTO `city` VALUES (135,'Canberra','AUS','Capital Region',322723);
INSERT INTO `city` VALUES (136,'Gold Coast','AUS','Queensland',311932);
INSERT INTO `city` VALUES (137,'Newcastle','AUS','New South Wales',270324);
INSERT INTO `city` VALUES (138,'Central Coast','AUS','New South Wales',227657);
INSERT INTO `city` VALUES (139,'Wollongong','AUS','New South Wales',219761);
INSERT INTO `city` VALUES (140,'Hobart','AUS','Tasmania',126118);
INSERT INTO `city` VALUES (141,'Geelong','AUS','Victoria',125382);
INSERT INTO `city` VALUES (142,'Townsville','AUS','Queensland',109914);
INSERT INTO `city` VALUES (143,'Cairns','AUS','Queensland',92273);
INSERT INTO `city` VALUES (144,'Bakı','AZE','Bakı',1787800);
INSERT INTO `city` VALUES (145,'Gəncə','AZE','Gəncə',299300);
INSERT INTO `city` VALUES (146,'Sumqayıt','AZE','Sumqayıt',283000);
INSERT INTO `city` VALUES (147,'Mingəçevir','AZE','Mingəçevir',93900);
INSERT INTO `city` VALUES (148,'Nassau','BHS','New Providence',172000);
INSERT INTO `city` VALUES (149,'al-Manama','BHR','al-Manama',148000);
INSERT INTO `city` VALUES (150,'Dhaka','BGD','Dhaka',3612850);
INSERT INTO `city` VALUES (151,'Chittagong','BGD','Chittagong',1392860);
INSERT INTO `city` VALUES (152,'Khulna','BGD','Khulna',663340);
INSERT INTO `city` VALUES (153,'Rajshahi','BGD','Rajshahi',294056);
INSERT INTO `city` VALUES (154,'Narayanganj','BGD','Dhaka',202134);
INSERT INTO `city` VALUES (155,'Rangpur','BGD','Rajshahi',191398);
INSERT INTO `city` VALUES (156,'Mymensingh','BGD','Dhaka',188713);
INSERT INTO `city` VALUES (157,'Barisal','BGD','Barisal',170232);
INSERT INTO `city` VALUES (158,'Tungi','BGD','Dhaka',168702);
INSERT INTO `city` VALUES (159,'Jessore','BGD','Khulna',139710);
INSERT INTO `city` VALUES (160,'Comilla','BGD','Chittagong',135313);
INSERT INTO `city` VALUES (161,'Nawabganj','BGD','Rajshahi',130577);
INSERT INTO `city` VALUES (162,'Dinajpur','BGD','Rajshahi',127815);
INSERT INTO `city` VALUES (163,'Bogra','BGD','Rajshahi',120170);
INSERT INTO `city` VALUES (164,'Sylhet','BGD','Sylhet',117396);
INSERT INTO `city` VALUES (165,'Brahmanbaria','BGD','Chittagong',109032);
INSERT INTO `city` VALUES (166,'Tangail','BGD','Dhaka',106004);
INSERT INTO `city` VALUES (167,'Jamalpur','BGD','Dhaka',103556);
INSERT INTO `city` VALUES (168,'Pabna','BGD','Rajshahi',103277);
INSERT INTO `city` VALUES (169,'Naogaon','BGD','Rajshahi',101266);
INSERT INTO `city` VALUES (170,'Sirajganj','BGD','Rajshahi',99669);
INSERT INTO `city` VALUES (171,'Narsinghdi','BGD','Dhaka',98342);
INSERT INTO `city` VALUES (172,'Saidpur','BGD','Rajshahi',96777);
INSERT INTO `city` VALUES (173,'Gazipur','BGD','Dhaka',96717);
INSERT INTO `city` VALUES (174,'Bridgetown','BRB','St Michael',6070);
INSERT INTO `city` VALUES (175,'Antwerpen','BEL','Antwerpen',446525);
INSERT INTO `city` VALUES (176,'Gent','BEL','East Flanderi',224180);
INSERT INTO `city` VALUES (177,'Charleroi','BEL','Hainaut',200827);
INSERT INTO `city` VALUES (178,'Liège','BEL','Liège',185639);
INSERT INTO `city` VALUES (179,'Bruxelles [Brussel]','BEL','Bryssel',133859);
INSERT INTO `city` VALUES (180,'Brugge','BEL','West Flanderi',116246);
INSERT INTO `city` VALUES (181,'Schaerbeek','BEL','Bryssel',105692);
INSERT INTO `city` VALUES (182,'Namur','BEL','Namur',105419);
INSERT INTO `city` VALUES (183,'Mons','BEL','Hainaut',90935);
INSERT INTO `city` VALUES (184,'Belize City','BLZ','Belize City',55810);
INSERT INTO `city` VALUES (185,'Belmopan','BLZ','Cayo',7105);
INSERT INTO `city` VALUES (186,'Cotonou','BEN','Atlantique',536827);
INSERT INTO `city` VALUES (187,'Porto-Novo','BEN','Ouémé',194000);
INSERT INTO `city` VALUES (188,'Djougou','BEN','Atacora',134099);
INSERT INTO `city` VALUES (189,'Parakou','BEN','Borgou',103577);
INSERT INTO `city` VALUES (190,'Saint George','BMU','Saint George´s',1800);
INSERT INTO `city` VALUES (191,'Hamilton','BMU','Hamilton',1200);
INSERT INTO `city` VALUES (192,'Thimphu','BTN','Thimphu',22000);
INSERT INTO `city` VALUES (193,'Santa Cruz de la Sierra','BOL','Santa Cruz',935361);
INSERT INTO `city` VALUES (194,'La Paz','BOL','La Paz',758141);
INSERT INTO `city` VALUES (195,'El Alto','BOL','La Paz',534466);
INSERT INTO `city` VALUES (196,'Cochabamba','BOL','Cochabamba',482800);
INSERT INTO `city` VALUES (197,'Oruro','BOL','Oruro',223553);
INSERT INTO `city` VALUES (198,'Sucre','BOL','Chuquisaca',178426);
INSERT INTO `city` VALUES (199,'Potosí','BOL','Potosí',140642);
INSERT INTO `city` VALUES (200,'Tarija','BOL','Tarija',125255);
INSERT INTO `city` VALUES (201,'Sarajevo','BIH','Federaatio',360000);
INSERT INTO `city` VALUES (202,'Banja Luka','BIH','Republika Srpska',143079);
INSERT INTO `city` VALUES (203,'Zenica','BIH','Federaatio',96027);
INSERT INTO `city` VALUES (204,'Gaborone','BWA','Gaborone',213017);
INSERT INTO `city` VALUES (205,'Francistown','BWA','Francistown',101805);
INSERT INTO `city` VALUES (206,'São Paulo','BRA','São Paulo',9968485);
INSERT INTO `city` VALUES (207,'Rio de Janeiro','BRA','Rio de Janeiro',5598953);
INSERT INTO `city` VALUES (208,'Salvador','BRA','Bahia',2302832);
INSERT INTO `city` VALUES (209,'Belo Horizonte','BRA','Minas Gerais',2139125);
INSERT INTO `city` VALUES (210,'Fortaleza','BRA','Ceará',2097757);
INSERT INTO `city` VALUES (211,'Brasília','BRA','Distrito Federal',1969868);
INSERT INTO `city` VALUES (212,'Curitiba','BRA','Paraná',1584232);
INSERT INTO `city` VALUES (213,'Recife','BRA','Pernambuco',1378087);
INSERT INTO `city` VALUES (214,'Porto Alegre','BRA','Rio Grande do Sul',1314032);
INSERT INTO `city` VALUES (215,'Manaus','BRA','Amazonas',1255049);
INSERT INTO `city` VALUES (216,'Belém','BRA','Pará',1186926);

INSERT INTO `city` VALUES (1980,'Zhenjiang','CHN','Jiangsu',368316);
INSERT INTO `city` VALUES (1981,'Huaibei','CHN','Anhui',366549);
INSERT INTO `city` VALUES (1982,'Qinhuangdao','CHN','Hebei',364972);
INSERT INTO `city` VALUES (1983,'Guilin','CHN','Guangxi',364130);
INSERT INTO `city` VALUES (1984,'Liupanshui','CHN','Guizhou',363954);
INSERT INTO `city` VALUES (1985,'Panjin','CHN','Liaoning',362773);
INSERT INTO `city` VALUES (1986,'Yangquan','CHN','Shanxi',362268);
INSERT INTO `city` VALUES (1987,'Jinxi','CHN','Liaoning',357052);
INSERT INTO `city` VALUES (1988,'Liaoyuan','CHN','Jilin',354141);
INSERT INTO `city` VALUES (1989,'Lianyungang','CHN','Jiangsu',354139);
INSERT INTO `city` VALUES (1990,'Xianyang','CHN','Shaanxi',352125);
INSERT INTO `city` VALUES (1991,'Tai´an','CHN','Shandong',350696);
INSERT INTO `city` VALUES (1992,'Chifeng','CHN','Inner Mongolia',350077);
INSERT INTO `city` VALUES (1993,'Shaoguan','CHN','Guangdong',350043);
INSERT INTO `city` VALUES (1994,'Nantong','CHN','Jiangsu',343341);
INSERT INTO `city` VALUES (1995,'Leshan','CHN','Sichuan',341128);
INSERT INTO `city` VALUES (1996,'Baoji','CHN','Shaanxi',337765);
INSERT INTO `city` VALUES (1997,'Linyi','CHN','Shandong',324720);
INSERT INTO `city` VALUES (1998,'Tonghua','CHN','Jilin',324600);
INSERT INTO `city` VALUES (1999,'Siping','CHN','Jilin',317223);
INSERT INTO `city` VALUES (2000,'Changzhi','CHN','Shanxi',317144);
INSERT INTO `city` VALUES (2001,'Tengzhou','CHN','Shandong',315083);
INSERT INTO `city` VALUES (2002,'Chaozhou','CHN','Guangdong',313469);
INSERT INTO `city` VALUES (2003,'Yangzhou','CHN','Jiangsu',312892);
INSERT INTO `city` VALUES (2004,'Dongwan','CHN','Guangdong',308669);
INSERT INTO `city` VALUES (2005,'Ma´anshan','CHN','Anhui',305421);
INSERT INTO `city` VALUES (2006,'Foshan','CHN','Guangdong',303160);
INSERT INTO `city` VALUES (2007,'Yueyang','CHN','Hunan',302800);
INSERT INTO `city` VALUES (2008,'Xingtai','CHN','Hebei',302789);
INSERT INTO `city` VALUES (2009,'Changde','CHN','Hunan',301276);
INSERT INTO `city` VALUES (2010,'Shihezi','CHN','Xinxiang',299676);
INSERT INTO `city` VALUES (3842,'Wichita','USA','Kansas',344284);
INSERT INTO `city` VALUES (3849,'Tampa','USA','Florida',303447);
INSERT INTO `city` VALUES (3850,'Buffalo','USA','New York',292648);
INSERT INTO `city` VALUES (3851,'Saint Paul','USA','Minnesota',287151);
INSERT INTO `city` VALUES (3852,'Corpus Christi','USA','Texas',277454);
INSERT INTO `city` VALUES (3853,'Aurora','USA','Colorado',276393);
INSERT INTO `city` VALUES (3854,'Raleigh','USA','North Carolina',276093);
INSERT INTO `city` VALUES (3855,'Newark','USA','New Jersey',273546);
INSERT INTO `city` VALUES (3856,'Lexington-Fayette','USA','Kentucky',260512);


DELETE FROM `city` WHERE `ID` = 3011;
DELETE FROM `city` WHERE `ID` = 2000;
DELETE FROM `city` WHERE `CountryCode` = 'CHN' and `Population` < 310000;
Update `city` set `Population` = 1790000 where `ID` = 1;
Update `city` set `Population` = 127900 where `Name` = 'Mazar-e-Sharif';


DELETE FROM `city` WHERE `ID` = 3012;
DELETE FROM `city` WHERE `ID` = 2001;
DELETE FROM `city` WHERE `CountryCode` = 'USA' and `Population` < 300000;
Update `city` set `Population` = 240000 where `ID` = 2;
Update `city` set `Population` = 310000 where `Name` = 'Tampa';

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
INSERT INTO `country` VALUES ('CMR','Cameroon','Africa','Central Africa',475442.00,1960,15085000,54.8,9174.00,8596.00,'Cameroun/Cameroon','Republic','Paul Biya',1804,'CM');
INSERT INTO `country` VALUES ('COD','Congo, The Democratic Republic of the','Africa','Central Africa',2344858.00,1960,51654000,48.8,6964.00,2474.00,'République Démocratique du Congo','Republic','Joseph Kabila',2298,'CD');
INSERT INTO `country` VALUES ('COG','Congo','Africa','Central Africa',342000.00,1960,2943000,47.4,2108.00,2287.00,'Congo','Republic','Denis Sassou-Nguesso',2296,'CG');
INSERT INTO `country` VALUES ('COK','Cook Islands','Oceania','Polynesia',236.00,NULL,20000,71.1,100.00,NULL,'The Cook Islands','Nonmetropolitan Territory of New Zealand','Elisabeth II',583,'CK');
INSERT INTO `country` VALUES ('COL','Colombia','South America','South America',1138914.00,1810,42321000,70.3,102896.00,105116.00,'Colombia','Republic','Andrés Pastrana Arango',2257,'CO');
INSERT INTO `country` VALUES ('COM','Comoros','Africa','Eastern Africa',1862.00,1975,578000,60.0,4401.00,4361.00,'Komori/Comores','Republic','Azali Assoumani',2295,'KM');
INSERT INTO `country` VALUES ('CPV','Cape Verde','Africa','Western Africa',4033.00,1975,428000,68.9,435.00,420.00,'Cabo Verde','Republic','António Mascarenhas Monteiro',1859,'CV');
INSERT INTO `country` VALUES ('CRI','Costa Rica','North America','Central America',51100.00,1821,4023000,75.8,10226.00,9757.00,'Costa Rica','Republic','Miguel Ángel Rodríguez Echeverría',584,'CR');
INSERT INTO `country` VALUES ('CUB','Cuba','North America','Caribbean',110861.00,1902,11201000,76.2,17843.00,18862.00,'Cuba','Socialistic Republic','Fidel Castro Ruz',2413,'CU');
INSERT INTO `country` VALUES ('CXR','Christmas Island','Oceania','Australia and New Zealand',135.00,NULL,2500,NULL,0.00,NULL,'Christmas Island','Territory of Australia','Elisabeth II',1791,'CX');
INSERT INTO `country` VALUES ('CYM','Cayman Islands','North America','Caribbean',264.00,NULL,38000,78.9,1263.00,1186.00,'Cayman Islands','Dependent Territory of the UK','Elisabeth II',553,'KY');
INSERT INTO `country` VALUES ('CYP','Cyprus','Asia','Middle East',9251.00,1960,754700,76.7,9333.00,8246.00,'Kýpros/Kibris','Republic','Glafkos Klerides',2430,'CY');
INSERT INTO `country` VALUES ('CZE','Czech Republic','Europe','Eastern Europe',78866.00,1993,10278100,74.5,55017.00,52037.00,'¸esko','Republic','Václav Havel',3339,'CZ');
INSERT INTO `country` VALUES ('DEU','Germany','Europe','Western Europe',357022.00,1955,82164700,77.4,2133367.00,2102826.00,'Deutschland','Federal Republic','Johannes Rau',3068,'DE');
INSERT INTO `country` VALUES ('DJI','Djibouti','Africa','Eastern Africa',23200.00,1977,638000,50.8,382.00,373.00,'Djibouti/Jibuti','Republic','Ismail Omar Guelleh',585,'DJ');
INSERT INTO `country` VALUES ('DMA','Dominica','North America','Caribbean',751.00,1978,71000,73.4,256.00,243.00,'Dominica','Republic','Vernon Shaw',586,'DM');
INSERT INTO `country` VALUES ('DNK','Denmark','Europe','Nordic Countries',43094.00,800,5330000,76.5,174099.00,169264.00,'Danmark','Constitutional Monarchy','Margrethe II',3315,'DK');
INSERT INTO `country` VALUES ('DOM','Dominican Republic','North America','Caribbean',48511.00,1844,8495000,73.2,15846.00,15076.00,'República Dominicana','Republic','Hipólito Mejía Domínguez',587,'DO');
INSERT INTO `country` VALUES ('DZA','Algeria','Africa','Northern Africa',2381741.00,1962,31471000,69.7,49982.00,46966.00,'Al-Jaza’ir/Algérie','Republic','Abdelaziz Bouteflika',35,'DZ');

DELETE FROM `country` WHERE `Code` = 'DOM';
DELETE FROM `country` WHERE `Code` = 'DJI';

DELETE FROM `country` WHERE `Code` = 'CYM';
DELETE FROM `country` WHERE `Code` = 'CUB';

INSERT INTO `country` VALUES ('ESP','Spain','Europe','Southern Europe',505992.00,1492,39441700,78.8,553233.00,532031.00,'España','Constitutional Monarchy','Juan Carlos I',653,'ES');
INSERT INTO `country` VALUES ('EST','Estonia','Europe','Baltic Countries',45227.00,1991,1439200,69.5,5328.00,3371.00,'Eesti','Republic','Lennart Meri',3791,'EE');

INSERT INTO `country` VALUES ('FJI','Fiji Islands','Oceania','Melanesia',18274.00,1970,817000,67.9,1536.00,2149.00,'Fiji Islands','Republic','Josefa Iloilo',764,'FJ');
INSERT INTO `country` VALUES ('FLK','Falkland Islands','South America','South America',12173.00,NULL,2000,NULL,0.00,NULL,'Falkland Islands','Dependent Territory of the UK','Elisabeth II',763,'FK');
INSERT INTO `country` VALUES ('FRA','France','Europe','Western Europe',551500.00,843,59225700,78.8,1424285.00,1392448.00,'France','Republic','Jacques Chirac',2974,'FR');
INSERT INTO `country` VALUES ('FRO','Faroe Islands','Europe','Nordic Countries',1399.00,NULL,43000,78.4,0.00,NULL,'Føroyar','Part of Denmark','Margrethe II',901,'FO');
INSERT INTO `country` VALUES ('FSM','Micronesia, Federated States of','Oceania','Micronesia',702.00,1990,119000,68.6,212.00,NULL,'Micronesia','Federal Republic','Leo A. Falcam',2689,'FM');
INSERT INTO `country` VALUES ('GAB','Gabon','Africa','Central Africa',267668.00,1960,1226000,50.1,5493.00,5279.00,'Le Gabon','Republic','Omar Bongo',902,'GA');
INSERT INTO `country` VALUES ('GBR','United Kingdom','Europe','British Islands',242900.00,1066,59623400,77.7,1378330.00,1296830.00,'United Kingdom','Constitutional Monarchy','Elisabeth II',456,'GB');
INSERT INTO `country` VALUES ('GEO','Georgia','Asia','Middle East',69700.00,1991,4968000,64.5,6064.00,5924.00,'Sakartvelo','Republic','Eduard Ševardnadze',905,'GE');
INSERT INTO `country` VALUES ('GHA','Ghana','Africa','Western Africa',238533.00,1957,20212000,57.4,7137.00,6884.00,'Ghana','Republic','John Kufuor',910,'GH');
INSERT INTO `country` VALUES ('GIB','Gibraltar','Europe','Southern Europe',6.00,NULL,25000,79.0,258.00,NULL,'Gibraltar','Dependent Territory of the UK','Elisabeth II',915,'GI');
INSERT INTO `country` VALUES ('GIN','Guinea','Africa','Western Africa',245857.00,1958,7430000,45.6,2352.00,2383.00,'Guinée','Republic','Lansana Conté',926,'GN');
INSERT INTO `country` VALUES ('GLP','Guadeloupe','North America','Caribbean',1705.00,NULL,456000,77.0,3501.00,NULL,'Guadeloupe','Overseas Department of France','Jacques Chirac',919,'GP');
INSERT INTO `country` VALUES ('GMB','Gambia','Africa','Western Africa',11295.00,1965,1305000,53.2,320.00,325.00,'The Gambia','Republic','Yahya Jammeh',904,'GM');
INSERT INTO `country` VALUES ('GNB','Guinea-Bissau','Africa','Western Africa',36125.00,1974,1213000,49.0,293.00,272.00,'Guiné-Bissau','Republic','Kumba Ialá',927,'GW');
INSERT INTO `country` VALUES ('GNQ','Equatorial Guinea','Africa','Central Africa',28051.00,1968,453000,53.6,283.00,542.00,'Guinea Ecuatorial','Republic','Teodoro Obiang Nguema Mbasogo',2972,'GQ');
INSERT INTO `country` VALUES ('GRC','Greece','Europe','Southern Europe',131626.00,1830,10545700,78.4,120724.00,119946.00,'Elláda','Republic','Kostis Stefanopoulos',2401,'GR');
INSERT INTO `country` VALUES ('GRD','Grenada','North America','Caribbean',344.00,1974,94000,64.5,318.00,NULL,'Grenada','Constitutional Monarchy','Elisabeth II',916,'GD');
INSERT INTO `country` VALUES ('GRL','Greenland','North America','North America',2166090.00,NULL,56000,68.1,0.00,NULL,'Kalaallit Nunaat/Grønland','Part of Denmark','Margrethe II',917,'GL');
INSERT INTO `country` VALUES ('GTM','Guatemala','North America','Central America',108889.00,1821,11385000,66.2,19008.00,17797.00,'Guatemala','Republic','Alfonso Portillo Cabrera',922,'GT');
INSERT INTO `country` VALUES ('GUF','French Guiana','South America','South America',90000.00,NULL,181000,76.1,681.00,NULL,'Guyane française','Overseas Department of France','Jacques Chirac',3014,'GF');
INSERT INTO `country` VALUES ('GUM','Guam','Oceania','Micronesia',549.00,NULL,168000,77.8,1197.00,1136.00,'Guam','US Territory','George W. Bush',921,'GU');
INSERT INTO `country` VALUES ('GUY','Guyana','South America','South America',214969.00,1966,861000,64.0,722.00,743.00,'Guyana','Republic','Bharrat Jagdeo',928,'GY');
INSERT INTO `country` VALUES ('HKG','Hong Kong','Asia','Eastern Asia',1075.00,NULL,6782000,79.5,166448.00,173610.00,'Xianggang/Hong Kong','Special Administrative Region of China','Jiang Zemin',937,'HK');
INSERT INTO `country` VALUES ('HMD','Heard Island and McDonald Islands','Antarctica','Antarctica',359.00,NULL,0,NULL,0.00,NULL,'Heard and McDonald Islands','Territory of Australia','Elisabeth II',NULL,'HM');
INSERT INTO `country` VALUES ('HND','Honduras','North America','Central America',112088.00,1838,6485000,69.9,5333.00,4697.00,'Honduras','Republic','Carlos Roberto Flores Facussé',933,'HN');
INSERT INTO `country` VALUES ('HRV','Croatia','Europe','Southern Europe',56538.00,1991,4473000,73.7,20208.00,19300.00,'Hrvatska','Republic','Štipe Mesic',2409,'HR');
INSERT INTO `country` VALUES ('HTI','Haiti','North America','Caribbean',27750.00,1804,8222000,49.2,3459.00,3107.00,'Haïti/Dayti','Republic','Jean-Bertrand Aristide',929,'HT');
INSERT INTO `country` VALUES ('HUN','Hungary','Europe','Eastern Europe',93030.00,1918,10043200,71.4,48267.00,45914.00,'Magyarország','Republic','Ferenc Mádl',3483,'HU');
INSERT INTO `country` VALUES ('IDN','Indonesia','Asia','Southeast Asia',1904569.00,1945,212107000,68.0,84982.00,215002.00,'Indonesia','Republic','Abdurrahman Wahid',939,'ID');
INSERT INTO `country` VALUES ('IND','India','Asia','Southern and Central Asia',3287263.00,1947,1013662000,62.5,447114.00,430572.00,'Bharat/India','Federal Republic','Kocheril Raman Narayanan',1109,'IN');
INSERT INTO `country` VALUES ('IOT','British Indian Ocean Territory','Africa','Eastern Africa',78.00,NULL,0,NULL,0.00,NULL,'British Indian Ocean Territory','Dependent Territory of the UK','Elisabeth II',NULL,'IO');
INSERT INTO `country` VALUES ('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic','Mary McAleese',1447,'IE');
INSERT INTO `country` VALUES ('IRN','Iran','Asia','Southern and Central Asia',1648195.00,1906,67702000,69.7,195746.00,160151.00,'Iran','Islamic Republic','Ali Mohammad Khatami-Ardakani',1380,'IR');
INSERT INTO `country` VALUES ('IRQ','Iraq','Asia','Middle East',438317.00,1932,23115000,66.5,11500.00,NULL,'Al-´Iraq','Republic','Saddam Hussein al-Takriti',1365,'IQ');
INSERT INTO `country` VALUES ('ISL','Iceland','Europe','Nordic Countries',103000.00,1944,279000,79.4,8255.00,7474.00,'Ísland','Republic','Ólafur Ragnar Grímsson',1449,'IS');
INSERT INTO `country` VALUES ('ISR','Israel','Asia','Middle East',21056.00,1948,6217000,78.6,97477.00,98577.00,'Yisra’el/Isra’il','Republic','Moshe Katzav',1450,'IL');
INSERT INTO `country` VALUES ('ITA','Italy','Europe','Southern Europe',301316.00,1861,57680000,79.0,1161755.00,1145372.00,'Italia','Republic','Carlo Azeglio Ciampi',1464,'IT');
INSERT INTO `country` VALUES ('UKR','Ukraine','Europe','Eastern Europe',603700.00,1991,50456000,66.0,42168.00,49677.00,'Ukrajina','Republic','Leonid Kutšma',3426,'UA');
INSERT INTO `country` VALUES ('USA','United States','North America','North America',9363520.00,1776,278357000,77.1,8510700.00,8110900.00,'United States','Federal Republic','George W. Bush',3813,'US');
INSERT INTO `country` VALUES ('JPN','Japan','Asia','Eastern Asia',377829.00,-660,126714000,80.7,3787042.00,4192638.00,'Nihon/Nippon','Constitutional Monarchy','Akihito',1532,'JP');


DELETE FROM `country` WHERE `Code` = 'ITA';
DELETE FROM `country` WHERE `Code` = 'IOT';
DELETE FROM `country` WHERE `Name` = 'Haiti';
DELETE FROM `country` WHERE `Name` = 'Honduras';
UPDATE `country` SET `Population` = 126724000 WHERE `Code` = 'JPN';
UPDATE `country` SET `LifeExpectancy` = 65 WHERE `Code` = 'IND';  


DELETE FROM `country` WHERE `Code` = 'HRV';
DELETE FROM `country` WHERE `Code` = 'GUY';
DELETE FROM `country` WHERE `Name` = 'Guinea-Bissau';
DELETE FROM `country` WHERE `Name` = 'Micronesia';
UPDATE `country` SET `Population` = 39441800 WHERE `Code` = 'ESP';
UPDATE `country` SET `LifeExpectancy` = 66 WHERE `Code` = 'IND';  

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
INSERT INTO `countrylanguage` VALUES ('ABW','Dutch','T',5.3);
INSERT INTO `countrylanguage` VALUES ('ABW','English','F',9.5);
INSERT INTO `countrylanguage` VALUES ('ABW','Papiamento','F',76.7);
INSERT INTO `countrylanguage` VALUES ('ABW','Spanish','F',7.4);
INSERT INTO `countrylanguage` VALUES ('AFG','Balochi','F',0.9);
INSERT INTO `countrylanguage` VALUES ('AFG','Dari','T',32.1);
INSERT INTO `countrylanguage` VALUES ('AFG','Pashto','T',52.4);
INSERT INTO `countrylanguage` VALUES ('AFG','Turkmenian','F',1.9);
INSERT INTO `countrylanguage` VALUES ('AFG','Uzbek','F',8.8);
INSERT INTO `countrylanguage` VALUES ('AGO','Ambo','F',2.4);
INSERT INTO `countrylanguage` VALUES ('AGO','Chokwe','F',4.2);
INSERT INTO `countrylanguage` VALUES ('AGO','Kongo','F',13.2);
INSERT INTO `countrylanguage` VALUES ('AGO','Luchazi','F',2.4);
INSERT INTO `countrylanguage` VALUES ('AGO','Luimbe-nganguela','F',5.4);
INSERT INTO `countrylanguage` VALUES ('AGO','Luvale','F',3.6);
INSERT INTO `countrylanguage` VALUES ('AGO','Mbundu','F',21.6);
INSERT INTO `countrylanguage` VALUES ('AGO','Nyaneka-nkhumbi','F',5.4);
INSERT INTO `countrylanguage` VALUES ('AGO','Ovimbundu','F',37.2);
INSERT INTO `countrylanguage` VALUES ('AIA','English','T',0.0);
INSERT INTO `countrylanguage` VALUES ('ALB','Albaniana','T',97.9);
INSERT INTO `countrylanguage` VALUES ('ALB','Greek','F',1.8);
INSERT INTO `countrylanguage` VALUES ('ALB','Macedonian','F',0.1);
INSERT INTO `countrylanguage` VALUES ('AND','Catalan','T',32.3);


DELETE FROM `countrylanguage` WHERE `CountryCode` = 'AND';
DELETE FROM `countrylanguage` WHERE `Language` = 'Mbundu';
UPDATE `countrylanguage` SET `Percentage` = 1.0 WHERE `CountryCode` = 'AIA' AND `Language` = 'English';

DELETE FROM `countrylanguage` WHERE `CountryCode` = 'AGO';
DELETE FROM `countrylanguage` WHERE `Language` = 'Luvale';
UPDATE `countrylanguage` SET `Percentage` = 2.0 WHERE `CountryCode` = 'AFG' AND `Language` = 'Turkmenian';

INSERT INTO `countrylanguage` VALUES ('ANT','Dutch','T',0.0);
INSERT INTO `countrylanguage` VALUES ('ANT','English','F',7.8);
INSERT INTO `countrylanguage` VALUES ('ANT','Papiamento','T',86.2);
INSERT INTO `countrylanguage` VALUES ('ARE','Arabic','T',42.0);
INSERT INTO `countrylanguage` VALUES ('ARE','Hindi','F',0.0);
INSERT INTO `countrylanguage` VALUES ('ARG','Indian Languages','F',0.3);
INSERT INTO `countrylanguage` VALUES ('ARG','Italian','F',1.7);
INSERT INTO `countrylanguage` VALUES ('ARG','Spanish','T',96.8);
INSERT INTO `countrylanguage` VALUES ('ARM','Armenian','T',93.4);
INSERT INTO `countrylanguage` VALUES ('ARM','Azerbaijani','F',2.6);
INSERT INTO `countrylanguage` VALUES ('ASM','English','T',3.1);
INSERT INTO `countrylanguage` VALUES ('ASM','Samoan','T',90.6);
INSERT INTO `countrylanguage` VALUES ('ASM','Tongan','F',3.1);
INSERT INTO `countrylanguage` VALUES ('ATG','Creole English','F',95.7);
INSERT INTO `countrylanguage` VALUES ('ATG','English','T',0.0);
INSERT INTO `countrylanguage` VALUES ('AUS','Arabic','F',1.0);
INSERT INTO `countrylanguage` VALUES ('AUS','Canton Chinese','F',1.1);
INSERT INTO `countrylanguage` VALUES ('AUS','English','T',81.2);
INSERT INTO `countrylanguage` VALUES ('AUS','German','F',0.6);
INSERT INTO `countrylanguage` VALUES ('AUS','Greek','F',1.6);
INSERT INTO `countrylanguage` VALUES ('AUS','Italian','F',2.2);
INSERT INTO `countrylanguage` VALUES ('AUS','Serbo-Croatian','F',0.6);
INSERT INTO `countrylanguage` VALUES ('AUS','Vietnamese','F',0.8);
INSERT INTO `countrylanguage` VALUES ('AUT','Czech','F',0.2);
INSERT INTO `countrylanguage` VALUES ('AUT','German','T',92.0);
INSERT INTO `countrylanguage` VALUES ('AUT','Hungarian','F',0.4);
INSERT INTO `countrylanguage` VALUES ('AUT','Polish','F',0.2);
INSERT INTO `countrylanguage` VALUES ('AUT','Romanian','F',0.2);
INSERT INTO `countrylanguage` VALUES ('AUT','Serbo-Croatian','F',2.2);
INSERT INTO `countrylanguage` VALUES ('AUT','Slovene','F',0.4);
INSERT INTO `countrylanguage` VALUES ('AUT','Turkish','F',1.5);
INSERT INTO `countrylanguage` VALUES ('AZE','Armenian','F',2.0);
INSERT INTO `countrylanguage` VALUES ('AZE','Azerbaijani','T',89.0);
INSERT INTO `countrylanguage` VALUES ('AZE','Lezgian','F',2.3);
INSERT INTO `countrylanguage` VALUES ('AZE','Russian','F',3.0);
INSERT INTO `countrylanguage` VALUES ('BDI','French','T',0.0);
INSERT INTO `countrylanguage` VALUES ('BDI','Kirundi','T',98.1);
INSERT INTO `countrylanguage` VALUES ('BDI','Swahili','F',0.0);
INSERT INTO `countrylanguage` VALUES ('BEL','Arabic','F',1.6);
INSERT INTO `countrylanguage` VALUES ('BEL','Dutch','T',59.2);
INSERT INTO `countrylanguage` VALUES ('BEL','French','T',32.6);
INSERT INTO `countrylanguage` VALUES ('BEL','German','T',1.0);
INSERT INTO `countrylanguage` VALUES ('BEL','Italian','F',2.4);
INSERT INTO `countrylanguage` VALUES ('BEL','Turkish','F',0.9);
INSERT INTO `countrylanguage` VALUES ('BEN','Adja','F',11.1);
INSERT INTO `countrylanguage` VALUES ('BEN','Aizo','F',8.7);
INSERT INTO `countrylanguage` VALUES ('BEN','Bariba','F',8.7);
INSERT INTO `countrylanguage` VALUES ('BEN','Fon','F',39.8);
INSERT INTO `countrylanguage` VALUES ('BEN','Ful','F',5.6);
INSERT INTO `countrylanguage` VALUES ('BEN','Joruba','F',12.2);
INSERT INTO `countrylanguage` VALUES ('BEN','Somba','F',6.7);
INSERT INTO `countrylanguage` VALUES ('BFA','Busansi','F',3.5);
INSERT INTO `countrylanguage` VALUES ('BFA','Dagara','F',3.1);
INSERT INTO `countrylanguage` VALUES ('BFA','Dyula','F',2.6);
INSERT INTO `countrylanguage` VALUES ('BFA','Ful','F',9.7);
INSERT INTO `countrylanguage` VALUES ('BFA','Gurma','F',5.7);
INSERT INTO `countrylanguage` VALUES ('BFA','Mossi','F',50.2);
INSERT INTO `countrylanguage` VALUES ('BGD','Bengali','T',97.7);
INSERT INTO `countrylanguage` VALUES ('BGD','Chakma','F',0.4);
INSERT INTO `countrylanguage` VALUES ('BGD','Garo','F',0.1);
INSERT INTO `countrylanguage` VALUES ('BGD','Khasi','F',0.1);
INSERT INTO `countrylanguage` VALUES ('BGD','Marma','F',0.2);
INSERT INTO `countrylanguage` VALUES ('BGD','Santhali','F',0.1);
INSERT INTO `countrylanguage` VALUES ('BGD','Tripuri','F',0.1);
INSERT INTO `countrylanguage` VALUES ('BGR','Bulgariana','T',83.2);
INSERT INTO `countrylanguage` VALUES ('BGR','Macedonian','F',2.6);
INSERT INTO `countrylanguage` VALUES ('BGR','Romani','F',3.7);
INSERT INTO `countrylanguage` VALUES ('BGR','Turkish','F',9.4);
INSERT INTO `countrylanguage` VALUES ('BHR','Arabic','T',67.7);
INSERT INTO `countrylanguage` VALUES ('BHR','English','F',0.0);
INSERT INTO `countrylanguage` VALUES ('BHS','Creole English','F',89.7);
INSERT INTO `countrylanguage` VALUES ('BHS','Creole French','F',10.3);
INSERT INTO `countrylanguage` VALUES ('BIH','Serbo-Croatian','T',99.2);
INSERT INTO `countrylanguage` VALUES ('BLR','Belorussian','T',65.6);
INSERT INTO `countrylanguage` VALUES ('BLR','Polish','F',0.6);
INSERT INTO `countrylanguage` VALUES ('BLR','Russian','T',32.0);
INSERT INTO `countrylanguage` VALUES ('BLR','Ukrainian','F',1.3);
INSERT INTO `countrylanguage` VALUES ('BLZ','English','T',50.8);
INSERT INTO `countrylanguage` VALUES ('BLZ','Garifuna','F',6.8);
INSERT INTO `countrylanguage` VALUES ('BLZ','Maya Languages','F',9.6);
INSERT INTO `countrylanguage` VALUES ('BLZ','Spanish','F',31.6);
INSERT INTO `countrylanguage` VALUES ('BMU','English','T',100.0);
INSERT INTO `countrylanguage` VALUES ('BOL','Aimará','T',3.2);
INSERT INTO `countrylanguage` VALUES ('BOL','Guaraní','F',0.1);
INSERT INTO `countrylanguage` VALUES ('BOL','Ketšua','T',8.1);
INSERT INTO `countrylanguage` VALUES ('BOL','Spanish','T',87.7);
INSERT INTO `countrylanguage` VALUES ('BRA','German','F',0.5);
INSERT INTO `countrylanguage` VALUES ('BRA','Indian Languages','F',0.2);
INSERT INTO `countrylanguage` VALUES ('BRA','Italian','F',0.4);
INSERT INTO `countrylanguage` VALUES ('BRA','Japanese','F',0.4);


DELETE FROM `countrylanguage` WHERE `CountryCode` = 'BRA';

DELETE FROM `countrylanguage` WHERE `CountryCode` = 'BLZ';

INSERT INTO `countrylanguage` VALUES ('BRB','Bajan','F',95.1);
INSERT INTO `countrylanguage` VALUES ('BRB','English','T',0.0);
INSERT INTO `countrylanguage` VALUES ('BRN','Chinese','F',9.3);
INSERT INTO `countrylanguage` VALUES ('BRN','English','F',3.1);
INSERT INTO `countrylanguage` VALUES ('BRN','Malay','T',45.5);
INSERT INTO `countrylanguage` VALUES ('BRN','Malay-English','F',28.8);
INSERT INTO `countrylanguage` VALUES ('BTN','Asami','F',15.2);
INSERT INTO `countrylanguage` VALUES ('BTN','Dzongkha','T',50.0);
INSERT INTO `countrylanguage` VALUES ('BTN','Nepali','F',34.8);
INSERT INTO `countrylanguage` VALUES ('BWA','Khoekhoe','F',2.5);
INSERT INTO `countrylanguage` VALUES ('BWA','Ndebele','F',1.3);
INSERT INTO `countrylanguage` VALUES ('BWA','San','F',3.5);
INSERT INTO `countrylanguage` VALUES ('BWA','Shona','F',12.3);
INSERT INTO `countrylanguage` VALUES ('BWA','Tswana','F',75.5);
INSERT INTO `countrylanguage` VALUES ('CAF','Banda','F',23.5);
INSERT INTO `countrylanguage` VALUES ('CAF','Gbaya','F',23.8);
INSERT INTO `countrylanguage` VALUES ('CAF','Mandjia','F',14.8);
INSERT INTO `countrylanguage` VALUES ('CAF','Mbum','F',6.4);
INSERT INTO `countrylanguage` VALUES ('CAF','Ngbaka','F',7.5);
INSERT INTO `countrylanguage` VALUES ('CAF','Sara','F',6.4);
INSERT INTO `countrylanguage` VALUES ('CAN','Chinese','F',2.5);
INSERT INTO `countrylanguage` VALUES ('CAN','Dutch','F',0.5);
INSERT INTO `countrylanguage` VALUES ('CAN','English','T',60.4);
INSERT INTO `countrylanguage` VALUES ('CAN','Eskimo Languages','F',0.1);
INSERT INTO `countrylanguage` VALUES ('CAN','French','T',23.4);
INSERT INTO `countrylanguage` VALUES ('CAN','German','F',1.6);
INSERT INTO `countrylanguage` VALUES ('CAN','Italian','F',1.7);
INSERT INTO `countrylanguage` VALUES ('CAN','Polish','F',0.7);
INSERT INTO `countrylanguage` VALUES ('CAN','Portuguese','F',0.7);
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
INSERT INTO `countrylanguage` VALUES ('CHN','Puyi','F',0.2);
INSERT INTO `countrylanguage` VALUES ('CHN','Tibetan','F',0.4);
INSERT INTO `countrylanguage` VALUES ('CHN','Tujia','F',0.5);
INSERT INTO `countrylanguage` VALUES ('CHN','Uighur','F',0.6);


UPDATE `countrylanguage` SET `Percentage` = 91.8 WHERE `CountryCode` = 'CHN' AND `Language` = 'Chinese';
DELETE FROM `countrylanguage` WHERE `CountryCode` = 'CAN' AND `Language` = 'Italian';

UPDATE `countrylanguage` SET `Percentage` = 8.0 WHERE `CountryCode` = 'CHE' AND `Language` = 'Italian';
DELETE FROM `countrylanguage` WHERE `CountryCode` = 'CAN' AND `Language` = 'Spanish';

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



