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

        self.plotear_senal(una_senal, una_senal_reflejada[0])

        # Proceso la senal
        return self.detector.detectar(una_senal,una_senal_reflejada,\
            tiempo_inicial, sampling_f)


    # Graphs
    def plotear_senal(self, orig, ref):
        import matplotlib.pyplot as plt

        x = xrange(0,len(orig))

        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
        ax1.plot(x, orig, label="Original")
        ax2.plot(x, ref, label="Reflejada")
        ax1.legend(loc="best")
        ax2.legend(loc="best")
        plt.show(True)
