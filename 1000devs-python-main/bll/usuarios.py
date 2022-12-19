from dal.db import Db

def agregar(apellido, nombre, fecha_nacimiento, dni, correo_electronico, usuario, contrasenia, rol_Id):    
    sql = "INSERT INTO Usuarios(Apellido, Nombre, FechaNacimiento, Dni, CorreoElectronico, NombreUsuario, Contrasenia, id_rol) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, usuario, Db.encriptar_contraseña(contrasenia), rol_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, apellido, nombre, fecha_nacimiento, dni, correo_electronico, contrasenia, rol_Id):    
    sql = "UPDATE Usuarios SET Apellido = ?, Nombre = ?, FechaNacimiento = ?, Dni = ?, CorreoElectronico = ?, Contrasenia = ?, id_rol = ? WHERE id = ? AND Activo = 1;"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, Db.encriptar_contraseña(contrasenia), rol_Id, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Usuarios SET Activo = 0 WHERE id = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Usuarios WHERE id = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT u.id, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.NombreUsuario, u.id_rol, r.rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.id_rol = r.id
            WHERE u.Activo = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(usuario):    
    sql = '''SELECT u.id, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.NombreUsuario, u.id_rol, r.rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.id_rol = r.id
            WHERE u.NombreUsuario LIKE ? AND u.Activo = 1;'''    
    parametros = ('%{}%'.format(usuario),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(usuario, contrasenia):    
    sql = "SELECT NombreUsuario FROM Usuarios WHERE NombreUsuario = ? AND Contrasenia = ? AND Activo = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None

def existe(usuario):
    sql = "SELECT COUNT(*) FROM Usuarios WHERE NombreUsuario = ? AND Activo = 1;"
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT u.id, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.NombreUsuario, u.id_rol, r.rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.id_rol = r.id
            WHERE u.id = ? AND u.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def obtener_nombre_usuario(usuario):
    sql = '''SELECT u.id, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.NombreUsuario, u.id_rol, r.rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.id_rol = r.id
            WHERE u.NombreUsuario = ? AND u.Activo = 1;'''
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)    
    return result