from operacijos.irasas import Irasas

class Islaidos(Irasas):
    def __init__(self, suma, isigyta, info):
        super().__init__(suma)
        self.isigyta = isigyta
        self.info = info

    def __repr__(self):
        return f"Išlaidos: {self.suma}"
