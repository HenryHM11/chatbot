import difflib
import re

Cuestions = {
    "hola": "¡Holi! ¿En qué puedo ayudarte?",
    "bye": "Bye te espero pronto!",
    "¿cómo estás?": "Estoy bien, gracias por preguntar.",
    "default": "No entiendo lo que estás diciendo. ¿Puedes reformular tu pregunta?",
    "quien te creo": "Mi creadora es Keisy Vallejos Carrera. ¿Interesante no crees?",
    "si": "excelente",
}

Cuestions_ban = {
    "serrano": "de racismo",
    "tonto": "de insulto",
    "imbécil": "de insulto",
    "estúpido": "de insulto",
    "sin papá": "de insulto",
    "malparido": "de insulto",
    "idiota": "de insulto",
    "cabron": "de insulto",
    "indigena": "de insulto",
    "paisano": "de insulto",
    "maldito ": "de insulto",
    "huanaco": "de insulto",
    "nigger": "de insulto",
    "prieto": "de insulto",
    "gordo": "de insulto",
    "pou": "de insulto",
    "negra": "de insulto",
    "moreno": "de insulto",
    "gay": "de insulto",
    "homosexual": "de insulto",
    "tonta": "de insulto",
    "tonto": "de insulto",
    "joder": "de insulto",
    "silencio negro": "de racismo",
    "negro": "de racismo",
    "cholo tonto": "de discriminación",
    "cholo": "de discriminación",
    "basura": "de contenido ofensivo",
    "tarado": "de comportamiento irrespetuoso",
    "largate": "de ofensa",
    "pobre": "de lenguaje humillante",
}

Neuro ={
    "Me sieto triste": "Ohh en que puedo ayudarte, dejame que soy un chaat bot especializado en ayudar a los humanos con sus emociones",
    "Mal":"Sabes, sentirse mal es normal eres humano y las emociones no son malas ",
    "Que puedo hacer": "Experimentar tristeza es algo normal, Así que si te apetece llorar, hazlo, es sanador y te vas a sentir más aliviado ¿Sientes Ansiedad?",
    "ok":"Te brindare tecnicas para la ansiedad : Respiración: tomar aire y llevarlo a nuestro diafragma, al vientre, sin hinchar el pecho",
    "Estoy enojado":"oh calma, dahite va un chiste : ¿como se dice papel en japones ?",
    "nose":"Sacamoko jaja , espero haberte ayudado"
}

def process_input(usuario_key):
    usuario_key = usuario_key.lower()
    mejor_mind = difflib.get_close_matches(usuario_key, Cuestions.keys())
    if mejor_mind:
        respuesta = Cuestions[mejor_mind[0]]
    else:
        respuesta = "No entiendo lo que estás diciendo. ¿Puedes reformular tu pregunta?"
    return respuesta

def process_input_neuro(usuario_key):
    usuario_key = usuario_key.lower()
    mejor_mind = difflib.get_close_matches(usuario_key, Neuro.keys())
    if mejor_mind:
        respuesta = Neuro[mejor_mind[0]]
        return respuesta
    return None

def process_input_ban(usuario_key):
    usuario_key = usuario_key.lower()
    for palabra_ban in Cuestions_ban:
        if palabra_ban in usuario_key:
            asteriscos = palabra_ban[0] + '*' * (len(palabra_ban)-1)
            respuesta = f"Lo siento, pero la palabra {asteriscos} incumple con nuestras normas al ser una expresión {Cuestions_ban[palabra_ban]}."
            return respuesta
    return None

def es_operacion_matematica(usuario_key):
    patron_operacion = re.compile(r'\b(\d+\s*[\+\-\*/]\s*\d+)\b')
    return bool(patron_operacion.search(usuario_key))

if __name__ == "__main__":
    print("Chatbot: ¡Hola! Soy kiti un chatbot. Puedes escribir 'Bye' para salir.")

    while True:
        usuario_key = input("Tú: ")

        if usuario_key.lower() == "bye":
            print("Chatbot: Bye te espero pronto!")
            break

        respuesta_ban = process_input_ban(usuario_key)

        if respuesta_ban:
            print("Chatbot: " + respuesta_ban)
        else:
            respuesta_neuro = process_input_neuro(usuario_key)
            if respuesta_neuro:
                resultado = respuesta_neuro
                print("Chatbot: " + resultado)

            if es_operacion_matematica(usuario_key):
                resultado = eval(usuario_key)
                print("Chatbot: El resultado es {}".format(resultado))
            else:
                respuesta = process_input(usuario_key)
                print("Chatbot: " + respuesta)
