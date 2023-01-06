
from tesla.auth.modal import UserBaseModal
from tesla.modal import Model, CharField, ImageField, TextField
from dataclasses import dataclass


class Project(Model):
    name = CharField()
    cover = ImageField(upload_to='projects')
    description = TextField()
    addr = CharField()

    def __meta__(self):
        return ('id', 'name', 'addr')


class Testimonial(Model):
    name = CharField()
    image = ImageField(upload_to='testimodials')
    body = TextField()
    position = CharField()

    def __meta__(self):
        return ('id', 'name', 'position')
