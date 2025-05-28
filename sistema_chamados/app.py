from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(_name_)

# Criação do banco
def init_db():
    conn = sqlite3.connect('chamados.db') # cria e/ou conecta ao banco de dados
    cursor = conn.cursor() # Permite executar comandos SQL
    
    # Criação da tabela chamados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros_chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'Aberto'
        )
    ''')
    conn.commit() # salva as alterações feitas na conexão do BD
    conn.close() # Fecha a conexão com o Banco de Dados
    
@app.route('/') # Define a rota principal da aplicação (/)
def index(): # Função index para ser chamada na rota (/)
    conn = sqlite3.connect('chamados.db') # Faz a conexão com o BD chamados
    cursor = conn.cursor() # Permite executar comandos sql
    cursor = execute("SELECT * FROM registros_chamados") # Executa a consulta sql
    chamados = cursor.fetchall() # Coleta a consulta sql da tabela registros_chamados
    conn.close() # Fecha a conexão com o BD chamados
    return render_template('index.html', chamados=chamados) # Carrega o HTML e envia os dados para mostrar o navegador

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        conn = sqlite3.connect('chamados.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registros_chamados (titulo, descricao) VALUES (?, ?)", (titulo, descricao))
        conn.comit()
        conn.close()
        return redirect('/')
    return render_template('criar.html')