import telebot

#chave do bot
chave_api = '5113751813:AAEomz8_ZBi352EAon-iQdI8-vRQNorjyRk'

bot = telebot.TeleBot(chave_api)


@bot.message_handler(commands='Comida')
def Comida(mensagem):
    bot.send_message(
        mensagem.chat.id,
        'Cardápio:\n/pizza\n/hamburguer\n/nhoque\n/sopa\n/Cancelar\nEscolha uma opção para selecionar.'
    )


@bot.message_handler(commands='pizza')
def pizza(mensagem):
    if mensagem.text == '/pizza':
        bot.send_message(mensagem.chat.id, 'Pizza Confirmada!')


@bot.message_handler(commands='hamburguer')
def hamburguer(mensagem):
    if mensagem.text == '/hamburguer':
        bot.send_message(mensagem.chat.id, 'Hamburguer Confirmado!')


@bot.message_handler(commands='nhoque')
def nhoque(mensagem):
    if mensagem.text == '/nhoque':
        bot.send_message(mensagem.chat.id, 'Nhoque Confirmado!')


@bot.message_handler(commands='sopa')
def sopa(mensagem):
    if mensagem.text == '/sopa':
        bot.send_message(mensagem.chat.id, 'Sopa Confirmada!')
#verificar como posso fazer com que essas funções não executem se n estiver na aba do cardapio

@bot.message_handler(commands='Cancelar')
def sair(mensagem):
    bot.send_message(mensagem.chat.id, 'Cancelado!')


@bot.message_handler(commands='Comida_com_bebidas')
def Comida_com_bebidas(mensagem):
    bot.send_message(
        mensagem.chat.id,
        'Cardápio:\n/pizza\n/hambuguer\n/nhoque\n/sopa\nBebidas:\n/Coca_cola_2l\n/Guarana_antartica_2l\n/Fanta_laranja_2l.\n/Latinha_500ml\n/Cancelar\nClique para selecionar.'
    )


@bot.message_handler(commands='Bebidas')
def Bebidas(mensagem):
    bot.send_message(
        mensagem.chat.id,
        'Bebidas:\n/Coca_cola_2l\n/Guarana_antartica_2l\n/Fanta_laranja_2l.\n/Latinha_500ml\n/Cancelar\nClique para selecionar.'
    )


@bot.message_handler(commands='Cancelar_pedido')
def sair(mensagem):
    bot.send_message(mensagem.chat.id, 'Volte sempre!')


def verificar(mensagem):
    if mensagem.text == '/menu':
        return True
    else:
        return False
    # só vai rodar com o /menu, porem precisa de alguns ajustes

@bot.message_handler(func=verificar)

def responder(mensagem):
    menu = '''

Olá, seja bem-vindo ao sistema de pedidos!\nSelecione uma opção para escolher o seu pedido:

/Comida
/Comida_com_bebidas
/Bebidas
/Cancelar_pedido

    '''
    bot.reply_to(mensagem, menu)


''' bot.send_message(mensagem.chat.id, 'resposta no mesmo chat') 
    bot.send_message(-626105153, 'resposta podendo ser enviada para outro chat') aqui eu envio mensagem a alguem ou grupo
'''

#looping
bot.polling()
