from dal.db import Db
from datetime import datetime

def insert_pedido(id_producto, id_pedido, cantidad, precio_unitario):
    sql = "INSERT INTO Detalle_Pedido(ProductoId, PedidoId, Cantidad, PrecioUnitario) VALUES(?, ?, ?, ?);"
    parametros = (id_producto, id_pedido, cantidad, precio_unitario)
    Db.ejecutar(sql, parametros)

def listar(id_pedido):
    sql = '''SELECT p.nombre, p.marca, dp.Cantidad, dp.PrecioUnitario 
            FROM Detalle_Pedido dp 
            INNER JOIN Productos p ON p.id = dp.ProductoId 
            WHERE dp.Activo = 1 AND dp.PedidoId = ? ;'''
    parametros = (id_pedido,)
    result = Db.consultar(sql, parametros,True)
    return result