'''
Disciplina: Linguagem de programação
Aula prática - Programa para cálculo de IMC(Índice de massa corporal)
Aluno: José Erivan Ramalho Ferreira Filho
'''

print("Bem vindo ao programa de cálculo de IMC ou Índice de massa corporal!")

'''
Primeiro temos a captura dos dados de entrada do usuário para que o cálculo seja realizado.
Lembrando que o conteúdo de validação de dados de entrada e tratamento de exceção ainda não foi passado,
mas já tive oportunidade de estudar em outras linguagens;
'''
while True:
    try:
        peso = float(input("Primeiro precisamos do seu peso em quilos(Ex: 53.2): "))
        altura = float(input("Agora precisamos da sua altura em metros(Ex: 1.5): "))
        if(peso < 0 or altura < 0):
            print("Entre com um valor válido maior que 0(zero).")
        else:
            break
    except ValueError as identifier:
        print("Por favor entre somente com valores numéricos.")
    

#Precisamos então fazer o cálculo do IMC utilizando da fórmula: IMC = peso / (altura)²;
imc = peso / (altura * altura)

'''
Verificamos em qual faixa o IMC do usuário está:
- Menor que 18.5 = Peso insuficiente
- Entre 18.5 e 24.9 = Peso normal
- Entre 25 e 29.9 Sobrepeso
- Entre 30 e 34.9 Obesidade
- Maior que 35 Obesidade extrema
E fazemos a checagem dos dados e suas faixas para obter o resultado e entregamos para o usuário;
'''
if(imc <= 18.5):
    print(f"Seu imc teve o valor de: {imc:.1f}, seu peso está abaixo do ideal.")
elif(imc > 18.5 and imc <= 24.9):
    print(f"Seu imc teve o valor de: {imc:.1f}, seu peso está na faixa ideal.")
elif(imc >= 25 and imc <= 29.9):
    print(f"Seu imc teve o valor de: {imc:.1f}, seu peso está acima do ideal(Indicação de sobrepeso).")
elif (imc >= 30 and imc <= 34.9):
    print(f"Seu imc teve o valor de: {imc:.1f}, seu peso está acima do ideal.(Indicação de obesidade).")
elif (imc > 35):
    print(f"Seu imc teve o valor de: {imc:.1f}, seu peso está muito acima do ideal(Indicação de obesidade extrema).")
else:
    print("Não foi possível fazer o cálculo, verifique os dados e tente novamente.")
    
'''
Por fim temos o programa de cálculo de IMC, 
que de acordo com as informações passadas chega em um resultado final
e trasmite isso para o usuário de forma simples e direta.
'''
    