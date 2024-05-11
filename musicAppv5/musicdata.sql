-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: localhost    Database: MusicApp
-- ------------------------------------------------------
-- Server version	8.0.36

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

--
-- Table structure for table `Genres`
--

DROP TABLE IF EXISTS `Genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genres` (
  `Genre_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Genre_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genres`
--

LOCK TABLES `Genres` WRITE;
/*!40000 ALTER TABLE `Genres` DISABLE KEYS */;
INSERT INTO `Genres` VALUES (1,'Pop'),(2,'Classical'),(3,'Jazz');
/*!40000 ALTER TABLE `Genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Instrument_track`
--

DROP TABLE IF EXISTS `Instrument_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Instrument_track` (
  `Instrument_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Ethnic_Influence` varchar(50) DEFAULT NULL,
  `Chord_Progression` varchar(50) DEFAULT NULL,
  `Song_ID` int DEFAULT NULL,
  `Mood_ID` int DEFAULT NULL,
  PRIMARY KEY (`Instrument_ID`),
  KEY `Song_ID` (`Song_ID`),
  KEY `Mood_ID` (`Mood_ID`),
  CONSTRAINT `instrument_track_ibfk_1` FOREIGN KEY (`Song_ID`) REFERENCES `Songs` (`Song_ID`),
  CONSTRAINT `instrument_track_ibfk_2` FOREIGN KEY (`Mood_ID`) REFERENCES `Mood` (`Mood_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Instrument_track`
--

LOCK TABLES `Instrument_track` WRITE;
/*!40000 ALTER TABLE `Instrument_track` DISABLE KEYS */;
INSERT INTO `Instrument_track` VALUES (1,'Electric Guitar','American','E-A-D-G-B-E',1,1),(2,'Piano','European','C-G-Am-F',2,2),(3,'Violin','Asian','D-G-B-E-A',3,3);
/*!40000 ALTER TABLE `Instrument_track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mood`
--

DROP TABLE IF EXISTS `Mood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mood` (
  `Mood_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Mood_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mood`
--

LOCK TABLES `Mood` WRITE;
/*!40000 ALTER TABLE `Mood` DISABLE KEYS */;
INSERT INTO `Mood` VALUES (1,'Happy'),(2,'Sad'),(3,'Energetic');
/*!40000 ALTER TABLE `Mood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Musical_Keys`
--

DROP TABLE IF EXISTS `Musical_Keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Musical_Keys` (
  `Key_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Note1` varchar(10) DEFAULT NULL,
  `Note2` varchar(10) DEFAULT NULL,
  `Note3` varchar(10) DEFAULT NULL,
  `Note4` varchar(10) DEFAULT NULL,
  `Note5` varchar(10) DEFAULT NULL,
  `Note6` varchar(10) DEFAULT NULL,
  `Note7` varchar(10) DEFAULT NULL,
  `Mood_ID` int DEFAULT NULL,
  PRIMARY KEY (`Key_ID`),
  KEY `Mood_ID` (`Mood_ID`),
  CONSTRAINT `musical_keys_ibfk_1` FOREIGN KEY (`Mood_ID`) REFERENCES `Mood` (`Mood_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Musical_Keys`
--

LOCK TABLES `Musical_Keys` WRITE;
/*!40000 ALTER TABLE `Musical_Keys` DISABLE KEYS */;
INSERT INTO `Musical_Keys` VALUES (1,'C Major','C','D','E','F','G','A','B',1),(2,'G Minor','G','A','Bb','C','D','E','F',2),(3,'E Major','E','F#','G#','A','B','C#','D#',3);
/*!40000 ALTER TABLE `Musical_Keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Song_Maker`
--

DROP TABLE IF EXISTS `Song_Maker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Song_Maker` (
  `User_ID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Song_Maker`
--

LOCK TABLES `Song_Maker` WRITE;
/*!40000 ALTER TABLE `Song_Maker` DISABLE KEYS */;
INSERT INTO `Song_Maker` VALUES (1,'Lala','lala@gmail.com'),(2,'WillSmith','will.smith@gmail.com'),(3,'Alicekeys','alicekeys@gmail.com');
/*!40000 ALTER TABLE `Song_Maker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Songs`
--

DROP TABLE IF EXISTS `Songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Songs` (
  `Song_ID` int NOT NULL AUTO_INCREMENT,
  `Title` varchar(50) DEFAULT NULL,
  `Dancability` float DEFAULT NULL,
  `Artist` varchar(50) DEFAULT NULL,
  `Genre_ID` int DEFAULT NULL,
  `Key_ID` int DEFAULT NULL,
  `User_ID` int DEFAULT NULL,
  `Lyrics` text,
  `Creation_Date` date DEFAULT NULL,
  `Released_Status` tinyint(1) DEFAULT NULL,
  `Time_Signature` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Song_ID`),
  KEY `Genre_ID` (`Genre_ID`),
  KEY `Key_ID` (`Key_ID`),
  KEY `User_ID` (`User_ID`),
  CONSTRAINT `songs_ibfk_1` FOREIGN KEY (`Genre_ID`) REFERENCES `Genres` (`Genre_ID`),
  CONSTRAINT `songs_ibfk_2` FOREIGN KEY (`Key_ID`) REFERENCES `Musical_Keys` (`Key_ID`),
  CONSTRAINT `songs_ibfk_3` FOREIGN KEY (`User_ID`) REFERENCES `Song_Maker` (`User_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Songs`
--

LOCK TABLES `Songs` WRITE;
/*!40000 ALTER TABLE `Songs` DISABLE KEYS */;
INSERT INTO `Songs` VALUES (1,'Radio',0.3,'Lana Del Rey',2,1,1,'Not even they can stop me now...','2012-01-01',1,'4/4'),(2,'So Long, London',0.45,'Taylor Swift',2,2,2,'So long,London...','2024-04-18',1,'4/4'),(3,'Back to Black',0.75,'Amy Winehouse',3,3,3,'He left no words to regret...','2012-04-03',1,'4/4');
/*!40000 ALTER TABLE `Songs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-23 13:52:03
