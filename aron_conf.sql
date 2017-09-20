-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
-- 
-- Host: localhost    Database: aron_conf
-- ------------------------------------------------------
-- Server version	5.5.54-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `log_data` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `utente` varchar(32) DEFAULT NULL,
  `azione` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbClient`
--

DROP TABLE IF EXISTS `tbClient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbClient` (
  `id_client` int(11) NOT NULL AUTO_INCREMENT,
  `client` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbClient`
--

LOCK TABLES `tbClient` WRITE;
/*!40000 ALTER TABLE `tbClient` DISABLE KEYS */;
INSERT INTO `tbClient` VALUES (4,'ABONECO');
/*!40000 ALTER TABLE `tbClient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbData`
--

DROP TABLE IF EXISTS `tbData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbData` (
  `hardware` varchar(255) NOT NULL,
  `item` varchar(255) NOT NULL,
  `it_data` varchar(16384) DEFAULT NULL,
  `id_client` int(11) DEFAULT NULL,
  `data` datetime DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbData`
--

LOCK TABLES `tbData` WRITE;
/*!40000 ALTER TABLE `tbData` DISABLE KEYS */;
INSERT INTO `tbData` VALUES ('INFO','INFO','Non Abbiamo la Gestione solo configurato armadio di rete',4,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `tbData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbGallery`
--

DROP TABLE IF EXISTS `tbGallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbGallery` (
  `id_client` int(11) DEFAULT NULL,
  `image` longblob,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tbGallery_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbGallery`
--

LOCK TABLES `tbGallery` WRITE;
/*!40000 ALTER TABLE `tbGallery` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbGallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbHardware`
--

DROP TABLE IF EXISTS `tbHardware`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbHardware` (
  `id_hardware` int(11) NOT NULL AUTO_INCREMENT,
  `hardware` varchar(45) DEFAULT NULL,
  `id_client` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_hardware`),
  KEY `fk_hardware_2_idx` (`id_client`),
  CONSTRAINT `fk_hardware` FOREIGN KEY (`id_client`) REFERENCES `tbClient` (`id_client`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbHardware`
--

LOCK TABLES `tbHardware` WRITE;
/*!40000 ALTER TABLE `tbHardware` DISABLE KEYS */;
INSERT INTO `tbHardware` VALUES (2,'INFO',4);
/*!40000 ALTER TABLE `tbHardware` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbHw`
--

DROP TABLE IF EXISTS `tbHw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbHw` (
  `hw` varchar(255) DEFAULT NULL,
  UNIQUE KEY `tbHw_hw_uindex` (`hw`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbHw`
--

LOCK TABLES `tbHw` WRITE;
/*!40000 ALTER TABLE `tbHw` DISABLE KEYS */;
INSERT INTO `tbHw` VALUES ('DNS'),('FILESERVER'),('FIREWALL'),('INFO'),('NAS'),('PRINTER'),('ROLES'),('ROUTER'),('SERVER'),('SERVER DC'),('SWITCH');
/*!40000 ALTER TABLE `tbHw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbIt`
--

DROP TABLE IF EXISTS `tbIt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbIt` (
  `items` varchar(255) DEFAULT NULL,
  UNIQUE KEY `tbIt_items_uindex` (`items`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbIt`
--

LOCK TABLES `tbIt` WRITE;
/*!40000 ALTER TABLE `tbIt` DISABLE KEYS */;
INSERT INTO `tbIt` VALUES ('AUTH-CODE'),('DOMINIO'),('HOST'),('IDRAC'),('ILO'),('INFO'),('IP ADDRESS'),('IP MASK'),('LAN'),('MODEL'),('NOME'),('NOTE'),('PASSWORD'),('RUOLO'),('SERIAL'),('SHARE DIRECTORY'),('SISTEMA OPERATIVO'),('SSLVPN PASSWORD'),('SSLVPN USER'),('STATIC ROUTE'),('TEAMVIEWER ID'),('TEAMVIEWER PSW'),('USER'),('VLAN'),('VPN PASW'),('VPN USER'),('WAN');
/*!40000 ALTER TABLE `tbIt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbItems`
--

DROP TABLE IF EXISTS `tbItems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbItems` (
  `id_hardware` int(11) NOT NULL AUTO_INCREMENT,
  `items` varchar(255) NOT NULL,
  `id_client` int(11) NOT NULL,
  KEY `fk_items_1_idx` (`id_hardware`,`id_client`),
  KEY `fk_tbItems_2_idx` (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbItems`
--

LOCK TABLES `tbItems` WRITE;
/*!40000 ALTER TABLE `tbItems` DISABLE KEYS */;
INSERT INTO `tbItems` VALUES (2,'INFO',4);
/*!40000 ALTER TABLE `tbItems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbLicense`
--

DROP TABLE IF EXISTS `tbLicense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbLicense` (
  `client` varchar(64) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `qty_dev` int(8) DEFAULT NULL,
  `active_date` date DEFAULT '0000-00-00',
  `exp_date` date DEFAULT '0000-00-00',
  `active_lic` tinyint(1) DEFAULT NULL,
  `req` varchar(64) DEFAULT NULL,
  `lic` varchar(64) DEFAULT NULL,
  `server_id` varchar(32) DEFAULT NULL,
  `pwd_client` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbLicense`
--

LOCK TABLES `tbLicense` WRITE;
/*!40000 ALTER TABLE `tbLicense` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbLicense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbUsers`
--

DROP TABLE IF EXISTS `tbUsers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbUsers` (
  `tbUser` varchar(16) NOT NULL,
  `tbPass` varchar(64) NOT NULL,
  `enable` int(1) DEFAULT NULL,
  `hash` varchar(32) DEFAULT NULL,
  UNIQUE KEY `tbUsers_UNIQUE` (`tbUser`),
  UNIQUE KEY `tbPass_UNIQUE` (`tbPass`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbUsers`
--

LOCK TABLES `tbUsers` WRITE;
/*!40000 ALTER TABLE `tbUsers` DISABLE KEYS */;
INSERT INTO `tbUsers` VALUES ('tony','$2b$12$D7YnWUlc/54t.BWWzBbtBe6QRRcD3gNLF/XVCXRHQYzieNuE0PoGG',2,'$2b$12$D7YnWUlc/54t.BWWzBbtBe');
/*!40000 ALTER TABLE `tbUsers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbfiles`
--

DROP TABLE IF EXISTS `tbfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbfiles` (
  `name_file` varchar(40) DEFAULT NULL,
  `buffer` longtext,
  `id_client` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbfiles`
--

LOCK TABLES `tbfiles` WRITE;
/*!40000 ALTER TABLE `tbfiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbfiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-20 17:07:44
