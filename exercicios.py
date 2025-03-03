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
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação