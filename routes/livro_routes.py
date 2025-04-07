from flask import Blueprint, render_template, request, redirect, session
from tinydb import TinyDB, Query

db = TinyDB('database/db.json')
livros = db.table('livros')
reservas = db.table('reservas')

livro_bp = Blueprint('livro', __name__)

@livro_bp.route('/buscar', methods=['GET', 'POST'])
def buscar_livro():
    if 'usuario' not in session:
        return redirect('/login')

    resultados = []
    if request.method == 'POST':
        termo = request.form['termo']
        resultados = livros.search(Query().titulo.matches(f'.*{termo}.*', flags='i'))
    return render_template('buscar_livro.html', resultados=resultados)

@livro_bp.route('/reservar/<int:livro_id>')
def reservar_livro(livro_id):
    if 'usuario' not in session:
        return redirect('/login')

    reservas.insert({
        'usuario_email': session['usuario']['email'],
        'livro_id': livro_id
    })
    return 'Livro reservado com sucesso!'
