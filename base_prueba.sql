BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Categoria_Productos" (
	"id"	INTEGER NOT NULL,
	"categoria"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Roles" (
	"id"	INTEGER NOT NULL,
	"rol"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Usuarios" (
	"id"	INTEGER NOT NULL,
	"nombre_usuario"	TEXT(50) NOT NULL UNIQUE,
	"email"	TEXT(50),
	"es_activo"	INTEGER NOT NULL DEFAULT 1,
	"id_rol"	INTEGER NOT NULL,
	CONSTRAINT "fk_id_rol" FOREIGN KEY("id_rol") REFERENCES "Roles"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Productos" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"precio"	REAL NOT NULL,
	"id_categoria"	INTEGER NOT NULL,
	CONSTRAINT "fk_categoria" FOREIGN KEY("id_categoria") REFERENCES "Categoria_Productos"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Ventas" (
	"id"	INTEGER NOT NULL,
	"id_usuario"	INTEGER NOT NULL,
	"id_producto"	INTEGER NOT NULL,
	"precio_venta_momento"	REAL NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	"fecha"	TEXT NOT NULL,
	CONSTRAINT "fk_id_usuario" FOREIGN KEY("id_usuario") REFERENCES "Usuarios"("id"),
	CONSTRAINT "fk_id_producto" FOREIGN KEY("id_producto") REFERENCES "Productos"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Categoria_Productos" ("id","categoria") VALUES (1,'lacteos'),
 (2,'carnes'),
 (3,'golosinas');
INSERT INTO "Roles" ("id","rol") VALUES (1,'administrador'),
 (2,'cliente'),
 (3,'supervisor');
INSERT INTO "Usuarios" ("id","nombre_usuario","email","es_activo","id_rol") VALUES (1,'Tomás Parada','tomasparada.tsap@gmail.com',1,1),
 (2,'Tomás Parada1','tomasparada.tsap@gmail.com',1,2),
 (7,'Tomás Parada2','tomasparada.tsap@gmail.com',1,2);
COMMIT;
