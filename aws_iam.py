"""
Este arquivo executa 3 tarefas:

1 - Leitura de arquivo csv com dados de usuário e armazenamento em listas
2 - Geração de senhas aleatórias com requisitos da AWS:
    Requisitos AWS:
        - Mínimo de 8 caracteres;
        - Mínimo de 1 letra maiúscula;
        - Mínimo de 1 letra minúscula;
        - Mínimo de 1 caracter especial;
        - Mínimo de 1 número.
    Regras de geração deste arquivo:
        - 9 caracteres aparecendo em ordem aleatória, sendo:
            - 2 letras maiúsculas;
            - 2 letras minúsculas;
            - 1 caracter especial;
            - 4 números
3 - Criação de novo arquivo csv com usuários e grupos do arquivo original e senha gerada aqui.
"""

import csv
from random import randint, choice, shuffle


def gera_senha():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    caracteres = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|']
    senha = []

    for n in range(2):  # Gera 4 letras, 2 minúsculas e 2 maiúsculas
        senha.append(choice(letras))
        senha.append(choice(letras).upper())

    for n in range(4):  # Gera 4 números entre 0 e 9
        senha.append(str(randint(0, 9)))

    senha.append(choice(caracteres))  # Gera 1 caracter especial
    shuffle(senha)  # Embaralha a lista aleatóriamente
    senha = ''.join(senha)  # Unifica os elementos da lista em uma única string
    return senha


usuario = []
grupo = []


with open('usuarios2.csv') as original:  # Abre o arquivo original para leitura
    leitor = csv.DictReader(original)
    for row in leitor:
        usuario.append(row['usuarios'])  # Armazena todos os usuários em uma lista
        grupo.append(row['grupo'])  # Armazena todos os grupos em uma lista


with open('usuarios_com_senha.csv', 'w') as destino:  # Cria o novo arquivo
    fieldnames = ['usuarios', 'grupo', 'senha']
    writer = csv.DictWriter(destino, fieldnames=fieldnames)
    writer.writeheader()
    for n in range(len(usuario)):
        # Escreve linhas no arquivo com cada usuário e respectivos grupos e senhas:
        writer.writerow({'usuarios': usuario[n], 'grupo': grupo[n], 'senha': gera_senha()})
