from dal.db import Db
from datetime import datetime

def insert_pedido(usuario_id):
    sql = "INSERT INTO Pedido(UsuarioId, Fecha) VALUES(?, ?);"
    fecha = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S")
    parametros = (usuario_id, fecha)
    Db.ejecutar(sql, parametros)

def obtener_id(usuario_id):
    sql = '''SELECT pe.Id 
            FROM Pedido pe 
            WHERE pe.UsuarioId = ? AND pe.Activo = 1 
            ORDER BY pe.Id DESC;'''
    parametros = (usuario_id,)
    result = Db.consultar(sql, parametros, False)    
    return result