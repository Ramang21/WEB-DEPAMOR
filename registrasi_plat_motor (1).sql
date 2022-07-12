-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 03, 2022 at 04:53 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `depamor`
--

-- --------------------------------------------------------

--
-- Table structure for table `registrasi_plat_motor`
--

CREATE TABLE `registrasi_plat_motor` (
  `id` int(11) NOT NULL,
  `Username` int(11) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `NomorPlat` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registrasi_plat_motor`
--

INSERT INTO `registrasi_plat_motor` (`id`, `Username`, `Nama`, `NomorPlat`, `Status`) VALUES
(13, 19090001, 'Ramang Darussalam', 'B 2001 RG', 'Mahasiswa'),
(14, 19090002, 'Ndaru ', 'G 2001 RG', 'Mahasiswa'),
(15, 199999, 'ucup', 'G 2001 RG', 'Mahasiswa'),
(16, 199999, 'al-an', 'b 2001 an', 'dosen');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registrasi_plat_motor`
--
ALTER TABLE `registrasi_plat_motor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `registrasi_plat_motor`
--
ALTER TABLE `registrasi_plat_motor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
