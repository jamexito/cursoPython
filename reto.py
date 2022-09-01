
def run():
    menu = """
    BIENVENIDO AL MENU DE SUMAR Y RESTAR CON JAMES BEJARANO
    
    Para sumar, escribe 1...
    Para restar, escribe 2...
    
    Elige una opción:
    
    """
    
    opcion = int(input(menu))
    while opcion != 1 and opcion != 2:
        print('\nIngresa una opción correcta\n')
        opcion = int(input(menu))
        continue
    n1 = int(input("Ingresa el primer número: "))
    n2 = int(input("Ingresa el segundo número: "))
    if opcion == 1:
        operacion = n1 + n2
    else:
        operacion = n1 - n2   
        
    print("El resultado de la operación es: " + str(operacion)) 
        

if __name__ == '__main__':
    run()