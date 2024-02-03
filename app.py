from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = "Luciana"
    idade = 42
    lista_nomes = ['Luciana', 'Auri', 'Guilherme', 'Levy']
    return render_template('index.html', nome=nome, idade=idade, lista_nomes=lista_nomes )

if __name__ == "__main__":
    app.run(debug=True)