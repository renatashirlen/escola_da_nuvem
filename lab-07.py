# Criar um programa para verificar se uma frase é um palíndromo
'''
Um palíndromo é uma palavra, frase ou número que pode ser lido da mesma forma da esquerda para a direita ou da direita para a esquerda, desconsiderando espaços, pontuação e diferenças entre maiúsculas e minúsculas.
'''

def is_palindramo(texto):
    texto_limpo = ''.join(
        char.lower() for char in texto if char.isalnum()  # Checa se todos os caracteres são alfanuméricos
    )
    return texto_limpo == texto_limpo[::-1]


print('Escreva uma frase ou palavra para verificar se é um palíndromo.\n '
'Exemplo: "Anotaram a data da maratona" é um palíndromo. \n Agora faça você! \n')

frase = input("Digite uma frase ou palavra: ")
resultado = is_palindramo(frase)

if resultado is True:
    print(f'A frase "{frase}" é um palíndromo')

else:
    print(f'A frase "{frase}" não é um palíndromo')


