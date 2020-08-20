# Resolve the problem!!

import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
char_lower= list(string.ascii_lowercase)           #Se incluye el abecedario en minuscula y mayuscula junto con los digitos
char_upper= list(string.ascii_uppercase) 
char_digit= list(string.digits)


def pass_sections(clist):
    # Esta funcion me permite generar una seccion de entre 2 y 4 caracteres de la contraseña escogiendo una muestra de la lista ingresada
    klen = random.randrange(2,5,2)
    psection=random.sample(clist,k=klen)
    return(psection)

def generate_password():
    # Start coding here
    # Genero una lista por cada seccion
    plower= pass_sections(char_lower)
    pupper= pass_sections(char_upper)
    pnumber= pass_sections(char_digit)
    psymbol= pass_sections(SYMBOLS)
    # Uno las secciones y las desordeno usando shuffle
    my_pass=(plower+pupper+pnumber+psymbol)
    random.shuffle(my_pass)
    
    return my_pass
    

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
