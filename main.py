import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # Parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    # Obtengo mi generador con los parametros adecuados
    MiGen = generador.Generador(amplitud, fase, frecuencia)

    MiDet = detector.Detector()

    #Creo un radar
    MiRad = radar.Radar(MiGen,MiDet)


    # Parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)

    # Creo un blanco
    MiBlanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco,\
        tiempo_inicial_del_blanco, tiempo_final_del_blanco)

    # Creo un medio
    MiMedio = medio.Medio([MiBlanco])

    # Comienzo la operacion
    MiRad.detectar(MiMedio, tiempo_inicial, tiempo_final)
if __name__ == "__main__":
    main()
