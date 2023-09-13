from peewee import SqliteDatabase, Model, CharField, DateField, ForeignKeyField, IntegerField, DecimalField
from datetime import datetime
db = SqliteDatabase('feu_vert.db')


class Fabricante(Model):
    id_registro = CharField()
    name = CharField()
    location = CharField()
    cif = CharField()

    class Meta:
        database = db


class Order(Model):
    id_registro = CharField()
    fecha = DateField(default=datetime.now())
    vendedor = CharField()
    price = DecimalField()

    class Meta:
        database = db


class Pieza(Model):
    id_registro = CharField()
    name = CharField()
    fecha_fabr = DateField()
    fabricante = ForeignKeyField(Fabricante, backref='piezas') #on_delete='DO_NOTHING'
    loc_fabricante = CharField()
    price = DecimalField()
    n_sold = IntegerField(default=0)

    class Meta:
        database = db


class PiezaOrderIntermediate(Model):
    pieza = ForeignKeyField(Pieza)
    order = ForeignKeyField(Order)

    class Meta:
        database = db


db.connect()
db.create_tables([Fabricante, Pieza, Order, PiezaOrderIntermediate])
db.close()
