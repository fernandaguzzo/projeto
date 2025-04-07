from tinydb import TinyDB, Query

db = TinyDB('database/db.json')
reservas = db.table('reservas')
ReservaQuery = Query()

class Reserva:
    def __init__(self, usuario_email, livro_id):
        self.usuario_email = usuario_email
        self.livro_id = livro_id

    def salvar(self):
        reservas.insert({
            'usuario_email': self.usuario_email,
            'livro_id': self.livro_id
        })

    def listar_por_usuario(self):
        return reservas.search(ReservaQuery.usuario_email == self.usuario_email)

    def listar_todas(self):
        return reservas.all()
