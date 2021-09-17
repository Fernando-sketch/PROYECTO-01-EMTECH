from lifestore_file import *

def generar_ventas_productos():
    ventas_productos = []

    for producto in lifestore_products:
        id_producto = producto[0]
        nombre_producto = producto[1]
        categoria_producto = producto[3]

        unidades_vendidas = 0
        
        for venta in lifestore_sales:
            id_producto_venta = venta[1]
            devolucion = venta[4]
            
            if id_producto == id_producto_venta and devolucion == 0:
                unidades_vendidas += 1

        if unidades_vendidas == 0:
            ventas_productos.append([nombre_producto, unidades_vendidas, categoria_producto])
    
    return ventas_productos

def ordenar_mayores_ventas(ventas_productos):
    return sorted(ventas_productos, key=lambda x: x[1], reverse=True)

def mostrar_mayores_ventas_productos(mayores_ventas_productos):
    print('\n>>>> LOS 50 PRODUCTOS CON MAYORES VENTAS <<<<\n')
    cuenta = 0
    for producto in mayores_ventas_productos[:50]:
        cuenta += 1
        print(f'{str(cuenta).zfill(2)}. {producto[0]} | Unidades vendidas: {producto[1]} | Categoria: {producto[2]}')

def ordenar_menores_ventas(ventas_productos):
    return sorted(ventas_productos, key=lambda x: (x[2], x[1]))

def mostrar_menores_ventas_productos(menores_ventas_productos):
    print('\n>>>> PRODUCTOS CON MENORES VENTAS POR CATEGORÍA <<<<')
    categoria = ''
    cuenta = 0
    for producto in menores_ventas_productos:
        if categoria != producto[2]:
            categoria = producto[2]
            cuenta = 0
            print(f'\n{categoria.capitalize()}:\n')
        if cuenta < 10:
            cuenta += 1
            print(f'{str(cuenta).zfill(2)}. {producto[0]} | Unidades vendidas: {producto[1]}')


def generar_busquedas_productos():
    busquedas_productos = []

    for product in lifestore_products:
        id_producto = product[0]
        nombre_producto = product[1]
        categoria_producto = product[3]
        
        num_busquedas = 0

        for busqueda in lifestore_searches:
            id_producto_busqueda = busqueda[1]
            
            if id_producto == id_producto_busqueda:
                num_busquedas += 1
        
        if num_busquedas > 0:
            busquedas_productos.append([nombre_producto, num_busquedas, categoria_producto])
    
    return busquedas_productos

def ordenar_mayores_busquedas(busquedas_productos):
    return sorted(busquedas_productos, key=lambda x: x[1], reverse=True)

def mostrar_mayores_busquedas_productos(mayores_busquedas_productos):
    print('\n>>>> LOS 50 PRODUCTOS CON MAYORES BÚSQUEDAS <<<<\n')
    cuenta = 0
    for producto in mayores_busquedas_productos[:50]:
        cuenta += 1
        print(f'{str(cuenta).zfill(2)}. {producto[0]} | N.° búsquedas {producto[1]}')

def ordenar_menores_busquedas(busquedas_productos):
    return sorted(busquedas_productos, key=lambda x: (x[2], x[1]))
        
def mostrar_menores_busquedas_productos(menores_busquedas_productos):
    print('\n>>>> PRODUCTOS CON MENORES BÚSQUEDAS POR CATEGORÍA <<<<')
    categoria = ''
    cuenta = 0
    for producto in menores_busquedas_productos:
        if categoria != producto[2]:
            categoria = producto[2]
            cuenta = 0
            print(f'\n{categoria.capitalize()}:\n')
        if cuenta < 10:
            cuenta += 1
            print(f'{str(cuenta).zfill(2)}. {producto[0]} | N.° búsquedas {producto[1]}')


def generar_reseñas_productos():
    
    reseñas_productos = []

    for producto in lifestore_products:
        id_producto = producto[0]
        nombre_producto = producto[1]

        puntaje_total = 0
        cuenta = 0

        for venta in lifestore_sales:
            id_producto_venta = venta[1]
            reseña_venta = venta[2]

            if id_producto == id_producto_venta:
                puntaje_total += reseña_venta
                cuenta += 1
        
        if cuenta > 0:
            puntaje_promedio = puntaje_total / cuenta
            reseñas_productos.append([nombre_producto, puntaje_promedio])
    
    return reseñas_productos

def ordenar_mejores_reseñas(reseñas_productos):
    return sorted(reseñas_productos, key=lambda x: x[1], reverse=True)

def mostrar_mejores_reseñas_productos(mejores_reseñas_productos):
    print('\n>>>> LOS 20 PRODUCTOS CON MEJORES RESEÑAS <<<<\n')
    cuenta = 0
    for producto in mejores_reseñas_productos[:20]:
        cuenta += 1
        print(f'{str(cuenta).zfill(2)}. {producto[0]} | Puntaje: {round(producto[1], 1)}')

def ordenar_peores_reseñas(reseñas_productos):
    return sorted(reseñas_productos, key=lambda x: x[1])

def mostrar_peores_reseñas_productos(peores_reseñas_productos):
    print('\n>>>> LOS 20 PRODUCTOS CON PEORES RESEÑAS <<<<\n')
    cuenta = 0
    for producto in peores_reseñas_productos[:20]:
        cuenta += 1
        print(f'{str(cuenta).zfill(2)}. {producto[0]} | Puntaje: {round(producto[1], 1)}')


def generar_ingresos_mensuales(año):
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    ingresos_y_ventas_mensuales = []
    
    for mes in meses:
        ingreso_mensual = 0
        ventas_mensual = 0
        
        for venta in lifestore_sales:
            # La lista fecha_separada contiene [dia, mes, año]
            fecha_separada = venta[3].split(sep='/')
            mes_venta = meses[int(fecha_separada[1]) - 1]
            id_producto_venta = venta[1]
            devuelto = venta[4]
            
            if devuelto == 0:
                if mes == mes_venta and año == fecha_separada[2]:
                    precio_producto = 0
                    
                    for producto in lifestore_products:
                        if id_producto_venta == producto[0]:
                            precio_producto = producto[2]
                            break
                    
                    ingreso_mensual += precio_producto
                    ventas_mensual += 1

        ingresos_y_ventas_mensuales.append([mes, ingreso_mensual, ventas_mensual])

    return ingresos_y_ventas_mensuales

def mostrar_ingresos_y_ventas_mensuales(ingresos_y_ventas_mensuales, año):
    print(f'\n>>>> INGRESOS Y VENTAS DEL AÑO {año} <<<<\n')
    total_ingresos = 0
    total_ventas = 0
    for mes in ingresos_y_ventas_mensuales:
        total_ingresos += mes[1]
        total_ventas += mes[2]
        print(f'Mes: {mes[0]} | Ingresos: {mes[1]} | Ventas: {mes[2]}')
    print('----------------------------------------------------------')
    print(f'Total de ingresos: {total_ingresos}')
    print(f'Total de ventas: {total_ventas}')