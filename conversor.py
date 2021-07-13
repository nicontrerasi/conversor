dolar = 718.17
cambio = input("Quieres convertir de CLP a Dólar [C] o de Dólar a CLP [D]?: ")
if cambio.upper() == "C" or cambio.upper() == "D":
    if cambio.upper() == "C":
        moneda = input("Ingresa cantidad de CLP que quieres convertir a dólar: ")
        calculo = int(moneda) / dolar
        print("La cantidad ingresada en pesos chilenos ($"+str(moneda)+") equivale a $"+str(round(calculo,2))+" dólares")
    elif cambio.upper() == "D":
        moneda = input("Ingresa cantidad de dólares que quieres convertir a CLP: ")
        calculo = float(moneda) * int(dolar)
        print("La cantidad ingresada en dólares ($"+str(moneda)+") equivale a $"+str(round(calculo))+" CLP")
else:
    print("Has ingresado un dato incorrecto, vuelve a intentarlo")