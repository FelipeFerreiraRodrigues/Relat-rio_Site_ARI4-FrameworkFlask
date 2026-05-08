from flask import Flask,render_template,request,session,redirect,url_for

app = Flask (__name__)
app.secret_key = 'zyfodias'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    user = request.form.get('user')
    password = request.form.get('password')

    if user == 'Zyfodias' and password == '01001010010001010100010001001001':
        session['logged'] = True
        return "Acesso liberado, olá Mestre Zyfodias"
    else:
        return "Acesso negado"
    
@app.route('/kamino', methods=['GET'])
def kamino():
    if 'logged' in session and session['logged'] == True:
      conteudo = """
      <h1>Planeta selecionado: Kamino</h1>
      <p>Kamino é um planeta oceânico, sua superfície inteira é coberta por mares hostís. Se encontra além da Orla Exterior, no Espaço Selvagem, sendo um planeta solitário sem uma estrela para orbitar, logo após o Labirinto de Rishi.</p>
      <p>A população principal do planeta são os Kaminoanos: Seres altos, esguios de pele pálida - possuem o melhor sistema de Clonagem em toda a galáxia, são especialistas e mestres em genética. Eles valorizam a ordem e pureza.</p>
      <br>
"""    
      return conteudo
    return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)