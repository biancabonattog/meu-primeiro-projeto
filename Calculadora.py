def calculadora ():
    while True: # loop sempre vai executar
        print ("Calculadora Simples") # titulo do menu
        print ()
        print ("1. Soma") #opções de menu
        print ("2. Subtração")
        print ("3. Multiplicação")
        print ("4. Divisão")
        print ("s. Sair")
        operacao = input ("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a Calculadora simples")
            break #termina a execução do loop

        if operacao not in [ '1', '2', '3', '4']:
            print ("Opção inválida! Tente novamente.")
            continue #reset o looping

        numero_1 = float(input ("Primeiro número")) #isso faz o python converter o texto em número operável
        numero_2 = float(input ("Segundo número"))

        if operacao == '1':
            resultado =  numero_1 + numero_2
            print (" O resultado da operação soma é:", resultado)
        elif operacao == '2': #elif é garantir que só uma operação aconteça #caso ao contrario se
            resultado =  numero_1 - numero_2
            print (" O resultado da operação subtração é:", resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print(" O resultado da operação multiplicação é:", resultado)
        else :
            if numero_2 == 0:
                print ("Divisões por zero não são possíveis. Tente novamente")
                continue
            else:
                resultado = numero_1 * numero_2
                print(" O resultado da operação divisão é:", resultado)

calculadora()

