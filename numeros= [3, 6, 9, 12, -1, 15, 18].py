numeros= [3, 6, 9, 12, -1, 15, 18]

for numero in numeros:
    if numero <0:
        print(f "encontrado numero negativo: {numero}. parando o processo.")
        break
    if numero % 2 == 0:
        print(f "numero par encontrado: {numero}. pulandopara o próximo.")
        continue
    print(f "processando o numero: {numero}")