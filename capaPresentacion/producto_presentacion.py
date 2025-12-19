import streamlit as st
from capaLogica.producto_logica import ProductoLogica

class ProductoPresentacion:
    def __init__(self):
        self.logica = ProductoLogica()

    def menu(self):
        st.title("Módulo Productos")
        menu = ["Listar", "Registrar", "Actualizar", "Eliminar"]
        opcion = st.sidebar.selectbox("Menú", menu)

        if opcion == "Listar":
            self.listar()
        elif opcion == "Registrar":
            self.registrar()
        elif opcion == "Actualizar":
            self.actualizar()
        elif opcion == "Eliminar":
            self.eliminar()

    def listar(self):
        st.subheader("Lista de Productos")
        productos = self.logica.listar()
        for p in productos:
            p['estado'] = "Activo" if p['estado'] == 1 else "No activo"
            p['precio'] = f"{p['precio']:.2f}"
        st.table(productos)

    def registrar(self):
        st.subheader("Registrar Producto")
        nombre = st.text_input("Nombre")
        categoria = st.text_input("Categoría")
        precio = st.number_input("Precio", min_value=0.0, format="%.2f")
        stock = st.number_input("Stock", min_value=0)
        if st.button("Registrar"):
            try:
                mensaje = self.logica.registrar(nombre, categoria, precio, stock)
                st.success(mensaje)
            except Exception as e:
                st.error(str(e))

    def actualizar(self):
        st.subheader("Actualizar Producto")
        id_prod = st.number_input("ID del producto", min_value=1)
        nombre = st.text_input("Nuevo nombre")
        categoria = st.text_input("Nueva categoría")
        precio = st.number_input("Nuevo precio", min_value=0.0, format="%.2f")
        stock = st.number_input("Nuevo stock", min_value=0)
        if st.button("Actualizar"):
            mensaje = self.logica.actualizar(id_prod, nombre, categoria, precio, stock)
            st.success(mensaje)

    def eliminar(self):
        st.subheader("Eliminar Producto")
        id_prod = st.number_input("ID del producto", min_value=1)
        if st.button("Eliminar"):
            mensaje = self.logica.eliminar(id_prod)
            st.success(mensaje)