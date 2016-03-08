class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final, sampling_f):
        """
        Los blancos en el medio reflejan la senal
        """
        # Inicio una lista de reflexiones
        senal_reflejada = []

        #Envio la senal a los blancos y escucho. Cada respuesta va en un canal
        #separado

        for blanco in self.blancos:
            senal_reflejada.append(blanco.reflejar(una_senal,\
                tiempo_inicial, tiempo_final, sampling_f))
        return senal_reflejada
