print("\n******************* Python Calculator ******************* \n\nSelecione o numro da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multipliação \n4 - Divisão")

entrada = input("\nDigite sua opção (1/2/3/4): ")

if int(entrada) == 1:
    primeiro = input("\nDigite o primeiro número: ")
    segundo = input("\nDigite o segundo número: ")
    soma = int(primeiro) + int(segundo)
    print("\nA soma dos valores são: " + str(soma) + "\n")
    
elif int(entrada) == 2:
    primeiro = input("\nDigite o primeiro número: ")
    segundo = input("\nDigite o segundo número: ")
    sub = int(primeiro) - int(segundo)
    print("\nA subtração dos valores são: " + str(sub) + "\n")
    
elif int(entrada) == 3:
    primeiro = input("\nDigite o primeiro número: ")
    segundo = input("\nDigite o segundo número: ")
    mul = int(primeiro) * int(segundo)
    print("\nA multipliação dos valores são: " + str(mul) + "\n")
    
elif int(entrada) == 4:
    primeiro = input("\nDigite o primeiro número: ")
    segundo = input("\nDigite o segundo número: ")
    div = int(primeiro) / int(segundo)
    print("\nA divisão dos valores são: " + str(div) + "\n")
    
elif int(entrada) < 1 or int(entrada) > 4 :
    print("\nOpção Invalida! Favor, tente novamente!")
