from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import bll.Categoria_productos as cat_prod
import tkinter.messagebox as tkMsgBox
import bll.productos as prod

class Producto(Toplevel):
    def __init__(self, master = None,id_producto = None):
        super().__init__(master)
        #setting title
        self.id_producto = id_producto
        self.title("productos")
        #setting window size
        width=380
        height=312
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=True, height=True)

        GLabel_174=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_174["font"] = ft
        GLabel_174["fg"] = "#333333"
        GLabel_174["justify"] = "center"
        GLabel_174["text"] = "Nombre:"
        GLabel_174.place(x=20,y=20,width=102,height=30)

        GLabel_467=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_467["font"] = ft
        GLabel_467["fg"] = "#333333"
        GLabel_467["justify"] = "center"
        GLabel_467["text"] = "Precio"
        GLabel_467.place(x=20,y=70,width=102,height=30)

        GLabel_332=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_332["font"] = ft
        GLabel_332["fg"] = "#333333"
        GLabel_332["justify"] = "center"
        GLabel_332["text"] = "Marca"
        GLabel_332.place(x=20,y=120,width=102,height=30)

        GLineEdit_218=Entry(self,name="nombre")
        GLineEdit_218["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_218["font"] = ft
        GLineEdit_218["fg"] = "#333333"
        GLineEdit_218["justify"] = "left"
        GLineEdit_218["text"] = ""
        GLineEdit_218.place(x=150,y=20,width=180,height=30)

        GLineEdit_456=Entry(self, name="precio")
        GLineEdit_456["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_456["font"] = ft
        GLineEdit_456["fg"] = "#333333"
        GLineEdit_456["justify"] = "left"
        GLineEdit_456["text"] = ""
        GLineEdit_456.place(x=150,y=70,width=180,height=30)

        GLineEdit_172=Entry(self,name="marca")
        GLineEdit_172["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_172["font"] = ft
        GLineEdit_172["fg"] = "#000000"
        GLineEdit_172["justify"] = "left"
        GLineEdit_172["text"] = ""
        GLineEdit_172.place(x=150,y=120,width=180,height=30)

        GButton_572=Button(self)
        GButton_572["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_572["font"] = ft
        GButton_572["fg"] = "#000000"
        GButton_572["justify"] = "center"
        GButton_572["text"] = "Aceptar"
        GButton_572.place(x=40,y=230,width=102,height=30)
        GButton_572["command"] = self.aceptar

        GButton_921=Button(self)
        GButton_921["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_921["font"] = ft
        GButton_921["fg"] = "#000000"
        GButton_921["justify"] = "center"
        GButton_921["text"] = "Cancelar"
        GButton_921.place(x=230,y=230,width=102,height=30)
        GButton_921["command"] = self.cancel

        GLabel_928=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_928["font"] = ft
        GLabel_928["fg"] = "#333333"
        GLabel_928["justify"] = "center"
        GLabel_928["text"] = "Categoria"
        GLabel_928.place(x=20,y=170,width=102,height=30)

        categorias = dict(cat_prod.listar())
        print(categorias)
        print(list(categorias.values()))
        
        cb_categorias = ttk.Combobox(self, state="readonly", values=list(categorias.values()), name="cbCategorias")
        cb_categorias.place(x=150,y=170,width=180,height=30)

        if self.id_producto is not None:
            p = prod.obtener(self.id_producto)
            if p is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del producto, reintente nuevamente")
               self.destroy()
            else:
                nombre  = p[0]
                GLineEdit_218.insert(0, nombre)
                precio = p[1]
                GLineEdit_456.insert(0, precio)
                marca = p[2]
                GLineEdit_172.insert(0, p[2])
                id_categoria = p[3]
                cb_categorias.current(id_categoria-1)
            

    def get_value(self, name):
        return self.nametowidget(name).get()
    
    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    
    def aceptar(self):
        try:
            nombre = self.get_value("nombre")
            precio = self.get_value("precio")
            marca = self.get_value("marca")
            categoria = self.get_index("cbCategorias")
            if nombre == "":
                tkMsgBox.showerror(self.master.title(), "Nombre es un valor requerido.")
                return
            if precio == "":
                tkMsgBox.showerror(self.master.title(), "Precio es un valor requerido.")
                return
            if marca == "":
                tkMsgBox.showerror(self.master.title(), "Marca es un valor requerido.")
                return
            if categoria == 0:
                tkMsgBox.showerror(self.master.title(), "Categoria es un valor requerido.")
                return
            if self.id_producto == None:
                if not prod.existe(nombre, precio, marca):
                    prod.cargar_producto(nombre, marca, precio, categoria)
                    tkMsgBox.showinfo("","Producto Cargado")
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()
            else: 
                prod.modificar_producto(nombre, marca, precio, categoria, self.id_producto)
                tkMsgBox.showinfo("","Producto Modificado")
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()
                

        except Exception as ex:
            tkMsgBox.showerror("ERROR", str(ex))
            
            

    def cancel(self):
        self.destroy()