from flask import request
from .player import Player


class Captain(Player):

    def __init__(self, id=0, firstname=None, lastname=None, age=0, experience=None, grade=0):
        super().__init__(id, firstname, lastname, age, experience)
        self.grade = grade

    def input(self):
        super().input()
        self.grade = request.form.get("grade")
