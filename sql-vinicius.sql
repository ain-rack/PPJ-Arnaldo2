CREATE DATABASE db_vinicius;

USE db_vinicius;

CREATE TABLE IF NOT EXISTS tlb_mes (
	id_mes smallint AUTO_INCREMENT PRIMARY KEY,
    meses varchar(50) NOT NULL,
    total_vendas float default NULL,
    total_cobrado float default NULL,
    total_restante float default NULL,
    ano int NOT NULL
);

LOCK TABLES tlb_mes WRITE;
INSERT INTO tlb_mes VALUES (1, 'Janeiro', NULL, NULL, NULL,'2022'), (2, 'Fevereiro', NULL, NULL, NULL,'2022'), (3, 'Março', NULL, NULL, NULL,'2022'), (4, 'Abril', NULL, NULL, NULL,'2022'), (5, 'Maio', NULL, NULL, NULL,'2022'), (6, 'Junho',  NULL, NULL, NULL,'2022'), (7, 'Julho', NULL, NULL, NULL,'2022'), (8, 'Agosto', NULL, NULL, NULL,'2022'), (9, 'Setembro',  NULL, NULL, NULL,'2022'), (10, 'Outubro',  NULL, NULL, NULL,'2022'), (11, 'Novembro',  NULL, NULL, NULL,'2022'), (12, 'Dezembro',  NULL, NULL, NULL,'2022');
UNLOCK TABLES;

USE db_vinicius;

CREATE TABLE IF NOT EXISTS tlb_cataguases (
	id_cat smallint AUTO_INCREMENT PRIMARY KEY,
    revendedoras varchar(50) NOT NULL,
    total_vendas float DEFAULT NULL,
    total_cobrado float DEFAULT NULL,
    total_restante float DEFAULT NULL,
    mes varchar(50) NOT NULL,
    ano int NOT NULL
);
    
LOCK TABLES tlb_cataguases WRITE;
INSERT INTO tlb_cataguases VALUES (1, 'Maria', '600', '400', '200','Fevereiro', '2022'), (2, 'Fatima', '400', '200', '200', 'Março', '2022'), (3, 'Silvana', '500', '300', '200', 'Maio', '2022');
UNLOCK TABLES;

USE db_vinicius;

CREATE TABLE IF NOT EXISTS tlb_r_dos_lagos (
	id_cat smallint AUTO_INCREMENT PRIMARY KEY,
    revendedoras varchar(50) NOT NULL,
    total_vendas float DEFAULT NULL,
    total_cobrado float DEFAULT NULL,
    total_restante float DEFAULT NULL,
    mes varchar(50) NOT NULL,
    ano int NOT NULL
);
    
LOCK TABLES tlb_r_dos_lagos WRITE;
INSERT INTO tlb_r_dos_lagos VALUES (1, 'Maria', '600', '400', '200', 'Fevereiro', '2022'), (2, 'Fatima', '400', '200', '200', 'Fevereiro', '2022'), (3, 'Silvana', '500', '300', '200', 'Fevereiro', '2022');
UNLOCK TABLES;

USE db_vinicius;

CREATE TABLE IF NOT EXISTS tlb_mage (
	id_cat smallint AUTO_INCREMENT PRIMARY KEY,
    revendedoras varchar(50) NOT NULL,
    total_vendas float DEFAULT NULL,
    total_cobrado float DEFAULT NULL,
    total_restante float DEFAULT NULL,
    mes varchar(50) NOT NULL,
    ano int NOT NULL
);
    
LOCK TABLES tlb_mage WRITE;
INSERT INTO tlb_mage VALUES (1, 'Mariana', '600', '400', '200', 'Fevereiro', '2022'), (2, 'Bruna', '400', '200', '200', 'Fevereiro', '2022'), (3, 'Renata', '500', '300', '200', 'Fevereiro', '2022');
UNLOCK TABLES;
