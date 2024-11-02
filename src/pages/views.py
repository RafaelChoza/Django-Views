import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)


def saludo(request):
    return HttpResponse("Hola, hasta que pude hacer que se vea")

def productos(request):
    class Producto:
        def __init__(self, nombre, precio, inventario):
            self.nombre = nombre
            self.precio = precio
            self.inventario = inventario

        def aplicar_descuento(self, porcentaje):
            #Aplica un descuento al precio del producto.
            self.precio -= self.precio * (porcentaje / 100)

        def actualizar_inventario(self, cantidad):
            #Actualiza la cantidad de inventario disponible.
            self.inventario += cantidad

        def mostrar_informacion(self):
            #Muestra la información del producto.
            return (f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Inventario: {self.inventario} unidades")
    
    class ProductoDigital(Producto):
        def __init__(self, nombre, precio, inventario, tamano_archivo, formato):
            super().__init__(nombre, precio, inventario)
            self.tamano_archivo = tamano_archivo
            self.formato = formato

        def mostrar_informacion(self):
            #Muestra la información del producto digital.
            info_producto = super().mostrar_informacion()
            return f"{info_producto}, Tamaño del archivo: {self.tamano_archivo}MB, Formato: {self.formato}"

        def descargar(self):
            #Simula la descarga del producto digital.
            return f"Descargando {self.nombre} en formato {self.formato}..."
        
        # Ejemplo de uso
    producto1 = Producto("Camiseta", 20.00, 100)
    producto1.aplicar_descuento(10)
    producto1.actualizar_inventario(50)
    info_producto1 = producto1.mostrar_informacion()

    producto_digital1 = ProductoDigital("Ebook", 15.00, 200, 5, "PDF")
    producto_digital1.aplicar_descuento(20)
    info_producto_digital1 = producto_digital1.mostrar_informacion()
    descarga_producto_digital1 = producto_digital1.descargar()

    response_content = (
        f"{info_producto1}<br>"
        f"{info_producto_digital1}<br>"
        f"{descarga_producto_digital1}<br>"
    )

    return HttpResponse(response_content)
