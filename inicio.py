"""
REFERENCIA DE LOS CAMPOS EN LAS COLECCIONES DE MONGODB
empleados:                    |   clientes:                     |   pedidos:            |   productos:   |
* _id                         |   * _id                         |   * _id               |   * _id        |
* nombre                      |   * nombre                      |   * cliente_id        |   * nombre     |
* fechaRegistro (automático)  |   * fechaRegistro (automático)  |   * fecha_pedido      |   * valor      |
* email                       |   * email                       |   * monto_total       |   * stock      |
* direccion                   |   * direccion                   |           -           |       --       |
* telefono                    |   * telefono                    |           -           |       --       |
"""

import os, json
from pymongo import MongoClient
from datetime import datetime
from datetime import timezone

with open("prod.json", "r", encoding="utf-8") as archivo:
    productos = json.load(archivo)

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["empresa"]
col_empleados = db["empleados"]
col_clientes = db["clientes"]
col_pedidos = db["pedidos"]
col_productos = db["productos"]
print("Conexión exitosa")

def limpiar_pantalla():
    os.system("cls")
    print("-" * 20)

def ingresar_emp():
    limpiar_pantalla()
    print("INGRESAR EMPLEADO")
    nombre = input("Nombre: ")
    email = input("Email: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    empleado = {
        "nombre": nombre,
        "email": email,
        "direccion": direccion,
        "telefono": telefono,
        "fechaRegistro": datetime.now(timezone.utc)
    }
    col_empleados.insert_one(empleado)
    print("-" * 20)
    print("Empleado ingresado con éxito.")

def ingresar_cli():
    limpiar_pantalla()
    print("INGRESAR CLIENTE")
    nombre = input("Nombre: ")
    email = input("Email: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    cliente = {
        "nombre": nombre,
        "email": email,
        "direccion": direccion,
        "telefono": telefono,
        "fechaRegistro": datetime.now(timezone.utc)
    }
    col_clientes.insert_one(cliente)
    print("-" * 20)
    print("Cliente ingresado con éxito.")

def mostrar_emp():
    limpiar_pantalla()
    print("EMPLEADOS REGISTRADOS")
    empleados = col_empleados.find()
    for emp in empleados:
        print(f"ID: {emp['_id']}")
        print(f"Nombre: {emp['nombre']}")
        print(f"Email: {emp['email']}")
        print(f"Dirección: {emp['direccion']}")
        print(f"Teléfono: {emp['telefono']}")
        print(f"Fecha de registro: {emp['fechaRegistro']}")
        print("-" * 20)

def mostrar_cli():
    limpiar_pantalla()
    print("CLIENTES REGISTRADOS")
    clientes = col_clientes.find()
    for cli in clientes:
        print(f"ID: {cli['_id']}")
        print(f"Nombre: {cli['nombre']}")
        print(f"Email: {cli['email']}")
        print(f"Dirección: {cli['direccion']}")
        print(f"Teléfono: {cli['telefono']}")
        print(f"Fecha de registro: {cli['fechaRegistro']}")
        print("-" * 20)

def mostrar_prod():
    limpiar_pantalla()
    print("PRODUCTOS DISPONIBLES")
    for prod in productos:
        print(f"ID: {prod['_id']}")
        print(f"Nombre: {prod['nombre']}")
        print(f"Valor: {prod['valor']}")
        print(f"Stock: {prod['stock']}")
        print("-" * 20)

def ingresar_pedido():
    limpiar_pantalla()
    print("INGRESAR PEDIDO")
    cliente_id = input("ID del cliente: ")
    # validar que el cliente existe
    cliente = col_clientes.find_one({"_id": cliente_id})
    if not cliente:
        print("El cliente ingresado no existe.")
        return
    # mostrar productos disponibles
    print("Productos disponibles:")
    for prod in productos:
        print(f"ID: {prod['_id']} - Nombre: {prod['nombre']} - Valor: {prod['valor']} - Stock: {prod['stock']}")
        producto_id = input("ID del producto: ")
        # validar que el producto existe y tiene stock
        producto = next((p for p in productos if p["_id"] == producto_id), None)
        if not producto:
            print("El producto ingresado no existe.")
            return
        if producto["stock"] <= 0:
            print("El producto seleccionado no tiene stock disponible.")
def main():
    while True:
        print("MENU PRINCIPAL")
        print("1. Ingresar empleado")
        print("2. Ingresar cliente")
        print("3. Mostrar empleados")
        print("4. Mostrar clientes")
        print("5. Mostrar productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresar_emp()
        elif opcion == "2":
            ingresar_cli()
        elif opcion == "3":
            mostrar_emp()
        elif opcion == "4":
            mostrar_cli()
        elif opcion == "5":
            mostrar_prod()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
