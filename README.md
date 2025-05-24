Projeto Web Básico de Sistema de Chamados

# Linguagens Utilizadas:
- Python
- HTML + Bootstrap
- SQLite

# Funcionalidades:
- Ver chamados cadastrados.
- Criar novos chamados.
- Alterar status do chamado (Aberto / Em andamento / Fechado).
- Tudo rodando localmente via navegador em http://localhost:5000.

# Estrutura do Projeto:

sistema chamados/

|-- app.py
|-- chamados.py
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- criar.html

# app.py:
- Criar o servidor web local;
- Se conectar ao banco de dados SQLite;
- Definir as rotas (/, /criar, etc);
- Lidar com o envio e exibição dos chamados.

