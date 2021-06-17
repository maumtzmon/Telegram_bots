
########################################################################
#
# Plantilla para crear un bot en Telegram
# Ing. Mauricio Martinez Montero
# LabDet, Criogenia. Instituto de Ciencias Nucleares, UNAM.
#
# Pequeña plantilla que incluye librerias basicas para el manejo de 
# un bot en Telegram utilizando Python 3 y que esta pensado para ser 
# montado en un ordenador o dispositivo electronico que soporte
# python 3 o micropython (pendiente)
#
#
########################################################################

# Librerias basicas de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.messagehandler import MessageHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Message

# Librerias para uso de recursos de sistema
import logging, os, signal, time

# Librerias de archivos que se encuentran montados en el mismo directorio que el bot
from mensajes import output_mensajes
from funciones import funcion_externa

# Token generado por el Bot Father, ver @BotFather en telegram
Token_Telegram='1875550428:AAHYqucTFw9z7GF8chxiUIJliBVOBSsmFA8' 

#Esto es para que el bot esté buscando constantemente en el servidor por mensajes nuevos.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(mesage)s', level=logging.INFO)
logger = logging.getLogger('Kalib Bot')

#Variables y archivos que va a utilizar para sus procesos
door = False

######################################################################
# Definicion de funciones principales del bot

# Funcion para iniciar el bot
def start(update, context):
    logger.info('He recibido un comando start')
    name = update.effective_chat.first_name #Se obtiene el nombre del usario.
    chat_id = update.effective_chat.id #obtenemos el Chat ID a donde se andara el mensaje
    text = "Hola "+ name +" que gusto!\nEstas probando un bot de telegram. Intenta presionar cualquiera de los Botones. \n" #  Chat Id="+str(chat_id)
    keyboard(chat_id, text, context) #Se envía el mensaje y sale el comando.
    return 0
    
# Funcion para generar botones permitidos en el teclado de Telegram
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

# Funciones para los procesos del bot, funciones que realizan una accion
# al presionar cualquiera de los botones disponibles

def boton1(update, context):
    logger.info('He recibido un comando Boton 1')
    text = output_mensajes('boton1')
    chat_id = update.effective_chat.id
    keyboard(chat_id, text, context)
    return 0

def boton2(update,
 context):
    logger.info('He recibido un comando Boton 2')
    text = output_mensajes('boton2') + funcion_externa()
    chat_id = update.effective_chat.id
    keyboard(chat_id, text, context)
    return 0

def boton3(update, context):
    #intentar enviar imagen de matplotlib
    global door   
    
    logger.info('He recibido un comando Boton 3')
    text = output_mensajes('boton3')
    chat_id = update.effective_chat.id
    keyboard(chat_id, text, context)
    door = True

    #query = update.callback_query
    #query.answer()

    #return 0

# Funcion que maneja los mensajes de texto enviados por el usuario al bot
# sean o no solicitados por el bot

def Text(update,context):
    # 'global door' es una variable que indica si el mensaje se espera por la 
    # accion de un boton o si se recibio el mensaje sin haberlo esperado
    global door

    logger.info('recibí mensaje, estoy en text')
    chat_id = update.effective_chat.id
    name = update.effective_chat.first_name
    try:
        link = update.effective_chat.link.split('/')[-1]
    except:
        link = 'no_tiene_link'
    print(link + '/' + name)
    
    if door == True:

        text = "Perfecto, recibi tu mensaje"
        context.bot.send_message(chat_id, text)

        messageRecived = update.message.text

        text = 'El mensaje recibido fue: \n-' + messageRecived
        context.bot.send_message(chat_id,text)
        
        chat_id_to_Mau = 18616105 #este chat_id es mio, me enviara un mensaje para indicar que alguien esta usando el bot
        text_to_Mau = 'el usuario: ' + name + '/ @'+ link + ', hizo una sugerencia para implementar: \n'+ messageRecived
        context.bot.send_message(chat_id_to_Mau,text_to_Mau)
        
        door = False
    
    else:

        text = "Que gusto " + name + ", Soy el bot Kali! quieres intentar usar los botones para conocer las opciones de este bot"
        context.bot.send_message(chat_id, text)
        
        
        chat_id_to_Mau = 18616105 #este chat_id es mio, me enviara un mensaje para indicar que alguien esta usando el bot
        messageRecived = update.message.text
        text_to_Mau = 'el usuario: @' + link + ' / ' + name + ', mando un mensaje a kaliBot: \n'+ messageRecived + '\n '
        context.bot.send_message(chat_id_to_Mau,text_to_Mau)
        


######################################################################
# Main del programa

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

    #inicia el bot y se mantiene a la espera de la interaccion con un usuario
    updater.start_polling()
    updater.idle()

