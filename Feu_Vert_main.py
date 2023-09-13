from Proyecto_Final.Feu_Vert_Models import Fabricante, Pieza, Order, PiezaOrderIntermediate
from Proyecto_Final.Feu_Vert_piezas import info_pieza, create_pieza, modificar_pieza, delete_pieza
from Proyecto_Final.Feu_Vert_fabricantes import info_fabricante, create_fabricante, modificar_fabricante, \
    delete_fabricante
from Proyecto_Final.Feu_Vert_ordenes import get_info_orden, crear_orden
from Proyecto_Final.Feu_Vert_Informes import get_total_sold, get_total_benefit, find_bestseller, \
    find_worstsellers, get_most_expensive, get_fabr_epoca, get_season_sales, get_fabr_register, \
    get_locations, get_best_employee
import json

# Funciones Menu
def show_main_menu():
    print('MENU:\n'
          'P para operaciones con piezas\n'
          'F para operaciones con fabricantes\n'
          'I para informes\n'
          'O para ordenes\n'
          'S para salir')
    user_text = input('\nDime qué quieres hacer ahora: ')
    return user_text.upper()


def show_pieza_menu():
    print('\nMENU PIEZA\n'
          'Para cualquier operación, ten a mano el número de registro de la pieza.\n'
          'Crear pieza: A\n'
          'Info pieza: B\n'
          'Modificar pieza: C\n'
          'Eliminar pieza : D\n')
    user_text = input('\nDime qué quieres hacer ahora: ')
    return user_text.upper()


def show_fabricante_menu():
    print('\nMENU FABRICANTE\n'
          'Crear fabricante: A\n'
          'Info fabricante: B\n'
          'Modificar fabricante: C\n'
          'Eliminar fabricante: D')
    user_text = input('\nDime qué quieres hacer ahora: ')
    return user_text.upper()


def show_orden_menu():
    print('\nMENU ORDEN\n'
          'Crear orden: A\n'
          'Info orden: B\n')
    user_text = input('\nDime qué quieres hacer ahora: ')
    return user_text.upper()


def get_reports():
    print('\nMENU INFORMES\n'
          'Número de piezas vendidas: A\n'
          'Ingresos totales por la venta de piezas: B\n'
          'Fabricante más vendido: C\n'
          'Fabricante menos vendido: D\n'
          'Fabricante cuyas piezas son más caras: E\n'
          'En qué época del año de fabrican mas piezas: F\n'
          'En qué época del año de venden mas piezas: G\n'
          'Listado completo de locaciones de fabricación de piezas, ordenado alfabéticamente: H\n'
          'Listado completo de fabricantes ordenados por su número de registro: I\n'
          'El empleado del mes: J')
    user_text = input('\nDime qué quieres hacer ahora: ')
    return user_text.upper()


# Programa principal
print('¡Bienvenido al sistema de registros!')
while True:
    user_text = show_main_menu()
    if user_text == 'P':
        user_text = show_pieza_menu()
        if user_text == 'A':
            create_pieza()
        elif user_text == 'B':
            info_pieza()
        elif user_text == 'C':
            modificar_pieza()
        elif user_text == 'D':
            delete_pieza()
        else:
            show_main_menu()
    elif user_text == 'F':
        user_text = show_fabricante_menu()
        if user_text == 'A':
            create_fabricante()
        elif user_text == 'B':
            info_fabricante()
        elif user_text == 'C':
            modificar_fabricante()
        elif user_text == 'D':
            delete_fabricante()
        else:
            show_main_menu()
    elif user_text == 'O':
        user_text = show_orden_menu()
        if user_text == 'A':
            crear_orden()
        elif user_text == 'B':
            get_info_orden()
        else:
            show_main_menu()
    elif user_text == 'I':
        user_text = get_reports()
        if user_text == 'A':
            get_total_sold()
        elif user_text == 'B':
            get_total_benefit()
        elif user_text == 'C':
            find_bestseller()
        elif user_text == 'D':
            data = find_worstsellers()
            with open('informe_ventas.json', 'w') as fichero:
                json.dump(data, fichero)
            print('El informe se ha generado con éxito')
        elif user_text == 'E':
            get_most_expensive()
        elif user_text == 'F':
            get_fabr_epoca()
        elif user_text == 'G':
            get_season_sales()
        elif user_text == 'H':
            data = get_locations()
            with open('informe_ventas.json', 'w') as fichero:
                json.dump(data, fichero)
            print('El informe se ha generado con éxito')
        elif user_text == 'I':
            data = get_fabr_register()
            with open('informe_ventas.json', 'w') as fichero:
                json.dump(data, fichero)
            print('El informe se ha generado con éxito')
        elif user_text == 'J':
            get_best_employee()
        else:
            show_main_menu()
    elif user_text == 'S':
        print('¡Hasta luego!')
        break
    else:
        print('No te entiendo.')
        show_main_menu()

