import google.generativeai as genai
 
genai.configure(api_key="AIzaSyB00olEP1p-rPl3hJI4XCXYmNLACniF6Xo")

modelo = genai.GenerativeModel('gemini-2.0-flash')

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append({'role': 'user', 'parts': [mensagem]})

    resposta = modelo.generate_content(lista_mensagens)

    lista_mensagens.append({'role': 'model', 'parts': [resposta.text]})

    return resposta.text

lista_mensagens = []
while True:
    texto = input('Escreva aqui sua mensagem: ')

    if texto.lower() == 'sair':
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        print('Chatbot:', resposta)
