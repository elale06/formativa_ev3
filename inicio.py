import os, json
from pymongo import MongoClient
from datetime import datetime

with open("prod.json", "r", encoding="utf-8") as archivo:
    productos = json.load(archivo)

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["empresa"]
col_empleados = db["empleados"]
col_clientes = db["clientes"]
col_pedidos = db["pedidos"]
print("Conexión exitosa")

def limpiar_pantalla():
    os.system("cls")

def ingresar_emp():
    limpiar_pantalla()
    print("INGRESAR EMPLEADO")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    cargo = input("Cargo: ")
    salario = float(input("Salario: "))
    empleado = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cargo": cargo,
        "salario": salario
    }
    col_empleados.insert_one(empleado)
    print("Empleado ingresado exitosamente")

def mostrar_empleados():
    limpiar_pantalla()
    print("LISTA DE EMPLEADOS")
    empleados = col_empleados.find()
    for emp in empleados:
        print(f"ID: {emp['_id']}")
        print(f"Nombre: {emp['nombre']} {emp['apellido']}")
        print(f"Edad: {emp['edad']}")
        print(f"Cargo: {emp['cargo']}")
        print(f"Salario: {emp['salario']}")
        print("-" * 20)

while True:
    print("-" * 20)
    print("MENU PRINCIPAL")
    print("-" * 20)