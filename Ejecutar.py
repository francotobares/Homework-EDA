from Class import numericSecuence_class


def adivinaPersona():

    numeroPersona = numericSecuence_class.Lista()
    numeroMaquina = numericSecuence_class.Lista()
    numeroMaquina.setContent()
    print(numeroMaquina.content)

    while numeroPersona.resultado.getCorrectos() != len(numeroMaquina.getContent()):
        numeroPersona.resultado.limpiar()
        numeroPersona.setContent([int(i) for i in str(input("Introduce un tu numero de 4 digitos: "))])
        while not numeroPersona.validate():
            t = [int(i) for i in str(input("Introduce un tu numero de 4 digitos: "))]
            numeroPersona.setContent(t)
        numeroPersona.comparacion(numeroMaquina.content)
        print("Tus valores correctos son: " +
              str(numeroPersona.resultado.getCorrectos()))
        print("Tus valores incorrectos son: " +
              str(numeroPersona.resultado.getIncorrecto()))
        print("Tus valores regulares son: " +
              str(numeroPersona.resultado.getRegulares()))
    print("Ganaste")


def adivinaMaquina():

    numeroMaquina = numericSecuence_class.Lista()
    numeroPersona = numericSecuence_class.Lista()
    listaInvalidos = []
    numeroMaquina.setContent()
    numeroPersona.setContent()
    listaInvalidos.append(numeroPersona.getContent())
    print("¿Es este tu numero?: " + str(numeroPersona.getContent()))
    while not numeroPersona.resultado.validate():
        numeroPersona.resultado.limpiar()
        numeroPersona.resultado.setCorrectos(int(input("Introduce los valores correctos: ")))
        numeroPersona.resultado.setIncorrectos(int(input("Introduce los valores incorrectos: ")))
        numeroPersona.resultado.setRegulares(int(input("Introduce los valores regulares: ")))
        if not numeroPersona.resultado.validate():
            print("La suma de valores no puede ser mayor o menor a 4")
    numeroMaquina.resultado.setCorrectos(numeroPersona.resultado.getCorrectos())
    numeroMaquina.resultado.setRegulares(numeroPersona.resultado.getRegulares())
    numeroMaquina.resultado.setIncorrectos(numeroPersona.resultado.getIncorrecto())
    while numeroMaquina.resultado.getCorrectos() != 4:
        valida = False
        numeroMaquina.listaEnBaseACondicionales(numeroPersona.getContent())
        while not valida:
            valida = True
            for k in range(len(listaInvalidos)):
                if numeroMaquina.getContent() == listaInvalidos[k]:
                    numeroMaquina.listaEnBaseACondicionales(numeroPersona.getContent())
                    valida = False
        print("¿Es este tu numero?: " + str(numeroMaquina.content))
        numeroMaquina.resultado.limpiar()
        while not numeroMaquina.resultado.validate():
            numeroMaquina.resultado.limpiar()
            numeroMaquina.resultado.setCorrectos(int(input("Introduce los valores correctos: ")))
            numeroMaquina.resultado.setIncorrectos(int(input("Introduce los valores incorrectos: ")))
            numeroMaquina.resultado.setRegulares(int(input("Introduce los valores regulares: ")))
            if not numeroMaquina.resultado.validate():
                print("La suma de valores no puede ser mayor o menor a 4")
        if numeroMaquina.resultado.getCorrectos() > numeroPersona.resultado.getCorrectos():
            reasignarResultadosLista(numeroPersona,numeroMaquina,listaInvalidos)
        elif numeroMaquina.resultado.getCorrectos() == numeroPersona.resultado.getCorrectos():
            if numeroMaquina.resultado.getRegulares() >= numeroPersona.resultado.getRegulares():
                reasignarResultadosLista(numeroPersona,numeroMaquina, listaInvalidos)
        else:
            listaInvalidos.append(numeroMaquina.content.copy())
    print("Ganaste")

 
def reasignarResultadosLista(numeroPersona,numeroMaquina,listaInvalidos):
    listaInvalidos.append(numeroPersona.content.copy())
    numeroPersona.setContent(numeroMaquina.getContent())
    numeroMaquina.resultado.setCorrectos(numeroPersona.resultado.getCorrectos())
    numeroMaquina.resultado.setRegulares(numeroPersona.resultado.getRegulares())
    numeroMaquina.resultado.setIncorrectos(numeroPersona.resultado.getIncorrecto())

adivinaMaquina()
