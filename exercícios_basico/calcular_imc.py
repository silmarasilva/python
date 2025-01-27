# Problema: Calcule o IMC (Índice de Massa Corporal) de uma pessoa e indique a classificação.

def calculate_imc(weight, height):
    imc = weight / (height ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

print(calculate_imc(70, 1.75))  # Peso normal
print(calculate_imc(95, 1.75))  # Obesidade
