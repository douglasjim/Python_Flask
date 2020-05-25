from flask import Flask, render_template,request,redirect,session,flash, url_for

app = Flask(__name__)
app.secret_key = 'alura'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

listas_teste = ['texto1', 'texto2', 'texto3']
jogo1 = Jogo('Super mario', 'Acao', 'SNES')
jogo2 = Jogo('Megaman', 'Acao', 'Play2')
lista = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista,lista2 = listas_teste)

@app.route('/form')
def form():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('form')))
    return render_template('form.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Tela de login',proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'douglas' == request.form['usuario'] and '12345' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Credenciais incorretas')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('login'))


app.run(debug=True)
