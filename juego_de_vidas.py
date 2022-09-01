from fileinput import close


def juego(vidas):
    num_a = 5
    
    num = int(input("Escribe un número: "))
    
    if num < 0 or num > 10:
        vidas -= 1
        print("Número inválido, pierdes una vida!!!!")
        return vidas
    elif num_a > num:
        vidas -= 1
        print("El número ingresado es menor al del sistema, pierdes una vida!!!")
        return vidas
    elif(num == num_a):
        print("Vayaaa, es un empate!!")
        return vidas
    else:
        vidas += 1
        print("Genial, le ganaste al sistema!!")
        return vidas

        
def run():
    print("""
          El juego consiste en escribir un npumero mayor al que genera el sistema en un rango del 1 al 10,
          tienes 3 oportunidades de ganar.
          Suerte!!!!!!""")
    vidas = 3
    
    while(True):
        if vidas == 0:
            print("Fin del juego!")
            break
        
        vidas = juego(vidas)
        print("Te quedan " + str(vidas) + " vidas.")
        

if __name__ == '__main__':
    run()
