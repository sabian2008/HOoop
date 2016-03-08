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

        # Consigo cuanto tiempo y desde cuando debo modificar la senal
        delta_t = (self.tiempo_final - tiempo_inicial).seconds
        min_t = max([self.tiempo_inicial, tiempo_inicial]).seconds

        # Paso esos valores de tiempo a valores de muestra
        delta_t = round(delta_t / sampling_f)
        min_t = round((tiempo_final - min_t) / sampling_f)
        max_t = round(min([tiempo_final,min_t + delta_t]))

        # Si delta t es menor que cero, entonces no hay reflexion
        if (not delta_t < 0):
            # Desde el t minimo hasta el maximo de interseccion
            # modifico la senal
            for i in range(min_t, max_t):
                senal[i] = senal[i] + self.amplitud
