#MARCO MARTINEZ MALAGON
import json

from os import system
system("cls")
dinero_enviado={}
cargar_transaccion={}
transacciones = {}
usuarios = {}
fechas={}
fechas_retiros={}
disponible=0
colchon=0

def agregar_transaccion(descripcion, cantidad, tipo, fecha):
    transacciones[descripcion] = (cantidad, tipo)
    fechas[fecha]=(descripcion, cantidad)
    print("Transacción agregada con éxito.")



def ver_transacciones():
    for descripcion, (cantidad, tipo) in transacciones.items():
        print(descripcion, "- Cantidad:", cantidad, "- Tipo:", tipo)

def filtrar_por_tipo(tipo):
    transacciones_filtradas = []
    for descripcion, (cantidad, tipo_transaccion) in transacciones.items():
        if tipo_transaccion == tipo:
            transacciones_filtradas.append((descripcion, cantidad))
    return transacciones_filtradas

def filtrar_por_fecha():
    for x , (y, z) in fechas.items():
        print("En la fecha:", x , "hay este movimiento:", y, "con esta cantidad", z)

def retiros():
    global disponible
    origen=input("De donde va a retirar el dinero:")
    fecha_del_retiro=input("que fecha es hoy:")
    if origen == "disponible":
        
        print("tiene disponible:", disponible)
        retiro=float(input("cuanto va a retirar:"))
        if retiro > disponible:
            print("retiro no disponible")
        elif retiro <= disponible:
            disponible-=retiro
            fechas_retiros[fecha_del_retiro]=(retiro, origen)
            return print("retiro exitoso, ahora tiene disponible:", disponible)
        
        elif origen == "colchon":
            print("ese colchon no es para gastar")
            menu()
        


def guardar_transacciones():
    with open("transacciones.json", "w") as archivo:
        json.dump(transacciones, archivo)
    print("Transacciones guardadas con éxito.")

def cargar_transacciones():
    global transacciones
    with open("transacciones.json", "r") as archivo:
        transacciones = json.load(archivo)
    print("Transacciones cargadas con éxito.")

def enviar_dinero():
    global disponible
    cuenta=int(input("Numero de cuenta que desea enviar dinero "))
    enviar=int(input("Cuanto dinero va a enviar:"))
    fecha=input("ingrese la fecha de hoy:")

    if enviar > disponible:
        print("Cantidad no disponible")
    elif enviar < disponible:
        disponible-=enviar
        print("envio exitoso")
        dinero_enviado[cuenta]=(enviar, fecha)
def envido_dinero():
    for i ,(y,z) in dinero_enviado.items():
        print("ha enviado :", i , "la cantidad de :", y, "el dia:", z)
def menu():
    while True:
        try:
            print("\nBienvenido al gestor de finanzas personales.")
            print("1. Agregar transacción")
            print("2. Ver balance")
            print("3. Ver transacciones")
            print("4. Filtrar transacciones por tipo")
            print("5. Filtrar transacciones por fecha")
            print("6. Hacer retiro")
            print("7. Guardar transacciones")
            print("8. Cargar transacciones")
            print("9. Enviar dinero ")
            print("10. ver dinero enviado")
            print("11. Cerrar sesion")

            opcion = int(input("Seleccione una opción: "))
            if opcion > 11 :
                print("opcion no valida ")
                menu()
            elif opcion == 11 :
                print("Cerrando sesion...")
                iniciar_sesion()
            elif opcion == 1:
                print("Bolsillos: disponible y colchon")
                descripcion = input("Ingrese la descripción de la transacción: ")
                cantidad = float(input("Ingrese la cantidad de la transacción: "))
                
                tipo = input("Ingrese el tipo de la transacción (ingresos o gastos): ")
                origen= input("en que bolsillo desea hacer la transaccion:")
                fecha=input("ingrese la fecha de hoy:")

                global disponible 
                global colchon
                if tipo != "ingresos" and tipo != "gastos":
                    print("error")
                
                elif tipo == "ingresos" and origen == "disponible":
                    disponible+=cantidad
                    agregar_transaccion(descripcion, cantidad, tipo, fecha)
                    print("agregada")

                elif tipo == "gastos" and origen == "disponible" and disponible == 0:
                    print("no puedes gastar porque no tienes con que")
                    menu()
                elif tipo == "gastos" and origen == "disponible":
                    disponible-=cantidad
                    agregar_transaccion(descripcion, cantidad, tipo, fecha)
                    print("agregada")

                
                elif tipo == "gastos" and origen == "colchon" :
                    print("solo ingresos")
                    menu()
                

                

                
                else:    
                    agregar_transaccion(descripcion, cantidad, tipo, fecha)

            elif opcion == 2:
                
                print("estos son sus balances:")
                print("bolsillo disponible:",disponible)
                print("bolsillo colchon:",colchon)

            elif opcion == 3:
                ver_transacciones()

            elif opcion == 4:
                tipo = input("Ingrese el tipo de transacción que desea filtrar (ingresos o gastos): ")
                transacciones_filtradas = filtrar_por_tipo(tipo)
                print("Transacciones filtradas:")
                for descripcion, cantidad in transacciones_filtradas:
                    print(descripcion, "- Cantidad:", cantidad)
            elif opcion ==5:
                filtrar_por_fecha()
                
            
            elif opcion == 6:
                
                retiros()

                
            elif opcion == 7:
                guardar_transacciones()
            elif opcion == 8:
                cargar_transacciones()
            elif opcion == 9:
                enviar_dinero()
            elif opcion == 10:
                envido_dinero()

        except ValueError:
            print("Opcion no valida")
            continue




def registrar_usuario():
    while True:
        try:

            nombre_usuario = input("Ingrese su nombre de usuario para el registro: ")
            contraseña = input("Ingrese su contraseña para registarlo : ")
            usuarios[nombre_usuario] = contraseña
            print("Usuario registrado correctamente")
            menu()
        except ValueError:
            print("error")
            continue


def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso")
        cargar_transacciones()
        menu()
        
        
    
        
    else:
        print("Nombre de usuario o contraseña incorrecta, debe registrarse primero")
        registrar_usuario()
        

iniciar_sesion()