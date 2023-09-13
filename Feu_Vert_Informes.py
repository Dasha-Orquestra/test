from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order, PiezaOrderIntermediate
from datetime import datetime
import json


# Número de piezas vendidas
def get_total_sold():
    total = 0
    for pieza in Pieza.select():
        total += pieza.n_sold
    print(f'El numero total de piezas vendidas es: {total}.')


# get_total_sold()


# Ingresos totales por la venta de piezas - Hecho
def get_total_benefit():
    total = 0
    for order in Order.select():
        total += order.price
    print(f'Los ingresos totales de todas las piezas vendidas son de: {total} euros.')


# get_total_benefit()

# Fabricante más vendido - Hecho, pero con mucho codigo
def find_bestseller():
    fabrica = {}
    for pieza in Pieza.select():
        if pieza.fabricante in fabrica.keys():
            fabrica[pieza.fabricante] += pieza.n_sold
        else:
            fabrica[pieza.fabricante] = pieza.n_sold
    fabrica_values = list(fabrica.values())
    fabrica_keys = list(fabrica.keys())
    best = max(fabrica_values)
    best_value_index = fabrica_values.index(best)
    best_key = fabrica_keys[fabrica_values.index(best)]
    bestseller = Fabricante.get(Fabricante.id == best_key)
    print(f'El fabricante más vendido es {bestseller.name}.\n'
          f'En total ha vendido {best} piezas.')


# find_bestseller()

# Fabricante menos vendido - Hecho, pero Re-think!
def find_worstsellers():
    fabrica = {}
    for pieza in Pieza.select():
        if pieza.fabricante in fabrica.keys():
            fabrica[pieza.fabricante] += pieza.n_sold
        else:
            fabrica[pieza.fabricante] = pieza.n_sold
    fabrica_values = list(fabrica.values())
    worst = min(fabrica_values)
    data = []
    for pieza in Pieza.select().where(Pieza.n_sold == worst):
        dict = {
            'Nombre de la pieza': pieza.name,
            'Fabricante de la pieza': pieza.fabricante.name,
            'Piezas vendidas': pieza.n_sold
        }
        data.append(dict)
    return data


# find_worstsellers()

# Fabricante cuyas piezas son más caras
# No me queda claro como lo deberiamos comparar...
# Al final simplemente busco a quien pertenece la pieza mas cara
def get_most_expensive():
    precio_mas_caro = 0
    fabr_mas_caro = ''
    pieza_mas_cara = ''
    for fabricante in Fabricante.select():
        piezas_fabricante = Pieza.select().where(Pieza.fabricante == fabricante)
        for pieza in piezas_fabricante:
            if precio_mas_caro < pieza.price:
                precio_mas_caro = pieza.price
                fabr_mas_caro = fabricante.name
                pieza_mas_cara = pieza.name
    print(f'La pieza más cara es \'{pieza_mas_cara}\' con el precio de {precio_mas_caro}.\n'
          f'Pertenece al fabricante {fabr_mas_caro}.')
# get_most_expensive()


# En qué época del año de fabrican mas piezas (invierno, primavera,verano, otoño)
# Hecho, raro y con mucho código...
def get_fabr_epoca():
    seasons = {
        'winter': 0,
        'spring': 0,
        'summer': 0,
        'fall': 0
    }
    for pieza in Pieza.select():
        month = pieza.fecha_fabr.month
        if 3 <= month <= 5:
            seasons['spring'] += 1
        elif 6 <= month <= 8:
            seasons['summer'] += 1
        elif 9 <= month <= 11:
            seasons['fall'] += 1
        else:
            seasons['winter'] += 1
    var_1 = list(seasons.keys())
    var_2 = list(seasons.values())
    best = max(var_2)
    best_index = var_2.index(best)
    print(f'La mayoría de las piezas se fabrica en {var_1[best_index]}.')


# get_fabr_epoca()


# En qué época del año de venden mas piezas (invierno, primavera,verano, otoño)
def get_season_sales():
    meses = []
    ventas = []
    for pieza in Pieza.select():
        meses.append(pieza.fecha_fabr.month)
        ventas.append(pieza.n_sold)
    max_ventas = max(ventas)
    ind = ventas.index(max_ventas)
    mes_mas_vendido = meses[ind]
    if 3 <= mes_mas_vendido <= 5:
        print('La mayoria de piezas se vende en primavera.\n'
              f'En el mes número {mes_mas_vendido} hemos vendido {max_ventas} piezas.')
    elif 6 <= mes_mas_vendido <= 8:
        print('La mayoria de piezas se vende en verano.\n'
              f'En el mes número {mes_mas_vendido} hemos vendido {max_ventas} piezas.')
    elif 9 <= mes_mas_vendido <= 11:
        print('La mayoria de piezas se vende en otoño.\n'
              f'En el mes número {mes_mas_vendido} hemos vendido {max_ventas} piezas.')
    else:
        print('La mayoria de piezas se vende en invierno.\n'
              f'En el mes número {mes_mas_vendido} hemos vendido {max_ventas} piezas.')

# get_season_sales()

# Listado completo de locaciones de fabricación de piezas, ordenado alfabéticamente.
# Volver a mirar: json se queja del campo decimal.
def get_locations():
    data = []
    for pieza in Pieza.select().order_by(Pieza.loc_fabricante):
        dict = {
            'Id_registro': pieza.id_registro,
            'Nombre': pieza.name,
            'Fabricante': pieza.fabricante.name,
            'Localidad': pieza.loc_fabricante,
#            'Precio': pieza.price,
            'Ventas': pieza.n_sold
        }
        data.append(dict)
    return data
# get_locations()


# Listado completo de fabricantes ordenados por su número de registro - Hecho.
def get_fabr_register():
    data = []
    for fabricante in Fabricante.select().order_by(Fabricante.id_registro):
        dict = {
            'id_registro': fabricante.id_registro,
            'nombre': fabricante.name,
            'localidad': fabricante.location,
            'CIF': fabricante.cif
        }
        data.append(dict)
    return data

# get_fabr_register()


# El empleado del mes (vendedor con más compras)
def get_best_employee():
    orders = Order.select().order_by(Order.vendedor)
    vendedores = []
    for order in orders:
        vendedores.append(order.vendedor)
    vendedores_set = set(vendedores)
    for vendedor in vendedores_set:
        total = 0
        suma = 0
        piezas = Pieza.select().join(PiezaOrderIntermediate).join(Order).where(Order.vendedor == vendedor)
        for pieza in piezas:
            total += pieza.n_sold
            suma += pieza.price
#            print(pieza.price)
        print(f'\n¡{vendedor} es el mejor empleado!\nHa vendido {total} piezas con un importe de {suma} euros.')

# get_best_employee()





