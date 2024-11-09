-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 09, 2024 at 05:06 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_kmeans`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Admin'),
(2, 'Guru BK'),
(3, 'Siswa');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 2, 17),
(26, 2, 18),
(27, 2, 19),
(28, 2, 20),
(29, 2, 21),
(30, 2, 22),
(31, 2, 23),
(32, 2, 24),
(33, 3, 17),
(34, 3, 18),
(35, 3, 19),
(36, 3, 20),
(37, 3, 21),
(38, 3, 22),
(39, 3, 23),
(40, 3, 24);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$Sf2rWxdx0CQSteDYzyBO86$yj//I2fPM3kxrXhj0XcoKsciUwtAag6PO+jceoUnJLg=', '2024-11-09 16:06:11.611448', 1, 'admin', 'Admin', 'Pusat', 'admin@gmail.com', 1, 1, '2024-08-22 11:20:43.000000'),
(2, 'pbkdf2_sha256$260000$EBd0qwRonZhN3N5q7C4OIB$oOE27Y2WZkzT9rs75z4REftjPadsW7u/CfUlhMPpj5Q=', '2024-10-27 18:07:58.142850', 0, 'irham_hsb', 'IRHAM', 'HASIBUAN', 'irhamhsb@gmail.com', 0, 1, '2024-10-25 15:01:08.000000'),
(3, 'pbkdf2_sha256$260000$Ly2mXn3Jc0xkMouOIxveuX$SxFZpWTcESA0nMmKmJZkD6QjMCzFcLdYCWI3P7gxSCE=', '2024-10-28 14:12:27.000000', 0, 'jamilah_rambe', 'Jamilah', 'Rambe', 'jamilah@gmail.com', 0, 1, '2024-10-27 20:07:18.000000'),
(4, 'pbkdf2_sha256$260000$bk0ryQUAxiuyd5CiKJMiAK$qblRnyQtJ2E0M3seHxUazH4Na5o/c2GqL00PDiFV66k=', '2024-11-09 16:02:05.774700', 0, 'beriman_rambe', 'Beriman', 'Rambe', 'berimanrambe@gmai.com', 0, 1, '2024-10-27 20:22:56.489500'),
(5, 'pbkdf2_sha256$260000$K7Vy2iBqWwJ9uSCuDPrwcH$w1Q2W4JGRK+OSIC8BZuHWSbNR+vdCBdNkfuv3bhSlRc=', '2024-11-09 16:02:39.974786', 0, 'untung_rambe', 'Untung', 'Rambe', 'untung@gmail.com', 0, 1, '2024-11-09 14:23:37.613893'),
(6, 'pbkdf2_sha256$260000$iF7SIIQOUYbCMcoG8b8yMr$ZjSOEkWcU8jOXqTolaZDQa8pI5nRzz+4FVf//rTzN2o=', '2024-11-09 15:28:38.756245', 0, 'guru_bk', 'Anton', 'Sinaga', 'guru_bk@gmail.com', 0, 1, '2024-11-09 14:38:55.963007');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(6, 1, 1),
(1, 2, 3),
(4, 3, 3),
(15, 4, 3),
(13, 5, 3),
(16, 6, 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `data_history`
--

CREATE TABLE `data_history` (
  `id` int(11) NOT NULL,
  `s_fisik` int(2) NOT NULL,
  `s_verbal` int(2) NOT NULL,
  `s_psikologis` int(2) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_history`
--

INSERT INTO `data_history` (`id`, `s_fisik`, `s_verbal`, `s_psikologis`, `created_at`, `updated_at`) VALUES
(1, 752, 210, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(2, 562, 366, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(3, 945, 511, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(4, 855, 1564, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(5, 621, 1452, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(6, 566, 150, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(7, 774, 220, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(8, 421, 784, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(9, 295, 664, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(10, 455, 501, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(11, 664, 1020, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(12, 911, 1033, 2022, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(13, 1033, 1233, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(14, 1244, 1445, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(15, 1292, 1348, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(16, 1340, 1689, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(17, 1190, 1754, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(18, 1560, 1249, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(19, 2006, 1541, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(20, 800, 500, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(21, 2003, 1995, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(22, 2030, 1465, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(23, 1606, 1884, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(24, 1377, 1576, 2023, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(25, 1672, 1784, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(26, 1504, 1792, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(27, 1411, 1771, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(28, 1366, 2011, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(29, 1522, 1574, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(30, 1400, 1666, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(31, 904, 704, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57'),
(32, 504, 611, 2024, '2024-09-13 05:06:57', '2024-09-13 05:06:57');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-10-25 14:57:55.983295', '1', 'Admin', 1, '[{\"added\": {}}]', 3, 1),
(2, '2024-10-25 14:58:45.721641', '2', 'Guru BK', 1, '[{\"added\": {}}]', 3, 1),
(3, '2024-10-25 14:58:52.349050', '3', 'Siswa', 1, '[{\"added\": {}}]', 3, 1),
(4, '2024-10-25 14:59:03.537622', '3', 'Siswa', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1),
(5, '2024-10-25 15:01:09.383323', '2', 'irham_hsb', 1, '[{\"added\": {}}]', 4, 1),
(6, '2024-10-25 15:01:41.465358', '2', 'irham_hsb', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Groups\", \"Last login\"]}}]', 4, 1),
(7, '2024-10-25 15:25:41.346819', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"First name\"]}}]', 4, 1),
(8, '2024-10-28 14:12:21.798133', '3', 'jamilah_rambe', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1),
(9, '2024-10-28 14:12:49.040275', '3', 'jamilah_rambe', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(10, '2024-10-28 16:23:13.629725', '4', 'beriman_rambe', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'apps', 'm_data'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-22 11:02:24.436821'),
(2, 'auth', '0001_initial', '2024-08-22 11:02:25.177023'),
(3, 'admin', '0001_initial', '2024-08-22 11:02:25.391876'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-22 11:02:25.417867'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-22 11:02:25.469851'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-22 11:02:25.599021'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-22 11:02:25.684707'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-22 11:02:25.709701'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-22 11:02:25.721697'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-22 11:02:25.761647'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-22 11:02:25.764645'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-22 11:02:25.779641'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-22 11:02:25.801632'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-22 11:02:25.820965'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-22 11:02:25.854253'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-22 11:02:25.877244'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-22 11:02:25.894747'),
(18, 'sessions', '0001_initial', '2024-08-22 11:02:25.965016');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4h76wmni6g7ce32hnt0dpwc5k88yrgpj', '.eJxVjEEOwiAQRe_C2hAYO0Bduu8ZyMAMtmpoUtqV8e7apAvd_vfef6lI2zrGrckSJ1YXZdXpd0uUH1J3wHeqt1nnua7LlPSu6IM2Pcwsz-vh_h2M1MZv3TsjmcQBi3CBAmiz6cK5t31i710wgMVhcIgCxqOXQiYDEgC4jkm9P-NHN3c:1t5SWP:CQunFMepbStnQthNuE149VkDD2ZE5E7LqSbAypnhIFk', '2024-11-11 16:23:13.645269'),
('6noemnj6d17ox0ad2vi4l5yqrbtk5kxa', '.eJxVjEEOwiAQRe_C2pBCGWBcuu8ZCANTqRqalHZlvLtt0oVu33v_v0WI21rC1ngJUxZXocTll1FMT66HyI9Y77NMc12XieSRyNM2OcyZX7ez_TsosZV97axFSJr0qLRnDUiI6EiTZ0UGydkxeWDM2iH0Ziem8x2A641l9CQ-X8IBNro:1sposP:m7qy5x-1_IjuGAhuAJyiDJcmw5cy7szTrFV7xskar4o', '2024-09-29 13:01:17.672861'),
('7jrkbanibpubszrd70novln04m2hydif', '.eJxVjEEOwiAQRe_C2pChHQRcuu8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3ERKE6_W6D44LqDdKd6azK2ui5zkLsiD9rl1BI_r4f7d1Col29tFWbWOIIiE0ExaGTtrAFwka1zYIl4NOMAUZswYM4Z8xmCIbQpIon3B8EMN3U:1t9mYT:Sewvxp4WWlK7dCfmz0ry9lpD-KIo-d-Jor8xWMBX5qg', '2024-11-23 14:35:13.287862'),
('mm0szv1c96hvystfvo2xv1xqjsuastag', '.eJxVjMsOwiAQRf-FtSHA8Cgu3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmmp1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb918hpMEUVNyuYIgEYq9CX5nGwEssrp4kkQemknqT1IIIe2RBBGOuvY-wPdvTdQ:1t5R0h:rma1OBcS8ezt6jj44vl1xkHZO1xAePooGFiUGT3KZf0', '2024-11-11 14:46:23.635109'),
('ohepgx9dx9jfofeltzukmydulutd3j7t', '.eJxVjEEOwiAQRe_C2pBCGWBcuu8ZCANTqRqalHZlvLtt0oVu33v_v0WI21rC1ngJUxZXocTll1FMT66HyI9Y77NMc12XieSRyNM2OcyZX7ez_TsosZV97axFSJr0qLRnDUiI6EiTZ0UGydkxeWDM2iH0Ziem8x2A641l9CQ-X8IBNro:1su7YQ:oKNpVu3IpamewDutyTfmY_qnfDsNK6ZvtJ5siQ-AuRs', '2024-10-11 09:46:26.804022'),
('qbwfh75gmzbo13f1ilfgmbps107pki3q', '.eJxVjEEOwiAQRe_C2pBCGWBcuu8ZCANTqRqalHZlvLtt0oVu33v_v0WI21rC1ngJUxZXocTll1FMT66HyI9Y77NMc12XieSRyNM2OcyZX7ez_TsosZV97axFSJr0qLRnDUiI6EiTZ0UGydkxeWDM2iH0Ziem8x2A641l9CQ-X8IBNro:1sojEa:hMDezYxfJ29zlE3L5viLd9ra8aNBVTNaCegWTDvbn0Q', '2024-09-26 12:47:40.606613'),
('vpm857fq0z5zw93twgt48pgjol7wtc50', '.eJxVjEEOwiAQRe_C2pBCGWBcuu8ZCANTqRqalHZlvLtt0oVu33v_v0WI21rC1ngJUxZXocTll1FMT66HyI9Y77NMc12XieSRyNM2OcyZX7ez_TsosZV97axFSJr0qLRnDUiI6EiTZ0UGydkxeWDM2iH0Ziem8x2A641l9CQ-X8IBNro:1t9nyV:uT0M-T0lxGbTYVZadhgtM_mAfKComwzFAmukFKb0JUQ', '2024-11-23 16:06:11.616293'),
('yzd8mo9sdicsmpl2slt126g9s91hsc6d', '.eJxVjEEOwiAQRe_C2pAyMMC4dO8ZCDBUqoYmpV0Z765NutDtf-_9lwhxW2vYelnCxOIsjDj9binmR2k74Htst1nmua3LlOSuyIN2eZ25PC-H-3dQY6_fGoHRO8BiLXrtbCSHxlkoCpLV3hKVAcgoVgyQ84ikvSONPCYcIivx_gCfVDZ2:1t5SWX:GJtq4DjiWGTXCKmXgFh57piHEZCzBTAjEUxwtwNCYwU', '2024-11-11 16:23:21.394903');

-- --------------------------------------------------------

--
-- Table structure for table `kuesioner`
--

CREATE TABLE `kuesioner` (
  `id` int(11) NOT NULL,
  `question_text` text NOT NULL,
  `question_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kuesioner`
--

INSERT INTO `kuesioner` (`id`, `question_text`, `question_type`) VALUES
(1, 'Seberapa sering Anda dipukul atau didorong oleh teman ?', 'fisik'),
(2, 'Seberapa sering Anda dijambak atau dijewer oleh teman?', 'fisik'),
(3, 'Seberapa sering barang-barang Anda dirusak oleh teman?', 'fisik'),
(4, 'Seberapa sering Anda didorong atau dijatuhkan dengan sengaja oleh teman?', 'fisik'),
(5, 'Seberapa sering Anda dipukul dengan benda oleh teman?', 'fisik'),
(8, 'Seberapa sering Anda dipanggil dengan nama yang menghina?', 'verbal'),
(9, 'Seberapa sering Anda diejek karena penampilan fisik?', 'verbal'),
(10, 'Seberapa sering Anda diberi julukan yang membuat Anda merasa tersinggung?', 'verbal'),
(11, 'Seberapa sering Anda diejek atau dihina oleh teman?', 'verbal'),
(12, 'Seberapa sering Anda diancam secara verbal oleh teman?', 'verbal'),
(13, 'Seberapa sering Anda dikucilkan atau tidak diajak bergabung dengan teman?', 'psikologis'),
(14, 'Seberapa sering Anda didiamkan atau diabaikan oleh teman?', 'psikologis'),
(15, 'Seberapa sering Anda merasa diintimidasi oleh teman secara psikologis?', 'psikologis'),
(16, 'Seberapa sering Anda dijauhi atau dihindari oleh teman?', 'psikologis'),
(17, 'Seberapa sering Anda mendengar teman menyebarkan gosip buruk tentang Anda?', 'psikologis');

-- --------------------------------------------------------

--
-- Table structure for table `responses`
--

CREATE TABLE `responses` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `kuesioner_id` int(11) DEFAULT NULL,
  `answer` int(11) DEFAULT NULL,
  `submission_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `responses`
--

INSERT INTO `responses` (`id`, `user_id`, `kuesioner_id`, `answer`, `submission_date`) VALUES
(1, 2, 1, 2, '2024-10-25 16:30:07'),
(2, 2, 2, 1, '2024-10-25 10:30:06'),
(3, 2, 3, 1, '2024-10-25 10:30:11'),
(4, 2, 4, 4, '2024-10-25 10:30:19'),
(5, 2, 5, 3, '2024-10-25 10:30:25'),
(6, 3, 1, 1, '2024-10-28 07:14:08'),
(7, 3, 2, 2, '2024-10-28 07:14:13'),
(8, 3, 3, 3, '2024-10-28 07:14:17'),
(9, 3, 4, 2, '2024-10-28 07:14:21'),
(10, 3, 5, 1, '2024-10-28 07:14:26'),
(11, 3, 13, 5, '2024-10-28 07:14:31'),
(12, 3, 14, 3, '2024-10-28 07:14:36'),
(13, 3, 15, 4, '2024-10-28 07:14:41'),
(14, 3, 16, 1, '2024-10-28 07:14:46'),
(15, 3, 17, 2, '2024-10-28 07:14:50'),
(16, 3, 8, 1, '2024-10-28 07:15:04'),
(17, 3, 10, 1, '2024-10-28 07:26:15'),
(18, 3, 9, 2, '2024-10-28 07:26:25'),
(19, 3, 11, 4, '2024-10-28 07:26:32'),
(20, 3, 12, 5, '2024-10-28 07:26:38'),
(21, 4, 1, 1, '2024-10-28 07:47:48'),
(22, 4, 2, 3, '2024-10-28 07:47:53'),
(23, 4, 3, 4, '2024-10-28 07:47:57'),
(24, 4, 4, 3, '2024-10-28 07:48:06'),
(25, 4, 13, 3, '2024-10-28 07:48:11'),
(26, 4, 5, 1, '2024-10-28 07:48:16'),
(27, 4, 14, 5, '2024-10-28 07:48:20'),
(28, 4, 16, 2, '2024-10-28 07:48:25'),
(29, 4, 15, 2, '2024-10-28 07:48:34'),
(30, 4, 17, 5, '2024-10-28 07:48:39'),
(31, 4, 8, 1, '2024-10-28 07:48:49'),
(32, 4, 10, 2, '2024-10-28 07:49:01'),
(33, 4, 9, 1, '2024-10-28 07:49:10'),
(34, 4, 12, 4, '2024-10-28 07:49:16'),
(35, 4, 11, 3, '2024-10-28 07:49:21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `data_history`
--
ALTER TABLE `data_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `kuesioner`
--
ALTER TABLE `kuesioner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `responses`
--
ALTER TABLE `responses`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `data_history`
--
ALTER TABLE `data_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `kuesioner`
--
ALTER TABLE `kuesioner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `responses`
--
ALTER TABLE `responses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
