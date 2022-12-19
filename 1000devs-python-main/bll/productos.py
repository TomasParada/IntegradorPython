from dal.db import Db

def cargar_producto(nombre, marca, precios, id_categ):    
    sql = "INSERT INTO Productos(nombre, marca, precio, id_categoria) VALUES(?, ?, ?, ?);"
    parametros = (nombre, marca, precios, id_categ)
    Db.ejecutar(sql, parametros)

def modificar_producto(nombre, marca, precios, id_categ, id):    
    sql = "UPDATE Productos SET nombre = ?,marca = ?, precio = ?, id_categoria = ? WHERE id = ?;"
    parametros = (nombre, marca, precios, id_categ, id)
    Db.ejecutar(sql, parametros) 

def existe(nombre, precio, marca):
    sql = "SELECT COUNT(*) FROM Productos WHERE nombre = ? AND precio = ? AND marca = ?;"
    parametros = (nombre, precio, marca)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def listar():
    sql = '''SELECT p.id, p.nombre, p.precio, p.marca, cp.categoria
            FROM Productos p
            INNER JOIN Categoria_Productos cp ON p.id_categoria = cp.id;'''
    result = Db.consultar(sql)
    return result

def obtener(id_producto):
    sql = '''SELECT p.nombre, p.precio, p.marca, p.id_categoria
            FROM Productos p 
            WHERE p.id = ?;'''
    parametros = (id_producto,)
    result = Db.consultar(sql, parametros, False)    
    return result

def eliminar(id):
    sql = "DELETE FROM Productos WHERE id = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)