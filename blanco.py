class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
	self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial, tiempo_final, sampling_f):
        import math

        ret = list(senal)
        # # Consigo cuanto tiempo (y muestras) debo modificar la senal
        # delta_t = (self.tiempo_final - tiempo_inicial).seconds
        # delta_t = int(math.ceil(delta_t / sampling_f))

        # Consigo cuando empiezo a modificar (si negativo, es en muestra 0 y
        # ni lo paso a muestras)
        min_t = (self.tiempo_inicial - tiempo_inicial).seconds
        if min_t > 0:
            min_t = int(math.floor(min_t / sampling_f))
        else:
            min_t = 0

        # Consigo cuando termino de modificar, misma idea
        max_t = (self.tiempo_final - tiempo_final).seconds
        if max_t > 0:
            max_t = len(senal) - 1
        else:
            max_t = int(math.ceil((self.tiempo_final - tiempo_inicial).seconds \
                / sampling_f))

        # Si estoy en las condiciones de deteccion, modifico la senal
        if (self.tiempo_final > tiempo_inicial) and \
            (self.tiempo_inicial < tiempo_final):
            # Desde el t minimo hasta el maximo de interseccion
            # modifico la senal
            for i in range(min_t, max_t):
                ret[i] = senal[i] + self.amplitud
        return ret
