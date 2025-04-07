from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from tinydb import TinyDB, Query

db = TinyDB('database/db.json')
usuarios = db.table('usuarios')

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        Usuario = Query()
        user = usuarios.get(Usuario.email == email)
        if user and check_password_hash(user['senha'], senha):
            session['usuario'] = user
            return redirect('/buscar')
        return 'Login inválido'
    return render_template('login.html')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])
        tipo = request.form['tipo']  
        usuarios.insert({'nome': nome, 'email': email, 'senha': senha, 'tipo': tipo})
        return redirect('/login')
    return render_template('cadastro.html')
