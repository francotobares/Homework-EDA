from random import randint
import random
from Class import resultado_class


class Lista:

    def __init__(self, content=[]):
        self.content = content
        self.resultado = resultado_class.Resultados()

    def validate(self):
        return len(self.content) == 4

    def setContent(self, contenido=[]):
        self.content = self.random(4, 9) if len(contenido) == 0 else contenido

    def getContent(self):
        return self.content

    def random(self, cantidad, rango):
        lista = []
        while len(lista) < cantidad:
            r = randint(0, rango)
            if r not in lista:
                lista.append(r)

        return lista

    def comparacion(self, numeroMaquina):

        for x in range(0, len(self.content)):
            if self.content[x] == numeroMaquina[x]:
                self.resultado.increaseCorrectos()
            else:
                if self.content[x] in numeroMaquina:
                    self.resultado.increaseRegulares()
                if self.content[x] not in numeroMaquina:
                    self.resultado.increaseIncorrecto()

    def listaEnBaseACondicionales(self, listaActual):
        posiciones = self.listasAleatoriasDePosiciones()
        

        self.setCorrectValues(posiciones,listaActual)
        #modificar valores regulares
        if len(posiciones[2]) > 0:
           posiciones[1] = self.setRegularValues(posiciones,listaActual)
        #modificar valores incorrectos
        


    def setCorrectValues(self,posiciones,listaActual):
        for x in range(0, self.resultado.getCorrectos()):
            for y in range(len(listaActual)):
                if posiciones[0][x] == listaActual.index(listaActual[y]):
                    self.content[y] = listaActual[y]
    

    def setRegularValues(self,posiciones,listaActual):
        listaRevuelta = []
        if len(posiciones[2]) > 0:
            modificar = posiciones[2] + posiciones[1]
            modificar.sort()
            for x in range(self.resultado.getRegulares()+self.resultado.getIncorrecto()):
                for y in range(len(listaActual)):
                    if modificar[x] == listaActual.index(listaActual[y]):
                        listaRevuelta.append(listaActual[y])
            random.shuffle(modificar)
            for x in range(self.resultado.regular):
                for y in range(len(listaActual)):
                    if modificar[x] == listaActual.index(listaActual[y]):
                        self.content[y] = listaRevuelta[x]
                        modificar[x]="a"
            modificar = [x for x in modificar if type(x) == int]
            return modificar


    def setIncorrectValues(self,posiciones,listaActual):
        for l in range(self.resultado.getIncorrecto()):
            for e in range(len(listaActual)):
                if posiciones[1][l] == listaActual.index(listaActual[e]):
                    ret = False
                    while ret == False:
                        valor = randint(0, 9)
                        if valor in self.content: ret = False
                        if valor not in self.content: ret = True
                        if valor not in self.content: self.content[e] = valor
    
    def listasAleatoriasDePosiciones(self):
        posicionesCorrectos = self.random(self.resultado.getCorrectos(), len(self.content) - 1)
        posicionesRegulares = []
        posicionesIncorrectos = []
        while len(posicionesRegulares) < self.resultado.getRegulares():
            posicionesRegulares = self.random(self.resultado.getRegulares(), len(self.content) - 1)
            for i in range(len(posicionesRegulares)):
                if len(posicionesRegulares) > 0:
                    if posicionesRegulares[i] in posicionesCorrectos: posicionesRegulares.clear()
        while len(posicionesIncorrectos) < self.resultado.getIncorrecto():
            posicionesIncorrectos = self.random(self.resultado.getIncorrecto(), len(self.content) - 1)
            for i in range(len(posicionesIncorrectos)):
                if len(posicionesIncorrectos) > 0:
                    if posicionesIncorrectos[i] in posicionesCorrectos: posicionesIncorrectos.clear()
                if len(posicionesIncorrectos) > 0:
                    if posicionesIncorrectos[i] in posicionesRegulares: posicionesIncorrectos.clear()

        return [posicionesCorrectos, posicionesIncorrectos, posicionesRegulares]
