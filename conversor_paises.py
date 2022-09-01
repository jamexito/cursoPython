def conversor(pregunta,t_cambio):
    moneda = input(pregunta)
    moneda = float(moneda)
    cambio = moneda/t_cambio
    cambio = round(cambio,2)
    cambio = str(cambio)
    print("Tienes $" + cambio + " dólares.")

menu = """
Bienvenidos al conversor de monedas 🤷‍♂️

1 - Pesos Colombianos
2 - Soles
3 - Pesos Mexicanos

Elija una opción """

opcion = int(input(menu))

if opcion == 1:
    conversor('Cuántos pesos Colombianos tienes? ',3785)
elif opcion == 2:
    conversor('Cuántos pesos soles tienes? ',3.89)
elif opcion == 3:
    conversor('Cuántos pesos Colombianos tienes? ',36)
else:
    print("Elija una opcion correcta")






