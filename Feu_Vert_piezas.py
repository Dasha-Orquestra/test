from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order
from datetime import datetime
from Proyecto_Final.Feu_Vert_fabricantes import create_fabricante


def info_pieza():
    dato = input('Dime el numero de registro de la pieza: ')
    try:
        pieza = Pieza.get(Pieza.id_registro == dato.upper())
        print(f'{pieza.id_registro} - {pieza.name} - {pieza.fabricante.name} - {pieza.loc_fabricante} - {pieza.price}')
    except:
        print('Se ha producido un error.')


def create_pieza():
    id = input('Número de registro de la pieza: ')
    name = input('Nombre de la pieza: ')
    precio = float(input('El precio de la pieza: '))
    user_text = input('Hemos trabajado antes con el fabricante de la pieza? (s / n): ')
    if user_text.upper() == 'S':
        dato = input('Dime el nombre o el cif del fabricante: ')
        fabricante = Fabricante.get((Fabricante.name == dato) | (Fabricante.cif == dato))
    elif user_text.upper() == 'N':
        fabricante = create_fabricante()
    loc = fabricante.location
    pieza = Pieza.create(id_registro=id.upper(), name=name, fecha_fabr=datetime.now(),
                          fabricante=fabricante, loc_fabricante=loc, price=precio)
    print(f'La pieza {pieza.name} se ha creado con éxito.')


def modificar_pieza():
    dato = input('Dime el numero de registro de la pieza que quieres modificar: ')
    try:
        pieza = Pieza.get(Pieza.id_registro == dato)
        new_id = input('El nuevo numero de registro de la pieza: ')
        new_name = input('El nombre nuevo de la pieza: ')
        f = input('La fecha de fabricación en el formato: dd.mm.yyyy: ')
        day = int(f[0]+f[1])
        month = int(f[3]+f[4])
        year = int(f[-4]+f[-3]+f[-2]+f[-1])
        new_fecha = datetime(day=day, month=month, year=year)
        fabricante = input('Hemos trabajado antes con el fabricante de la pieza? (s / n): ')
        if fabricante.upper() == 'S':
            dato = input('Dime el nombre o el cif del fabricante: ')
            fabricante = Fabricante.get((Fabricante.name == dato) | (Fabricante.cif == dato))
        elif fabricante.upper() == 'N':
            fabricante = create_fabricante()
        new_localidad = fabricante.location
        new_price = input('Dime el precio nuevo de la pieza: ')
        pieza.id_registro = new_id
        pieza.name = new_name
        pieza.fecha_fabr = new_fecha
        pieza.fabricante = fabricante
        pieza.loc_fabricante = new_localidad
        pieza.price = new_price
        pieza.save()
        print('Los datos de la pieza se han modificado con éxito')
    except:
        print('Se ha producido un error.')


def delete_pieza():
    dato = input('Dime el número de registro de la pieza que quieres borrar: ')
    try:
        pieza = Pieza.get(Pieza.id_registro == dato.upper())
        pieza.delete_instance()
        print(f'El registro se ha borrado.')
    except:
        print('Se ha producido un error.')


# info_pieza()
# create_pieza()
# modificar_pieza()
# delete_pieza()

