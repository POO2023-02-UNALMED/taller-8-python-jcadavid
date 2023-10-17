class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__sexo = sexo

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getAltura(self):
        return self.__altura

    def getSexo(self):
        return self.__sexo

