datos= [0,0,0,0,0,0,0,0,0,0,0,0,0
        ,1,1,1,1,1,1,1,1,1,1
        ,2,2,2,2,2,2,2
        ,3,3,3,3,3,3
        ,4,4]

def media(datos):
    return sum(datos)/len(datos)

def mediana(datos):
    if(len(datos)%2 == 0):
        return (datos[int(len(datos)/2)] + datos[int((len(datos)+1)/2)]) / 2
    else:
        return datos[(len(datos)+1)/2]

if __name__ == '__main__':
    print(media(datos))
    print(mediana(datos))