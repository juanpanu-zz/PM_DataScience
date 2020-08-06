from datetime import datetime
import pytz

utc_time = datetime.now()
print("UTC time:", utc_time.strftime("%m/%d/%Y, %H:%M:%S"))

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá time:", bogota_date.strftime("%m/%d/%Y, %H:%M:%S"))


tucuman_timezone = pytz.timezone("America/Argentina/Tucuman")
tucuman_date = datetime.now(tucuman_timezone)
print("Tucumán time:", tucuman_date.strftime("%m/%d/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Mexico time:", mexico_date.strftime("%m/%d/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas time:", mexico_date.strftime("%m/%d/%Y, %H:%M:%S"))

