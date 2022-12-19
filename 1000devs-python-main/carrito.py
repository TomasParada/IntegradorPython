from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.productos as prod
from agregar_producto import Producto
import bll.pedido as pedido
import bll.detalle_pedido as detalle_pedido

class Carrito(Toplevel):
    def __init__(self, master=None, usuario_id = None):
        super().__init__(master)        
        self.usuario_id = usuario_id
        self.master = master
        self.select_id = -1        
        self.title("Carrito")        
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
        GLabel_464["text"] = "Carrito:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("Nombre", "Marca","Cantidad","Precio"), name="tvCarrito")
        tv.column("#0", width=78)
        tv.column("Nombre", width=100, anchor=CENTER)
        tv.column("Marca", width=150, anchor=CENTER)
        tv.column("Cantidad", width=150, anchor=CENTER)
        tv.column("Precio", width=150, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("Nombre", text="Nombre", anchor=CENTER)
        tv.heading("Marca", text="Marca", anchor=CENTER)
        tv.heading("Cantidad", text="Cantidad", anchor=CENTER)
        tv.heading("Precio", text="Precio", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=40,width=750,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)

        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=600,y=10,width=150,height=25)
        btn_eliminar["command"] = self.eliminar

    def eliminar(self):
        print("ola")


    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvCarrito")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refrescar(self):        
        tvproductos = self.nametowidget("tvCarrito")
        for record in tvproductos.get_children():
            tvproductos.delete(record)
        result = pedido.obtener_id(self.usuario_id)
        id_pedido = result[0]
        productos = detalle_pedido.listar(id_pedido)
        for i in range(len(productos)):
            p = productos[i]
            tvproductos.insert("", END, text=str(i+1), values=(p[0], p[1], p[2], p[3])) 