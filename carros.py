import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 

# 1. Criar a aplicacao Flask
app = Flask(__name__)

# 2. Configurar o banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///garagem.db"

app.secret_key = os.environ.get("SECRET_KEY", "chave-de-estudo-local")

# 3. Conectar Flask ao SQLAlchemy
db = SQLAlchemy(app)

# 4. Criar o modelo da tabela Nota
class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)

# Modelo da tabela Tarefa
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    feita = db.Column(db.Boolean, default=False)    

# 5. Criar as tabelas no banco
with app.app_context():
    db.create_all()



carros = [
    {
        "id": 1,
        "marca": "Volkswagen",
        "modelo": "Gol",
        "foto": "https://cdn.motor1.com/images/mgl/YAAopq/s1/volkswagen-gol-1.0-2023.webp",
        "opcionais": [
            "Ar-condicionado",
            "Direção hidráulica",
            "Vidros elétricos"
        ]
    },

    {
        "id": 2,
        "marca": "Fiat",
        "modelo": "Uno",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHYNeDe9kYWQvPr3DZU_tMJ2XSCGNzWwJ2CVo__M5XrYsX9WaliNhTsqnr&s=10",
        "opcionais": [
            "Ar-condicionado",
            "Travas elétricas"
        ]
    },

    {
        "id": 3,
        "marca": "Chevrolet",
        "modelo": "Onix",
        "foto": "https://cdn.motor1.com/images/mgl/AbOg2/s1/4x3/chevrolet-onix-2019.webp",
        "opcionais": [
            "Multimídia",
            "Câmera de ré",
            "Sensor de estacionamento",
            "Direção elétrica"
        ]
    },

    {
        "id": 4,
        "marca": "Fiat",
        "modelo": "Argo",
        "foto": "https://argo.fiat.com.br//asset/productDetails/mosaic/design.webp",
        "opcionais": [
            "Ar-condicionado",
            "Direção elétrica",
            "Vidros elétricos"
        ]
    },

    {
        "id": 5,
        "marca": "Toyota",
        "modelo": "Corolla",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkfXXbznIIx6whsvJeOW_g8k5OL4acxQSgFkMnsgrrNQ&s=10",
        "opcionais": [
            "Ar digital",
            "Piloto automático",
            "Câmera de ré",
            "Bancos de couro",
            "Chave presencial",
            "Sensor de estacionamento"
        ]
    },

    {
        "id": 6,
        "marca": "Honda",
        "modelo": "Civic",
        "foto": "https://cdn.motor1.com/images/mgl/mBrOo/s1/honda-civic-exl-2020.webp",
        "opcionais": [
            "Ar digital",
            "Teto solar",
            "Bancos de couro",
            "Câmera de ré",
            "Piloto automático"
        ]
    },

    {
        "id": 7,
        "marca": "Volkswagen",
        "modelo": "Polo",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ80zQ1JMbfU7jiYcdEgCcGCMw6mpy95aavz1oIgVeRTwY0bEKRoiUP9ss&s=10",
        "opcionais": [
            "Multimídia",
            "Direção elétrica",
            "Ar-condicionado"
        ]
    },

    {
        "id": 8,
        "marca": "Hyundai",
        "modelo": "HB20",
        "foto": "https://cdn.motor1.com/images/mgl/XR6vp/s1/4x3/hyundai-hb20-2019.webp",
        "opcionais": [
            "Multimídia",
            "Câmera de ré"
        ]
    },

    {
        "id": 9,
        "marca": "Fiat",
        "modelo": "Mobi",
        "foto": "https://midiawm1.webmotors.com.br/wp-content/uploads/2023/03/24140932/Fiat-Mobi-Trekking-0668-scaled.webp",
        "opcionais": [
            "Ar-condicionado"
        ]
    },

    {
        "id": 10,
        "marca": "Chevrolet",
        "modelo": "Tracker",
        "foto": "https://cdn.motor1.com/images/mgl/vxoyQG/s1/chevrolet-tracker-premier-1.2t-2023.webp",
        "opcionais": [
            "Ar digital",
            "Câmera de ré",
            "Piloto automático",
            "Alerta de colisão",
            "Sensor de estacionamento"
        ]
    }
]

@app.route("/id/<int:numero>")
def buscar_id(numero):

    for carro in carros:
        if carro["id"] == numero:
            return render_template("carro.html", carro=carro)

    return "Carro nao encontrado", 404

@app.route("/marca/<marca>")
def buscar_marca(marca):

    encontrados = []

    for carro in carros:
        if carro["marca"].lower() == marca.lower():
            encontrados.append(carro["modelo"])

    if encontrados:
        return ", ".join(encontrados)

    return "Marca não encontrada", 404

@app.route("/")
def inicio():
    return render_template("home.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/carros")
def listar_carros():
    return render_template("lista_carros.html", carros=carros)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    if request.method == "POST":

        nota = request.form["nota"]
        comentario = request.form["comentario"]

        return render_template(
            "obrigado.html",
            nota=nota,
            comentario=comentario
        )

    return render_template("feedback.html")

@app.route("/notas", methods=["GET", "POST"])
def notas():

    if request.method == "POST":

        texto = request.form.get("texto", "").strip()

        if not texto or len(texto) > 200:
            flash("Digite uma nota de 1 a 200 caracteres.")

        else:
            nova_nota = Nota(texto=texto)

            db.session.add(nova_nota)
            db.session.commit()
            flash("Nota salva com sucesso!")

        return redirect(url_for("notas"))

    todas_notas = db.session.execute(
        db.select(Nota).order_by(Nota.id.desc())
    ).scalars().all()

    return render_template(
        "notas.html",
        notas=todas_notas
    )

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    nota = db.get_or_404(Nota, id)

    if request.method == "POST":

        texto = request.form.get("texto", "").strip()

        if not texto or len(texto) > 200:
            flash("Digite uma nota de 1 a 200 caracteres.")
            return render_template("editar.html", nota=nota)

        nota.texto = texto
        db.session.commit()

        flash("Nota atualizada com sucesso!")

        return redirect(url_for("notas"))

    return render_template("editar.html", nota=nota)

@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):

    nota = db.get_or_404(Nota, id)

    db.session.delete(nota)
    db.session.commit()

    flash("Nota excluida com sucesso!")

    return redirect(url_for("notas"))

@app.route("/tarefas")
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form["titulo"]

    if titulo.strip():
        nova_tarefa = Tarefa(titulo=titulo)
        db.session.add(nova_tarefa)
        db.session.commit()
        flash("Nota salva com sucesso!")

    return redirect(url_for("listar_tarefas"))


@app.route("/concluir/<int:tarefa_id>", methods=["POST"])
def concluir(tarefa_id):

    tarefa = db.get_or_404(Tarefa, tarefa_id)

    tarefa.feita = not tarefa.feita

    db.session.commit()
    flash("Status da tarefa atualizado!")

    return redirect(url_for("listar_tarefas"))


@app.route("/apagar/<int:tarefa_id>", methods=["POST"])
def apagar(tarefa_id):

    tarefa = db.get_or_404(Tarefa, tarefa_id)

    db.session.delete(tarefa)
    db.session.commit()
    flash("Tarefa apagada com sucesso!")

    return redirect(url_for("listar_tarefas"))








