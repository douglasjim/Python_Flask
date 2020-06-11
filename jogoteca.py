from flask import Flask, render_template,request,redirect,session,flash, url_for

app = Flask(__name__)
app.secret_key = 'alura'

class Videos:
    def __init__(self, nome, tema, link):
        self.nome = nome
        self.tema = tema
        self.link = link

# consigo colocar os videos apenas manualmente um video ou pelo link
videos1 = Videos('Primeiro ', 'Eletronic','https://www.youtube.com/embed/GEmWdwxHjSs')
videos2 = Videos('Segundo ', 'Rap','https://www.youtube.com/embed/r40pC9kyoj0')
lista = [videos1,videos2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Videos', videos=lista)

@app.route('/form')
def form():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('form')))
    return render_template('form.html', titulo='Novo Video')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    tema = request.form['tema']
    link = request.form['link']
    movies = Videos(nome,tema,link)
    lista.append(movies)
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
        flash(request.form['usuario'] + ' Credenciais incorretas')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('login'))


app.run(debug=True)
