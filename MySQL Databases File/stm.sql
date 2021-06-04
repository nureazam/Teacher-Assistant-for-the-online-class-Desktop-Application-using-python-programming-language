-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2020 at 04:41 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stm`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `roll_no` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`roll_no`, `name`, `email`, `gender`, `contact`, `dob`, `address`) VALUES
(1, 'Md.Nur-E-Azam', 'nur.azam@gmail.com', 'male', '012457896', 'A1=8, A2=8,miss', 'Quiz1=20, Quiz2=19, Quiz3=20, Mid1=30, Mid2=30, Final = 30\n\n\n\n\n\n\n\n\n\n'),
(2, 'Hridoy Shaha', 'hridoyshaha@gmail.com', 'male', '017789456123', 'A1=8, A2=10, A3=9', 'Quiz1=15, Quiz2=18, Quiz3=20, Mid1=25, Mid2=28, Final = 35\n'),
(3, 'Ashiq', 'ashiq@gmail.com', 'male', '016987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n'),
(4, 'Ashiq', 'ashiq@gmail.com', 'male', '1698745120', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n'),
(5, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n'),
(6, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=5', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n'),
(7, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n'),
(8, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n'),
(9, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n'),
(10, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n'),
(11, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n'),
(12, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n'),
(13, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n'),
(14, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n'),
(15, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(16, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(17, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(18, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(19, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=20, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(20, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(21, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(22, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 35\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(24, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(25, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(26, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(27, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(28, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(29, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 40\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(23, 'Ashiq', 'ashiq@gmail.com', 'male', '16987451203', 'A1=10, A2=10, A3=9', 'Quiz1=20, Quiz2=18, Quiz3=20, Mid1=30, Mid2=28, Final = 35\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
(31, 'Abdur Razzak', 'abrurrazzak0096@gmail.com', 'male', '1786832506', 'A1=20, A2=19', 'Quiz1=15, Quiz2=15, Mid1=25, Mid2=24\n\n\n'),
(1512268042, 'Md.Nur-E-Azam', 'nur.azam@gmail.com', 'male', '12457896', 'A1=8, A2=8,miss', 'Quiz1=20, Quiz2=19, Quiz3=20, Mid1=30, Mid2=30, Final = 30\n\n\n\n\n\n\n\n\n\n\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
