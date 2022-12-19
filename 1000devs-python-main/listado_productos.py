from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.productos as prod
from agregar_producto import Producto

class Productos(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("Listado de Productos")        
        width=800
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Productos:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("Nombre", "Precio", "Marca","Categoria"), name="tvProductos")
        tv.column("#0", width=78)
        tv.column("Nombre", width=100, anchor=CENTER)
        tv.column("Precio", width=150, anchor=CENTER)
        tv.column("Marca", width=150, anchor=CENTER)
        tv.column("Categoria", width=150, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("Nombre", text="Nombre", anchor=CENTER)
        tv.heading("Precio", text="Precio", anchor=CENTER)
        tv.heading("Marca", text="Marca", anchor=CENTER)
        tv.heading("Categoria", text="Categoria", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=40,width=750,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=530,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=610,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=690,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar

    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Producto(self)
        

    def editar(self): 
        Producto(self, id_producto = self.select_id)

    def eliminar(self):
        if self.select_id == -1:
            tkMsgBox.showerror("ERROR","No se selecciono producto")
        else:
            answer =  tkMsgBox.askokcancel(self.title(), "¿Está seguro de eliminar este registro?")   
            if answer:
                prod.eliminar(self.select_id)
                self.refrescar()

    def refrescar(self):        
        tvproductos = self.nametowidget("tvProductos")
        for record in tvproductos.get_children():
            tvproductos.delete(record)
        productos = prod.listar()
        for p in productos:
            tvproductos.insert("", END, text=p[0], values=(p[1], p[2], p[3], p[4]))