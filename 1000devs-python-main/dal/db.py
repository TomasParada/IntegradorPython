import sqlite3
from datetime import date
import hashlib

class Db:
    database = "SuperMarket.db"

    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(Db.database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(Db.database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_categoriaproducto = """CREATE TABLE IF NOT EXISTS "Categoria_Productos" (
                                "id"	INTEGER NOT NULL,
                                "categoria"	TEXT NOT NULL,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );"""

        sql_productos = """CREATE TABLE IF NOT EXISTS "Productos" (
	                    "id"	INTEGER NOT NULL,
	                    "nombre"	TEXT NOT NULL,
                        "precio"	REAL NOT NULL,
                        "marca"	    TEXT NOT NULL,
                        "id_categoria"	INTEGER NOT NULL,
                        PRIMARY KEY("id" AUTOINCREMENT),
                        CONSTRAINT "fk_categoria" FOREIGN KEY("id_categoria") REFERENCES "Categoria_Productos"("id")
                    );"""

        sql_ventas = """CREATE TABLE IF NOT EXISTS "Ventas" (
                    "id"	INTEGER NOT NULL,
                    "id_usuario"	INTEGER NOT NULL,
                    "id_producto"	INTEGER NOT NULL,
                    "precio_venta_momento"	REAL NOT NULL,
                    "cantidad"	INTEGER NOT NULL,
                    "fecha"	TEXT NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT),
                    CONSTRAINT "fk_id_usuario" FOREIGN KEY("id_usuario") REFERENCES "Usuarios"("id"),
                    CONSTRAINT "fk_id_producto" FOREIGN KEY("id_producto") REFERENCES "Productos"("id")
                );"""

        sql_roles = """CREATE TABLE IF NOT EXISTS "Roles" (
                    "id"	INTEGER NOT NULL,
                    "rol"	VARCHAR(30) NOT NULL UNIQUE,
                    "Activo"	INTEGER NOT NULL DEFAULT 1,
                    PRIMARY KEY("id" AUTOINCREMENT)
                );"""

        sql_usuarios = """CREATE TABLE IF NOT EXISTS "Usuarios" (
                        "id"	INTEGER NOT NULL,
                        "Apellido"	VARCHAR(50),
                        "Nombre"	VARCHAR(30),
                        "FechaNacimiento"	VARCHAR(23),
                        "Dni"	INTEGER,
                        "CorreoElectronico"	VARCHAR(30),
                        "NombreUsuario"	VARCHAR(15) UNIQUE,
                        "Contrasenia"	VARCHAR(100),
                        "id_rol"	INTEGER NOT NULL,
                        "Activo"	INTEGER NOT NULL DEFAULT 1,
                        PRIMARY KEY("id" AUTOINCREMENT),
                        CONSTRAINT "fk_id_rol" FOREIGN KEY("id_rol") REFERENCES "Roles"("id")
                    );"""

        sql_pedido = """CREATE TABLE IF NOT EXISTS "Pedido" (
                    "Id"	INTEGER NOT NULL,
                    "UsuarioId"	INTEGER,
                    "Fecha"	VARCHAR(30),
                    "Total"	REAL,
                    "Activo"	INTEGER NOT NULL DEFAULT 1,
                    PRIMARY KEY("Id" AUTOINCREMENT),
                    FOREIGN KEY("UsuarioId") REFERENCES "Usuarios"
                );"""

        sql_detallepedido = """CREATE TABLE IF NOT EXISTS "Detalle_Pedido" (
                            "ProductoId"	INTEGER,
                            "PedidoId"	INTEGER,
                            "Cantidad"	VARCHAR(50),
                            "PrecioUnitario"	INTEGER,
                            "Subtotal"	INTEGER,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            FOREIGN KEY("ProductoId") REFERENCES "Productos"("id")
                        );"""

        tablas = {"categoria_productos": sql_categoriaproducto,
            "productos": sql_productos,
            "ventas": sql_ventas,
            "Roles": sql_roles,
            "Usuarios": sql_usuarios,
            "pedido":sql_pedido,
            "detalle_pedido":sql_detallepedido
        }

        with sqlite3.connect(Db.database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
            cnn.commit()
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (id, rol) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        tablas = {"Roles": sql_roles}

        with sqlite3.connect(Db.database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)
            cnn.commit()

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()