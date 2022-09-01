def run():
    # mi_diccionario = {
    #     'clave1': 1,
    #     'clave2': 2,
    #     'clave3': 3
    # }
    
    # print(mi_diccionario['clave1'])
    # print(mi_diccionario['clave2'])
    # print(mi_diccionario['clave3'])
    
    poblacion_paises = {
        'Argentina': 125236655,
        'Peru': 32151161462,
        'Holanda': 16131113,
        'EEUU': 16131662662,
    }

    # print(poblacion_paises['EEUU'])
    
    # for pais in poblacion_paises.keys(): #keys es para imprimir las llaves
    #     print(pais)
    
    # for pais in poblacion_paises.values(): #values es para imprimir los valores
    #      print(pais)
    
    for pais, poblacion in poblacion_paises.items(): #items es para imprimir las llaves junto con los valores
         print(pais + ' tiene ' + str(poblacion) + ' habitantes.' )

if __name__ == '__main__':
    run()