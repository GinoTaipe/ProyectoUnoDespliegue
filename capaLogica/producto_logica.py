from capaDatos.producto_datos import ProductoDatos

class ProductoLogica:
    def __init__(self):
        self.datos = ProductoDatos()

    def registrar(self, nombre, categoria, precio, stock):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.datos.insertar(nombre, categoria, precio, stock)
        return "Producto registrado correctamente."

    def listar(self):
        return self.datos.listar()

    def actualizar(self, id_prod, nombre, categoria, precio, stock):
        existente = self.datos.buscar_por_id(id_prod)
        if not existente:
            return "Producto no encontrado."
        self.datos.actualizar(id_prod, nombre, categoria, precio, stock)
        return "Producto actualizado correctamente."

    def eliminar(self, id_prod):
        existente = self.datos.buscar_por_id(id_prod)
        if not existente:
            return "Producto no encontrado."
        self.datos.eliminar(id_prod)
        return "Producto eliminado correctamente."