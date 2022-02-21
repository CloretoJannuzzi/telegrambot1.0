#from email import message
import telebot
import os

chave_api = '5113751813:AAEomz8_ZBi352EAon-iQdI8-vRQNorjyRk'
bot = telebot.TeleBot(chave_api)
''' usar caso não queria utilizar os comandose sim mensagens para o bot.
def v1(mensagem):
    if mensagem == 'opcao1':
        return True
    else:
        return False'''


@bot.message_handler(commands='opcao1')
def opcao1(mensagem):
    bot.reply_to(mensagem, 'selecionado 1')


@bot.message_handler(commands='opcao2')
def opcao2(mensagem):
    bot.reply_to(mensagem, 'selecionado 2')


@bot.message_handler(commands='opcao3')
def opcao3(mensagem):
    bot.reply_to(mensagem, 'seleciando 3')
    #print(mensagem)
    bot.send_message(mensagem.chat.id, 'grupo')
    # aqui eu envio amensagem sem responder a que me enviaram
    #bot.send_message(-626105153, 'ola grup')# aqui eu envio mensagem a alguem ou grupo


@bot.message_handler(commands='sair')
def sair(mensagem):
    bot.reply_to(mensagem, 'volte sempre!')
    #responde a mensagem marcando a pessoa


def verificar(mensagem):
    return True
    # qualquer mensagem vai rodar o bot
    # somente no privado. Em grupo ele só é executado quando tem algum comando.


@bot.message_handler(func=verificar)
#quando será executado / pega a info do polling e diz quando o responder tem que ser executado
def responder(mensagem):
    menu = '''

Olá, seja bem-vindo!{os.linesep}Selecione uma opção para fazer o seu pedido:

/opcao1
/opcao2
/opcao3
/Cancelar

    '''
    bot.reply_to(mensagem, menu)


bot.polling()  # sempre lendo
