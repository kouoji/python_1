idades_usuario = []

def obter_idade_usuario():
    """
    Obter a idade do usuário e adicioná-la à lista.

    Retorna:
        None
    """

    idade = int(input("Digite sua idade: "))


    idades_usuario.append(idade)

def imprimir_idade_usuario():
    """
    Imprimir a idade do usuário da lista.

    Retorna:
        None
    """

    idade = idades_usuario[-1]

    print(f"Você tem {idade} anos de idade.")


obter_idade_usuario()


imprimir_idade_usuario()