-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2018 at 04:27 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 5.6.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soulmet`
--

-- --------------------------------------------------------

--
-- Table structure for table `proposal`
--

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL,
  `romeo_id` int(11) NOT NULL,
  `juliet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proposal`
--

INSERT INTO `proposal` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES
(1, 5, 6),
(2, 6, 5),
(3, 5, 11),
(4, 14, 10),
(5, 14, 3),
(6, 5, 14),
(7, 10, 7),
(8, 14, 5),
(9, 15, 5),
(10, 5, 15),
(11, 19, 18),
(12, 18, 19);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `city`) VALUES
(1, 'Eisenberg', 'rahul@gmail.com', 'rahul1234', 'Male', 'Delhi'),
(3, 'Dave', 'deb@h.com', '1223', 'Male', 'Kolkata'),
(4, 'Salman', 'sallu@gmail.com', '123', 'Male', 'Heaven'),
(5, 'Robb', 'robb@gmail.com', 'robb123', 'Male', 'Winterfell'),
(6, 'Bruce', 'wayne@gmail.com', '12345', 'Male', 'Gotham'),
(7, 'Daenerys', 'danny@gmail.com', 'danny69', 'Female', 'Dragonstone'),
(8, 'Sumona', 'Sumona@gmail.com', 'sumona69', 'Female', 'Behala'),
(9, 'Russell', 'crowe@lol.in', 'rc132', 'Male', 'New Zealand'),
(10, 'Orlando', 'bloom', 'ob23', 'Male', 'Mordor'),
(11, 'cersei', 'lan@gmail.com', 'cl23', 'Female', 'Hell'),
(14, 'Pucci', 'p@g', 'p11', 'Female', 'Bravos'),
(15, 'Dorthy', 'dorthy@g', 'dg', 'Female', 'Chicago'),
(16, 'Quinn', 'Q@abc', 'abc', 'Female', 'Gotham'),
(18, 'Coutinho', 'c@b', '12345', 'Male', 'Barcelona'),
(19, 'Maron Brando', 'marlon', 'marlon', 'Male', 'Sicily');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proposal`
--
ALTER TABLE `proposal`
  ADD PRIMARY KEY (`proposal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `proposal`
--
ALTER TABLE `proposal`
  MODIFY `proposal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
