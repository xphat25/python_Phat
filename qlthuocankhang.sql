-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3307
-- Thời gian đã tạo: Th10 04, 2025 lúc 04:58 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `madm` int(11) NOT NULL,
  `tendm` varchar(100) NOT NULL,
  `mota` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`madm`, `tendm`, `mota`) VALUES
(1, 'Hot Sale', 'Sản phẩm đang giảm giá mạnh'),
(2, 'Thuốc', 'Các loại thuốc chữa bệnh ho'),
(3, 'áo', 'áo dài'),
(4, 'Thực phẩm chức năng', 'Thực phẩm hỗ trợ sức khỏe'),
(7, 'vitamin – sức khỏe', 'Tăng sức đề kháng, chống oxy hóa, hỗ trợ hấp thu sắt.'),
(8, 'dạ dày', 'Ức chế tiết acid dạ dày, điều trị trào ngược, loét dạ dày – tá tràng.');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `masp` int(11) NOT NULL,
  `tensp` varchar(255) NOT NULL,
  `giaban` decimal(10,2) NOT NULL,
  `giacu` decimal(10,2) DEFAULT NULL,
  `giamgia` int(11) DEFAULT NULL,
  `soluong` int(11) DEFAULT 0,
  `hinhanh` varchar(255) DEFAULT NULL,
  `madm` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`masp`, `tensp`, `giaban`, `giacu`, `giamgia`, `soluong`, `hinhanh`, `madm`) VALUES
(1, 'Nước tẩy trang Bioderma Sensibio', 398750.00, 515000.00, 25, 16, 'bioderma.jpg', 1),
(2, 'Tăm chỉ nha khoa Okamura 734503', 18000.00, 22000.00, 18, 20, 'okamura.jpg', 1),
(3, 'Nước súc miệng Listerine Cool Mint', 81000.00, 169000.00, 52, 16, 'listerine.jpg', 1),
(4, 'Nước Yến Collagen Green Bird Nutrient', 22500.00, 30000.00, 25, 60, 'greenbird.jpg', 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`madm`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`masp`),
  ADD KEY `madm` (`madm`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `madm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `masp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`madm`) REFERENCES `danhmuc` (`madm`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
