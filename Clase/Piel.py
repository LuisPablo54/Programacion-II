import random

pesoPromedio = 200
desviacionEstandar = pesoPromedio * 0.005
for i in range(1, 100):
    pesoPieza = random.gauss(pesoPromedio, desviacionEstandar)
    pesoTotal= 0
    pesoTotal += pesoPieza
    pesoPrimera = pesoPieza

    for i in range(1, 20):
       pesoPromedio = random.gauss(pesoPromedio, desviacionEstandar)
       pesoTotal += pesoPromedio

    numeroPiezas = round(pesoTotal / pesoPrimera)
    print("Peso total:", pesoTotal, " Piezas:", numeroPiezas)