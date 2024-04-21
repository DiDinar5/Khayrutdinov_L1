from flask import request

class Player:
    def __init__(self, id=0, firstname=None, lastname=None, age=0, experience=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.experience = experience

    def input(self):
        self.id = request.form.get("id")
        self.firstname = request.form.get("firstname")
        self.lastname = request.form.get("lastname")
        self.age = request.form.get("age")
        self.experience = request.form.get('experience')
