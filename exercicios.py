import math

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
primeiro_numero = int(input("Insira o Primeiro Número"))
segundo_numero = int(input("Insira o Segundo Número"))
resultado = primeiro_numero + segundo_numero
print(f"O resultado é: {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_usuario = float(input("Insira um Número"))
calculo_resto_divisao = numero_usuario % 5
print(f"O resultado é: {calculo_resto_divisao}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
primeiro_numero = float(input("Insira o Primeiro Número"))
segundo_numero = float(input("Insira o Segundo Número"))
resultado = primeiro_numero * segundo_numero
print(f"O resultado é: {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
primeiro_numero = int(input("Insira o Primeiro Número"))
segundo_numero = int(input("Insira o Segundo Número"))
resultado = primeiro_numero // segundo_numero
print(f"O resultado é: {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_usuario = float(input("Insira um Número"))
resultado = math.sqrt(numero_usuario)
print(f"O resultado é: {resultado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
primeiro_numero = float(input("Insira o Primeiro Número"))
segundo_numero = float(input("Insira o Segundo Número"))
resultado = primeiro_numero + segundo_numero
print(f"O resultado é: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
primeiro_numero = float(input("Insira o Primeiro Número"))
segundo_numero = float(input("Insira o Segundo Número"))
soma = primeiro_numero + segundo_numero
divisao = soma / 2
print(f"O resultado é: {divisao}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base_usuario = float(input("Insira a Base"))
expoente_usuario = float(input("Insira o Expoente"))
resultado = base_usuario ** expoente_usuario
print(f"O resultado é: {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Insira a Temperatura C°"))
formula = (celsius * 1.8) + 32
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
      % (celsius, formula))

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
tamanho = float(input("Insira o Raio do Círculo"))
formula = math.pi(tamanho) * 2
print(f"O resultado é: {formula}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
dado_usuario = str(input("Escreva Algo Aqui"))
convercao_maiusculas = dado_usuario.upper()
resultado_convercao = print(convercao_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_usuario = str(input("Escreva Seu Nome Aqui"))
convercao_minusculas = nome_usuario.lower()
resultado_convercao = print(convercao_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase_usuario = str(input("Escreva Uma Frase Aqui"))
convercao_frase = frase_usuario.strip()
resultado_convercao = print(convercao_frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = str(input("Escreva Uma Data Aqui"))
ajuste_data = data_usuario.split("/")
resultado_ajuste = print(ajuste_data)
dia = print(ajuste_data[0])
mês = print(ajuste_data[1])
ano = print(ajuste_data[2])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
first_user_string = str(input("Write the first phrase here"))
second_user_string = str(input("Write the second phrase here"))
concatenated_string = first_user_string + "" + second_user_string
print(concatenated_string)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")