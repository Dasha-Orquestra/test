from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order, PiezaOrderIntermediate
from datetime import datetime

# Con muchas piezas no funciona...
# def crear_orden():
#     id_registro = input('Id del orden: ')
#     vendedor = input('Quién está gestionando este orden: ')
#     total_price = 0
#     piezas = []
#     print('Dime los numeros de registro de las piezas que quieres comprar.\nCuando acabes, presiona x.')
#     while True:
#         user_text = input('Pieza: ')
#         if user_text.upper() == 'X':
#             break
#         else:
#             pieza = Pieza.get(Pieza.id_registro == user_text)
#             total_price += pieza.price
#             piezas.append(pieza)
#         order = Order.create(id_registro=id_registro,
#                              fecha=datetime.now(), vendedor=vendedor, price=total_price)
#         for pieza in piezas:
#             pieza_order_intermediate = PiezaOrderIntermediate.create(pieza=pieza, order=order)
#     print('El orden se ha creado con éxito.')



def crear_orden():
    id_registro = input('Id del orden: ')
    vendedor = input('Quién está gestionando este orden: ')
    pieza = input('El numero de registro de la pieza: ')
    pieza = Pieza.get(Pieza.id_registro == pieza)
    price = pieza.price
    pieza.n_sold += 1
    pieza.save()
    order = Order.create(id_registro=id_registro.upper(), fecha=datetime.now(), vendedor=vendedor, price=price)
    pieza_order_intermediate = PiezaOrderIntermediate.create(pieza=pieza, order=order)
    print('El orden se ha creado con éxito.')


# No conseguí mostrar el nombre de la pieza... No se que hago mal.
def get_info_orden():
    dato=input('Dime el numero de registro del orden: ')
    try:
        order = Order.get(Order.id_registro == dato.upper())
#        pieza = Pieza.select().join(PiezaOrderIntermediate).join(Order).where(Order.id == order.id)
        print(f'La información de tu orden:\n{order.id_registro} - {order.vendedor} - {order.fecha} - {order.price}')
    except:
        print('Se ha producido un error.')

# crear_orden()
# get_info_orden()
