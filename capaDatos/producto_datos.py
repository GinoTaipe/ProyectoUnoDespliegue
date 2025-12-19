from conexion import supabase

class ProductoDatos:
    def listar(self):
        return supabase.table("producto").select("*").execute().data

    def insertar(self, nombre, categoria, precio, stock):
        supabase.table("producto").insert({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "estado": 1
        }).execute()

    def actualizar(self, id_producto, nombre, categoria, precio, stock):
        supabase.table("producto").update({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock
        }).eq("id", id_producto).execute()

    def eliminar(self, id_producto):
        supabase.table("producto").update({"estado": 0}).eq("id", id_producto).execute()

    def buscar_por_id(self, id_producto):
        resultado = supabase.table("producto").select("*").eq("id", id_producto).execute().data
        return resultado[0] if resultado else None
