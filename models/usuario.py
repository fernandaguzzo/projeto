from tinydb import TinyDB, Query
from werkzeug.security import generate_password_hash, check_password_hash

db = TinyDB('database/db.json')
usuarios = db.table('usuarios')
UsuarioQuery = Query()

class Usuario:
    def __init__(self, nome, email, senha, tipo='usuario'):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def salvar(self):
        senha_hash = generate_password_hash(self.senha)
        usuarios.insert({
            'nome': self.nome,
            'email': self.email,
            'senha': senha_hash,
            'tipo': self.tipo
        })

    def autenticar(self):
        user = usuarios.get(UsuarioQuery.email == self.email)
        if user and check_password_hash(user['senha'], self.senha):
            return user
        return None

    def buscar_por_email(self):
        return usuarios.get(UsuarioQuery.email == self.email)
