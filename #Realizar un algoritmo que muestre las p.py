#Realizar un algoritmo que muestre las potencias de los primeros 10 números naturales.
num = 1
potencia = []
for i in range(1,11):
    potencia.append(i*i)
while num <= 10:
    print("potencia ",num, ": ",potencia[num-1])
    num = num + 1

