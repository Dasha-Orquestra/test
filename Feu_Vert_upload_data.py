from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order
from datetime import datetime


def upload_data_fabricantes(fichero_csv):
    fichero = open(fichero_csv, 'r')
    headers = fichero.readline()
    contenido = fichero.readlines()
    lista_fabricantes = []
    for item in contenido:
        lista_temporal = item.split(',')
        id_registro = lista_temporal[0]
        name = lista_temporal[1]
        location = lista_temporal[2]
        cif = lista_temporal[3].strip()
        tupla = (id_registro, name, location, cif)
        lista_fabricantes.append(tupla)
    print(lista_fabricantes)
    Fabricante.insert_many(lista_fabricantes, fields=[Fabricante.id_registro, Fabricante.name,
                                                      Fabricante.location, Fabricante.cif]).execute()
    fichero.close()

# No funciona con el main program por el nombre del fabricante, y no el ID.
def upload_data_piezas(fichero_csv):
    fichero = open(fichero_csv, 'r')
    headers = fichero.readline()
    contenido = fichero.readlines()
    lista_piezas = []
    for item in contenido:
        lista_temporal = item.split(',')
        id_registro = lista_temporal[0]
        pieza_name = lista_temporal[1]
        date = lista_temporal[2]
        fabr = lista_temporal[3]
        loc = lista_temporal[4]
        price = lista_temporal[5]
        tupla = (id_registro, pieza_name, date, fabr, loc, price.strip())
        lista_piezas.append(tupla)
    print(lista_piezas)
    Pieza.insert_many(lista_piezas, fields=[Pieza.id_registro, Pieza.name, Pieza.fecha_fabr, Pieza.fabricante,
                                            Pieza.loc_fabricante, Pieza.price]).execute()
    fichero.close()


listado_piezas = [
    {'id_registro': 'L35431',
     'name': 'Cilindro de freno de rueda Eje trasero/ izquierda/ derecha',
     'fecha_fabr': datetime(year=2020, month=1, day=25, hour=12, minute=17, second=22),
     'fabricante': 1,
     'loc_fabricante': 'Madrid',
     'price': 17.8
     },
    {'id_registro': 'T80723',
     'name': 'Cilindro de freno de rueda Eje trasero',
     'fecha_fabr': datetime(year=2020, month=2, day=28, hour=5, minute=32, second=37),
     'fabricante': 2,
     'loc_fabricante': 'Valladolid',
     'price': 35.8
     },
    {'id_registro': 'Y08798',
     'name': 'Cilindro de freno de rueda Eje trasero',
     'fecha_fabr': datetime(year=2020, month=1, day=7, hour=13, minute=20, second=7),
     'fabricante': 3,
     'loc_fabricante': 'Madrid',
     'price': 7.8
     },
    {'id_registro': 'V89246',
     'name': 'Cilindro de freno de rueda Eje trasero',
     'fecha_fabr': datetime(year=2020, month=3, day=23, hour=18, minute=13, second=3),
     'fabricante': 3,
     'loc_fabricante': 'Madrid',
     'price': 9.8
     },
    {'id_registro': 'W45086',
     'name': 'Cilindro de freno de rueda eje trasero ambos lados',
     'fecha_fabr':datetime(day=30, month=3, year=2020, hour=0, minute=33, second=0),
     'fabricante': 4,
     'loc_fabricante': 'Zaragoza',
     'price': 0.7
     },
    {'id_registro': 'N12958',
     'name': 'Lámpara JP Group',
     'fecha_fabr': datetime(day=9, month=1, year=2020, hour=12, minute=3, second=20),
     'fabricante': 5,
     'loc_fabricante': 'Valladolid',
     'price': 4.5
     },
    {'id_registro': 'E28903',
     'name': 'Lámpara CLASSIC',
     'fecha_fabr': datetime(day=1, month=4, year=2020, hour=4, minute=44, second=1),
     'fabricante': 5,
     'loc_fabricante': 'Pamplona',
     'price': 2.3
     },
    {'id_registro': 'K93636',
     'name': 'Junta/ tapa de culata de cilindro Corcho',
     'fecha_fabr': datetime(day=31, month=1, year=2020, hour=6, minute=5, second=31),
     'fabricante': 6,
     'loc_fabricante': 'Madrid',
     'price': 1.45
     },
    {'id_registro': 'C55938',
     'name': 'Anillo retén. cigüeñal FPM (caucho fluroado)',
     'fecha_fabr': datetime(day=10, month=1, year=2020, hour=22, minute=26, second=51),
     'fabricante': 7,
     'loc_fabricante': 'Pamplona',
     'price': 5.6
     },
    {'id_registro': 'L81262',
     'name': 'Anillo retén. cigüeñal FPM (caucho fluroado)',
     'fecha_fabr': datetime(day=3, month=1, year=2020, hour=7, minute=44, second=59),
     'fabricante': 7,
     'loc_fabricante': 'Valladolid',
     'price': 6
     },
    {'id_registro': 'V40320',
     'name': 'Juego de articulación. árbol de transmisión lado de engranaje',
     'fecha_fabr': datetime(day=31, month=1, year=2020, hour=20, minute=51, second=9),
     'fabricante': 8,
     'loc_fabricante': 'Valladolid',
     'price': 7.8
     },
    {'id_registro': 'M55508',
     'name': 'Correa trapezoidal 900mm',
     'fecha_fabr': datetime(day=23, month=1, year=2020, hour=21, minute=8, second=52),
     'fabricante': 9,
     'loc_fabricante': 'Madrid',
     'price': 2.3
     },
    {'id_registro': 'L82890',
     'name': 'Borne de batería',
     'fecha_fabr': datetime(day=10, month=1, year=2020, hour=15, minute=20, second=19),
     'fabricante': 10,
     'loc_fabricante': 'Zaragoza',
     'price': 5.4
     },
    {'id_registro': 'P63887',
     'name': 'Borne de batería',
     'fecha_fabr': datetime(day=6, month=2, year=2020, hour=11, minute=37, second=44),
     'fabricante': 11,
     'loc_fabricante': 'Valladolid',
     'price': 5
     },
    {'id_registro': 'A64788',
     'name': 'Bujía de encendido ULTRA Ancho llave: 21 mm. ULTRA',
     'fecha_fabr': datetime(day=1, month=2, year=2020, hour=0, minute=39, second=25),
     'fabricante': 12,
     'loc_fabricante': 'Madrid',
     'price': 7.5
     },
    {'id_registro': 'R41831',
     'name': 'Níquel Bujía de encendido Super plus Ancho llave: 20.8',
     'fecha_fabr': datetime(day=28, month=2, year=2020, hour=4, minute=41, second=29),
     'fabricante': 13,
     'loc_fabricante': 'Zaragoza',
     'price': 1.2
     },
    {'id_registro': 'P71885',
     'name': 'Classic Limpiaparabrisas lado del conductor. 400mm',
     'fecha_fabr': datetime(day=4, month=3, year=2020, hour=20, minute=19, second=37),
     'fabricante': 14,
     'loc_fabricante': 'Pamplona',
     'price': 4.3
     },
    {'id_registro': 'W23136',
     'name': 'Limpiaparabrisas delante',
     'fecha_fabr': datetime(day=16, month=3, year=2020, hour=17, minute=2, second=44),
     'fabricante': 15,
     'loc_fabricante': 'Madrid',
     'price': 6.4
     },
    {'id_registro': 'W57135',
     'name': 'Filtro de aceite',
     'fecha_fabr': datetime(day=5, month=2, year=2020, hour=13, minute=53, second=52),
     'fabricante': 16,
     'loc_fabricante': 'Zaragoza',
     'price': 7.4
     }
]

# upload_data_fabricantes('fabricantes.csv')
# upload_data_piezas('piezas.csv')
#
# for pieza in listado_piezas:
#     Pieza.create(**pieza)

