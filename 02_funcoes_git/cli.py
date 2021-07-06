from lancamento_vertical import height

altura_inicial = float(input("Forneça a altura inicial / m: "))
velocidade_inicial = float(input("Forneça a velocidade inicial / m/s: "))
tempo = float(input("Forneça o tempo / s: "))

altura = height(altura_inicial, velocidade_inicial, tempo)

print(f"Altura de {altura:.2f} m")
