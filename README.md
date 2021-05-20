# Criação de usuários na AWS com Ansible baseado em arquivo CSV

## Geração de senha automática dentro dos padrões da AWS

## Criação de grupos e configuração de suas políticas

### Projetado para arquivos CSV simples com usuários e grupos e políticas



- Playbook associado a um script Python.


- Com base em um arquivo CSV (exemplo com nome de grupos_politicas.csv), cria grupos, e adiciona políticas específicas a cada um deles.


- Em seguida lê outro arquivo CSV (exemplo com nome de usuarios2.csv) com nomes de funcionários e seus respectivos grupos.


- No próximo passo cria um novo arquivo CSV com os mesmos usuários e grupos do CSV de usuários original, adicionando uma coluna com senhas aleatórias dentro dos padrões atuais da AWS.


- Por fim executa a criação dos usuários baseando-se neste novo arquivo CSV.


- OBS: no arquivo qrupos_politicas.csv é necessário trocar em todas as linhas "IDdaContaAWS" pelo número do ID da conta que será usada.
