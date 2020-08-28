import random

def tirar_dado(numero_tiros):
    secuencia_tirios =[]

    for _ in range (numero_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_tirios.append(tiro)
    return secuencia_tirios

def main(numero_tiros, numero_intentos):
    tiros = []
    for _ in range(numero_intentos):
        secuencia_tiros= tirar_dado(numero_tiros)
        tiros.append(secuencia_tiros)

    tiros_1=0
    for tiro in tiros:
        if 1 in tiro:
            tiros_1 +=1
    prob_tiros_1 = tiros_1 / numero_intentos
    print(f'Probabilidad de obtener por lo menos un 1 en {numero_tiros} tiros = {prob_tiros_1}')


if __name__ == "__main__":
    numero_tiros = int(input('Cuantos tiros del dado:  '))
    numero_intentos = int(input('Cuantos intentos :  '))

    main(numero_tiros,numero_intentos)