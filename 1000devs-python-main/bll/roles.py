from dal.db import Db

def listar():
    sql = "SELECT id, rol FROM Roles ORDER BY id;"
    result = Db.consultar(sql)
    return result