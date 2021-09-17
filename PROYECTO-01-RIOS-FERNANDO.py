from main import *

# Lista que contine los nombres de usuario y contraseñas para acceder al sistema
administradores = [
    ['admin', '123'],
    ['fer', 'qwerty']
]

def procesar_login():
    intentos = 0
    print('\tLOGIN DE USUARIO')
    print('\t----------------\n')

    # Después de 3 intentos el programa se detiene
    while intentos < 3:
        usuario = input('Usuario: ')
        contraseña = input('Contraseña: ')
        es_admin = False

        for admin in administradores:
            if admin[0] == usuario and admin[1] == contraseña:
                es_admin = True
                break
        
        if es_admin:
            print('\n¡Bienvenido!\n')
            mostrar_menu()
            break
        else:
            print('\nERROR: El usuario o la contraseña es incorrecto\n')
            intentos += 1
    
    print('\nEl programa ha finalizado\n')

def mostrar_menu():
    while True:
        while True:
            print('\tMENÚ DE OPCIONES')
            print('\t----------------\n')
            print('1. Productos más vendidos')
            print('2. Porductos menos vendidos por categoría')
            print('3. Productos con mayores búsquedas')
            print('4. Productos con menores búsquedas por categoría')
            print('5. Productos con las mejores reseñas')
            print('6. Productos con las peores reseñas')
            print('7. Total de ingresos y ventas anual')
            print('0. Salir')
            opcion = int(input('Digite una opción (0-7): '))

            if 0 <= opcion <= 7:
                break
            else:
                print('\nERROR: Debe digitar un número entero en el rango especificado')
                continuar()
        
        if opcion == 0:
            break
        elif opcion == 1:
            ventas_productos = generar_ventas_productos()
            mayores_ventas_productos = ordenar_mayores_ventas(ventas_productos)
            mostrar_mayores_ventas_productos(mayores_ventas_productos)
        elif opcion == 2:
            ventas_productos = generar_ventas_productos()
            menores_ventas_productos = ordenar_menores_ventas(ventas_productos)
            mostrar_menores_ventas_productos(menores_ventas_productos)
        elif opcion == 3:
            busquedas_productos = generar_busquedas_productos()
            mayores_busquedas_productos = ordenar_mayores_busquedas(busquedas_productos)
            mostrar_mayores_busquedas_productos(mayores_busquedas_productos)
        elif opcion == 4:
            busquedas_productos = generar_busquedas_productos()
            menores_busquedas_productos = ordenar_menores_busquedas(busquedas_productos)
            mostrar_menores_busquedas_productos(menores_busquedas_productos)
        elif opcion == 5:
            reseñas_productos = generar_reseñas_productos()
            mejores_reseñas_productos = ordenar_mejores_reseñas(reseñas_productos)
            mostrar_mejores_reseñas_productos(mejores_reseñas_productos)
        elif opcion == 6:
            reseñas_productos = generar_reseñas_productos()
            peores_reseñas_productos = ordenar_peores_reseñas(reseñas_productos)
            mostrar_peores_reseñas_productos(peores_reseñas_productos)
        else:
            while True:
                año = input('\nDigite el año (Ej. 2020): ')
                
                # Valida que el dato ingresado por el usuario sea un número entero de 4 digitos
                if año.isdecimal() and len(año) == 4:
                    ingresos_y_ventas_mensuales = generar_ingresos_mensuales(año)
                    mostrar_ingresos_y_ventas_mensuales(ingresos_y_ventas_mensuales, año)
                    break
                
                print('ERROR: Digite un año valido')
                continuar()

        continuar()

# Función que espera hasta que el usuario de un enter para seguir con la ejecución del programa
def continuar():
    print('\nPresione Enter para continuar...', end='')
    input()
    print()

procesar_login()