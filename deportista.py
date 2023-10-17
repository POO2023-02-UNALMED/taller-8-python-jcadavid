from persona import Persona
class Deportista():
    def __init__(self, deporte, anosPracticando):
        self.__deporte = deporte
        self.__anosPracticando = anosPracticando

    def getDeporte(self):
        return self.__deporte

    def getAñosPracticando(self):
        return self.__anosPracticando