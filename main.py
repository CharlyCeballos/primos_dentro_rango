from copy import copy
from os import name, system

os_type = name

def es_primo(num, n=2):
    if n >= num:
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        return False

def generar_numeros_primos_rango(inicio, final):
    numero_evaluado = copy(inicio)
    salida = []

    try:
        while numero_evaluado <= final:
            response = es_primo(numero_evaluado)
            if response:
                salida.append(numero_evaluado)
            numero_evaluado = numero_evaluado + 1
    except Exception as error:
        print(f"Error2: \n  {error=} \n  {type(error)=}")

    print(' '.join(str(i) for i in salida))
    print(f'{len(salida)} números primos desde {inicio} hasta {numero_evaluado - 1}')
    if os_type == 'nt':
        system('pause')

def preguntar_rango():
    if(os_type == 'posix'):
        system('clear')
    else:
        system('cls')
    print('¿En qué rango de números naturales (ℕ) desea generar los números primos?')

    try:
        inicio = int(input('Inicio del rango: '))
        final = int(input('Final del rango: '))

        if inicio > 0 and final > 0 and inicio <= final:
            generar_numeros_primos_rango(inicio, final)
        else:
            print('La cantidad debe ser ℕ (número natural) y el final debe ser mayor al inicio.')
    except Exception as error:
        print(f"Error1: \n  {error=} \n  {type(error)=}")

preguntar_rango()
