from flask import Flask, render_template
# Questão 1, primeiro item

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template('pedra_papel_tesoura.html', mensagem='', opcao_computador='', opcao_jogador='')

@app.route("/<opcao_jogador>")
def checar_opcao(opcao_jogador):
    mensagem = ''

    # Questão 1, segundo item
    opcao_computador = ''

    # Questão 1, terceiro item

    # Questão 2, primeiro item

    # Questão 2, segundo item
    
    # Questão 2, terceiro item
  
    return render_template('pedra_papel_tesoura.html', mensagem=mensagem, opcao_computador=opcao_computador, opcao_jogador=opcao_jogador)

@app.route("/extra")
def acessar_extra():
  return render_template('extra.html')