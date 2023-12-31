
from flask import Flask, render_template, request, jsonify
from chatbot import process_input, process_input_neuro, process_input_ban, es_operacion_matematica, Learning
from data import cargar_datos, guardar_datos


app = Flask(__name__)

@app.route('/')
def index():
    Cuestions, Cuestions_ban, Neuro, Learning = cargar_datos()
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

    print(f"Bot Response: {bot_response}")

    return jsonify({'bot_response': bot_response})


@app.route('/store_learning_response', methods=['POST'])
def store_learning_response():
    user_message = request.form['user_message']
    user_learning_response = request.form['user_learning_response']

    Cuestions, Cuestions_ban, Neuro, Learning = cargar_datos()
    Learning[user_message.lower()] = user_learning_response
    guardar_datos({'Cuestions': Cuestions, 'Cuestions_ban': Cuestions_ban, 'Neuro': Neuro, 'Learning': Learning})

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
