# Criação de usuários na AWS com Ansible baseado em arquivo CSV

## Geração de senha automática dentro dos padrões da AWS

## Criação de grupos e configuração de suas políticas

### Projetado para arquivos CSV simples com usuários e grupos e políticas



- Playbook associado a um script Python.


- Lê um arquivo criptografado id.yml onde está armazenada a ARN de uma política customizada que pode expor a ID da conta da AWS.


- Com base em um arquivo CSV (exemplo com nome de grupos_politicas.csv) e no arquivo criptografado id.yml, cria grupos, e adiciona políticas específicas a cada um deles.


- Em seguida lê outro arquivo CSV (exemplo com nome de usuarios2.csv) com nomes de funcionários e seus respectivos grupos.


- No próximo passo cria um novo arquivo CSV com os mesmos usuários e grupos do CSV de usuários original, adicionando uma coluna com senhas aleatórias dentro dos padrões atuais da AWS.


- Por fim executa a criação dos usuários baseando-se neste novo arquivo CSV.


by Daniel Gil
