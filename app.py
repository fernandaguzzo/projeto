from flask import Flask
from routes.auth_routes import auth_bp
from routes.livro_routes import livro_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'


app.register_blueprint(auth_bp)
app.register_blueprint(livro_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)
