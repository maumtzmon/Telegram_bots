from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.messagehandler import MessageHandler

import logging, os, signal, time

from funciones import funcion_externa

Token_Telegram='1875550428:AAHYqucTFw9z7GF8chxiUIJliBVOBSsmFA8' #token generado por el Bot Father, ver @BotFather en telegram

#Esto es para que el bot esté constantemente buscando en el servidor por mensajes nuevos.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(mesage)s', level=logging.INFO)
logger = logging.getLogger('Kalib Bot')

#Variables y archivos que va a utilizar para sus procesos
door = False

#Funciones para que el bot funcione

#Funcion para iniciar el bot
def start(update, context):
    logger.info('He recibido un comando start')
    name = update.effective_chat.first_name #Se obtiene el nombre del usario.
    chat_id = update.effective_chat.id #obtenemos el Chat ID a donde se andara el mensaje
    text = "Hola "+ name +" que gusto!\nEstas probando un bot de telegram. Intenta presionar cualquiera de los Botones. \n" #  Chat Id="+str(chat_id)
    keyboard(chat_id, text, context) #Se envía el mensaje y sale el comando.
    return 0
    
#funcion para generar botones permitidos en el teclado de Telegram
def keyboard(chat_id, text, context):
    kb = [[KeyboardButton("/Boton_1")], \
         [KeyboardButton("/Boton_2")], \
         [KeyboardButton("/Boton_3")], \
         #[KeyboardButton("/Boton_4a"), KeyboardButton("/Boton_4b")], \
         #[KeyboardButton("/Boton_5a"), KeyboardButton("/Boton_5b")], \
         #[KeyboardButton("/Boton_6")]]
        ]
    kb1 = ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id, text, reply_markup=kb1)
    return 0

#funciones para los procesos del bot
def boton1(update, context):
    logger.info('He recibido un comando Boton 1')
    text = "Dentro de esta funcion podemos poner algun proceso, que devuelva un mensaje de texto en pantalla. \
    \n\nPor ejemplo: \
    \n\nMensajes de ayuda, sobre como utilizar el bot.\
    \n\nEl resultado de algun analisis.  "
    chat_id = update.effective_chat.id
    keyboard(chat_id, text, context)
    return 0

def boton2(update,
 context):
    logger.info('He recibido un comando Boton 2')
    text = 'Este es un ejemplo usando una funcion que devuelve una tabla usando Pandas, en donde tenemos renglones (0,1,2) y columnas (a,b,c).\n\n' \
        + funcion_externa()
    chat_id = update.effective_chat.id
    keyboard(chat_id, text, context)
    return 0

def boton3(update, context):
    #intentar enviar imagen de matplotlib
    global door   
    
    logger.info('He recibido un comando Boton 3')
    text = "sigo pensando aun que podemos hacer en este boton. Que se te ocurre, escribelo abajo ;)"
    chat_id = update.effective_chat.id
    keyboard(chat_id, text, context)
    door = True

    #query = update.callback_query
    #query.answer()

    #return 0

def Text(update,context):
    global door

    logger.info('recibí mensaje, estoy en text')
    chat_id = update.effective_chat.id
    name = update.effective_chat.first_name
    link = update.effective_chat.link.split('/')[-1]
    
    if door == True:

        text = "Perfecto, recibi tu mensaje"
        
        context.bot.send_message(chat_id, text)

        messageRecived = update.message.text

        text = 'El mensaje recibido fue: \n-' + messageRecived

        context.bot.send_message(chat_id,text)
        
        chat_id_to_Mau = 18616105
        text_to_Mau = 'el usuario: ' + name + '/ @'+ link + ', hizo una sugerencia para implementar: \n'+ messageRecived
        context.bot.send_message(chat_id_to_Mau,text_to_Mau)
    
    else:

        text = "Que gusto " + name + ", Soy el bot Kali! quieres intentar usar los botones para conocer las opciones de este bot"
        context.bot.send_message(chat_id, text)
        
        
        chat_id_to_Mau = 18616105
        messageRecived = update.message.text
        text_to_Mau = 'el usuario: @' + link + ' / ' + name + ', hizo una sugerencia para implementar: \n'+ messageRecived + '\n '
        context.bot.send_message(chat_id_to_Mau,text_to_Mau)
        




if __name__ == '__main__':

    updater = Updater(Token_Telegram, use_context=True)
    dispatcher = updater.dispatcher

    #comandos y conexion de cada uno a su respectiva funcion
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('Boton_1', boton1))
    dispatcher.add_handler(CommandHandler('Boton_2', boton2))
    dispatcher.add_handler(CommandHandler('Boton_3', boton3))
    # dispatcher.add_handler(CommandHandler())
    # dispatcher.add_handler(CommandHandler())
    # dispatcher.add_handler(CommandHandler())
    
    #maneja la recepcion de texto por parte de un remitente y Text() maneja ese mensaje
    dispatcher.add_handler(MessageHandler(Filters.text, Text))


    updater.start_polling()
    updater.idle()

