"""
Define el similador del Radar
"""


class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector


    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """

        # Consigo una senal con una cierta frecuencia de muestreo
        una_senal, sampling_f = self.generador.generar(tiempo_inicial,\
            tiempo_final)

        # Consigo el resultado de las reflexiones de esa senal
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        tiempo_final, sampling_f)

        # Proceso la senal
        return self.detector.detectar(una_senal,una_senal_reflejada,\
            tiempo_inicial, sampling_f)


    #TODO agregar el metodo plotear_senal
