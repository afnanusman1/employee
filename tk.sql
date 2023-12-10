-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: tk
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `announcement`
--

DROP TABLE IF EXISTS `announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `announcement` (
  `Date` date NOT NULL,
  `Event` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcement`
--

LOCK TABLES `announcement` WRITE;
/*!40000 ALTER TABLE `announcement` DISABLE KEYS */;
INSERT INTO `announcement` VALUES ('2023-04-01','Meeting - New tender details (on 2/4/2023)'),('2023-04-18','Meeting with IT department on 21/4/2023'),('2023-05-23','Blood donation campaign will be conducted on 26/5/2023 at the main seminar hall'),('2023-06-14','Meeting with operations department on 16/2/2023'),('2023-07-21','Meeting with marketing department on 25/7/2023'),('2023-08-19','Meeting with sales department on 22/8/2023'),('2023-09-11','Meeting with production department on 13/9/2023'),('2023-10-11','12th anniversary party will be conducted on 22/10/2020 at Le Meridian Hotel'),('2023-11-01','Training will be conducted by the fire service on 9/11/2023'),('2023-12-09','Meeting with quality department on 12/12/2023');
/*!40000 ALTER TABLE `announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `complaint`
--

DROP TABLE IF EXISTS `complaint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complaint` (
  `Date` date NOT NULL,
  `Id` int DEFAULT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Problem` text,
  `Status` char(10) DEFAULT 'Not Solved',
  KEY `Id` (`Id`),
  CONSTRAINT `complaint_ibfk_1` FOREIGN KEY (`Id`) REFERENCES `detail` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complaint`
--

LOCK TABLES `complaint` WRITE;
/*!40000 ALTER TABLE `complaint` DISABLE KEYS */;
INSERT INTO `complaint` VALUES ('2023-12-07',2,'Peter Hogan','The system in my cabin is not working','Solved');
/*!40000 ALTER TABLE `complaint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dept` (
  `Dept_No` int NOT NULL,
  `Name` varchar(10) DEFAULT NULL,
  `HOD` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Dept_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept`
--

LOCK TABLES `dept` WRITE;
/*!40000 ALTER TABLE `dept` DISABLE KEYS */;
INSERT INTO `dept` VALUES (1,'IT','David John'),(2,'Marketing','Tony Thompson'),(3,'Sales','Peter Hogan'),(4,'Operation','Steven Rock'),(5,'Production','Charlie John'),(6,'Quality','Alex Joshy');
/*!40000 ALTER TABLE `dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail`
--

DROP TABLE IF EXISTS `detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail` (
  `Id` int NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Designation` char(100) DEFAULT NULL,
  `Dept_No` int DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Sex` char(6) DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT (25000),
  `Mobile` char(10) DEFAULT NULL,
  `Email` char(100) DEFAULT NULL,
  `Username` char(100) DEFAULT NULL,
  `Password` char(100) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Mobile` (`Mobile`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Mobile_2` (`Mobile`),
  UNIQUE KEY `mobile_3` (`Mobile`),
  UNIQUE KEY `mobile_4` (`Mobile`),
  UNIQUE KEY `mobile_5` (`Mobile`),
  UNIQUE KEY `Mobile_6` (`Mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail`
--

LOCK TABLES `detail` WRITE;
/*!40000 ALTER TABLE `detail` DISABLE KEYS */;
INSERT INTO `detail` VALUES (1,'David John','HR Manager',1,'1990-01-08','Male',75000.00,'0505214734','david@gmail.com','admin','david@123'),(2,'Peter Hogan','Sales Manager',3,'1991-08-10','Male',50000.00,'0524324734','peter@gmail.com','peter','peter@123'),(3,'Tony Thompson','Marketing Manager',2,'1999-10-12','Male',25000.00,'1234567890','tony@gmail.com','tony','tony@123'),(4,'Steven Rock','Operation Manager',4,'1990-03-01','Male',25000.00,'3216549870','steven@gmail.com','steven','steven@123'),(5,'Charlie John','Production Engineer',5,'1992-03-07','Male',25000.00,'9876054321','charlie@gmail.com','charlie','charlie@123'),(6,'Alex Joshy','Quality Analyst',6,'1991-02-05','Male',25000.00,'5647891230','alex@gmail.com','alex','alex@123'),(7,'Emma Jackson','Software Engineer',1,'1993-03-01','Female',25000.00,'4561237890','emma@gmail.com','emma','emma@123'),(8,'Sarah Joseph','Sales Executive',3,'1992-07-04','Female',25000.00,'8527041963','sarah@gmail.com','sarah','sarah@123'),(9,'Gwen Jacob','Sales Director',3,'1990-11-03','Female',25000.00,'9638520741','gwen@gmail.com','gwen','gwen@123');
/*!40000 ALTER TABLE `detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `terminate`
--

DROP TABLE IF EXISTS `terminate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `terminate` (
  `Name` varchar(100) DEFAULT NULL,
  `Designation` char(100) DEFAULT NULL,
  `Dept_No` int DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Sex` char(6) DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `Mobile` char(10) DEFAULT NULL,
  `Email` char(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `terminate`
--

LOCK TABLES `terminate` WRITE;
/*!40000 ALTER TABLE `terminate` DISABLE KEYS */;
INSERT INTO `terminate` VALUES ('Steven Stone','Operation Manager',4,'1991-03-04','Male',25000.00,'3216549870','steven@gmail.com');
/*!40000 ALTER TABLE `terminate` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-11  2:20:35
