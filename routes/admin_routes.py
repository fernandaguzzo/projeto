from flask import Blueprint, render_template, session
from tinydb import TinyDB

db = TinyDB('database/db.json')
reservas = db.table('reservas')
usuarios = db.table('usuarios')

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
def dashboard():
    if 'usuario' not in session or session['usuario']['tipo'] != 'bibliotecaria':
        return 'Acesso negado'

    total_reservas = len(reservas)
    total_usuarios = len([u for u in usuarios.all() if u['tipo'] == 'usuario'])

    return render_template('dashboard.html', total_reservas=total_reservas, total_usuarios=total_usuarios)
