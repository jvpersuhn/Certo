import sys
sys.path.append("C:/Users/jvper/OneDrive/Área de Trabalho/Certo")
from controller.squad_controller import BackController, FrontController,SGBDController , SquadController, BackEnd, FrontEnd, SGBD, Squad 
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

bc = BackController()
fc = FrontController()
sc = SGBDController()
sqc = SquadController()

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/listar')
def listar():
    l = sqc.select_all()
    return render_template('listar.html', lista = l)

@app.route('/excluir')
def excluir():
    id = request.args['id']
    sqc.delete(id)
    return redirect('/listar')

@app.route('/cadastrar')
def cadastrar():
    id = request.args['id']
    nome = request.args['nome']
    desc = request.args['desc']
    qtdPessoas = request.args['qtd']

    squad = Squad(id,nome,desc,qtdPessoas)

    idF = request.args['idF']
    nomeF = request.args['nomeF']
    descF = request.args['descF']
    versaoF = request.args['versaoF']

    front = FrontEnd(idF,nomeF,descF,versaoF)

    idB = request.args['idB']
    nomeB = request.args['nomeB']
    descB = request.args['descB']
    versaoB = request.args['versaoB']

    back = BackEnd(idB, nomeB, descB, versaoF)

    idS = request.args['idS']
    nomeS = request.args['nomeS']
    descS = request.args['descS']
    versaoS = request.args['versaoS']

    sgbd = SGBD(idS,nomeS,descS,versaoS)

    squad.id_linguagemFront = fc.insert(front)
    squad.id_linguagemBack = bc.insert(back)
    squad.id_sgbd = sc.insert(sgbd)

    if idF == 0:
        sqc.insert(squad)
    else:
        sqc.update(squad)

app.run(debug=True)