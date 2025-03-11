# Calcula a média entre um número x de valores entrada pelo usuário. 
# O programa deve tratar entradas inválidas. A quantidade de entradas será definida pelo usuário. 
# O programa deve exibir a média e o total de valores válidos registrados até que ele dê o comando de fim


notas = []
while True:
    try:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break

        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor de 0 a 10.")    
    except ValueError:
        print("Entrada Inválida. Por favor, digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas válidas registradas: {len(notas)}")
else:
    print("Nenhuma nota válida registrada")