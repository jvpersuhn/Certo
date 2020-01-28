import sys
sys.path.append("C:/Users/900143/Desktop/Certo")
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
    id = int(request.args['id'])
    sqc.delete(sqc.select_byId(id))
    return redirect('/listar')

@app.route('/cadastrar')
def cadastrar():
    if 'id' in request.args:
        squad = sqc.select_byId(request.args['id'])
    else:
        squad = Squad(0,'','','')
    
    return render_template('cadastrar.html', squad = squad)
    

@app.route('/salvar')
def salvar():
    id = int(request.args['id'])
    nome = request.args['nome']
    desc = request.args['desc']
    qtdPessoas = request.args['numPessoas']

    squad = Squad(id,nome,desc,qtdPessoas)

    idF = request.args['idF']
    if idF:
        idF = int(idF)
    else:
        idF = 0
    nomeF = request.args['nomeF']
    descF = request.args['descF']
    versaoF = request.args['versaoF']

    front = FrontEnd(idF,nomeF,descF,versaoF)

    idB = request.args['idB']
    if idB:
        idB = int(idB)
    else:
        idB = 0
    nomeB = request.args['nomeB']
    descB = request.args['descB']
    versaoB = request.args['versaoB']

    back = BackEnd(idB, nomeB, descB, versaoB)

    idS = request.args['idS']
    if idS:
        idS = int(idS)
    else:
        idS = 0
    nomeS = request.args['nomeS']
    descS = request.args['descS']
    versaoS = request.args['versaoS']

    sgbd = SGBD(idS,nomeS,descS,versaoS)

    if id == 0:
        squad.id_linguagemFront = fc.insert(front)
        squad.id_linguagemBack = bc.insert(back)
        squad.id_sgbd = sc.insert(sgbd)
        sqc.insert(squad)
    else:
        squad.linguagemFront = front
        squad.linguagemBack = back
        squad.sgbd = sgbd
        squad.id_linguagemFront = idF
        squad.id_linguagemBack = idB
        squad.id_sgbd = idS
        sqc.update(squad)

    return redirect('/listar')
        

app.run(debug=True)