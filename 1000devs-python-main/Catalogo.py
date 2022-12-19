from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.productos as prod
import bll.pedido as pedido
import bll.detalle_pedido as detalle_pedido
from carrito import Carrito

class Catalogo(Toplevel):
    def __init__(self, master=None, usuario_id = None):
        super().__init__(master)        
        self.usuario_id = usuario_id
        self.master = master
        self.select_id = -1        
        self.title("Catalogo")        
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

        GLineEdit_456=Entry(self, name="cantidad")
        GLineEdit_456["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_456["font"] = ft
        GLineEdit_456["fg"] = "#333333"
        GLineEdit_456["justify"] = "left"
        GLineEdit_456["text"] = ""
        GLineEdit_456.place(x=500,y=10,width=70,height=25)
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Agregar al carrito"
        btn_eliminar.place(x=600,y=10,width=150,height=25)
        btn_eliminar["command"] = self.agregar

        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Ver carrito"
        btn_eliminar.place(x=330,y=10,width=150,height=25)
        btn_eliminar["command"] = self.ver_carrito

    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        self.id_pedido = -1
        try:
            result = pedido.obtener_id(self.usuario_id)
            if result is not None:
                self.id_pedido = result[0]
            if self.id_pedido == -1:#Creamos el pedido
                pedido.insert_pedido(self.usuario_id)
            result = pedido.obtener_id(self.usuario_id)
            self.id_pedido = result[0]

            cantidad = self.get_value("cantidad")
            if cantidad == "":
                tkMsgBox.showerror(self.master.title(), "Cantidad no especificada.")
                return
            else:
                producto = prod.obtener(self.select_id)
                detalle_pedido.insert_pedido(self.select_id, self.id_pedido, cantidad, producto[1])
                tkMsgBox.showinfo("","Producto Agregado al Carrito")
        except Exception as ex:
            print(str(ex))
            
    def ver_carrito(self): 
        Carrito(self,self.usuario_id)
    
    def get_value(self, name):
        return self.nametowidget(name).get()
    

    def refrescar(self):        
        tvproductos = self.nametowidget("tvProductos")
        for record in tvproductos.get_children():
            tvproductos.delete(record)
        productos = prod.listar()
        for p in productos:
            tvproductos.insert("", END, text=p[0], values=(p[1], p[2], p[3], p[4])) 