class Resultados:
    def __init__(self):
        self.correcto = 0
        self.regular = 0
        self.incorrecto = 0


    def getCorrectos(self):
        return self.correcto


    def getRegulares(self):
        return self.regular


    def getIncorrecto(self):
        return self.incorrecto


    def setCorrectos(self, suma):
        self.correcto = suma


    def setIncorrectos(self, suma):
        self.incorrecto = suma


    def setRegulares(self, suma):
        self.regular = suma


    def increaseCorrectos(self):
        self.correcto = self.correcto + 1


    def increaseRegulares(self):
        self.regular = self.regular + 1


    def increaseIncorrecto(self):
        self.incorrecto = self.incorrecto + 1

    def limpiar(self):
        self.incorrecto = 0
        self.regular = 0
        self.correcto = 0

    def validate(self):
        return self.correcto + self.regular + self.incorrecto == 4