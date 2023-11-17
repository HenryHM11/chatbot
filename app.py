#app.py
from flask import Flask, render_template, request, jsonify
from chatbot import process_input, process_input_neuro, process_input_ban, es_operacion_matematica

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']

    respuesta_ban = process_input_ban(user_message)

    if respuesta_ban:
        bot_response = respuesta_ban
    else:
        respuesta_neuro = process_input_neuro(user_message)
        if respuesta_neuro:
            bot_response = respuesta_neuro
        elif es_operacion_matematica(user_message):
            resultado = eval(user_message)
            bot_response = "El resultado es {}".format(resultado)
        else:
            bot_response = process_input(user_message)

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
