# Criação de usuários na AWS com Ansible baseado em arquivo CSV

## Geração de senha automática dentro dos padrões da AWS

### Projetado para um arquivo CSV simples com usuários e grupos



- Playbook associado a um script Python que lê um arquivo CSV simples com nomes de funcionários e seus respectivos grupos.


- Em seguida cria um novo arquivo CSV com os mesmos usuários e grupos do CSV original, adicionando uma coluna com senhas aleatórias dentro dos padrões atuais da AWS.


- Por fim executa a criação dos usuários baseando-se neste novo arquivo CSV.
