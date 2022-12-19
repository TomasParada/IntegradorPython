from dal.db import Db

def listar():
    sql = "SELECT id, categoria FROM Categoria_Productos ORDER BY id;"
    result = Db.consultar(sql)
    return result