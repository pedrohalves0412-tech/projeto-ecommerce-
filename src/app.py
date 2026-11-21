
from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00},
    {"id": 2, "nome": "Celular", "preco": 1500.00},
    {"id": 3, "nome": "Fone de ouvido", "preco": 120.00}
]

@app.route("/")
def inicio():
    return "Bem-vindo à Loja Fácil!"

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)
