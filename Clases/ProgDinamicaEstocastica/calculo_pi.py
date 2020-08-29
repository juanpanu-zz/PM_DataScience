import random
import math
import statistics as std
def lanzar_agujas(nAgujas):
    dentro_circulo = 0

    for _ in range (nAgujas):
        x = random.random()*random.choice([0 ,1 ])
        y = random.random()*random.choice([0 ,1 ])
        distancia_centro = math.sqrt(x**2 + y**2)

        if distancia_centro <= 1:
            dentro_circulo += 1
    return (4* dentro_circulo)/ nAgujas

def estimacion(nAgujas, nIntentos):
    estimados = []
    for _ in range (nIntentos):
        est_pi = lanzar_agujas(nAgujas)
        estimados.append(est_pi)

    media = std.mean(estimados)
    sigma = std.stdev(estimados)
    print(f'Pi={round(media,5)}, sigma = {round(sigma,5)} Agujas = {nAgujas}')

    return (media,sigma)


def estimar_pi(presicion,nIntentos):
    nAgujas= 1000
    sigma = presicion

    while sigma >= presicion / 1.96:
        media,sigma = estimacion(nAgujas,nIntentos)
        nAgujas*=2

    return media

if __name__ == "__main__":
    estimar_pi(0.01,1000)