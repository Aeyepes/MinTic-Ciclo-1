def welcome_message(user_name):

    string = "Welcome "+ user_name
    string += " ,bye!"

    print(string)
    return string
#welcome_message("Teacher Diego Ivan")
#welcome_message("Julian")
#welcome_message("Andres Y")

def bye():
    print(" bye!!")


def fibonacci_imprimir(serie):
    n = serie
    a, b = 0, 1
    print(f"Imprime los enteros de la serie: {serie} ")
    
    while a < n:
        print(a, end= " ")
        a, b = b, a + b

def fibonacci_lista(serie):
    n = serie
    a, b = 0, 1
    resultado = []
    print(f"Imprime la lista de la serie: {serie} ")
    
    while a < n:
        resultado.append(a)
        a, b = b, a + b
    
    print(resultado)
    #return resultado


