# Estas lineas son para ver las sentencias de SQL y ver los errores cuando se produce una except
import traceback
import logging

from peewee import DoesNotExist

from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order, PiezaOrderIntermediate
from datetime import datetime

# Estas lineas son para mostrar lineas de las sentencias que se ejecutan con peewee
# Si no quieres que se vean las lineas, esto es solo para ver lo que hace, comentalas
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# con muchas piezas no funciona...
def crear_orden():
    id_registro = input('Id del orden: ')
    vendedor = input('Quién está gestionando este orden: ')
    total_price = 0
    piezas = []
    print('Dime los numeros de registro de las piezas que quieres comprar.\nCuando acabes, presiona x.')

    while True:
        user_text = input('Pieza: ')
        if user_text.upper() == 'X':
            break
        else:
            try:
                pieza = Pieza.get(Pieza.id_registro == user_text)
                total_price += pieza.price1
                piezas.append(pieza)
            except DoesNotExist:
                print('No se ha encontrado el registro')
            except:
                print('Excepcion indeterminada')
                # Esta linea es para que te muestre el motivo del error por pantalla
                traceback.print_exc()

    order = Order.create(id_registro=id_registro,
                         fecha=datetime.now(), vendedor=vendedor, price=total_price)
    for pieza in piezas:
        pieza_order_intermediate = PiezaOrderIntermediate.create(pieza=pieza, order=order)

    print('La orden se ha creado con éxito.')

# def crear_orden():
#     id_registro = input('Id del orden: ')
#     vendedor = input('Quién está gestionando este orden: ')
#     pieza = input('Pieza: ')
#     pieza = Pieza.get(Pieza.id_registro == pieza)
#     price = pieza.price
#     order = Order.create(id_registro=id_registro, fecha=datetime.now(), vendedor=vendedor, price=price)
#     pieza_order_intermediate = PiezaOrderIntermediate.create(pieza=pieza, order=order)
#     print('El orden se ha creado con éxito.')


def get_info_orden():
    dato=input('Dime el numero de registro del orden: ')
    order = Order.get(Order.id_registro == dato)
    print(f'La información de tu orden:\n{order.id_registro} - {order.vendedor} - {order.fecha} - {order.price}')


crear_orden()
# get_info_orden()
