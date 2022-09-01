soles = input("Cuántos soles tienes? ")
soles = float(soles)
dolar = 3.68
cambio = soles/dolar
cambio = round(cambio,2)
cambio = str(cambio)
print("Tienes $" + cambio + " dólares.")