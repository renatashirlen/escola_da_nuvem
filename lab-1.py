#Funçao para adicionar uma pessoa a lista
def adicionar_pessoas(lista,nome,idade,profissao):
    pessoa ={"nome":nome, "idade":idade,"profissao":profissao}
    lista.append(pessoa)

#função para mostrar as pessoas
def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome:{pessoa['nome']},Idade: {pessoa['idade']}, Profissao:{pessoa['profissao']}")

#lista para armazenar pessoas 
pessoas = []

#adicionando pessoas em uma lista
adicionar_pessoas(pessoas,"ana",25,"engenheira")
adicionar_pessoas(pessoas,"leo",30,"medico")
adicionar_pessoas(pessoas,"lucas",33,"professor")

#exibir a lista de pessoas
exibir_pessoas(pessoas)