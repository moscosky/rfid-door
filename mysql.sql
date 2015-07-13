CREATE TABLE IF NOT EXISTS `cards` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `tagId` bigint(18) unsigned NOT NULL,
  `active` enum('0','1') COLLATE utf8_czech_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE IF NOT EXISTS `readings` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `tagId` bigint(18) unsigned NOT NULL,
  `time` bigint(14) unsigned NOT NULL,
  `action` varchar(255) COLLATE utf8_czech_ci DEFAULT 'logout',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
