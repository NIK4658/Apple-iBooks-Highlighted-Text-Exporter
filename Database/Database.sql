-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 15, 2022 at 04:27 PM
-- Server version: 10.5.15-MariaDB-0+deb11u1
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Database`
--

-- --------------------------------------------------------

--
-- Table structure for table `AUTHORS`
--

CREATE TABLE `AUTHORS` (
  `ID` int(11) NOT NULL,
  `Name` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `BOOKS`
--

CREATE TABLE `BOOKS` (
  `ID` int(11) NOT NULL,
  `Title` text NOT NULL,
  `ReleaseYear` year(4) DEFAULT NULL,
  `FileName` text DEFAULT NULL,
  `AuthorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `TEXTNOTES`
--

CREATE TABLE `TEXTNOTES` (
  `ID` int(11) NOT NULL,
  `CreatedTime` int(11) DEFAULT NULL,
  `InsertedTime` timestamp NOT NULL DEFAULT current_timestamp(),
  `Style` int(11) DEFAULT NULL,
  `Paragraph` text DEFAULT NULL,
  `PersonalNote` text DEFAULT NULL,
  `Content` text DEFAULT NULL,
  `AuthorID` int(11) DEFAULT NULL,
  `BookID` int(11) DEFAULT NULL,
  `UserUploaded` int(11) DEFAULT NULL,
  `UpVotes` int(11) NOT NULL DEFAULT 0,
  `DownVotes` int(11) NOT NULL DEFAULT 0,
  `Public` tinyint(1) NOT NULL DEFAULT 1,
  `Reviewed` tinyint(1) NOT NULL DEFAULT 0,
  `BadWords` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `AUTHORS`
--
ALTER TABLE `AUTHORS`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `BOOKS`
--
ALTER TABLE `BOOKS`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `AuthorID` (`AuthorID`);

--
-- Indexes for table `TEXTNOTES`
--
ALTER TABLE `TEXTNOTES`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `AuthorID` (`AuthorID`),
  ADD KEY `BookID` (`BookID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `AUTHORS`
--
ALTER TABLE `AUTHORS`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BOOKS`
--
ALTER TABLE `BOOKS`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `TEXTNOTES`
--
ALTER TABLE `TEXTNOTES`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `BOOKS`
--
ALTER TABLE `BOOKS`
  ADD CONSTRAINT `BOOKS_ibfk_1` FOREIGN KEY (`AuthorID`) REFERENCES `AUTHORS` (`ID`);

--
-- Constraints for table `TEXTNOTES`
--
ALTER TABLE `TEXTNOTES`
  ADD CONSTRAINT `TEXTNOTES_ibfk_1` FOREIGN KEY (`AuthorID`) REFERENCES `AUTHORS` (`ID`),
  ADD CONSTRAINT `TEXTNOTES_ibfk_2` FOREIGN KEY (`BookID`) REFERENCES `BOOKS` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
