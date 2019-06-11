/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.1.222
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : 192.168.1.222:3306
 Source Schema         : reptile

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 11/06/2019 18:03:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for reptileUrl
-- ----------------------------
DROP TABLE IF EXISTS `reptileUrl`;
CREATE TABLE `reptileUrl`  (
  `id` int(128) UNSIGNED NOT NULL AUTO_INCREMENT,
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `reptilestatus` int(1) UNSIGNED NULL DEFAULT 0,
  `getstatus` int(1) UNSIGNED NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of reptileUrl
-- ----------------------------
INSERT INTO `reptileUrl` VALUES (1, 'https://tieba.baidu.com/p/6038341188', 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
