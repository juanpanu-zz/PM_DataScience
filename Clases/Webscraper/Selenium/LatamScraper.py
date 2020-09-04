# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# %%
URL = 'https://www.latam.com/es_co/apps/personas/booking?fecha1_dia=01&fecha1_anomes=2021-06&fecha2_dia=15&fecha2_anomes=2021-06&from_city2=LON&to_city2=BOG&auAvailability=1&ida_vuelta=ida_vuelta&vuelos_origen=Bogot%C3%A1&from_city1=BOG&vuelos_destino=Londres&to_city1=LON&flex=1&vuelos_fecha_salida_ddmmaaaa=01/06/2021&vuelos_fecha_regreso_ddmmaaaa=15/06/2021&cabina=Y&nadults=1&nchildren=0&ninfants=0&cod_promo=&stopover_outbound_days=0&stopover_inbound_days=0#/'
# %%
def get_prices(vuelo):
    """
    Funcion que retorna una lista de diccionarios con las distintas tarifas
    """
    tarifas = vuelo.find_elements_by_xpath('//div[@class="fares-table-container"]//tfoot//td[contains(@class,"fare-")]')
    precio_tarifa=[]
    for tarifa in tarifas:
        nombre= tarifa.find_element_by_xpath('.//label').get_attribute('for')
        sym = tarifa.find_element_by_xpath('.//span[@class="price"]/span[@class="currency-symbol"]').text
        valor = tarifa.find_element_by_xpath('.//span[@class="price"]/span[@class="value"]').text
        dict_tarifa={nombre:{'moneda':sym,'valor':valor}}
        precio_tarifa.append(dict_tarifa)
    return precio_tarifa
# %%
def get_datos_escalas(vuelo):
    """
    Funcion que retorna una lista de diccionarios con la informacion de las escalas de cada vuelo
    """
    
    segmentos = vuelo.find_elements_by_xpath('//div[@class="sc-hZSUBg gfeULV"]/div[@class="sc-cLQEGU hyoued"]')
    info_escalas = []
    for segmento in segmentos:
        #Origen - Destino
        origen,destino = segmento.find_elements_by_xpath('.//div[@class="sc-iujRgT jEtESl"]//abbr[@class="sc-hrWEMg hlCkST"]')
        #Salida - llegada
        hora_salida, hora_llegada = segmento.find_elements_by_xpath('.//div[@class="sc-iujRgT jEtESl"]//time')
        #Duracion
        duracion_vuelo=segmento.find_element_by_xpath('.//span[@class="sc-esjQYD dMquDU"]/time').get_attribute('datetime')
        #Num vuelo
        num_vuelo=segmento.find_element_by_xpath('.//div[@class="airline-flight-details"]/b').text
        #Modelo
        modelo = segmento.find_element_by_xpath('.//div[@class="airline-flight-details"]/span[@class="sc-gzOgki uTyOl"]').text
        if segmento != segmentos[-1]:
            #Duracion Escala
            escala = segmento.find_element_by_xpath('//div[@class="sc-hMFtBS cfwWiO"]//span[@class="sc-esjQYD dMquDU"]/time').get_attribute('datetime')
        else:
            escala =''
        escalas_dict={
            'origen': origen.text,
            'hora_salida': hora_salida.get_attribute('datetime'),
            'destino': destino.text,
            'hora_llegada' : hora_llegada.get_attribute('datetime'),
            'duracion_vuelo' : duracion_vuelo,
            'num_vuelo' : num_vuelo,
            'modelo' : modelo,
            'duracion_escala' : escala}
        info_escalas.append(escalas_dict)
    
    return info_escalas
# %%
def get_times(vuelo):
    """
    Funcion que retorna un diccionario con los horarios de salida y llegada de cada vuelo, incluyendo duración.
    Nota:la duración del vuelo no es hora de llegada - hora de salida, puede haber diferencia de horarios entre el origen y el destino
    """
    hora_salida = vuelo.find_element_by_xpath('.//div[@class="departure"]/time').get_attribute('datetime')
    hora_llegada = vuelo.find_element_by_xpath('.//div[@class="arrival"]/time').get_attribute('datetime')
    duracion_vuelo = vuelo.find_element_by_xpath('.//span[@class="duration"]/time').get_attribute('datetime').replace('PT','')
    dict_times = {
        'hora_salida':hora_salida,
        'hora_llegada':hora_llegada,
        'duracion_vuelo':duracion_vuelo
    }
    return dict_times
# %%
def get_flights_info(driver):
    vuelos = driver.find_elements_by_xpath('//li[@class="flight"]')
    print(f'Se encontraron {len(vuelos)} vuelos')
    print('Iniciando Scraping...')
    info =[]
    for vuelo in vuelos:
        #Get general times for flight
        times = get_times(vuelo)
        #CLick sobre boton Escalas
        boton_escalas = vuelo.find_element_by_xpath('.//div[@class="flight-summary-stops-description"]/button')
        boton_escalas.click()
        escalas = get_datos_escalas(vuelo)
        driver.find_element_by_xpath('//div[@class="modal-content sc-iwsKbI eHVGAN"]//button[@class="close"]').click()
        #click sobr el vuelo para ver precios
        vuelo.click()
        precios = get_prices(vuelo)
        vuelo.click()
        info.append({'precios':precios,'tiempos':times,'escalas':escalas})
    return info
# %%
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path = 'D:\_Me\Selenium\Chromedriver', options=options)
driver.get(URL)
# delay
delay = 10
try:
    #Dinamic delay
    vuelo = WebDriverWait(driver,delay).until(EC.presence_of_all_elements_located((By.XPATH, '//li[@class="flight"]')))
    print('La página terminó de Cargar')
    info_vuelos = get_flights_info(driver)
except TimeoutException:
    print('La página tardó demasiado en cargar')
    info_vuelos=[]
driver.close()
# %%
print(info_vuelos)
# %%
import json

with open('data.json', 'w') as fp:
    json.dump(info_vuelos , fp, indent=4)