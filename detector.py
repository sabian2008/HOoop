class Detector(object):

    def __init__(self):
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def detectar(self, original, senal, comienzo, sampling_f):

        for line in senal:
            if (not original == line ):
                print "Se detecto algo"
