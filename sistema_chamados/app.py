from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(_name_)

# Criação do banco
def init_db():
    conn = sqlite3.connect('chamados.db') # cria e/ou conecta ao banco de dados
    cursor = conn.cursor() # Permite executar comandos SQL
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'Aberto'
        )
    ''')
    conn.commit()
    conn.close()
    
@app.route('')