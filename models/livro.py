from tinydb import TinyDB, Query

db = TinyDB('database/db.json')
livros = db.table('livros')
LivroQuery = Query()

class Livro:
    def __init__(self, titulo, autor, data_lancamento, sinopse):
        self.titulo = titulo
        self.autor = autor
        self.data_lancamento = data_lancamento
        self.sinopse = sinopse
        self.edicao = edicao

    def salvar(self):
        livros.insert({
            'titulo': self.titulo,
            'autor': self.autor,
            'data_lancamento' = data_lancamento
            'sinopse' = sinopse
            'edicao' = edicao

        })

    def buscar_por_termo(self):
        return livros.search(LivroQuery.titulo.matches(f'.*{self.titulo}.*', flags='i'))

    def buscar_por_id(self, doc_id):
        return livros.get(doc_id=doc_id)
