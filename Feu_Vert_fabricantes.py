from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order
from datetime import datetime


def info_fabricante():
    dato = input('Dime el nombre o el cif del fabricante: ')
    try:
        fabricante = Fabricante.get((Fabricante.name == dato.upper()) | (Fabricante.cif == dato.upper()))
        print(f'{fabricante.id_registro} - {fabricante.name} - {fabricante.location} - {fabricante.cif}')
    except:
        print('Se ha producido un error.')


def create_fabricante():
    id = input('ID del fabricante: ')
    name = input('Nombre del fabricante: ')
    location = input('Localización del fabricante: ')
    cif = input('El CIF del fabricante: ')
    fabricante = Fabricante.create(id_registro=id.upper(), name=name.upper(),
                                   location=location.capitalize(), cif=cif.upper())
    print(f'El fabricante {fabricante.name} se ha creado con éxito.')
    return fabricante.id


def modificar_fabricante():
    dato = input('Dime el nombre o el cif del fabricante cuyos datos quieres modificar: ')
    try:
        fabricante = Fabricante.get((Fabricante.name == dato.upper()) | (Fabricante.cif == dato.upper()))
        new_id = input('El nuevo numero de registro del fabricante: ')
        new_name = input('El nombre nuevo del fabricante: ')
        new_location = input('La localización nueva del fabricante: ')
        new_cif = input('El CIF nuevo del fabricante: ')
        fabricante.id_registro = new_id.upper()
        fabricante.name = new_name.upper()
        fabricante.location = new_location.capitalize()
        fabricante.cif = new_cif.upper()
        fabricante.save()
        print('Los datos del fabricante se han modificado con éxito')
    except:
        print('Se ha producido un error.')


def delete_fabricante():
    dato = input('Dime el nombre o el cif del fabricante cuyo registro quieres eliminar: ')
    try:
        fabricante = Fabricante.get((Fabricante.name == dato.upper()) | (Fabricante.cif == dato.upper()))
        fabricante.delete_instance()
        print(f'El registro se ha borrado.')
    except:
        print('Se ha producido un error.')


# info_fabricante()
# create_fabricante()
# modificar_fabricante()
# delete_fabricante()
