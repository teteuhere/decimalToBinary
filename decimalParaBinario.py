def decimal_to_bin(decimal):
    if decimal ==0:
        return "0"

    pilha=[]
    while decimal>0:
        restante=decimal%2
        pilha.append(str(restante))
        decimal//=2

    binario="".join(pilha[::-1])
    return binario

while True:
    entrada=input("Escolha um numero maior que zero ou digite sair para encerrar: ")
    if entrada.lower()== 'sair':
        break
    try:
        decimal=int(entrada)
        if decimal<0:
            print("O numero deve ser maior ou igual a zero")
            continue

        binario=decimal_to_bin(decimal)
        print(f' O valor em {decimal} é: {binario}  em binario')
    except ValueError:
        print("Invalido, escolha um numero maior ou finalize(sair)")