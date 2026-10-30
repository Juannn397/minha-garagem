
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Ola, minha primeira pagina Flask!"

@app.route("/sobre")
def sobre():
    return "Estou aprendendo Flask no SENAI."

@app.route("/cardapio")
def cardapio():
    return """
    <h1>Meu Cardapio</h1>
    <ul>
        <li>Pizza</li>
        <li>Calentado</li>
        <li>Hamburguer</li>
    </ul>
    """

from markupsafe import escape

@app.route("/ola/<nome>")
def ola(nome):
    return f"<h1>Olá, {escape(nome)}!</h1>"

@app.route("/quadrado/<int:n>")
def quadrado(n):
    return f"O quadrado de {n} é {n * n}"

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    resultado = a + b
    return f"{a} + {b} = {resultado}"
