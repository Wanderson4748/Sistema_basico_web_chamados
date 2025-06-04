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
### Consultas SQLs realizadas:

conn = sqlite3.connect('chamados.db')
**. CRIA OU CONECTA AO BANCO DE DADOS .**

cursor = conn.cursor()
**. Permite executar comandos SQL no SQLite3 .**

cursor.execute('''
    *Comandos SQL*
''')
**. Executa um ou mais comandos SQL .**

CREATE TABLE IF NOT EXISTS registros_chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT DEFAULT 'Aberto'
)
**. Linha 43: Verifica se existe a tabela registro_chamados caso não é criado .**

**. Linha 44: Cria a tupla ID como inteiro, chave primária e autoincrementado .**

**. Linha 45: cria a tupla titulo como texto não nulo, ou seja não pode ficar em branco .**

**. Linha 46: cria a tupla descricao como texto .**

**. Linha 47: cria a tupla status, sendo preenchida por padrão como "Aberto" .**

conn.commit()
**. Salva as alterações feitas na conexão do BD .**

conn.close()
**. Fecha a conexão com o Banco de Dados .**

cursor = execute("SELECT * FROM registros_chamados")
**. Seleciona todas as tuplas de todas as colunas da tabela registro_chamados .**

chamados = cursor.fetchall()
**. Coleta o que foi feito na consulta sql .**

return render_template('index.html', chamados=chamados)
**. Carrega o HTML e envia os dados para mostrar o navegador .**

cursor.execute("UPDATE registros_chamados SET status = ? WHERE id = ?", (status, id))

**. Executa um comando de atualização na tabela registros_chamados .**





