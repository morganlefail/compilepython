def calcular_imc(peso, altura):
    # A fórmula do IMC é peso (kg) / (altura (m))^2
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# Obtendo dados do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calculando o IMC
imc = calcular_imc(peso, altura)

# Classificando o IMC
classificacao = classificar_imc(imc)

# Exibindo os resultados
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
