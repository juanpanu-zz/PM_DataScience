import requests
import json
import os

URL= "https://www.dolarsi.com/api/api.php?type=valoresprincipales"

def get_information(url):
    response = requests.get(url)
    content = json.loads(response.content)
    dolar_value = float(content[0]['casa']['compra'].replace(',','.'))
    return dolar_value
    

def run(url):
    dolar_value = get_information(url)
    pesos_to_dolares = lambda pesos, dolar_value: pesos / dolar_value
    dolar_to_pesos = lambda dolares, dolar_value: dolars* dolar_value

    menu="""
    Bienvenido al conversor de monedas dinámico

    [1]Dolares a pesos
    [2]Pesos a dolares

    Escribe tu opción:"""

    choice = input(menu)
            
    if choice == '1':
        os.system('cls')
        dolars = float(input('Cuantos dólares tienes?:'))
        pesos = dolar_to_pesos(dolars,dolar_value)
        print(f'Tienes {pesos} pesos')
    elif choice == '2':
        os.system('cls')
        pesos = float(input('Cuantos pesos tienes?:'))
        dolars = pesos_to_dolares(pesos,dolar_value)
        print(f'Tienes {dolars} dolares')
        
    else:
        print('Elige una opción correcta')

if __name__ == "__main__":
    run(URL)
