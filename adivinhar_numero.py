from flask import Flask, render_template, request
# Questão 1, primeiro item
import random 


app = Flask(__name__)

# Questao 1, segundo item
numero_secreto =  random.randint(1,100)

@app.route("/", methods=['GET', 'POST'])
def checar_palpite():
    mensagem = ''
    if request.method == 'POST':
        palpite = int(request.form['palpite'])
        # Questão 2, primeiro item
        print("palpite")
        palpitecon = int(palpite)

        # Questão 2, segundo item
        if palpite > numero_secreto: 
          mensagem = "Tente um número menor"
        elif palpite < numero_secreto:
           mensagem = "Tente um número maior"
        else: mensagem = f"Parabéns!! Você acertou o número {numero_secreto}"

    return render_template('adivinhar_numero.html', mensagem=mensagem)
